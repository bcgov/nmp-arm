--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6
-- Dumped by pg_dump version 10.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: arm_applicationequipmentoption; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_applicationequipmentoption (
    id integer NOT NULL,
    value character varying(50) NOT NULL,
    description character varying(250) NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE public.arm_applicationequipmentoption OWNER TO "bcarm";

--
-- Name: arm_applicationequipmentoption_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_applicationequipmentoption_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_applicationequipmentoption_id_seq OWNER TO "bcarm";

--
-- Name: arm_applicationequipmentoption_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_applicationequipmentoption_id_seq OWNED BY public.arm_applicationequipmentoption.id;


--
-- Name: arm_applicationriskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_applicationriskrating (
    id integer NOT NULL,
    applicator_name character varying(50) NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text
);


ALTER TABLE public.arm_applicationriskrating OWNER TO "bcarm";

--
-- Name: arm_applicationriskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_applicationriskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_applicationriskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_applicationriskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_applicationriskrating_id_seq OWNED BY public.arm_applicationriskrating.id;


--
-- Name: arm_criticalareaoption; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_criticalareaoption (
    id integer NOT NULL,
    description character varying(250) NOT NULL,
    active boolean NOT NULL,
    value character varying(50) NOT NULL
);


ALTER TABLE public.arm_criticalareaoption OWNER TO "bcarm";

--
-- Name: arm_criticalareaoption_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_criticalareaoption_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_criticalareaoption_id_seq OWNER TO "bcarm";

--
-- Name: arm_criticalareaoption_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_criticalareaoption_id_seq OWNED BY public.arm_criticalareaoption.id;


--
-- Name: arm_criticalareariskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_criticalareariskrating (
    id integer NOT NULL,
    answer character varying(10) NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text
);


ALTER TABLE public.arm_criticalareariskrating OWNER TO "bcarm";

--
-- Name: arm_criticalareariskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_criticalareariskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_criticalareariskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_criticalareariskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_criticalareariskrating_id_seq OWNED BY public.arm_criticalareariskrating.id;


--
-- Name: arm_foragedensityoption; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_foragedensityoption (
    id integer NOT NULL,
    value integer NOT NULL,
    description character varying(250) NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE public.arm_foragedensityoption OWNER TO "bcarm";

--
-- Name: arm_foragedensityoption_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_foragedensityoption_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_foragedensityoption_id_seq OWNER TO "bcarm";

--
-- Name: arm_foragedensityoption_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_foragedensityoption_id_seq OWNED BY public.arm_foragedensityoption.id;


--
-- Name: arm_foragedensityriskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_foragedensityriskrating (
    id integer NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text,
    range_minimum numeric(5,2) NOT NULL,
    range_maximum numeric(5,2) NOT NULL
);


ALTER TABLE public.arm_foragedensityriskrating OWNER TO "bcarm";

--
-- Name: arm_foragedensityriskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_foragedensityriskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_foragedensityriskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_foragedensityriskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_foragedensityriskrating_id_seq OWNED BY public.arm_foragedensityriskrating.id;


--
-- Name: arm_forageheightoption; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_forageheightoption (
    id integer NOT NULL,
    value numeric(3,1) NOT NULL,
    description character varying(250) NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE public.arm_forageheightoption OWNER TO "bcarm";

--
-- Name: arm_forageheightoption_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_forageheightoption_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_forageheightoption_id_seq OWNER TO "bcarm";

--
-- Name: arm_forageheightoption_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_forageheightoption_id_seq OWNED BY public.arm_forageheightoption.id;


--
-- Name: arm_forageheightriskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_forageheightriskrating (
    id integer NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text,
    range_minimum numeric(5,2) NOT NULL,
    range_maximum numeric(5,2) NOT NULL
);


ALTER TABLE public.arm_forageheightriskrating OWNER TO "bcarm";

--
-- Name: arm_forageheightriskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_forageheightriskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_forageheightriskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_forageheightriskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_forageheightriskrating_id_seq OWNED BY public.arm_forageheightriskrating.id;


--
-- Name: arm_formfield; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_formfield (
    id integer NOT NULL,
    field_name character varying(50) NOT NULL,
    title character varying(100) NOT NULL,
    description text
);


ALTER TABLE public.arm_formfield OWNER TO "bcarm";

--
-- Name: arm_formfield_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_formfield_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_formfield_id_seq OWNER TO "bcarm";

--
-- Name: arm_formfield_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_formfield_id_seq OWNED BY public.arm_formfield.id;


--
-- Name: arm_manuresetbackdistanceriskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_manuresetbackdistanceriskrating (
    id integer NOT NULL,
    distance_minimum numeric(10,2) NOT NULL,
    distance_maximum numeric(10,2) NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text
);


ALTER TABLE public.arm_manuresetbackdistanceriskrating OWNER TO "bcarm";

--
-- Name: arm_manuresetbackdistanceriskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_manuresetbackdistanceriskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_manuresetbackdistanceriskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_manuresetbackdistanceriskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_manuresetbackdistanceriskrating_id_seq OWNED BY public.arm_manuresetbackdistanceriskrating.id;


--
-- Name: arm_preciptation24riskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_preciptation24riskrating (
    id integer NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text,
    range_minimum numeric(5,2) NOT NULL,
    range_maximum numeric(5,2) NOT NULL
);


ALTER TABLE public.arm_preciptation24riskrating OWNER TO "bcarm";

--
-- Name: arm_preciptation24riskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_preciptation24riskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_preciptation24riskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_preciptation24riskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_preciptation24riskrating_id_seq OWNED BY public.arm_preciptation24riskrating.id;


--
-- Name: arm_preciptation72riskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_preciptation72riskrating (
    id integer NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text,
    range_minimum numeric(5,2) NOT NULL,
    range_maximum numeric(5,2) NOT NULL
);


ALTER TABLE public.arm_preciptation72riskrating OWNER TO "bcarm";

--
-- Name: arm_preciptation72riskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_preciptation72riskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_preciptation72riskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_preciptation72riskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_preciptation72riskrating_id_seq OWNED BY public.arm_preciptation72riskrating.id;


--
-- Name: arm_riskcutoffsetting; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_riskcutoffsetting (
    id integer NOT NULL,
    risk_level_name character varying(4) NOT NULL,
    display character varying(11) NOT NULL,
    minimum_score integer NOT NULL,
    maximum_score integer NOT NULL,
    message text NOT NULL
);


ALTER TABLE public.arm_riskcutoffsetting OWNER TO "bcarm";

--
-- Name: arm_riskcutoffsetting_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_riskcutoffsetting_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_riskcutoffsetting_id_seq OWNER TO "bcarm";

--
-- Name: arm_riskcutoffsetting_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_riskcutoffsetting_id_seq OWNED BY public.arm_riskcutoffsetting.id;


--
-- Name: arm_soilmoistureoption; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_soilmoistureoption (
    id integer NOT NULL,
    value integer NOT NULL,
    description character varying(250) NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE public.arm_soilmoistureoption OWNER TO "bcarm";

--
-- Name: arm_soilmoistureoption_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_soilmoistureoption_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_soilmoistureoption_id_seq OWNER TO "bcarm";

--
-- Name: arm_soilmoistureoption_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_soilmoistureoption_id_seq OWNED BY public.arm_soilmoistureoption.id;


--
-- Name: arm_soilmoistureriskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_soilmoistureriskrating (
    id integer NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text,
    range_minimum numeric(5,2) NOT NULL,
    range_maximum numeric(5,2) NOT NULL
);


ALTER TABLE public.arm_soilmoistureriskrating OWNER TO "bcarm";

--
-- Name: arm_soilmoistureriskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_soilmoistureriskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_soilmoistureriskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_soilmoistureriskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_soilmoistureriskrating_id_seq OWNED BY public.arm_soilmoistureriskrating.id;


--
-- Name: arm_soiltypeoption; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_soiltypeoption (
    id integer NOT NULL,
    value character varying(50) NOT NULL,
    description character varying(250) NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE public.arm_soiltypeoption OWNER TO "bcarm";

--
-- Name: arm_soiltypeoption_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_soiltypeoption_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_soiltypeoption_id_seq OWNER TO "bcarm";

--
-- Name: arm_soiltypeoption_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_soiltypeoption_id_seq OWNED BY public.arm_soiltypeoption.id;


--
-- Name: arm_soiltyperiskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_soiltyperiskrating (
    id integer NOT NULL,
    soil_type character varying(10) NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text
);


ALTER TABLE public.arm_soiltyperiskrating OWNER TO "bcarm";

--
-- Name: arm_soiltyperiskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_soiltyperiskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_soiltyperiskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_soiltyperiskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_soiltyperiskrating_id_seq OWNED BY public.arm_soiltyperiskrating.id;


--
-- Name: arm_surfaceconditionoption; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_surfaceconditionoption (
    id integer NOT NULL,
    value character varying(50) NOT NULL,
    description character varying(250) NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE public.arm_surfaceconditionoption OWNER TO "bcarm";

--
-- Name: arm_surfaceconditionoption_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_surfaceconditionoption_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_surfaceconditionoption_id_seq OWNER TO "bcarm";

--
-- Name: arm_surfaceconditionoption_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_surfaceconditionoption_id_seq OWNED BY public.arm_surfaceconditionoption.id;


--
-- Name: arm_surfaceconditionriskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_surfaceconditionriskrating (
    id integer NOT NULL,
    surface_condition character varying(10) NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text
);


ALTER TABLE public.arm_surfaceconditionriskrating OWNER TO "bcarm";

--
-- Name: arm_surfaceconditionriskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_surfaceconditionriskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_surfaceconditionriskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_surfaceconditionriskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_surfaceconditionriskrating_id_seq OWNED BY public.arm_surfaceconditionriskrating.id;


--
-- Name: arm_watertabledepthoption; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_watertabledepthoption (
    id integer NOT NULL,
    value integer NOT NULL,
    description character varying(250) NOT NULL,
    active boolean NOT NULL
);


ALTER TABLE public.arm_watertabledepthoption OWNER TO "bcarm";

--
-- Name: arm_watertabledepthoption_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_watertabledepthoption_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_watertabledepthoption_id_seq OWNER TO "bcarm";

--
-- Name: arm_watertabledepthoption_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_watertabledepthoption_id_seq OWNED BY public.arm_watertabledepthoption.id;


--
-- Name: arm_watertableriskrating; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.arm_watertableriskrating (
    id integer NOT NULL,
    risk_value integer NOT NULL,
    risk_display_text character varying(10) NOT NULL,
    caution_message text,
    show_stop_application boolean NOT NULL,
    stop_application_message text,
    range_minimum numeric(5,2) NOT NULL,
    range_maximum numeric(5,2) NOT NULL
);


ALTER TABLE public.arm_watertableriskrating OWNER TO "bcarm";

--
-- Name: arm_watertableriskrating_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.arm_watertableriskrating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.arm_watertableriskrating_id_seq OWNER TO "bcarm";

--
-- Name: arm_watertableriskrating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.arm_watertableriskrating_id_seq OWNED BY public.arm_watertableriskrating.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO "bcarm";

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO "bcarm";

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO "bcarm";

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO "bcarm";

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO "bcarm";

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO "bcarm";

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO "bcarm";

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO "bcarm";

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO "bcarm";

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO "bcarm";

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO "bcarm";

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO "bcarm";

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO "bcarm";

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO "bcarm";

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO "bcarm";

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO "bcarm";

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO "bcarm";

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO "bcarm";

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO "bcarm";

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: bcarm
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO "bcarm";

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: bcarm
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO "bcarm";

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bcarm
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: arm_applicationequipmentoption id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_applicationequipmentoption ALTER COLUMN id SET DEFAULT nextval('public.arm_applicationequipmentoption_id_seq'::regclass);


--
-- Name: arm_applicationriskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_applicationriskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_applicationriskrating_id_seq'::regclass);


--
-- Name: arm_criticalareaoption id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_criticalareaoption ALTER COLUMN id SET DEFAULT nextval('public.arm_criticalareaoption_id_seq'::regclass);


--
-- Name: arm_criticalareariskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_criticalareariskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_criticalareariskrating_id_seq'::regclass);


--
-- Name: arm_foragedensityoption id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_foragedensityoption ALTER COLUMN id SET DEFAULT nextval('public.arm_foragedensityoption_id_seq'::regclass);


--
-- Name: arm_foragedensityriskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_foragedensityriskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_foragedensityriskrating_id_seq'::regclass);


--
-- Name: arm_forageheightoption id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_forageheightoption ALTER COLUMN id SET DEFAULT nextval('public.arm_forageheightoption_id_seq'::regclass);


--
-- Name: arm_forageheightriskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_forageheightriskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_forageheightriskrating_id_seq'::regclass);


--
-- Name: arm_formfield id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_formfield ALTER COLUMN id SET DEFAULT nextval('public.arm_formfield_id_seq'::regclass);


--
-- Name: arm_manuresetbackdistanceriskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_manuresetbackdistanceriskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_manuresetbackdistanceriskrating_id_seq'::regclass);


--
-- Name: arm_preciptation24riskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_preciptation24riskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_preciptation24riskrating_id_seq'::regclass);


--
-- Name: arm_preciptation72riskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_preciptation72riskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_preciptation72riskrating_id_seq'::regclass);


--
-- Name: arm_riskcutoffsetting id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_riskcutoffsetting ALTER COLUMN id SET DEFAULT nextval('public.arm_riskcutoffsetting_id_seq'::regclass);


--
-- Name: arm_soilmoistureoption id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_soilmoistureoption ALTER COLUMN id SET DEFAULT nextval('public.arm_soilmoistureoption_id_seq'::regclass);


--
-- Name: arm_soilmoistureriskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_soilmoistureriskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_soilmoistureriskrating_id_seq'::regclass);


--
-- Name: arm_soiltypeoption id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_soiltypeoption ALTER COLUMN id SET DEFAULT nextval('public.arm_soiltypeoption_id_seq'::regclass);


--
-- Name: arm_soiltyperiskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_soiltyperiskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_soiltyperiskrating_id_seq'::regclass);


--
-- Name: arm_surfaceconditionoption id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_surfaceconditionoption ALTER COLUMN id SET DEFAULT nextval('public.arm_surfaceconditionoption_id_seq'::regclass);


--
-- Name: arm_surfaceconditionriskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_surfaceconditionriskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_surfaceconditionriskrating_id_seq'::regclass);


--
-- Name: arm_watertabledepthoption id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_watertabledepthoption ALTER COLUMN id SET DEFAULT nextval('public.arm_watertabledepthoption_id_seq'::regclass);


--
-- Name: arm_watertableriskrating id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_watertableriskrating ALTER COLUMN id SET DEFAULT nextval('public.arm_watertableriskrating_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Data for Name: arm_applicationequipmentoption; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_applicationequipmentoption (id, value, description, active) FROM stdin;
1	below_application	Below surface applicator (eg, injector, incorportaion within 24 hours)	t
2	surface_application	Surface application (eg, splash plate, tank, aerator)	t
3	irrigation_sprinkler	Irrigation sprinkler (eg, Big Gun)	t
4	grazing	Grazing	t
5	soild_manure_application	Solid manure or fertilizer application	t
\.


--
-- Data for Name: arm_applicationriskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_applicationriskrating (id, applicator_name, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message) FROM stdin;
1	below_application	2	Low-Med	This is a low risk method of application. Watch for compaction on your field if soil is wet. Follow current manure setback distances.	f	\N
2	surface_application	3	Low-Med	Be cautious of turnaround areas and low spots. Watch for compaction on your field if applying to wet soils. Follow current manure setback distances. Use of an aerator is a good method when applying to grass in a higher risk time.	f	\N
3	irrigation_sprinkler	6	Medium	While this method decreases compaction issues, it may increase the likelihood of runoff of manure from the surface of your field. Do not apply to saturated soils. Be sure to observe manure setbacks from critical areas at all times. Do not use this method if wind speed is greater than 10 mph.	f	\N
4	grazing	3	Low-Med	Grazing is a form of manure application. Be sure to observe manure application setback distances and maintain field cover to reduce a runoff event.	f	\N
5	soild_manure_application	5	Medium	Solid manure guidelines are the same as liquid manure. Follow all setback guidance. Make sure soild manure is spread evenly and incorporated into the soil surface prior to a rain event, which can significantly increase the probablility of a runoff event.	f	\N
\.


--
-- Data for Name: arm_criticalareaoption; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_criticalareaoption (id, description, active, value) FROM stdin;
1	Yes (answer next question)	t	yes
2	No	t	no
\.


--
-- Data for Name: arm_criticalareariskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_criticalareariskrating (id, answer, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message) FROM stdin;
1	yes	3	Low-Med	\N	f	\N
2	no	1	Low	\N	f	\N
\.


--
-- Data for Name: arm_foragedensityoption; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_foragedensityoption (id, value, description, active) FROM stdin;
5	-1	Other: Annual/Fallow/Row Crop Field (eg, new seeding, corn, berry, bare soil, etc.)	t
4	50	< 50% cover	t
3	60	50-70% cover	t
2	80	70-90% cover	t
1	100	90-100% cover	t
\.


--
-- Data for Name: arm_foragedensityriskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_foragedensityriskrating (id, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message, range_minimum, range_maximum) FROM stdin;
1	1	Low		f	\N	90.01	100.00
2	4	Medium	Caution: Cover is adequate, but make sure a dense filter strip lies adjacent to any waterways and/or observe seasonal setbacks from waterways, swales, and other areas that could lead to a ditch.	f	\N	70.01	90.00
3	7	Med-High	Caution: Cover is adequate, but make sure a dense filter strip lies adjacent to any waterways and/or observe seasonal setbacks from waterways, swales, and other areas that could lead to a ditch.	f	\N	50.01	70.00
4	9	High	Caution: Your field is at a higher risk for runoff. Observe 80 foot setbacks from ditches, waterways, swales etc, unless an adequate filter strip is in place next to waterway. In no water is adjacent to field, application is permitted.	f	\N	0.00	50.00
5	5	Medium		f	\N	-1.00	-1.00
\.


--
-- Data for Name: arm_forageheightoption; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_forageheightoption (id, value, description, active) FROM stdin;
1	0.0	No cover or < 2.5 cm (< 1 in)	t
2	5.0	2.5-7.5 cm (1-3 in)	t
3	10.0	7.5-15 cm (3-6 in)	t
4	20.0	>15 cm (>6 in)	t
5	-1.0	Not forage crop	t
\.


--
-- Data for Name: arm_forageheightriskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_forageheightriskrating (id, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message, range_minimum, range_maximum) FROM stdin;
1	1	Low		f	\N	15.01	999.00
2	4	Low-Med		f	\N	7.51	15.00
3	8	Med-High	Caution: There is an elevated water table at this location, which can cause a runoff event. Watch for ponding in low spots and soil saturation, and restrict application rates.	f	\N	2.51	7.50
4	8	High	Caution: There is an elevated water table at this location, which can cause a runoff event. Watch for ponding in low spots and soil saturation, and restrict application rates.	f	\N	0.00	2.50
5	2	Low-Med		f	\N	-1.00	-1.00
\.


--
-- Data for Name: arm_formfield; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_formfield (id, field_name, title, description) FROM stdin;
6	72Preciptation	72 hour Precipitation ( mm )	<a target="_blank" href="https://agri-nmp-msa.pathfinder.gov.bc.ca/">BC precipitation</a>
5	24Preciptation	24 hour Precipitation ( mm )	<a target="_blank" href="https://agri-nmp-msa.pathfinder.gov.bc.ca/">BC precipitation</a>
14	WaterbodyCriticalArea	Watercourse or Critical Area	Do you have a watercourse (i.e. stream, river, ditch, etc.) or identified critical area (i.e., swale, wetland, etc.) adjacent to your field (within 20 m)?
15	ManureSetback	<b>Manure Setback Distance (m)</b>	<i>Nutrient application setbacks must be at least 1.5 m for commercial fertilizers or subsurface injection of manures, or 3 m for other nutrient sources such as broadcast manure. As a beneficial management practice, a setback of 12 m or more is recommended.</i><br/><br/>How far away from the waterbody's high-water mark is manure set back during application?
8	SoilMoisture	Soil Moisture	
1	Main	BC Application Risk Management (ARM) Tool	Fill out this form no more than 24 hours <b>prior</b> to manure or fertilizer application. You can group similar fields together into one field unit.<br><br>After completion, please keep a copy of the questionnaire for your records. Information entered on this page is for assessment purposes only and is not shared with the Government of British Columbia.
12	FieldSurfaceConditions	Field Surface Condition	Check all that apply to your current field conditions. Selecting flooding, frozen soil, or snow or ice-covered soil will prevent saving or emailing this questionnaire as manure and fertilizer application is prohibited under these conditions.
11	ForageHeight	Forage Height	
13	ManureApplicationEquipment	Nutrient Application Equipment	Check equipment/method of application
10	ForageDensity	Forage Density ( % )	<a  target="_blank" href="https://www2.gov.bc.ca/gov/content/industry/agriculture-seafood/agricultural-land-and-environment/soil-nutrients/nutrient-management/what-to-apply/manure-application-seasonal-restrictions/field-cover-determination">Guidance on determining forage density</a>
9	WaterTableDepth	Water Table Depth	Current water table depth can be determined by nearby ditches, or by digging a hole in your field. In many areas, the water table may not be near the soil surface.<br><br> <a target="_blank" href="https://www2.gov.bc.ca/gov/content/industry/agriculture-seafood/agricultural-land-and-environment/soil-nutrients/nutrient-management/what-to-apply/manure-application-seasonal-restrictions/water-table-depth-determination">Guidance on determining water table depth</a>
7	SoilType	Soil Type	Enter the general soil type you want to apply to. The <a target="_blank" href="https://www2.gov.bc.ca/gov/content/environment/air-land-water/land/soil/soil-information-finder">B.C. Soil Information Finder Tool</a> (SIFT) can be used to determine soil type.
2	FarmName	Farm Name	
3	ApplicationDate	Application Date	Date you want to apply: You must do this evaluation no more than 24 hours prior to application.
4	FieldName	Field Name or Unit	Do a separate evaluation for each field or management unit. A "management unit" is a group of fields with similar soil, crop type, and management conditions.
\.


--
-- Data for Name: arm_manuresetbackdistanceriskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_manuresetbackdistanceriskrating (id, distance_minimum, distance_maximum, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message) FROM stdin;
2	1.50	11.99	4	Medium	Warning: Your setback is either lower than legal requirements or the recommended setback distance. Increasing setback distance will reduce the risk of off-site nutrient transport.	f	\N
1	12.00	99999999.00	1	Low		f	
3	0.00	1.49	7	Med-High	Warning: Your setback is either lower than legal requirements or the recommended setback distance. Increasing setback distance will reduce the risk of off-site nutrient transport.	t	STOP: NO APPLICATION PERMITTED
\.


--
-- Data for Name: arm_preciptation24riskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_preciptation24riskrating (id, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message, range_minimum, range_maximum) FROM stdin;
1	1	Low		f	\N	0.00	0.24
2	2	Low-Med		f	\N	0.25	1.24
3	3	Low-Med		f	\N	1.25	1.99
4	4	Medium		f	\N	2.00	2.49
6	5	Medium		f	\N	2.50	3.74
7	6	Medium		f	\N	3.75	4.99
8	7	Med-High		f	\N	5.00	6.24
9	8	Med-High	Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate.	f	\N	6.25	8.74
10	9	High	Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate.	f	\N	8.75	12.49
11	10	Extreme	Caution: More than 12 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate.	f	\N	12.50	999.00
\.


--
-- Data for Name: arm_preciptation72riskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_preciptation72riskrating (id, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message, range_minimum, range_maximum) FROM stdin;
1	1	Low		f	\N	0.00	1.24
2	2	Low-Med		f	\N	1.25	2.49
3	3	Low-Med		f	\N	2.50	4.99
4	4	Medium		f	\N	5.00	6.24
5	5	Medium	Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate.	f	\N	6.25	7.49
6	6	Medium	Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate.	f	\N	7.50	8.74
7	7	Med-High	Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate.	f	\N	8.75	9.99
8	8	Med-High	Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate.	f	\N	10.00	12.49
9	9	High	Caution: More than 12 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate.	f	\N	12.50	16.24
10	10	Extreme	Caution: More than 12 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate.	f	\N	16.00	999.00
\.


--
-- Data for Name: arm_riskcutoffsetting; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_riskcutoffsetting (id, risk_level_name, display, minimum_score, maximum_score, message) FROM stdin;
1	low	LOW RISK	0	27	The risk associated with manure application is low. Follow all guidelines and recommendations in your Plan for proper application.
2	med	MEDIUM RISK	28	41	Apply manure with caution. Follow all guidelines and recommendations in your Plan for proper application.
3	high	HIGH RISK	42	999	Do NOT apply manure at this time, the risk is too high. Wait and reevaluate.
\.


--
-- Data for Name: arm_soilmoistureoption; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_soilmoistureoption (id, value, description, active) FROM stdin;
1	95	90-100% (If your boots squish in the field, you are at saturation)	t
2	85	80-90% (In this range you would not comforatably drive a tractor into the field  and are worried about potential soil compaction due to field wetness)	t
3	60	60-80% (In this range you could comfortably drive a tractor out into the field without worrying about ruts or field compaction)	t
4	50	< 60% (In this range your soil is firm and starting to dry out)	t
\.


--
-- Data for Name: arm_soilmoistureriskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_soilmoistureriskrating (id, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message, range_minimum, range_maximum) FROM stdin;
1	1	Low		f	\N	0.00	59.99
2	2	Low-Med		f	\N	60.00	79.99
3	9	High	Caution: You may be at risk for runoff if soils are saturated. Check field conditions and the forecast, and restrict application rates so you don’t saturate your field.	f	\N	80.00	89.99
4	10	Extreme	Caution: You may be at risk for runoff if soils are saturated. Check field conditions and the forecast, and restrict application rates so you don’t saturate your field.	t	Stop: Do not apply at this time. The soil moisture is too high and the risk of runoff on this field is very high.	90.00	100.00
\.


--
-- Data for Name: arm_soiltypeoption; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_soiltypeoption (id, value, description, active) FROM stdin;
5	other	Don't know	t
1	sand	Coarse-Textured (Gravel, Sand, Loamy Sand, Sandy Loam)	t
2	silt	Medium-Textured (Loam, Silt Loam, Silt)	t
3	clay	Fine-Textured (Clay Loam, Silty Clay Loam, Silt Clay, Sandy Clay, Clay)	t
4	peat_muck	Organic (Peat/Muck)	t
\.


--
-- Data for Name: arm_soiltyperiskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_soiltyperiskrating (id, soil_type, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message) FROM stdin;
1	sand	1	Low	\N	f	\N
2	silt	2	Low-Med	\N	f	\N
3	clay	5	Medium	\N	f	\N
4	peat_muck	6	Medium	\N	f	\N
5	other	4	Medium	\N	f	\N
\.


--
-- Data for Name: arm_surfaceconditionoption; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_surfaceconditionoption (id, value, description, active) FROM stdin;
1	ponding	Ponding	t
5	tiles	Tiles present in field	t
6	none	None of the above	t
2	flooding	Flooding [current or potential (within 15 days)]	t
4	snow-ice	Snow or ice-covered soil [5 cm / 2 in or more of snow over 50% (or more) of the field]	t
3	frozen	Frozen soil [more than 5 cm / 2 in]	t
\.


--
-- Data for Name: arm_surfaceconditionriskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_surfaceconditionriskrating (id, surface_condition, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message) FROM stdin;
1	ponding	5	Medium	Ponding - Caution: Avoid ponded areas with appropriate seasonal setback distance, particularly if it drains to a waterway. Ponding can be a sign of a high water table, so be cautious of soil saturation.	f	\N
2	tiles	6	Medium	Tiles - Caution: Tiles must have at least 60 cm of cover, not be discharging manure, and their location must be known prior to application. Monitor tiles closely after application. If manure discharges from tile, plug immediately.	f	\N
3	none	0	Low	\N	f	\N
4	flooding	10	Extreme	Flooding - No application is allowed if flooding is predicted in a 15 day window after application.	t	Stop: No Application permitted
5	frozen	10	Extreme	Frozen - No application is allowed on soils frozen 2,5 cm or greater below the surface, or covered in snow.	t	Stop: No Application permitted
6	snow-ice	10	Extreme	Snow covered - No application is allowed if a field has at least 5 cm (2 in) or more of ice or snow over 50% or more of the area.	t	Stop: No Application permitted
\.


--
-- Data for Name: arm_watertabledepthoption; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_watertabledepthoption (id, value, description, active) FROM stdin;
1	15	0-30 cm (1-12 in)	t
2	40	30-60 cm (12-24 in)	t
3	90	60-120 cm (24-48 in)	t
4	150	> 120 cm (> 48 in)	t
\.


--
-- Data for Name: arm_watertableriskrating; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.arm_watertableriskrating (id, risk_value, risk_display_text, caution_message, show_stop_application, stop_application_message, range_minimum, range_maximum) FROM stdin;
1	1	Low		f	\N	120.00	999.00
2	4	Medium		f	\N	60.00	119.99
3	8	Med-High	Caution: There is an elevated water table at this location, which can cause a runoff event. Watch for ponding in low spots and soil saturation, and restrict application rates.	f	\N	30.00	59.99
4	10	Extreme	Caution: There is an elevated water table at this location, which can cause a runoff event. Watch for ponding in low spots and soil saturation, and restrict application rates.	f	\N	0.00	29.99
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can view permission	1	view_permission
5	Can add group	2	add_group
6	Can change group	2	change_group
7	Can delete group	2	delete_group
8	Can view group	2	view_group
9	Can add user	3	add_user
10	Can change user	3	change_user
11	Can delete user	3	delete_user
12	Can view user	3	view_user
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add site	6	add_site
22	Can change site	6	change_site
23	Can delete site	6	delete_site
24	Can view site	6	view_site
25	Can add log entry	7	add_logentry
26	Can change log entry	7	change_logentry
27	Can delete log entry	7	delete_logentry
28	Can view log entry	7	view_logentry
29	Can add application equipment option	8	add_applicationequipmentoption
30	Can change application equipment option	8	change_applicationequipmentoption
31	Can delete application equipment option	8	delete_applicationequipmentoption
32	Can view application equipment option	8	view_applicationequipmentoption
33	Can add application risk rating	9	add_applicationriskrating
34	Can change application risk rating	9	change_applicationriskrating
35	Can delete application risk rating	9	delete_applicationriskrating
36	Can view application risk rating	9	view_applicationriskrating
37	Can add caution message	10	add_cautionmessage
38	Can change caution message	10	change_cautionmessage
39	Can delete caution message	10	delete_cautionmessage
40	Can view caution message	10	view_cautionmessage
41	Can add critical area risk rating	11	add_criticalareariskrating
42	Can change critical area risk rating	11	change_criticalareariskrating
43	Can delete critical area risk rating	11	delete_criticalareariskrating
44	Can view critical area risk rating	11	view_criticalareariskrating
45	Can add forage density option	12	add_foragedensityoption
46	Can change forage density option	12	change_foragedensityoption
47	Can delete forage density option	12	delete_foragedensityoption
48	Can view forage density option	12	view_foragedensityoption
49	Can add forage height option	13	add_forageheightoption
50	Can change forage height option	13	change_forageheightoption
51	Can delete forage height option	13	delete_forageheightoption
52	Can view forage height option	13	view_forageheightoption
53	Can add form field	14	add_formfield
54	Can change form field	14	change_formfield
55	Can delete form field	14	delete_formfield
56	Can view form field	14	view_formfield
57	Can add manure setback distance risk rating	15	add_manuresetbackdistanceriskrating
58	Can change manure setback distance risk rating	15	change_manuresetbackdistanceriskrating
59	Can delete manure setback distance risk rating	15	delete_manuresetbackdistanceriskrating
60	Can view manure setback distance risk rating	15	view_manuresetbackdistanceriskrating
61	Can add restriction stop message	16	add_restrictionstopmessage
62	Can change restriction stop message	16	change_restrictionstopmessage
63	Can delete restriction stop message	16	delete_restrictionstopmessage
64	Can view restriction stop message	16	view_restrictionstopmessage
65	Can add risk cutoff setting	17	add_riskcutoffsetting
66	Can change risk cutoff setting	17	change_riskcutoffsetting
67	Can delete risk cutoff setting	17	delete_riskcutoffsetting
68	Can view risk cutoff setting	17	view_riskcutoffsetting
69	Can add risk rating value	18	add_riskratingvalue
70	Can change risk rating value	18	change_riskratingvalue
71	Can delete risk rating value	18	delete_riskratingvalue
72	Can view risk rating value	18	view_riskratingvalue
73	Can add soil moisture option	19	add_soilmoistureoption
74	Can change soil moisture option	19	change_soilmoistureoption
75	Can delete soil moisture option	19	delete_soilmoistureoption
76	Can view soil moisture option	19	view_soilmoistureoption
77	Can add soil type option	20	add_soiltypeoption
78	Can change soil type option	20	change_soiltypeoption
79	Can delete soil type option	20	delete_soiltypeoption
80	Can view soil type option	20	view_soiltypeoption
81	Can add soil type risk rating	21	add_soiltyperiskrating
82	Can change soil type risk rating	21	change_soiltyperiskrating
83	Can delete soil type risk rating	21	delete_soiltyperiskrating
84	Can view soil type risk rating	21	view_soiltyperiskrating
85	Can add surface condition option	22	add_surfaceconditionoption
86	Can change surface condition option	22	change_surfaceconditionoption
87	Can delete surface condition option	22	delete_surfaceconditionoption
88	Can view surface condition option	22	view_surfaceconditionoption
89	Can add surface condition risk rating	23	add_surfaceconditionriskrating
90	Can change surface condition risk rating	23	change_surfaceconditionriskrating
91	Can delete surface condition risk rating	23	delete_surfaceconditionriskrating
92	Can view surface condition risk rating	23	view_surfaceconditionriskrating
93	Can add water table depth option	24	add_watertabledepthoption
94	Can change water table depth option	24	change_watertabledepthoption
95	Can delete water table depth option	24	delete_watertabledepthoption
96	Can view water table depth option	24	view_watertabledepthoption
97	Can add forage density risk rating	25	add_foragedensityriskrating
98	Can change forage density risk rating	25	change_foragedensityriskrating
99	Can delete forage density risk rating	25	delete_foragedensityriskrating
100	Can view forage density risk rating	25	view_foragedensityriskrating
101	Can add forage height risk rating	26	add_forageheightriskrating
102	Can change forage height risk rating	26	change_forageheightriskrating
103	Can delete forage height risk rating	26	delete_forageheightriskrating
104	Can view forage height risk rating	26	view_forageheightriskrating
105	Can add preciptation24 risk rating	27	add_preciptation24riskrating
106	Can change preciptation24 risk rating	27	change_preciptation24riskrating
107	Can delete preciptation24 risk rating	27	delete_preciptation24riskrating
108	Can view preciptation24 risk rating	27	view_preciptation24riskrating
109	Can add preciptation72 risk rating	28	add_preciptation72riskrating
110	Can change preciptation72 risk rating	28	change_preciptation72riskrating
111	Can delete preciptation72 risk rating	28	delete_preciptation72riskrating
112	Can view preciptation72 risk rating	28	view_preciptation72riskrating
113	Can add soil moisture risk rating	29	add_soilmoistureriskrating
114	Can change soil moisture risk rating	29	change_soilmoistureriskrating
115	Can delete soil moisture risk rating	29	delete_soilmoistureriskrating
116	Can view soil moisture risk rating	29	view_soilmoistureriskrating
117	Can add water table risk rating	30	add_watertableriskrating
118	Can change water table risk rating	30	change_watertableriskrating
119	Can delete water table risk rating	30	delete_watertableriskrating
120	Can view water table risk rating	30	view_watertableriskrating
121	Can add critical area option	31	add_criticalareaoption
122	Can change critical area option	31	change_criticalareaoption
123	Can delete critical area option	31	delete_criticalareaoption
124	Can view critical area option	31	view_criticalareaoption
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$150000$xIc12TAznw9c$lySNgjuJ/8aWgLGzy0/mrofmPPsVzyFzbI+yuOK+e40=	2020-09-25 21:34:00.014134+00	t	arm-admin				t	t	2019-08-31 14:16:16.508+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2019-09-20 16:04:33.386107+00	1	Main: It is recommended that you fill out this form no more than 24 hours <u>prior</u> to a manure application event, particularly from October through February. You can group similar fields together 	2	[{"changed": {"fields": ["description"]}}]	14	1
2	2019-09-20 16:05:18.690541+00	5	24Preciptation: Link to <a target="_blank" href="https://maps.whatcomcd.org/bc_msa">BC precipitation</a>	2	[{"changed": {"fields": ["description"]}}]	14	1
3	2019-09-20 16:05:38.515749+00	6	72Preciptation: Link to <a target="_blank" href="https://maps.whatcomcd.org/bc_msa">BC precipitation</a>	2	[{"changed": {"fields": ["description"]}}]	14	1
4	2019-09-20 16:05:47.393702+00	7	SoilType: Enter the general soil type you want to apply to. If you dont know your soil type, make your selection under "Don't know". Soil type can be found on your farm plan map.	2	[]	14	1
5	2019-09-20 16:05:58.990488+00	3	SoilTypeOption object (3)	2	[{"changed": {"fields": ["description"]}}]	20	1
6	2019-09-20 16:06:05.037895+00	2	SoilTypeOption object (2)	2	[{"changed": {"fields": ["description"]}}]	20	1
7	2019-09-20 16:06:11.065092+00	1	SoilTypeOption object (1)	2	[{"changed": {"fields": ["description"]}}]	20	1
8	2019-09-20 16:06:38.559367+00	9	WaterTableDepth: Water table can be determined by nearby ditches, or by digging a hole in your field. For more on how to determine water table depth, click <a target="_blank" href="http://www.wadairyp	2	[{"changed": {"fields": ["description"]}}]	14	1
9	2019-09-20 16:08:42.93135+00	8	SoilMoisture: Enter moisture value in %.	2	[{"changed": {"fields": ["description"]}}]	14	1
10	2019-09-20 16:12:44.603602+00	1	Main: It is recommended that you fill out this form no more than 24 hours <u>prior</u> to a manure application event, particularly from October through March. You can group similar fields together int	2	[{"changed": {"fields": ["description"]}}]	14	1
11	2019-09-20 16:20:00.863844+00	1	Main: It is recommended that you fill out this form no more than 24 hours <i>prior</i> to a manure application event, particularly from October through March. You can group similar fields together int	2	[{"changed": {"fields": ["description"]}}]	14	1
12	2019-09-20 16:21:55.306616+00	1	Main: This form should be filled out no more than 24 hours <i>prior</i> to a manure application event. You can group similar fields together into one field unit. For questions related to filling out a	2	[{"changed": {"fields": ["description"]}}]	14	1
13	2019-09-20 16:22:33.344536+00	1	Main: This form should be filled out no more than 24 hours <i>prior</i> to a manure application event. You can group fields with similar conditions together into one field unit. For questions related 	2	[{"changed": {"fields": ["description"]}}]	14	1
14	2019-09-20 16:22:51.709801+00	1	Main: This form should be filled out no more than 24 hours <i>prior</i> to a manure application event. You can group fields with similar conditions together into one field unit. <br><br> The completed	2	[{"changed": {"fields": ["description"]}}]	14	1
15	2019-09-20 16:23:01.737672+00	1	Main: This form should be filled out no more than 24 hours <i>prior</i> to a manure application event. You can group fields with similar conditions together into one field unit. <br><br> The completed	2	[]	14	1
16	2019-09-20 16:24:13.391342+00	1	SoilTypeOption object (1)	2	[{"changed": {"fields": ["description"]}}]	20	1
17	2019-09-20 16:24:58.886589+00	10	ForageDensity: Click link for guidance on how to determine forage density <a  target="_blank" href="http://www.wadairyplan.org/ARM/forage-density-determination">here</a>	2	[]	14	1
18	2019-09-20 16:26:15.725612+00	7	SoilType: Enter the general soil type you want to apply to. If you don't know your soil type, make your selection under "Don't know". Soil type can be found use the <a  target="_blank" href="https://w	2	[{"changed": {"fields": ["description"]}}]	14	1
19	2019-09-20 16:26:31.270825+00	7	SoilType: Enter the general soil type you want to apply to. If you don't know your soil type, make your selection under "Don't know". Soil type can be found use the <a  target="_blank" href="https://w	2	[]	14	1
20	2019-09-20 16:29:53.432979+00	1	SoilTypeOption object (1)	2	[{"changed": {"fields": ["description"]}}]	20	1
21	2019-09-20 16:30:00.429867+00	2	SoilTypeOption object (2)	2	[{"changed": {"fields": ["description"]}}]	20	1
22	2019-09-20 16:30:08.095436+00	3	SoilTypeOption object (3)	2	[{"changed": {"fields": ["description"]}}]	20	1
23	2019-09-20 16:30:14.509168+00	4	SoilTypeOption object (4)	2	[{"changed": {"fields": ["description"]}}]	20	1
24	2019-09-20 16:47:46.004893+00	1	Main: This form should be filled out no more than 24 hours <b>prior</b> to a manure application event. You can group fields with similar conditions together into one field unit. <br><br> The completed	2	[{"changed": {"fields": ["description"]}}]	14	1
25	2019-09-20 17:02:19.446835+00	4	SurfaceConditionOption object (4)	2	[{"changed": {"fields": ["description"]}}]	22	1
26	2019-09-20 17:19:27.562684+00	4	SurfaceConditionOption object (4)	2	[{"changed": {"fields": ["description"]}}]	22	1
27	2019-09-20 17:21:30.566722+00	3	SurfaceConditionOption object (3)	2	[{"changed": {"fields": ["description"]}}]	22	1
28	2019-09-20 17:23:21.652976+00	3	SurfaceConditionOption object (3)	2	[{"changed": {"fields": ["description"]}}]	22	1
29	2019-09-20 17:23:36.992671+00	3	SurfaceConditionOption object (3)	2	[{"changed": {"fields": ["description"]}}]	22	1
30	2019-09-20 17:24:15.07083+00	4	SurfaceConditionOption object (4)	2	[{"changed": {"fields": ["description"]}}]	22	1
31	2019-09-20 17:34:53.269772+00	5	SurfaceConditionRiskRating object (5)	2	[{"changed": {"fields": ["caution_message"]}}]	23	1
32	2019-09-20 17:35:59.669571+00	3	SurfaceConditionOption object (3)	2	[{"changed": {"fields": ["description"]}}]	22	1
33	2019-09-20 17:36:30.396316+00	3	SurfaceConditionOption object (3)	2	[{"changed": {"fields": ["description"]}}]	22	1
34	2019-09-20 17:37:19.046932+00	5	SurfaceConditionRiskRating object (5)	2	[{"changed": {"fields": ["caution_message"]}}]	23	1
35	2019-09-20 17:38:30.599113+00	3	SurfaceConditionOption object (3)	2	[{"changed": {"fields": ["description"]}}]	22	1
36	2019-09-20 18:10:04.835313+00	10	ForageDensity: <a  target="_blank" href="http://www.wadairyplan.org/ARM/forage-density-determination">Guidance on determining forage density</a>	2	[{"changed": {"fields": ["description"]}}]	14	1
37	2019-09-20 18:10:20.598908+00	10	ForageDensity: <a  target="_blank" href="http://www.wadairyplan.org/ARM/forage-density-determination">Guidance on determining forage density</a>	2	[]	14	1
38	2019-09-20 18:11:48.422779+00	9	WaterTableDepth: Water table can be determined by nearby ditches, or by digging a hole in your field.<br><br><a target="_blank" href="http://www.wadairyplan.org/ARM/water-table-depth-determination">Gu	2	[{"changed": {"fields": ["description"]}}]	14	1
39	2019-09-25 20:02:06.266785+00	1	CriticalAreaOption object (1)	1	[{"added": {}}]	31	1
40	2019-09-25 20:02:13.341818+00	2	CriticalAreaOption object (2)	1	[{"added": {}}]	31	1
41	2019-09-25 20:37:02.253914+00	1	Main: Fill out this form no more than 24 hours <b>prior</b> to a manure application event. You can group similar fields together into one field unit.<br><br>After completion, please keep a copy of the	2	[{"changed": {"fields": ["description"]}}]	14	1
42	2019-09-25 20:40:41.715868+00	7	SoilType: Enter the general soil type you want to apply to. The <a target="_blank" href="https://www2.gov.bc.ca/gov/content/environment/air-land-water/land/soil/soil-information-finder">B.C. Soil Info	2	[{"changed": {"fields": ["description"]}}]	14	1
43	2019-09-25 20:40:56.073181+00	7	SoilType: Enter the general soil type you want to apply to. The <a target="_blank" href="https://www2.gov.bc.ca/gov/content/environment/air-land-water/land/soil/soil-information-finder">B.C. Soil Info	2	[]	14	1
44	2019-09-25 20:41:57.668011+00	5	24Preciptation: <a target="_blank" href="https://maps.whatcomcd.org/bc_msa">BC precipitation</a>	2	[{"changed": {"fields": ["description"]}}]	14	1
45	2019-09-25 20:42:04.652418+00	5	24Preciptation: <a target="_blank" href="https://maps.whatcomcd.org/bc_msa">BC precipitation</a>	2	[]	14	1
46	2019-09-25 20:42:10.685315+00	6	72Preciptation: <a target="_blank" href="https://maps.whatcomcd.org/bc_msa">BC precipitation</a>	2	[{"changed": {"fields": ["description"]}}]	14	1
47	2019-09-25 20:43:49.351293+00	1	SoilTypeOption object (1)	2	[{"changed": {"fields": ["description"]}}]	20	1
48	2019-09-25 20:44:55.138345+00	2	SoilTypeOption object (2)	2	[{"changed": {"fields": ["description"]}}]	20	1
49	2019-09-25 20:45:01.833583+00	3	SoilTypeOption object (3)	2	[{"changed": {"fields": ["description"]}}]	20	1
50	2019-09-25 20:45:09.349508+00	4	SoilTypeOption object (4)	2	[{"changed": {"fields": ["description"]}}]	20	1
51	2019-09-25 20:45:31.05067+00	8	SoilMoisture: Enter moisture value in %.	2	[{"changed": {"fields": ["description"]}}]	14	1
52	2019-09-25 20:46:47.781686+00	10	ForageDensity: <a  target="_blank" href="http://www.wadairyplan.org/ARM/forage-density-determination">Guidance on determining forage density</a>	2	[{"changed": {"fields": ["description"]}}]	14	1
53	2019-09-25 20:50:30.877675+00	9	WaterTableDepth: Water table can be determined by nearby ditches, or by digging a hole in your field. In many areas, the water table may not be near the soil surface.<br><br> <a target="_blank" href="	2	[{"changed": {"fields": ["description"]}}]	14	1
54	2019-09-25 20:52:12.678487+00	15	ManureSetback: How far away from the waterbody's high-water mark is manure, fertilizer, or other nutrients set back during application?<br/><br/>Nutrient application setbacks must be at least 1.5 m fo	2	[{"changed": {"fields": ["title"]}}]	14	1
55	2019-09-25 20:53:14.816857+00	15	ManureSetback: How far away from the waterbody's high-water mark is manure, fertilizer, or other nutrients set back during application?<br/><br/><i>Nutrient application setbacks must be at least 1.5 m	2	[{"changed": {"fields": ["description"]}}]	14	1
56	2019-09-25 21:08:49.632739+00	1	Main: Fill out this form no more than 24 hours <b>prior</b> to manure application. You can group similar fields together into one field unit.<br><br>After completion, please keep a copy of the questio	2	[{"changed": {"fields": ["description"]}}]	14	1
57	2019-09-25 21:23:51.011935+00	14	WaterbodyCriticalArea: Do you have a waterbody (i.e. stream, river, actively draining ditch, etc.) or identified critical area (i.e., swale, wetland, etc.) adjacent to your field (within 20 m)?	2	[{"changed": {"fields": ["description"]}}]	14	1
58	2019-09-25 21:24:58.841174+00	2	CriticalAreaOption object (2)	2	[{"changed": {"fields": ["description"]}}]	31	1
59	2019-09-25 21:26:18.972085+00	9	WaterTableDepth: Water table can be determined by nearby ditches, or by digging a hole in your field. In many areas, the water table may not be near the soil surface.<br><br> <a target="_blank" href="	2	[{"changed": {"fields": ["description"]}}]	14	1
60	2019-09-25 21:31:38.193124+00	4	SurfaceConditionOption object (4)	2	[{"changed": {"fields": ["description"]}}]	22	1
61	2019-09-25 21:32:34.840931+00	3	SurfaceConditionOption object (3)	2	[{"changed": {"fields": ["description"]}}]	22	1
62	2019-09-25 21:35:47.333872+00	2	SurfaceConditionOption object (2)	2	[{"changed": {"fields": ["description"]}}]	22	1
63	2019-09-25 21:36:38.138127+00	2	SurfaceConditionOption object (2)	2	[{"changed": {"fields": ["description"]}}]	22	1
64	2019-09-25 21:38:14.770317+00	15	ManureSetback: How far away from the waterbody's high-water mark is manure set back during application?<br/><br/><i>Nutrient application setbacks must be at least 1.5 m for commercial fertilizers or s	2	[{"changed": {"fields": ["description"]}}]	14	1
65	2019-09-25 21:39:20.18618+00	3	SurfaceConditionOption object (3)	2	[{"changed": {"fields": ["description"]}}]	22	1
66	2019-09-25 21:40:10.075359+00	4	SurfaceConditionOption object (4)	2	[{"changed": {"fields": ["description"]}}]	22	1
67	2019-09-25 21:45:46.509304+00	12	FieldSurfaceConditions: Check all that apply to your current field conditions. Selecting flooding, frozen soil, or snow or ice-covered soil will prevent saving or emailing this questionnaire as manure	2	[{"changed": {"fields": ["description"]}}]	14	1
68	2019-09-25 21:46:42.810332+00	3	SurfaceConditionOption object (3)	2	[{"changed": {"fields": ["description"]}}]	22	1
69	2019-09-25 21:57:59.533164+00	4	ForageDensityOption object (4)	2	[{"changed": {"fields": ["description"]}}]	12	1
70	2019-09-25 21:58:05.515495+00	3	ForageDensityOption object (3)	2	[{"changed": {"fields": ["description"]}}]	12	1
71	2019-09-25 21:58:11.599775+00	2	ForageDensityOption object (2)	2	[{"changed": {"fields": ["description"]}}]	12	1
72	2019-09-25 21:58:18.039521+00	1	ForageDensityOption object (1)	2	[{"changed": {"fields": ["description"]}}]	12	1
73	2019-09-25 22:56:24.768636+00	9	WaterTableDepth: Current water table depth can be determined by nearby ditches, or by digging a hole in your field. In many areas, the water table may not be near the soil surface.<br><br> <a target="	2	[{"changed": {"fields": ["description"]}}]	14	1
74	2019-09-25 22:57:22.987855+00	14	WaterbodyCriticalArea: Do you have a watercourse (i.e. stream, river, ditch, etc.) or identified critical area (i.e., swale, wetland, etc.) adjacent to your field (within 20 m)?	2	[{"changed": {"fields": ["description"]}}]	14	1
75	2019-09-25 22:58:32.127264+00	14	WaterbodyCriticalArea: Do you have a watercourse (i.e. stream, river, ditch, etc.) or identified critical area (i.e., swale, wetland, etc.) adjacent to your field (within 20 m)?	2	[{"changed": {"fields": ["title"]}}]	14	1
76	2019-09-25 22:59:48.442191+00	15	ManureSetback: <i>Nutrient application setbacks must be at least 1.5 m for commercial fertilizers or subsurface injection of manures, or 3 m for other nutrient sources such as broadcast manure. As a b	2	[{"changed": {"fields": ["description"]}}]	14	1
77	2019-09-25 23:00:08.206967+00	15	ManureSetback: <i>Nutrient application setbacks must be at least 1.5 m for commercial fertilizers or subsurface injection of manures, or 3 m for other nutrient sources such as broadcast manure. As a b	2	[]	14	1
78	2019-09-25 23:01:08.913083+00	8	SoilMoisture: 	2	[{"changed": {"fields": ["description"]}}]	14	1
79	2019-09-25 23:45:59.438452+00	1	Main: Fill out this form no more than 24 hours <b>prior</b> to manure application. You can group similar fields together into one field unit.<br><br>After completion, please keep a copy of the questio	2	[{"changed": {"fields": ["title"]}}]	14	1
80	2019-09-25 23:46:30.31135+00	1	Main: Fill out this form no more than 24 hours <b>prior</b> to manure or fertilizer application. You can group similar fields together into one field unit.<br><br>After completion, please keep a copy 	2	[{"changed": {"fields": ["description"]}}]	14	1
81	2019-09-25 23:47:08.84976+00	12	FieldSurfaceConditions: Check all that apply to your current field conditions. Selecting flooding, frozen soil, or snow or ice-covered soil will prevent saving or emailing this questionnaire as manure	2	[{"changed": {"fields": ["description"]}}]	14	1
82	2019-09-25 23:48:23.079401+00	13	ManureApplicationEquipment: Check equipment/method of application	2	[{"changed": {"fields": ["title"]}}]	14	1
83	2019-09-25 23:49:21.791283+00	5	ApplicationEquipmentOption object (5)	2	[{"changed": {"fields": ["description"]}}]	8	1
84	2019-09-26 18:10:26.561188+00	1	ManureSetbackDistanceRiskRating object (1)	2	[{"changed": {"fields": ["caution_message"]}}]	15	1
85	2019-09-26 18:14:38.788962+00	3	ManureSetbackDistanceRiskRating object (3)	2	[{"changed": {"fields": ["show_stop_application", "stop_application_message"]}}]	15	1
86	2019-10-07 15:35:11.842084+00	10	ForageDensity: <a  target="_blank" href="https://www2.gov.bc.ca/gov/content/industry/agriculture-seafood/agricultural-land-and-environment/soil-nutrients/nutrient-management/what-to-apply/manure-appli	2	[{"changed": {"fields": ["description"]}}]	14	1
87	2019-10-07 15:36:31.162438+00	9	WaterTableDepth: Current water table depth can be determined by nearby ditches, or by digging a hole in your field. In many areas, the water table may not be near the soil surface.<br><br> <a target="	2	[{"changed": {"fields": ["description"]}}]	14	1
88	2020-09-25 21:35:25.854385+00	6	72Preciptation: <a target="_blank" href="https://agri-nmp-msa.pathfinder.gov.bc.ca/">BC precipitation</a>	2	[{"changed": {"fields": ["description"]}}]	14	1
89	2020-09-25 21:35:40.207418+00	5	24Preciptation: <a target="_blank" href="https://agri-nmp-msa.pathfinder.gov.bc.ca/">BC precipitation</a>	2	[{"changed": {"fields": ["description"]}}]	14	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	auth	permission
2	auth	group
3	auth	user
4	contenttypes	contenttype
5	sessions	session
6	sites	site
7	admin	logentry
8	arm	applicationequipmentoption
9	arm	applicationriskrating
10	arm	cautionmessage
11	arm	criticalareariskrating
12	arm	foragedensityoption
13	arm	forageheightoption
14	arm	formfield
15	arm	manuresetbackdistanceriskrating
16	arm	restrictionstopmessage
17	arm	riskcutoffsetting
18	arm	riskratingvalue
19	arm	soilmoistureoption
20	arm	soiltypeoption
21	arm	soiltyperiskrating
22	arm	surfaceconditionoption
23	arm	surfaceconditionriskrating
24	arm	watertabledepthoption
25	arm	foragedensityriskrating
26	arm	forageheightriskrating
27	arm	preciptation24riskrating
28	arm	preciptation72riskrating
29	arm	soilmoistureriskrating
30	arm	watertableriskrating
31	arm	criticalareaoption
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-09-20 14:40:03.780514+00
2	auth	0001_initial	2019-09-20 14:40:03.987309+00
3	admin	0001_initial	2019-09-20 14:40:04.295437+00
4	admin	0002_logentry_remove_auto_add	2019-09-20 14:40:04.355744+00
5	admin	0003_logentry_add_action_flag_choices	2019-09-20 14:40:04.374426+00
6	arm	0001_initial	2019-09-20 14:40:05.058744+00
7	contenttypes	0002_remove_content_type_name	2019-09-20 14:40:05.232029+00
8	auth	0002_alter_permission_name_max_length	2019-09-20 14:40:05.249075+00
9	auth	0003_alter_user_email_max_length	2019-09-20 14:40:05.32741+00
10	auth	0004_alter_user_username_opts	2019-09-20 14:40:05.341845+00
11	auth	0005_alter_user_last_login_null	2019-09-20 14:40:05.426754+00
12	auth	0006_require_contenttypes_0002	2019-09-20 14:40:05.433057+00
13	auth	0007_alter_validators_add_error_messages	2019-09-20 14:40:05.449705+00
14	auth	0008_alter_user_username_max_length	2019-09-20 14:40:05.55044+00
15	auth	0009_alter_user_last_name_max_length	2019-09-20 14:40:05.570238+00
16	auth	0010_alter_group_name_max_length	2019-09-20 14:40:05.637232+00
17	auth	0011_update_proxy_permissions	2019-09-20 14:40:05.734178+00
18	sessions	0001_initial	2019-09-20 14:40:05.78044+00
19	sites	0001_initial	2019-09-20 14:40:05.838498+00
20	sites	0002_alter_domain_unique	2019-09-20 14:40:05.877365+00
21	arm	0002_auto_20190924_1712	2019-09-25 17:20:37.855207+00
22	arm	0003_auto_20190925_0952	2019-09-25 17:20:38.39514+00
23	arm	0004_auto_20190925_1201	2019-09-25 20:00:41.591456+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: bcarm
--

COPY public.django_site (id, domain, name) FROM stdin;
4	example.com	example.com
\.


--
-- Name: arm_applicationequipmentoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_applicationequipmentoption_id_seq', 5, true);


--
-- Name: arm_applicationriskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_applicationriskrating_id_seq', 5, true);


--
-- Name: arm_criticalareaoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_criticalareaoption_id_seq', 2, true);


--
-- Name: arm_criticalareariskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_criticalareariskrating_id_seq', 2, true);


--
-- Name: arm_foragedensityoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_foragedensityoption_id_seq', 5, true);


--
-- Name: arm_foragedensityriskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_foragedensityriskrating_id_seq', 5, true);


--
-- Name: arm_forageheightoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_forageheightoption_id_seq', 5, true);


--
-- Name: arm_forageheightriskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_forageheightriskrating_id_seq', 5, true);


--
-- Name: arm_formfield_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_formfield_id_seq', 15, true);


--
-- Name: arm_manuresetbackdistanceriskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_manuresetbackdistanceriskrating_id_seq', 3, true);


--
-- Name: arm_preciptation24riskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_preciptation24riskrating_id_seq', 11, true);


--
-- Name: arm_preciptation72riskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_preciptation72riskrating_id_seq', 10, true);


--
-- Name: arm_riskcutoffsetting_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_riskcutoffsetting_id_seq', 3, true);


--
-- Name: arm_soilmoistureoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_soilmoistureoption_id_seq', 4, true);


--
-- Name: arm_soilmoistureriskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_soilmoistureriskrating_id_seq', 4, true);


--
-- Name: arm_soiltypeoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_soiltypeoption_id_seq', 5, true);


--
-- Name: arm_soiltyperiskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_soiltyperiskrating_id_seq', 5, true);


--
-- Name: arm_surfaceconditionoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_surfaceconditionoption_id_seq', 6, true);


--
-- Name: arm_surfaceconditionriskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_surfaceconditionriskrating_id_seq', 6, true);


--
-- Name: arm_watertabledepthoption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_watertabledepthoption_id_seq', 4, true);


--
-- Name: arm_watertableriskrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.arm_watertableriskrating_id_seq', 4, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 124, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 89, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 31, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 23, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bcarm
--

SELECT pg_catalog.setval('public.django_site_id_seq', 4, true);


--
-- Name: arm_applicationequipmentoption arm_applicationequipmentoption_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_applicationequipmentoption
    ADD CONSTRAINT arm_applicationequipmentoption_pkey PRIMARY KEY (id);


--
-- Name: arm_applicationriskrating arm_applicationriskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_applicationriskrating
    ADD CONSTRAINT arm_applicationriskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_criticalareaoption arm_criticalareaoption_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_criticalareaoption
    ADD CONSTRAINT arm_criticalareaoption_pkey PRIMARY KEY (id);


--
-- Name: arm_criticalareariskrating arm_criticalareariskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_criticalareariskrating
    ADD CONSTRAINT arm_criticalareariskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_foragedensityoption arm_foragedensityoption_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_foragedensityoption
    ADD CONSTRAINT arm_foragedensityoption_pkey PRIMARY KEY (id);


--
-- Name: arm_foragedensityriskrating arm_foragedensityriskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_foragedensityriskrating
    ADD CONSTRAINT arm_foragedensityriskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_forageheightoption arm_forageheightoption_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_forageheightoption
    ADD CONSTRAINT arm_forageheightoption_pkey PRIMARY KEY (id);


--
-- Name: arm_forageheightriskrating arm_forageheightriskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_forageheightriskrating
    ADD CONSTRAINT arm_forageheightriskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_formfield arm_formfield_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_formfield
    ADD CONSTRAINT arm_formfield_pkey PRIMARY KEY (id);


--
-- Name: arm_manuresetbackdistanceriskrating arm_manuresetbackdistanceriskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_manuresetbackdistanceriskrating
    ADD CONSTRAINT arm_manuresetbackdistanceriskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_preciptation24riskrating arm_preciptation24riskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_preciptation24riskrating
    ADD CONSTRAINT arm_preciptation24riskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_preciptation72riskrating arm_preciptation72riskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_preciptation72riskrating
    ADD CONSTRAINT arm_preciptation72riskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_riskcutoffsetting arm_riskcutoffsetting_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_riskcutoffsetting
    ADD CONSTRAINT arm_riskcutoffsetting_pkey PRIMARY KEY (id);


--
-- Name: arm_soilmoistureoption arm_soilmoistureoption_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_soilmoistureoption
    ADD CONSTRAINT arm_soilmoistureoption_pkey PRIMARY KEY (id);


--
-- Name: arm_soilmoistureriskrating arm_soilmoistureriskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_soilmoistureriskrating
    ADD CONSTRAINT arm_soilmoistureriskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_soiltypeoption arm_soiltypeoption_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_soiltypeoption
    ADD CONSTRAINT arm_soiltypeoption_pkey PRIMARY KEY (id);


--
-- Name: arm_soiltyperiskrating arm_soiltyperiskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_soiltyperiskrating
    ADD CONSTRAINT arm_soiltyperiskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_surfaceconditionoption arm_surfaceconditionoption_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_surfaceconditionoption
    ADD CONSTRAINT arm_surfaceconditionoption_pkey PRIMARY KEY (id);


--
-- Name: arm_surfaceconditionriskrating arm_surfaceconditionriskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_surfaceconditionriskrating
    ADD CONSTRAINT arm_surfaceconditionriskrating_pkey PRIMARY KEY (id);


--
-- Name: arm_watertabledepthoption arm_watertabledepthoption_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_watertabledepthoption
    ADD CONSTRAINT arm_watertabledepthoption_pkey PRIMARY KEY (id);


--
-- Name: arm_watertableriskrating arm_watertableriskrating_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.arm_watertableriskrating
    ADD CONSTRAINT arm_watertableriskrating_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: bcarm
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: bcarm
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

