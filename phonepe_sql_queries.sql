use phonepe_db;
-- 1 Top States
-- 1 Top States
SELECT state, SUM(transaction_amount) AS total
FROM aggregated_transaction
WHERE year = 2022 AND quarter = 1
GROUP BY state
ORDER BY total DESC
LIMIT 10;

-- 2 Transaction Type Share
-- 2 Transaction Type Share
SELECT transaction_type, SUM(transaction_amount) AS total
FROM aggregated_transaction
WHERE year = 2022 AND quarter = 1
GROUP BY transaction_type;

-- 3 Top Districts
SELECT district, SUM(transaction_amount) AS total
FROM top_transaction_district
WHERE year = 2022 AND quarter = 1
GROUP BY district
ORDER BY total DESC
LIMIT 10;

-- 4 Top Pincode
SELECT pincode, SUM(transaction_amount) AS total
FROM top_transaction_pincode
WHERE year = 2022 AND quarter = 1
GROUP BY pincode
ORDER BY total DESC
LIMIT 10;

-- 5 Yearly Growth
SELECT year, SUM(transaction_amount) AS total
FROM aggregated_transaction
GROUP BY year
ORDER BY year;

-- 1 Users by State
SELECT state, SUM(user_count) AS users
FROM aggregated_user
WHERE year = 2022 AND quarter = 1
GROUP BY state
ORDER BY users DESC;


-- 2 Brand Usage
SELECT brand, SUM(user_count) AS users
FROM aggregated_user
WHERE year = 2022 AND quarter = 1
GROUP BY brand

-- 3 Top District Users
SELECT district, SUM(registered_users) AS users
FROM map_user
WHERE year = 2022 AND quarter = 1
GROUP BY district
ORDER BY users DESC
LIMIT 10;
-- 4 App Opens
SELECT state, SUM(app_opens) AS opens
FROM map_user
WHERE year = 2022 AND quarter = 1
GROUP BY state
ORDER BY opens DESC;


-- 4 App Opens
SELECT state, SUM(app_opens) AS opens
FROM map_user
WHERE year = 2022 AND quarter = 1
GROUP BY state
ORDER BY opens DESC;

-- 5 Engagement Ratio
SELECT state,
       SUM(app_opens) / SUM(registered_users) AS engagement
FROM map_user
WHERE year = 2022 AND quarter = 1
GROUP BY state;


-- 1 Insurance by State
SELECT state, SUM(transaction_amount) AS total
FROM aggregated_insurance
WHERE year = 2022 AND quarter = 1
GROUP BY state
ORDER BY total DESC;

-- 2 Top District Insurance
SELECT district, SUM(insurance_amount) AS total
FROM top_insurance_district
WHERE year = 2022 AND quarter = 1
GROUP BY district
ORDER BY total DESC
LIMIT 10;

-- 4 Insurance Growth
SELECT year, SUM(transaction_amount) AS total
FROM aggregated_insurance
GROUP BY year
ORDER BY year;

-- 1 Low Performing States
SELECT state, SUM(transaction_amount) AS total
FROM aggregated_transaction
GROUP BY state
ORDER BY total ASC
LIMIT 10;

-- 2 Low Districts
SELECT district, SUM(transaction_amount) AS total
FROM map_transaction_district
WHERE year = 2022 AND quarter = 1
GROUP BY district
ORDER BY total ASC
LIMIT 10;

-- 3 State Contribution
SELECT state, SUM(transaction_amount) AS total
FROM map_transaction_state
WHERE year = 2022 AND quarter = 1
GROUP BY state;

-- 4 Combined Top Areas
SELECT state, district, SUM(transaction_amount) AS total
FROM map_transaction_combined
WHERE year = 2022 AND quarter = 1
GROUP BY state, district
ORDER BY total DESC
LIMIT 10;


-- 4 Combined Top Areas
SELECT state, district, SUM(transaction_amount) AS total
FROM map_transaction_combined
WHERE year = 2022 AND quarter = 1
GROUP BY state, district
ORDER BY total DESC
LIMIT 10;

-- 1 Yearly Users
SELECT year, SUM(user_count) AS users
FROM aggregated_user
GROUP BY year
ORDER BY year;

-- 2 Top States Users
SELECT state, SUM(user_count) AS users
FROM aggregated_user
GROUP BY state
ORDER BY users DESC;
-- 3 District Growth
SELECT district, SUM(registered_users) AS users
FROM map_user
GROUP BY district
ORDER BY users DESC
LIMIT 10;

-- 4 App Opens Growth
SELECT year, SUM(app_opens) AS opens
FROM map_user
GROUP BY year
ORDER BY year;


-- 5 Top Pincode Users
SELECT pincode, SUM(registered_users) AS users
FROM user_pincode
GROUP BY pincode
ORDER BY users DESC
LIMIT 10;

SELECT year, quarter, COUNT(*) 
FROM map_user
GROUP BY year, quarter;

SELECT quarter, SUM(app_opens)
FROM map_user
WHERE year = 2018
GROUP BY quarter;
SELECT year, SUM(app_opens)
FROM map_user
GROUP BY year;



SELECT year, quarter, SUM(app_opens)
FROM map_user
GROUP BY year, quarter;