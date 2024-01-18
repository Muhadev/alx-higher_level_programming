-- a script that displays the average temperature (Fahrenheit) by city
USE `hbtn_0c_0`;
SELECT city, AVG(`value`) AS `avg_temp`
FROM `temperature`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
