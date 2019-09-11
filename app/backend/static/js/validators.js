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

    27 : { 'display' : 'LOW RISK', 'message' : "The risk associated with manure application is low. Follow all guidelines and recommendations in your Plan for proper application." } ,
    28 : { 'display' : 'MEDIUM RISK', 'message' : "Apply manure with caution. Follow all guidelines and recommendations in your Plan for proper application." } ,
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
        if ( total <= 27 ) {
            cutoff = RISK_CUTOFF[ 27 ];
            color_class = "low";
        }
        
        else if ( total >= 28 && total < 42 ) {
            cutoff = RISK_CUTOFF[ 28 ];
            color_class = "med";
        }

        else if ( total >= 42 ) {
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


// window.CONFIG_VALIDATOR = {

//     fields : { 

//         precipitation_1 : { 
//             trigger : 'input change keyup' ,
//             validators : { 
//                 risk_rating: { 
//                     values :  [ 0,0.25,1.25,2,2.5,3.75,5,6.25,8.75,12.5, ] , // for mm

//                     caution_values : [ 
//                         { value: 6.25, message : "Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate." } , 
//                         { value: 12.5, message : "Caution: More than 12 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate." } ,
//                     ] ,
//                 } , 
//             } , 
//         } , 


//         precipitation_2 : { 
//             trigger : 'input change keyup' ,
//             validators : { 
//                 risk_rating: { 
//                     values :  [ 0,1.25,2.5,5,6.25,7.5,8.75,10,12.5,16.25, ] , // for mm
                    
//                     caution_values : [
//                         { value: 6.25, message : "Caution: More than 6 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate." } , 
//                         { value: 12.5, message : "Caution: More than 12 mm of rain can cause a runoff event on saturated soils. Pay extreme caution and/or limit manure application rate." } ,
//                     ] ,
//                 } , 
//             } , 
//         } , 


//         soil_moisture : { 
//             trigger : 'input change keyup' ,
//             validators : { 
//                 restrict_radio : { 
//                     comparitor : 'greaterthan', 
//                     stop_value : 90,
//                     stop_message :  "Stop: Do not apply at this time. The soil moisture is too high and the risk of runoff on this field is very high." ,
//                 } , 
//                 risk_rating: { 
//                     values : [0,60,65,70,74,75,76,79,80,90] ,
//                     caution_values : [ 
//                         { value : 80, message : "Caution: You may be at risk for runoff if soils are saturated. Check field conditions and the forecast, and restrict application rates so you don’t saturate your field."  } ,
//                         { value : 90, message : "Caution: You may be at risk for runoff if soils are saturated. Check field conditions and the forecast, and restrict application rates so you don’t saturate your field."  } ,
//                         { value : 90, message : "Caution: your soil may reach saturation with manure application. Postpone application, or apply at a low rate to avoid saturation." } ,
//                         { value : 95, message : "Caution: your soil may reach saturation with manure application. Postpone application, or apply at a low rate to avoid saturation." } ,
//                     ] ,
//                 } , 
//             } , 
//         } , 


//         water_table_depth: {
//             trigger : 'input change keyup' , 
//             validators : { 
//                 risk_rating: { 
//                     values : [ 49,40,36,30,28,24,20,18,16,12 ] ,
//                     caution_values : [
//                         { value : 12, message : "Caution: There is an elevated water table at this location, which can cause a runoff event. Watch for ponding in low spots and soil saturation, and restrict application rates."  } ,
//                         { value : 30, message : "Caution: There is an elevated water table at this location, which can cause a runoff event. Watch for ponding in low spots and soil saturation, and restrict application rates."  } ,
//                     ] , 
//                     is_reversed : true ,
//                 } , 
//             } , 
//         } , 


//         forage_density : {
//             validators : {
//                 // restrict_radio : { 
//                 //     comparitor : null , 
//                 //     stop_value : null  ,
//                 //     stop_message :  "" ,
//                 // } , 
//                 risk_rating : {
//                     values : [ 90, 85, 80, 75, 70, 65, 60, 55, 50, 40 ] ,
//                     caution_values : [ 
//                         { value : 0, message :  "Caution: Your field is at a higher risk for runoff. Observe 80 foot setbacks from ditches, waterways, swales etc, unless an adequate filter strip is in place next to waterway. In no water is adjacent to field, application is permitted."  } ,
//                         { value : 49, message : "Caution: Your field is at a higher risk for runoff. Observe 80 foot setbacks from ditches, waterways, swales etc, unless an adequate filter strip is in place next to waterway. In no water is adjacent to field, application is permitted." } ,
//                         { value : 59, message : "Caution: Cover is adequate, but make sure a dense filter strip lies adjacent to any waterways and/or observe seasonal setbacks from waterways, swales, and other areas that could lead to a ditch." } ,
//                         { value : 70, message : "Caution: Cover is adequate, but make sure a dense filter strip lies adjacent to any waterways and/or observe seasonal setbacks from waterways, swales, and other areas that could lead to a ditch." } ,
//                     ] ,
//                     is_reversed : true 
//                 } ,
//             }
//         } ,


//         forage_height : {
//             trigger : 'input change keyup' , 
//             validators : {
//                 risk_rating : {
//                     values : [7, 6, 3, 2.9, 2.5, 2.4, 2.3, 2, 0, -1] ,
//                     caution_values : [ 
//                         { value : 1, message : "Caution: Your field is at a higher risk for runoff. Make sure vegetation is dense and able to properly filter runoff if a large rain event is forecasted. Observe seasonal setbacks." } ,
//                         { value : 3, message : "Caution: Your field is at a higher risk for runoff. Make sure vegetation is dense and able to properly filter runoff if a large rain event is forecasted. Observe seasonal setbacks." } ,
//                     ] ,
//                     is_reversed : true 
//                 } ,
//             }
//         } ,


//         surface_condition : {   
//             validators : {
//                 restrict_radio : {
//                     comparitor : 'in' ,
//                     stop_values : { 'flooding' : true, 'frozen' : true, 'snow-ice' : true } ,
//                     stop_message : "Stop: No Application permitted" ,
//                 } ,
//                 surface_risk_rating: {
//                     comparitor : 'in' ,
//                     stop_values : { 'flooding' : true, 'frozen' : true, 'snow-ice' : true } ,
//                     caution_values : [
//                         { value : 'ponding', message : "Ponding - Caution: Avoid ponded areas with appropriate seasonal setback distance, particularly if it drains to a waterway. Ponding can be a sign of a high water table, so be cautious of soil saturation." } ,
//                         { value : 'flooding', message : "Flooding - No application is allowed if flooding is predicted in a 15 day window after application."  } ,
//                         { value : 'frozen', message : "Frozen - No application is allowed on soils frozen 2,5 cm or greater below the surface, or covered in snow." } ,
//                         { value : 'snow-ice', message : "Snow covered - No application is allowed if a field has at least 5 cm (2 in) or more of ice or snow over 50% or more of the area." } ,
//                         { value : 'tiles', message : "Tiles - Caution: Tiles must have at least 60 cm of cover, not be discharging manure, and their location must be known prior to application. Monitor tiles closely after application. If manure discharges from tile, plug immediately." } ,
//                     ] ,
//                 }
//             } ,
//         } ,

//         soil_type: {
//             trigger : 'input change keyup' , 
//             validators : {
//                 soil_type_risk_rating: {
//                 }
//             } ,
//         } ,

//         application_equipment: {
//             trigger : 'input change keyup' , 
//             validators : {
//                 applicator_risk_rating: {
//                 }
//             } ,
//         } ,


//         critical_area: {
//             validators : {
//                 show_hide: {
//                 },
//                 critical_area_risk_rating: {
//                 }
//             } ,
//         } ,


//         manure_setback_distance : {
//             trigger : 'input change keyup' , 
//             validators : {
//                 manure_setback_distance : {
//                 }
//             } ,
//         } ,
//     } , 

// };


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

            if ( value === 'below_application' ) {
                update_riskrating_ui( $field, { risk : 2 ,display : 'Low-Med' } );
                var caution = "This is a low risk method of application. Watch for compaction on your field if soil is wet. Follow current manure setback distances.";
                update_caution_ui( $field, caution );
            }
            else if ( value === 'surface_application' ) {
                update_riskrating_ui( $field, { risk : 3, display : 'Low-Med' } );
                var caution =  "Be cautious of turnaround areas and low spots. Watch for compaction on your field if applying to wet soils. Follow current manure setback distances. Use of an aerator is a good method when applying to grass in a higher risk time.";
                update_caution_ui( $field, caution );
            }
            else if ( value === 'irrigation_sprinkler' ) {
                update_riskrating_ui( $field, { risk : 6, display : 'Medium' } );
                var caution = "While this method decreases compaction issues, it may increase the likelihood of runoff of manure from the surface of your field. Do not apply to saturated soils. Be sure to observe manure setbacks from critical areas at all times. Do not use this method if wind speed is greater than 10 mph.";
                update_caution_ui( $field, caution );
            }
            else if ( value === 'grazing' ) {
                update_riskrating_ui( $field, { risk : 3, display : 'Low-Med' } );
                var caution = "Grazing is a form of manure application. Be sure to observe manure application setback distances and maintain field cover to reduce a runoff event.";
                update_caution_ui( $field, caution );
            }
            else if ( value === 'soild_manure_application' ) {
                update_riskrating_ui( $field, { risk : 5, display : 'Medium' } );
                var caution = "Solid manure guidelines are the same as liquid manure. Follow all setback guidance. Make sure soild manure is spread evenly and incorporated into the soil surface prior to a rain event, which can significantly increase the probablility of a runoff event.";
                update_caution_ui( $field, caution );
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

            if ( value === 'sand' ) {
                update_riskrating_ui( $field, { risk : 1 ,display : 'Low' } );
                var caution = "";
                update_caution_ui( $field, caution );
            }
            else if ( value === 'silt' ) {
                update_riskrating_ui( $field, { risk : 2, display : 'Low-Med' } );
                var caution =  "";
                update_caution_ui( $field, caution );
            }
            else if ( value === 'clay' ) {
                update_riskrating_ui( $field, { risk : 5, display : 'Medium' } );
                var caution = "";
                update_caution_ui( $field, caution );
            }
            else if ( value === 'peat_muck' ) {
                update_riskrating_ui( $field, { risk : 6, display : 'Medium' } );
                var caution = "";
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
                    update_riskrating_ui( $field, { risk : 10, display : 'Extreme' } );
                    has_extreme_flag = true;
                }
            }

            // handle 'none' option and 'Medium'
            if (  'none' in all_checked_values && Object.keys( all_checked_values ).length === 1 ) {
                update_riskrating_ui( $field, { risk: 0, display : 'Low' } );
            }
            else if( has_extreme_flag === false ) {

                if(Object.keys( all_checked_values ).length === 1)
                {
                    if('ponding' in all_checked_values)
                    {
                        update_riskrating_ui( $field, { risk: 5, display : 'Medium' } );
                    }
                    if('tiles' in all_checked_values)
                    {
                        update_riskrating_ui( $field, { risk: 6, display : 'Medium' } );
                    }
                }
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
    $.fn.bootstrapValidator.validators.critical_area_risk_rating = {
        validate: function(validator, $field, options) {
            var value = $field.val();
            //console.log( value );

            if ( value === 'no' ) {
                update_riskrating_ui( $field, { risk : 1 ,display : 'Low' } );
                var caution = "";
                update_caution_ui( $field, caution );
            }
            else if ( value === 'yes' ) {
                update_riskrating_ui( $field, { risk : 3, display : 'Low-Med' } );
                var caution =  "";
                update_caution_ui( $field, caution );
            }
            return true;
        }
    };
}(window.jQuery));


(function($) {
    $.fn.bootstrapValidator.validators.manure_setback_distance = {
        validate: function(validator, $field, options) {
            var value = $field.val();

            var caution = "Warning: Your setback is either lower than legal requirements or the recommended setback distance. Increasing setback distance will reduce the risk of off-site nutrient transport.";

            if ( value >= 12 ) {
                update_riskrating_ui( $field, { risk : 1 ,display : 'Low' } );
                update_caution_ui( $field, caution );
            }
            else if ( value <= 11.99 && value > 1.5 ) {
                update_riskrating_ui( $field, { risk : 4, display : 'Med' } );
                update_caution_ui( $field, caution );
            }
            else if ( value < 1.5 ) {
                update_riskrating_ui( $field, { risk : 7, display : 'High-Med' } );
                update_caution_ui( $field, caution );
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