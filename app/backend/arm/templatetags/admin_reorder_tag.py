"""
A set of tools giving you the ability to define custom ordering for the apps
and models in the admin app.

1. Add the setting ADMIN_REORDER to your settings.py as a tuple with each item
   containing a tuple of the app name and a tuple of the models within it, all
   defining the ordering to apply.
2. Drop the template tag code into admin_reorder_tag.py and put this into a
   templatetag package in one of your installed apps.
3. Drop the template code into your templates directory as admin/base_site.html

Credits:
--------

Stephen McDonald <steve@jupo.org>

License:
--------

Creative Commons Attribution-Share Alike 3.0 License
http://creativecommons.org/licenses/by-sa/3.0/

When attributing this work, you must maintain the Credits
paragraph above.
"""

################################################################################
# In settings.py define the app/model ordering
################################################################################
'''
ADMIN_REORDER = (
            ("app_name1", ("App1Model1", "App1Model2", "App1Model3")),
                ("app_name2", ("App2Model1", "App2Model2")),
                )
'''

################################################################################
# Add as admin_reorder_tag.py in one of your app's templatetag packages
################################################################################

from django import template
from django.conf import settings

import logging
logger = logging.getLogger( __file__ )

register = template.Library()


# from http://www.djangosnippets.org/snippets/1937/
def register_render_tag(renderer):
    """
    Decorator that creates a template tag using the given renderer as the
    render function for the template tag node - the render function takes two
    arguments - the template context and the tag token
    """
    def tag(parser, token):
        class TagNode(template.Node):
            def render(self, context):
                return renderer(context, token)
        return TagNode()
    for copy_attr in ("__dict__", "__doc__", "__name__"):
        setattr(tag, copy_attr, getattr(renderer, copy_attr))
    return register.tag(tag)

@register_render_tag
def admin_reorder(context, token):
    """
    Called in admin/base_site.html template override and applies custom ordering
    of apps/models defined by settings.ADMIN_REORDER
    """
    # sort key function - use index of item in order if exists, otherwise item
    sort = lambda order, item: (order.index(item), "") if item in order else ( len(order), item)
    order = OrderedDict(settings.ADMIN_REORDER)
    if "app_list" in context:
        # sort the app list
        context["app_list"].sort(key=lambda app: sort(list(order.keys()), app["app_url"].strip("/").split("/")[-1]))
        for i, app in enumerate(context["app_list"]):
            # sort the model list for each app
            app_name = app["app_url"].strip("/").split("/")[-1]
            if not app_name:
                app_name = app["name"].lower()
            model_order = [m.lower() for m in order.get(app_name, [])]
            context["app_list"][i]["models"].sort(key=lambda model: sort(model_order, model["admin_url"].strip("/").split("/")[-1]))
    return ""

################################################################################
# Add to your templates directory as: admin/base_site.html
################################################################################
'''
{% extends "admin/base.html" %}
{% load i18n admin_reorder_tag %}

{% block title %}{{ title }} | {% trans 'Django site admin' %}{% endblock %}

{% block branding %}
{% admin_reorder %}
<h1 id="site-name">{% trans 'Django administration' %}</h1>
{% endblock %}

{% block nav-global %}{% endblock %}
'''
