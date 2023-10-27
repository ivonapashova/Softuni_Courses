SELECT 
	e.id, 
	e.first_name,
	e.last_name,
	ROUND(e.salary, 2) AS formatted_salary,
	e.department_id,
    CASE e.department_id
        WHEN 1 THEN 'Management'
        WHEN 2 THEN 'Kitchen Staff'
        WHEN 3 THEN 'Service Staff'
        ELSE 'Other'
    END AS department_name
FROM 
	employees AS e;
