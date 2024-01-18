-- a script that displays the average temperature (Fahrenheit) by city
USE hbtn_0c_0;
SELECT city, AVG(temperature) AS average_temperature FROM your_table_name GROUP BY city ORDER BY average_temperature DESC;
