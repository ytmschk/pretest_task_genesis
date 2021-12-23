SELECT a.category_name, AVERAGE (c.cost) AS average_cost 
FROM adverts INNER JOIN costs ON a.id = c.id 
WHERE average_cost > 500
GROUP BY a.category_name 