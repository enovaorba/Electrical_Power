SELECT 'ConsDomestic' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 14 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic, 
       ROUND(A.activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic A
WHERE DAYOFWEEK(`time`) IN (6,7)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK)

UNION ALL

SELECT 'ConsGeneral' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 14 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic, 
       ROUND(A.activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consgeneral A
WHERE DAYOFWEEK(`time`) IN (6,7)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK)

UNION ALL

SELECT 'TotalCons' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 14 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic, 
       ROUND((A.activeIKWH + B.activeIKWH)/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic A
left join Gefen_LP_counters_30_minutes_Consgeneral B ON A.time=B.time
WHERE DAYOFWEEK(A.time) IN (6,7)
AND A.time >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND A.time < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK)

UNION ALL

SELECT 'GenDistGridTotal' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 14 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic, 
       0 AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic A
left join Gefen_LP_counters_30_minutes_Consgeneral B ON A.time=B.time
WHERE DAYOFWEEK(A.time) IN (6,7)
AND A.time >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND A.time < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK)

UNION ALL
 
SELECT 'ConsPlanGRID' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 14 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic, 
       ROUND((A.activeIKWH + B.activeIKWH)/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic A
left join Gefen_LP_counters_30_minutes_Consgeneral B ON A.time=B.time
WHERE DAYOFWEEK(A.time) IN (6,7)
AND A.time >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND A.time < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK)


UNION ALL

SELECT 'ConsDomestic' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 21 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic,  
       ROUND(A.activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic A
WHERE DAYOFWEEK(`time`) IN (1)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK)


UNION ALL

SELECT 'ConsGeneral' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 21 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic,  
       ROUND(A.activeIKWH/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consgeneral A
WHERE DAYOFWEEK(`time`) IN (1)
AND `time` >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND `time` < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK)


UNION ALL

SELECT 'TotalCons' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 21 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic,  
       ROUND((A.activeIKWH + B.activeIKWH)/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic A
left join Gefen_LP_counters_30_minutes_Consgeneral B ON A.time=B.time
WHERE DAYOFWEEK(A.time) IN (1)
AND A.time >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND A.time < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK)
UNION ALL

SELECT 'GenDistGridTotal' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 21 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic, 
       0 AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic A
left join Gefen_LP_counters_30_minutes_Consgeneral B ON A.time=B.time
WHERE DAYOFWEEK(A.time) IN (1)
AND A.time >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND A.time < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK)

UNION ALL
 
SELECT 'ConsPlanGRID' AS table_name, 
       DATE_FORMAT(DATE_ADD(A.time, INTERVAL 21 DAY), '%Y/%m/%d %H:%i:%s') AS time_predic, 
       ROUND((A.activeIKWH + B.activeIKWH)/1000, 2) AS activeIKWH
FROM Gefen_LP_counters_30_minutes_Consdomestic A
left join Gefen_LP_counters_30_minutes_Consgeneral B ON A.time=B.time
WHERE DAYOFWEEK(A.time) IN (1)
AND A.time >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 2 WEEK) -- Last week's data
AND A.time < DATE_SUB(DATE_SUB(CURDATE(), INTERVAL (DAYOFWEEK(CURDATE()) + 6) % 7 DAY), INTERVAL 1 WEEK);
