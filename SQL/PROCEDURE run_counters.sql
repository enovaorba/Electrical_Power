DELIMITER //

DROP PROCEDURE IF EXISTS run_counters //


CREATE PROCEDURE run_counters(start_param DATETIME, end_param DATETIME)
BEGIN

    -- First Query counters_30
    INSERT INTO Gefen_LP_counters_30_minutes_Consgeneral
    SELECT
        A.startOfInterval AS time,
        SUM(A.activeIKWH) AS activeIKWH
    FROM Gefen_LP A
    LEFT JOIN Consgeneral B ON A.meterNumber = B.meterNumber
    WHERE A.startOfInterval >= start_param AND A.startOfInterval < end_param
    AND B.meterNumber IS NOT NULL
    GROUP BY
        DATE(A.startOfInterval), HOUR(A.startOfInterval), MINUTE(A.startOfInterval) DIV 30
    ORDER BY
        time;

    INSERT INTO Gefen_LP_counters_30_minutes_Consdomestic
    SELECT
        A.startOfInterval AS time,
        SUM(A.activeIKWH) AS activeIKWH
    FROM Gefen_LP A
    LEFT JOIN Consgeneral B ON A.meterNumber = B.meterNumber
    WHERE A.startOfInterval >= start_param AND A.startOfInterval < end_param
    AND B.meterNumber IS NULL
    GROUP BY
        DATE(A.startOfInterval), HOUR(A.startOfInterval), MINUTE(A.startOfInterval) DIV 30
    ORDER BY
        time;

    -- Second Query _counters_hourly
    INSERT INTO Gefen_LP_counters_hourly_ConsGeneral
    SELECT
        A.startOfInterval AS time,
        SUM(A.activeIKWH) AS activeIKWH
    FROM Gefen_LP A
    LEFT JOIN Consgeneral B ON A.meterNumber = B.meterNumber
    WHERE A.startOfInterval >= start_param AND A.startOfInterval < end_param
    AND B.meterNumber IS NOT NULL
    GROUP BY
        DATE(A.startOfInterval), HOUR(A.startOfInterval)
    ORDER BY
        time;

    INSERT INTO Gefen_LP_counters_hourly_ConsDomestic
    SELECT
        A.startOfInterval AS time,
        SUM(A.activeIKWH) AS activeIKWH
    FROM Gefen_LP A
    LEFT JOIN Consgeneral B ON A.meterNumber = B.meterNumber
    WHERE A.startOfInterval >= start_param AND A.startOfInterval < end_param
    AND B.meterNumber IS NULL
    GROUP BY
        DATE(A.startOfInterval), HOUR(A.startOfInterval)
    ORDER BY
        time;

    -- Third Query
    INSERT INTO Gefen_LP_counters_daily_Consgeneral
    SELECT
        A.startOfInterval AS time,
        SUM(A.activeIKWH) AS activeIKWH
    FROM Gefen_LP A
    LEFT JOIN Consgeneral B ON A.meterNumber = B.meterNumber
    WHERE A.startOfInterval >= start_param AND A.startOfInterval < end_param
    AND B.meterNumber IS NOT NULL
    GROUP BY
        DATE(A.startOfInterval)
    ORDER BY
        time;

    INSERT INTO Gefen_LP_counters_daily_ConsDomestic
    SELECT
        A.startOfInterval AS time,
        SUM(A.activeIKWH) AS activeIKWH
    FROM Gefen_LP A
    LEFT JOIN Consgeneral B ON A.meterNumber = B.meterNumber
    WHERE A.startOfInterval >= start_param AND A.startOfInterval < end_param
    AND B.meterNumber IS NULL
    GROUP BY
        DATE(A.startOfInterval)
    ORDER BY
        time;

END //

DELIMITER ;

