CREATE VIEW view_continents_countries_currencies_details
AS
SELECT
	CONCAT_WS(': ', cont.continent_name, cont.continent_code) AS "Continent Details",
	CONCAT_WS(' - ', ctrs.country_name, ctrs.capital, ctrs.area_in_sq_km, 'km2') AS "Country Information",
	CONCAT(curr.description, ' (', curr.currency_code, ')') AS "Currencies"
	
FROM
	continents AS cont,
	countries AS ctrs,
	currencies AS curr
WHERE
	cont.continent_code = ctrs.continent_code
		AND
	ctrs.currency_code = curr.currency_code
ORDER BY
	"Country Information", "Currencies"
