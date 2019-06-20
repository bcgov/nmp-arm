
var total = 0;

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


window.RISK_CUTOFF = {

    24 : { 'display' : 'LOW RISK', 'message' : "The risk associated with manure application is low. Follow all guidelines and recommendations in your Plan for proper application." } ,
    25 : { 'display' : 'LOW-MED RISK', 'message' : "Apply manure following all guidelines and recommendations in your Plan." } ,
    31 : { 'display' : 'MEDIUM RISK', 'message' : "Apply manure with caution. Follow all guidelines and recommendations in your Plan for proper application." } ,
    40 : { 'display' : 'MEDIUM-HIGH RISK', 'message' : "If you apply manure, do so with EXTREME caution. Follow all recommendations, manure setback distances, and application guidelines in this worksheet and in your Plan." } ,
    50 : { 'display' : 'HIGH RISK', 'message' : "Do NOT apply manure at this time, the risk is too high. Wait and reevaluate." } ,

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
    remove_risk_rating_classes( $risk );
    add_risk_rating_classes( $risk );
    RATING[ $field.attr('name') ] = rating.risk;
    // update total 
    // rupdate( rating, override );
        // KV - use total of 72 hour precip for final rating
        
        total = RATING.precipitation_1  ;  // 24 h
        // check if 72 h value object exists
        if (RATING.precipitation_2 != null) {
           total = RATING.precipitation_2  ;  // 72 h
        }
        console.log( "[ TOTAL RISK ]: ", total );
    
        var cutoff = null;
        var cutoffmessage = null;
        var color_class = null;
        if ( total <= 1 ) {
            cutoff =  RISK_CUTOFF[ 24 ];
            color_class = "low";
        }
        else if ( total > 1 && total <= 4 ) {
            cutoff = RISK_CUTOFF[ 25 ];
            color_class = "low-med";
        }
        else if ( total > 4 && total <= 6 ) {
            cutoff = RISK_CUTOFF[ 31 ];
            color_class = "med";
        }
        else if ( total > 6 &&  total <= 8 ) {
            cutoff = RISK_CUTOFF[ 40 ];
            color_class = "med-high";
        }
        else if ( total >= 9 ) {
            cutoff = RISK_CUTOFF[ 50 ];
            color_class = "high";
        }
        if (color_class === "high"){
           remove_risk_rating_classes( $( "input[ name='total_risk' ]" ) );
           $( "input[ name='total_risk' ]" ).addClass( 'high' );
           $( "input[ name='total_risk' ]" ).val( 'NO APPLICATION' ); 
           $( "input[ name='total_risk' ]" ).parents( '.form-group' ).find( '.desc' ).text( "NO application, one or more indicators is above the critical value" ); 
        }
        else {
           remove_risk_rating_classes( $( "input[ name='total_risk' ]" ) );
           $( "input[ name='total_risk' ]" ).addClass( color_class );
           $( "input[ name='total_risk' ]" ).val( cutoff.display ); 
           $( "input[ name='total_risk' ]" ).parents( '.form-group' ).find( '.desc' ).text( cutoff.message ); 
        }

  

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
        if ( total <= 24 ) {
            cutoff = RISK_CUTOFF[ 24 ];
            color_class = "low";
        }
        else if ( total >= 25 && total < 31 ) {
            cutoff = RISK_CUTOFF[ 25 ];
            color_class = "low-med";
        }
        else if ( total >= 31 && total < 40 ) {
            cutoff = RISK_CUTOFF[ 31 ];
            color_class = "med";
        }
        else if ( total >= 40 &&  total < 50 ) {
            cutoff = RISK_CUTOFF[ 40 ];
            color_class = "med-high";
        }
        else if ( total >= 50 ) {
            cutoff = RISK_CUTOFF[ 50 ];
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
    // expects array of hashes
    // { 'value' : number, 'message' : str }
    /*
    var options = options || {};
    var is_reversed = options.is_reversed || false;
    if( is_reversed ) { L.reverse(); }
    */

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


window.CONFIG_VALIDATOR = {

    fields : { 

        precipitation_1 : { 
            trigger : 'input change keyup' ,
            validators : { 
                risk_rating: { 
                    // values :  [ 0, 0.01, 0.05, 0.08, 0.1, 0.15, 0.2, 0.25, 0.35, 0.5, ] , // for inches
                    values :  [ 0,0.254,1.27,2.032,2.54,3.81,5.08,6.35,8.89,12.7, ] , // for mm

                    caution_values : [ 
                        { value: 6.35, message : "Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate." } , 
                        { value: 12.7, message : "Caution: More than 12 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate." } ,
                    ] ,
                } , 
            } , 
        } , 


        precipitation_2 : { 
            trigger : 'input change keyup' ,
            validators : { 
                risk_rating: { 
                    // values : [ 0, 0.05, 0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5, 0.75, ] , // for inches
                    values :  [ 0,1.27,2.54,5.08,6.35,7.62,8.89,10.16,12.7,19.05, ] , // for mm
                    
                    caution_values : [
                        { value: 6.35, message : "Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate." } , 
                        { value: 12.7, message : "Caution: More than 12 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate." } ,
                    ] ,
                } , 
            } , 
        } , 


        soil_moisture : { 
            trigger : 'input change keyup' ,
            validators : { 
                restrict_radio : { 
                    comparitor : 'greaterthan' , 
                    stop_value : 95 ,
                    stop_message :  "Stop: Do not apply at this time. The soil moisture is too high and the risk of runoff on this field is very high." ,
                } , 
                risk_rating: { 
                    values : [55,60,65,70,75,80,85,90,95,100] ,
                    caution_values : [ 
                        { value : 80, message : "Caution: You may be at risk for runoff if soils are saturated. Check field conditions and the forecast, and restrict application rates so you don’t saturate your field."  } ,
                        { value : 90, message : "Caution: You may be at risk for runoff if soils are saturated. Check field conditions and the forecast, and restrict application rates so you don’t saturate your field."  } ,
                        { value : 90, message : "Caution: your soil may reach saturation with manure application. Postpone application, or apply at a low rate to avoid saturation." } ,
                        { value : 95, message : "Caution: your soil may reach saturation with manure application. Postpone application, or apply at a low rate to avoid saturation." } ,
                    ] ,
                } , 
            } , 
        } , 


        water_table_depth: {
            trigger : 'input change keyup' , 
            validators : { 
                risk_rating: { 
                    values : [ 48,40,36,30,28,24,20,18,16,12 ] ,
                    caution_values : [
                        { value : 12, message : "Caution: There is an elevated water table at this location, which can cause a runoff event. Watch for ponding in low spots and soil saturation, and restrict application rates."  } ,
                        { value : 30, message : "Caution: There is an elevated water table at this location, which can cause a runoff event. Watch for ponding in low spots and soil saturation, and restrict application rates."  } ,
                    ] , 
                    is_reversed : true ,
                } , 
            } , 
        } , 


        forage_density : {
            validators : {
                restrict_radio : { 
                    comparitor : null , 
                    stop_value : null  ,
                    stop_message :  "" ,
                } , 
                risk_rating : {
                    values : [ 90, 85, 80, 75, 70, 65, 60, 55, 50, 40 ] ,
                    caution_values : [ 
                        { value : 0, message :  "Caution: Your field is at a higher risk for runoff. Observe 80 foot setbacks from ditches, waterways, swales etc, unless an adequate filter strip is in place next to waterway. In no water is adjacent to field, application is permitted."  } ,
                        { value : 59, message : "Caution: Your field is at a higher risk for runoff. Observe 80 foot setbacks from ditches, waterways, swales etc, unless an adequate filter strip is in place next to waterway. In no water is adjacent to field, application is permitted." } ,
                        { value : 60, message : "Caution: Cover is adequate, but make sure a dense filter strip lies adjacent to any waterways and/or observe seasonal setbacks from waterways, swales, and other areas that could lead to a ditch." } ,
                        { value : 70, message : "Caution: Cover is adequate, but make sure a dense filter strip lies adjacent to any waterways and/or observe seasonal setbacks from waterways, swales, and other areas that could lead to a ditch." } ,
                    ] ,
                    is_reversed : true 
                } ,
            }
        } ,


        forage_height : {
            trigger : 'input change keyup' , 
            validators : {
                risk_rating : {
                    values : [5, 3.5, 3, 2.8, 2.5, 2, 1.5, 1.4, 1.2, 1] ,
                    caution_values : [ 
                        { value : 1, message : "Caution: Your field is at a higher risk for runoff. Make sure vegetation is dense and able to properly filter runoff if a large rain event is forecasted. Observe seasonal setbacks." } ,
                        { value : 3, message : "Caution: Your field is at a higher risk for runoff. Make sure vegetation is dense and able to properly filter runoff if a large rain event is forecasted. Observe seasonal setbacks." } ,
                    ] ,
                    is_reversed : true 
                } ,
            }
        } ,


        surface_condition : {
            validators : {
                restrict_radio : {
                    comparitor : 'in' ,
                    stop_values : { 'flooding' : true, 'frozen' : true } ,
                    stop_message : "Stop: No Application permitted" ,
                } ,
                surface_risk_rating: {
                    comparitor : 'in' ,
                    stop_values : { 'flooding' : true, 'frozen' : true } ,
                    caution_values : [
                        { value : 'ponding', message : "Ponding - Caution: Avoid ponded areas with appropriate seasonal setback distance, particularly if it drains to a waterway. Ponding can be a sign of a high water table, so be cautious of soil saturation." } ,
                        { value : 'flooding', message : "Flooding - No application is allowed if flooding is predicted in a 15 day window after application."  } ,
                        { value : 'frozen', message : "Frozen - No application is allowed on soils frozen 2,5 cm or greater below the surface, or covered in snow." } ,
                        { value : 'tiles', message : "Tiles - Caution: Tiles must have at least 60 cm of cover, not be discharging manure, and their location must be known prior to application. Monitor tiles closely after application. If manure discharges from tile, plug immediately." } ,
                    ] ,
                }
            } ,
        } ,


        application_equipment: {
            validators : {
                applicator_risk_rating: {
                }
            } ,
        } ,


        critical_area: {
            validators : {
                show_hide: {
                }
            } ,
        } ,


        manure_setback_distance : {
            trigger : 'input change keyup' , 
            validators : {
                manure_setback_distance : {
                    stop_message : "Stop: manure setbacks must be a minimum of 10 feet from May 1 to August 31 (40 for Big Gun use). 40 feet from September 1 to May. and 80 feet from October 1 to February 28",
                }
            } ,
        } ,



        vegetation_buffer : {
            validators : {
                restrict_radio : {
                    comparitor : 'equals' ,
                    stop_value : '100' ,
                    stop_message : 'Stop: a vegetation buffer is required',
                } ,
                risk_rating : {
                    values : [100, 80, 40, 35, 30, 25, 24, 22, 20, 10] ,
                    caution_values : [ 
                        { value : 22, message : "Caution: If you field is in grass, grass can act like a buffer if it is dense and greater than 7,5 cm in height. You may change your response to “yes” if in grass. If your field is not in grass, observe seasonal setbacks and consider vegetative buffers if needed."  } ,
                        { value : 34, message : "Caution: buffers may not be adequate to filter runoff, refer to your Nutrient Management Plan for proper buffer width. Make sure to follow all manure setback distances."  } ,
                    ] ,
                    is_reversed : true 
                } ,
            } ,
        } ,

    } , 

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

            if ( value === 'below_application' ) {
                update_riskrating_ui( $field, { risk : 1 ,display : 'Low-Med' } );
                var caution = "This is a low risk method of application. Watch for compaction on your field if soil is wet. Follow current manure setback distances.";
                update_caution_ui( $field, caution );
            }
            else if ( value === 'surface_application' ) {
                update_riskrating_ui( $field, { risk : 3, display : 'Medium' } );
                var caution =  "Be cautious of turnaround areas and low spots. Watch for compaction on your field if applying to wet soils. Follow current manure setback distances.";
                update_caution_ui( $field, caution );
                var risk = { risk : 4, display : RISK_RATING[ 4 ] };
                console.log( "[ RISK ]: ", risk );
                update_riskrating_ui( $field, risk );
            }
            else if ( value === 'surface_aerator' ) {
                update_riskrating_ui( $field, { risk : 3, display : 'Medium' } );
                var caution = "This is a good method when applying to grass in a higher risk time. Watch for compaction on your field if applying to wet soils. Follow current manure setback distances.";
                update_caution_ui( $field, caution );
                var risk = { risk : 4, display : RISK_RATING[ 4 ] }
                console.log( "[ RISK ]: ", risk );
                update_riskrating_ui( $field, risk );
            }
            else if ( value === 'irrigation_sprinkler' ) {
                update_riskrating_ui( $field, { risk : 4, display : 'Medium' } );
                var caution = "While this method decreases compaction issues, it may increase the likelihood of runoff of manure from the surface of your field. Do not apply to saturated soils. Be sure to observe manure setbacks from critical areas at all times.";
                update_caution_ui( $field, caution );
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
            var has_extreme_flag = false;
            for( var i = 0; i < values.length; i++ ) {
                var value = values[ i ];
                if ( value in options.stop_values ) {
                    update_riskrating_ui( $field, { risk : 9, display : 'Extreme' } );
                    has_extreme_flag = true;
                }
            }

            // handle 'none' option and 'Medium'
            if (  'none' in all_checked_values && Object.keys( all_checked_values ).length === 1 ) {
                update_riskrating_ui( $field, { risk: 0, display : 'Low' } );
            }
            else if( has_extreme_flag === false ) {
                update_riskrating_ui( $field, { risk: 3, display : 'Medium' } );
            }


            // cautions
            update_caution_ui( $field, null );
            for( var i = 0; i < values.length; i++ ) {
                var value = values[ i ];
                if ( value === 'ponding' ) {
                    update_caution_ui( $field, options.caution_values[0].message, true );
                }
                else if ( value === 'flooding' ) {
                    update_caution_ui( $field, options.caution_values[1].message, true );
                }
                else if ( value === 'frozen' ) {
                    update_caution_ui( $field, options.caution_values[2].message, true );
                }
                else if ( value === 'tiles' ) {
                    update_caution_ui( $field, options.caution_values[3].message, true );
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

            var apply_value = $( "input[name='apply_date']" ).val();
            if ( typeof apply_value === 'undefined' || apply_value === null || apply_value === "" ) {
                return {
                    valid : false ,
                    message : 'you need to provide an application date' ,
                }
            }

            var apply_date =  new Date( apply_value );

            var current_year = new Date().getFullYear();
            var january = new Date( '01/01/2014' ).setFullYear( current_year );
            var feb_28th = new Date( '02/28/2014' ).setFullYear( current_year );
            var april_30th = new Date( '04/30/2014' ).setFullYear( current_year );
            var august_31st = new Date( '08/31/2014' ).setFullYear( current_year );
            var sept_30th = new Date( '09/30/2014' ).setFullYear( current_year );
            var december = new Date( '12/31/2014' ).setFullYear( current_year );
        

            var error_flag = false;
            if ( (( apply_date >= january && apply_date < feb_28th ) || ( apply_date > sept_30th && apply_date <= december )) ) {
                if ( value < 80 ) {
                    error_flag = true; 
                }
            }

            if ( apply_date >= feb_28th && apply_date <= april_30th ) {
                if ( value < 40 ) {
                    error_flag = true;
                }
            }

            if ( apply_date > april_30th && apply_date <= august_31st ) {
                if ( value < 10 ) {
                    error_flag = true;
                }
            }

            if ( apply_date > august_31st && apply_date <= sept_30th ) {
                if ( value < 40 ) {
                    error_flag = true;
                }
            }


            if ( error_flag ) {
                return {
                    valid: false ,
                    message: options.stop_message
                };
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