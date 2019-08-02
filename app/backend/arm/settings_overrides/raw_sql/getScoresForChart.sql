CREATE OR REPLACE FUNCTION getScoresForChart( ref refcursor, my_client_submeasure_id int, start_date timestamp, end_date timestamp, series_id int )
RETURNS refcursor AS $$
DECLARE
BEGIN
    OPEN ref
        FOR
            SELECT EXTRACT( EPOCH from ( CASE WHEN schedule.date_answered IS NULL THEN schedule.date_due ELSE schedule.date_due END ) ) * 1000 as answer_date, score.score, series_id, severity.name, severity.color
            FROM client_measure_schedule schedule
                INNER JOIN client_submeasures subm ON subm.client_measure_id = schedule.client_measure_id
                LEFT JOIN client_scores score ON score.client_measure_schedule_id  = schedule.id AND score.client_submeasure_id = subm.id
                LEFT JOIN measures_sub_severity severity ON score.severity_id = severity.id
            WHERE subm."id" = my_client_submeasure_id
                AND schedule.date_due between start_date and end_date
            GROUP BY answer_date, score.score, severity.name, severity.color
            ORDER BY answer_date;
    RETURN ref;

EXCEPTION
    WHEN INTERNAL_ERROR THEN
         return null;
END;
$$ LANGUAGE plpgsql;
