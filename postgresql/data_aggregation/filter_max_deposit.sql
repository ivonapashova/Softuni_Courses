SELECT
	magic_wand_creator,
	MAX(deposit_amount) AS "Max Deposit Amount"
FROM
	wizard_deposits
WHERE
	deposit_amount < 20000
		OR
	deposit_amount > 40000
GROUP BY
	magic_wand_creator
ORDER BY
	"Max Deposit Amount" DESC
LIMIT 3;
