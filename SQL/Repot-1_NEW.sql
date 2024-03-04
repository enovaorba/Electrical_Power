SELECT 'Consdomestic' AS table_name, 
       DATE_ADD(time, INTERVAL 7 DAY) AS time_predic, 
       ROUND(activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic
WHERE DAYOFWEEK(`time`) IN (2,3)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 0 WEEK)

UNION ALL


SELECT 'Consgeneral' AS table_name, 
       DATE_ADD(time, INTERVAL 7 DAY) AS time_predic, 
       ROUND(activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consgeneral
WHERE DAYOFWEEK(`time`) IN (2,3)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 0 WEEK)

UNION ALL

SELECT 'GenDistGridTotal' AS table_name, 
       DATE_ADD(A.time, INTERVAL 7 DAY) AS time_predic, 
       ROUND((A.activeIKWH+B.activeIKWH)/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic A
left join Gefen_LP_counters_30_minutes_Consgeneral B ON A.time=B.time
WHERE DAYOFWEEK(A.time) IN (2,3)
AND A.time >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK) -- Last week's data
AND A.time < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 0 WEEK);