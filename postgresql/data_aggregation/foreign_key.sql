CREATE TABLE 
	employees_projects (
		id SERIAL PRIMARY KEY,
		employee_id INT,
		project_id INT,
		CONSTRAINT fk_projects
			FOREIGN KEY(project_id)
				REFERENCES projects(id),
		CONSTRAINT fk_employees
			FOREIGN KEY(employee_id)
				REFERENCES employees(id)
	);
