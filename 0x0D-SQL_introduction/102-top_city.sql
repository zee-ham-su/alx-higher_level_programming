-- a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT city, AVG(value) AS avg_temperature
FROM temperatures
WHERE MONTH=7 OR MONTH=8
GROUP BY city
ORDER BY avg_temperature DESC
LIMIT 3;
