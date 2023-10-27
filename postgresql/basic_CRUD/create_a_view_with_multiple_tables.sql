CREATE VIEW view_addresses
AS
SELECT
	CONCAT(first_name, ' ', last_name) AS "Full Name",
	department_id,
	CONCAT(number, ' ', street) AS "Address"
	
FROM
	employees AS e,
	addresses AS a
WHERE
	e.address_id = a.id
ORDER BY 
	"Address"
