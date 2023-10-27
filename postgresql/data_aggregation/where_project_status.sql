SELECT
    project_name,
    CASE
        WHEN start_date is NULL AND end_date is NULL THEN 'Ready for development'
        WHEN start_date IS NOT NULL and end_date IS NULL THEn 'In Progress'
        ELSE 'Done'
    END AS project_status
FROM
    projects
WHERE
    project_name LIKE '%Mountain%'
