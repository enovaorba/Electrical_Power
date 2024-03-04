SELECT DATE_ADD(time, INTERVAL 7 DAY) AS time_predic, ROUND(activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic
WHERE DAYOFWEEK(`time`) IN (6,7)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) - 1) DAY), INTERVAL 1 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) - 1) DAY), INTERVAL 0 WEEK)

UNION ALL

SELECT DATE_ADD(time, INTERVAL 14 DAY) AS time_predic, ROUND(activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic
WHERE DAYOFWEEK(`time`) IN (1)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) - 1) DAY), INTERVAL 1 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) - 1) DAY), INTERVAL 0 WEEK);




SELECT DATE_ADD(time, INTERVAL 7 DAY) AS time_predic, ROUND(activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consgeneral
WHERE DAYOFWEEK(`time`) IN (6,7)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) - 1) DAY), INTERVAL 1 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) - 1) DAY), INTERVAL 0 WEEK)

UNION ALL

SELECT DATE_ADD(time, INTERVAL 14 DAY) AS time_predic, ROUND(activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consgeneral
WHERE DAYOFWEEK(`time`) IN (1)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) - 1) DAY), INTERVAL 1 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) - 1) DAY), INTERVAL 0 WEEK);