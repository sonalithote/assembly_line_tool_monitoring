Data Monitoring Application:

Sample data to upload :

INSERT INTO tool (name, status, last_update, throughput, error_rate)
VALUES 
('Drill', 'active', '2025-03-24 12:00:00', 120.5, 0.02),
('Lathe', 'inactive', '2025-03-24 12:05:00', 100.0, 0.05),
('Welder', 'active', '2025-03-24 12:10:00', 200.0, 0.01),
('CNC Machine', 'maintenance', '2025-03-24 12:15:00', NULL, NULL),
('Grinder', 'active', '2025-03-24 12:20:00', 80.3, 0.03);


To run, start db server and kafka server then run the application to access the API's


Steps to install postgreSQL and start it:
Install PostgreSQL: In Terminal, run brew install postgresql. 
Start PostgreSQL: Run brew services start postgresql. 
Verify Installation: Open a new Terminal window and run psql -d postgres to connect to the PostgreSQL server. 
