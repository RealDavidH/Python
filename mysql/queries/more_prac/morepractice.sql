-- JOIN
-- Find all clients (first and last name) billing amounts and charged dates
select clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
from clients 
join billing on clients.id = billing.clients_id;

-- list all the domain
select sites.domain_name, leads.first_name, leads.last_name
from sites
join leads on sites.id = leads.sites_id;

-- Join muitple tables
-- get the names of the clients, their domain names, and the first names of all the leads generated from those sites.

SELECT clients.first_name AS client_first, clients.last_name, sites.domain_name, leads.first_name AS leads_first
from clients
join sites on clients.id = sites.clients_id
join leads on sites.id = leads.sites_id;

-- LEFT & RIGHT JOIN
-- List all the clients and the sites each client has, even if the client hasn't landed a site yet. 
SELECT clients.first_name, clients.last_name, sites.domain_name
FROM clients
RIGHT JOIN sites ON clients.id = sites.clients_id;

-- GROUPING ROWS
-- GROUP BY
-- SUM, MIN, MAX, AVG
-- Find all the clients (first and last name) and their total billing amounts
select clients.first_name, clients.last_name, SUM(billing.amount) AS total_billing
from clients 
join billing on clients.id = billing.clients_id
GROUP BY clients.id;

-- GROUP CONCAT
-- List all the domain names associated with each client
SELECT clients.first_name, clients.last_name, group_concat(' ',domain_name) AS domains
from clients
join sites on clients.id = sites.clients_id
group by clients.id;

-- Count
-- find the total number of leads for each site
select sites.domain_name, COUNT(leads.id) AS leads
from sites
join leads on sites.id = leads.sites_id
GROUP BY sites.id;
