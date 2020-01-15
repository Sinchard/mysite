DELETE
FROM
	reader_fiction
WHERE
	id NOT IN (
		SELECT
			dt.minno
		FROM
			(
				SELECT
					MIN(id) AS minno
				FROM
					reader_fiction
				GROUP BY
					fiction_id
			) dt
	)