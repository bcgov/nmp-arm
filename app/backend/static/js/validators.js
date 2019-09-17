window.RISK_RATING = {
    1 : 'Low' ,
    2 : 'Low-Med' ,
    3 : 'Low-Med' ,
    4 : 'Medium' ,
    5 : 'Medium' ,
    6 : 'Medium' ,
    7 : 'Med-High' ,
    8 : 'Med-High' ,
    9 : 'High' ,
    10: 'Extreme' ,
}

window.CAUTIONS  = {}
window.RATING = {}

window.remove_risk_rating_classes = function( $field ) {
    $field.removeClass( "low" );
    $field.removeClass( "low-med" );
    $field.removeClass( "med" );
    $field.removeClass( "med-high" );
    $field.removeClass( "high" );
};

window.add_risk_rating_classes = function( $field ) {
    if( /low/i.test( $field.text() ) ) {
        $field.addClass( "low" ); 
    }
    else if( /low-med/i.test( $field.text() ) ) {
        $field.addClass( "low-med" ); 
    }
    else if( /med-high/i.test( $field.text() ) ) {
        $field.addClass( "med-high" ); 
    }
    else if( /med/i.test( $field.text() ) ) {
        $field.addClass( "med" ); 
    }
    else if( /high/i.test( $field.text() ) ) {
        $field.addClass( "high" ); 
    }
    else if( /extreme/i.test( $field.text() ) ) {
        $field.addClass( "high" ); 
    }
};

window.update_riskrating_ui = function( $field, rating ) {

    var $risk = $field.parents( '.form-group' ).find( '.riskrating' );
    $risk.text( "Risk Rating: "+rating.display );
    var $hidden = $field.parents( '.form-group' ).find( 'input.riskhiddenfield:hidden' );
    if($hidden.length >= 1 )
    {
        $hidden[0].value = rating.display;
    }
    remove_risk_rating_classes( $risk );
    add_risk_rating_classes( $risk );
    RATING[ $field.attr('name') ] = rating.risk;
};


window.update_caution_ui = function( $field, message, append ) {
    var is_append = append || false;
    var $caution = $field.parents( '.form-group' ).find( '.cautionrating' );
    if ( message !== null && !is_append ) {
        $caution.text( message );
    }
    else if ( message !== null && is_append ) {
        $caution.append( $("</p>").text( message ) );
    }
    else {
        $caution.text( '' );
    }
};

window.sum_total_ratings = function( rating ){

    var total = 0;
    for ( var key in rating ) {
        var value = rating[ key ];
        if ( value !== null ) {
            total += value;
        }
    }
    return total;

};

$( document ).on( 'rating-update', function( e, rating, override ) {

    if ( typeof override === 'undefined' || override === null ) {

        var total = sum_total_ratings( rating );
        console.log( "[ TOTAL RISK ]: ", total );

        var cutoff = null;
        var color_class = null;
        if ( total <= RISK_CUTOFF[ 'low' ].maximum_score ) {
            cutoff = RISK_CUTOFF[ 'low' ];
            color_class = "low";
        }
        
        else if ( total >= RISK_CUTOFF[ 'med' ].minimum_score && total <= RISK_CUTOFF[ 'med' ].maximum_score ) {
            cutoff = RISK_CUTOFF[ 'med' ];
            color_class = "med";
        }

        else if ( total >= RISK_CUTOFF[ 'high' ].minimum_score ) {
            cutoff = RISK_CUTOFF[ 'high' ];
            color_class = "high";
        }
        remove_risk_rating_classes( $( "input[ name='total_risk' ]" ) );
        $( "input[ name='total_risk' ]" ).addClass( color_class );
        $( "input[ name='total_risk' ]" ).val( cutoff.display ); 
        $( "input[ name='total_risk' ]" ).parents( '.form-group' ).find( '.desc' ).text( cutoff.message ); 

    }
    else  {

        remove_risk_rating_classes( $( "input[ name='total_risk' ]" ) );
        $( "input[ name='total_risk' ]" ).addClass( 'high' );
        $( "input[ name='total_risk' ]" ).val( 'NO APPLICATION' ); 
        $( "input[ name='total_risk' ]" ).parents( '.form-group' ).find( '.desc' ).text( "NO application, one or more indicators is above the critical value" ); 

    }

})

window.calculate_caution = function( value_to_check, L, options ) {

    var left, right;
    for ( left=0,right=1; right < L.length; left++,right++ ) {
        if ( L[left].value <= value_to_check && value_to_check < L[right].value ) {
            return  L[left].message;
        }
        else if ( value_to_check === L[right].value ) {
           return  L[right].message;
        }
    }
    return null;
};


window.calculate_risk_rating = function( value_to_check, values, options ) {
    var options = options || {};
    var is_reversed = options.is_reversed || false;

    var L = [];
    values.forEach( function( value, indx ) {
        L.push( { 'value' : value, 'risk' : indx+1 } );
    })
    if( is_reversed ) { L.reverse(); }

    var left, right;
    if ( value_to_check < L[0].value ) value_to_check = L[0].value; // normalize
    for ( left=0,right=1; right < L.length; left++,right++ ) {
        console.log( L[left].value, " <= ", value_to_check, " && ", value_to_check, " < ", L[right].value );
        if ( L[left].value <= value_to_check && value_to_check < L[right].value ) {
            return { risk : L[left].risk , display : RISK_RATING[ L[left].risk ] };
        }
        else if ( value_to_check === L[right].value ) {
            console.log( value_to_check, " === ", L[right].value );
            return { risk : L[right].risk, display : RISK_RATING[ L[right].risk ] };
        }
    }

    if ( is_reversed ) {
        return { risk: 1, display : RISK_RATING[ 1 ] };
    }
    else {
        return { risk : 10, display : RISK_RATING[ 10 ] };
    }
};

(function($) {
    $.fn.bootstrapValidator.validators.restrict_radio = {
        validate: function(validator, $field, options) {
            var value = $field.val();

            var all_checked_values = {}
            if ( options.comparitor === 'in' ) {
                var all_inputs = $field.parents( '.form-group' ).find( 'input:checked' );
                for ( var i = 0; i < all_inputs.length; i++ ) {
                    all_checked_values[ $( all_inputs[ i ] ).val() ] = true;
                }
            }

            if ( options.comparitor === 'greaterthan' ) {
                if ( parseInt( value ) >= options.stop_value ) {
                    return {
                        valid: false ,
                        message: options.stop_message
                    };
                }
            }
            else if ( options.comparitor === 'lessthan' ) {
                if ( parseInt( value ) <= options.stop_value ) {
                    return {
                        valid: false ,
                        message: options.stop_message
                    };
                }
            }
            else if ( options.comparitor === 'equals' ) {
                if ( value === options.stop_value ) {
                    return {
                        valid: false ,
                        message: options.stop_message
                    };
                }
            }
            else if ( options.comparitor === 'in' ) {
                var values = Object.keys( all_checked_values );
                for( var i = 0; i < values.length; i++ ) {
                    var value = values[ i ];
                    if ( value in options.stop_values ) {
                        return {
                            valid: false ,
                            message: options.stop_message
                        };
                    }
                }
            }

            return true;
        }
    };
}(window.jQuery));

(function($) {
    $.fn.bootstrapValidator.validators.risk_rating = {
        validate: function(validator, $field, options) {
            var value = $field.val();
            var field = $field;

            if(field[0].name == 'precipitation_1')
            {
                for (var key in options)
                {
                    var setting = options[ key ]
                    if(value >= setting['range_minimum'] && value <= setting['range_maximum']){
                        console.log('precipitation_1')
                        console.log(key)
                        console.log(setting.risk_value)
                        console.log(setting.risk_display_text)
                        update_riskrating_ui( $field, { risk : setting.risk_value, display : setting.risk_display_text } );
                        update_caution_ui( $field, setting.caution_message );
                        break;
                    }
                }
    
                return true;                
            }

            var is_reversed = options.is_reversed || false;
            // exception for special text values
            if (value == 101){
              var risk = {
                'risk':  5,
                'display': RISK_RATING[ 5 ]
              }
            }
            else {
            //console.log( value );
               var risk = calculate_risk_rating( parseFloat( value ), options.values, { is_reversed : is_reversed } );
            }
            console.log( field );
            console.log( value );
            
            // var risk = calculate_risk_rating( parseFloat( value ), options.values, { is_reversed : is_reversed } );
            console.log( "[ RISK ]: ", risk );
            update_riskrating_ui( $field, risk );
            var caution = calculate_caution( value, options.caution_values, { is_reversed : is_reversed } );
            //console.log( "[ CAUTION ]: ", caution );
            update_caution_ui( $field, caution );

            return true;
        }
    };
}(window.jQuery));


(function($) {
    $.fn.bootstrapValidator.validators.show_hide = {
        validate: function(validator, $field, options) {
            var value = $field.val();
            if ( value === 'no' ) {
                $field.parents( 'form' ).find( '.show-hide-wrapper' ).attr( 'data-state', 'closed' );
            }
            else if ( value === 'yes' ) {
                $field.parents( 'form' ).find( '.show-hide-wrapper' ).attr( 'data-state', 'opened' );
            }
            return true;
        }
    };
}(window.jQuery));


(function($) {
    $.fn.bootstrapValidator.validators.applicator_risk_rating = {
        validate: function(validator, $field, options) {
            var value = $field.val();
            //console.log( value );


            for (var key in APPLICATION_EQUIPMENT_RISK_SETTINGS)
            {
                var setting = APPLICATION_EQUIPMENT_RISK_SETTINGS[ key ]
                if(value === key){
                    console.log('applicator_risk_rating')
                    console.log(key)
                    console.log(setting.risk_value)
                    console.log(setting.risk_display_text)
                    update_riskrating_ui( $field, { risk : setting.risk_value, display : setting.risk_display_text } );
                    update_caution_ui( $field, setting.caution_text );
                    break;
                }
            }
            return true;
        }
    };
}(window.jQuery));




(function($) {
    $.fn.bootstrapValidator.validators.soil_type_risk_rating = {
        validate: function(validator, $field, options) {
            var value = $field.val();
            //console.log( value );


            for (var key in SOIL_TYPE_RISK_SETTINGS)
            {
                var setting = SOIL_TYPE_RISK_SETTINGS[ key ]
                if(value === key){
                    console.log('soil_type_risk_rating')
                    console.log(key)
                    console.log(setting.risk_value)
                    console.log(setting.risk_display_text)
                    update_riskrating_ui( $field, { risk : setting.risk_value, display : setting.risk_display_text } );
                    update_caution_ui( $field, setting.caution_text );
                    break;
                }
            }

            return true;
        }
    };
}(window.jQuery));



(function($) {
    $.fn.bootstrapValidator.validators.surface_risk_rating = {
        validate: function(validator, $field, options) {
            var checked_value = $field.val();

            var all_checked_values = {}
            if ( options.comparitor === 'in' ) {
                var all_inputs = $field.parents( '.form-group' ).find( 'input:checked' );
                for ( var i = 0; i < all_inputs.length; i++ ) {
                    all_checked_values[ $( all_inputs[ i ] ).val() ] = true;
                }
            }
            
            var values = Object.keys( all_checked_values );
            var surface_risk = 0;
            console.log('surface_risk_rating')
            update_caution_ui( $field, null );
            for( var value in values ) {
                setting = SURFACE_CONDITION_RISK_SETTINGS[ values[value] ]
                surface_risk += setting.risk_value
                console.log('surface_risk: ' + surface_risk)
                update_riskrating_ui( $field, { risk : surface_risk, display : setting.risk_display_text } );
                update_caution_ui( $field, setting.caution_message, true );
            }

            return true;
        }
    };
}(window.jQuery));



(function($) {
    $.fn.bootstrapValidator.validators.critical_area_risk_rating = {
        validate: function(validator, $field, options) {
            var value = $field.val();
            //console.log( value );

            for (var key in CRITICAL_AREA_RISK_SETTINGS)
            {
                var setting = CRITICAL_AREA_RISK_SETTINGS[ key ]
                if(value === key){
                    console.log('critical_area_risk_rating')
                    console.log(key)
                    console.log(setting.risk_value)
                    console.log(setting.risk_display_text)
                    update_riskrating_ui( $field, { risk : setting.risk_value, display : setting.risk_display_text } );
                    update_caution_ui( $field, setting.caution_text );
                    break;
                }
            }

            return true;
        }
    };
}(window.jQuery));


(function($) {
    $.fn.bootstrapValidator.validators.manure_setback_distance = {
        validate: function(validator, $field, options) {
            var value = $field.val();

            console.log('manure_setback_distance')
            console.log(value)
            for (var key in MANURE_SETBACK_SETTINGS)
            {
                var setting = MANURE_SETBACK_SETTINGS[ key ]
                console.log(value.toString() + ' <= ' + setting.distance_maximum + ' ' + setting.risk_display_text)
                console.log(value.toString()     + ' >= ' + setting.distance_minimum + ' ' + setting.risk_display_text)
                if(value <= setting.distance_maximum && value >= setting.distance_minimum){
                    console.log(setting.risk_value)
                    console.log(setting.risk_display_text)
                    update_riskrating_ui( $field, { risk : setting.risk_value, display : setting.risk_display_text } );
                    update_caution_ui( $field, setting.caution_text );
                    break;
                }
            }

            return true;

        }
    };
}(window.jQuery));



function manualval(validator, $field, options) {
            var value = $field.val();
            var field = $field;
            var is_reversed = options.is_reversed || false;
            console.log( field );
            console.log( value );
            
            var risk = calculate_risk_rating( parseFloat( value ), options.values, { is_reversed : is_reversed } );
            console.log( "[ RISK ]: ", risk );
            update_riskrating_ui( $field, risk );
            var caution = calculate_caution( value, options.caution_values, { is_reversed : is_reversed } );
            //console.log( "[ CAUTION ]: ", caution );
            update_caution_ui( $field, caution );

            return true;
}