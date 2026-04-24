CREATE DATABASE IF NOT EXISTS phonepe_db;
drop database phonepe_db;
USE phonepe_db;
CREATE TABLE IF NOT EXISTS aggregated_transaction (
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE,
    PRIMARY KEY (state, year, quarter, transaction_type)
);
ALTER TABLE aggregated_transaction
ADD UNIQUE KEY unique_txn (
    state,
    year,
    quarter,
    transaction_type
);

CREATE TABLE IF NOT EXISTS aggregated_insurance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE,

    UNIQUE KEY unique_insurance (
        state,
        year,
        quarter,
        transaction_type
    )
);
SELECT COUNT(*) FROM aggregated_insurance;


CREATE TABLE IF NOT EXISTS aggregated_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    brand VARCHAR(100),
    user_count BIGINT,
    percentage DOUBLE,

    UNIQUE KEY unique_user (
        state,
        year,
        quarter,
        brand
    )
);


CREATE TABLE IF NOT EXISTS map_insurance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(150),
    transaction_count BIGINT,
    transaction_amount DOUBLE,

    UNIQUE KEY unique_map_insurance (
        state,
        year,
        quarter,
        district
    )
);
CREATE TABLE IF NOT EXISTS map_transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(150),
    transaction_count BIGINT,
    transaction_amount DOUBLE,

    UNIQUE KEY unique_map_txn (
        state,
        year,
        quarter,
        district
    )
);

CREATE TABLE IF NOT EXISTS map_transaction_state (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_count BIGINT,
    transaction_amount DOUBLE,

    UNIQUE KEY unique_state_txn (
        state,
        year,
        quarter
    )
);



CREATE TABLE IF NOT EXISTS map_transaction_district (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(150),
    year INT,
    quarter INT,
    transaction_count BIGINT,
    transaction_amount DOUBLE,

    UNIQUE KEY unique_district_transaction (
        state,
        district,
        year,
        quarter
    )
);

CREATE TABLE IF NOT EXISTS map_transaction_combined (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(150),
    year INT,
    quarter INT,
    transaction_count BIGINT,
    transaction_amount DOUBLE,
    level VARCHAR(20),

    UNIQUE KEY unique_combined (
        state,
        district,
        year,
        quarter,
        level
    )
);

CREATE TABLE IF NOT EXISTS map_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(150),
    year INT,
    quarter INT,
    registered_users BIGINT,
    app_opens BIGINT,

    UNIQUE KEY unique_user (
        state,
        district,
        year,
        quarter
    )
);
select * from map_user;
CREATE TABLE map_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL,
    quarter INT NOT NULL,
    state VARCHAR(100) NOT NULL,
    district VARCHAR(150),
    registered_users BIGINT,
    app_opens BIGINT
);
select * from map_users;
CREATE TABLE IF NOT EXISTS top_insurance_state (
    state VARCHAR(100),
    year INT,
    quarter INT,
    insurance_count BIGINT,
    insurance_amount DOUBLE,

    PRIMARY KEY (state, year, quarter)
);

CREATE TABLE IF NOT EXISTS top_insurance_district (
    state VARCHAR(100),
    district VARCHAR(150),
    year INT,
    quarter INT,
    insurance_count BIGINT,
    insurance_amount DOUBLE,

    PRIMARY KEY (state, district, year, quarter)
);


CREATE TABLE IF NOT EXISTS top_insurance_pincode (
    state VARCHAR(100),
    year INT,
    quarter INT,
    pincode INT,
    insurance_count BIGINT,
    insurance_amount DOUBLE,
    
    PRIMARY KEY (state, year, quarter, pincode)
);
drop table map_user;
CREATE TABLE top_transaction_district (
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(150),
    transaction_count BIGINT,
    transaction_amount DOUBLE,
    PRIMARY KEY (state, year, quarter, district)
);

CREATE TABLE top_transaction_pincode (
    state VARCHAR(100),
    year INT,
    quarter INT,
    pincode INT,
    transaction_count BIGINT,
    transaction_amount DOUBLE,
    PRIMARY KEY (state, year, quarter, pincode)
);

CREATE TABLE combined_top_transactions (
    level VARCHAR(20),              
    state VARCHAR(100),
    year INT,
    quarter INT,
    entity_name VARCHAR(150),       
    transaction_count BIGINT,
    transaction_amount DOUBLE,
    PRIMARY KEY (level, state, year, quarter, entity_name)
);
CREATE TABLE top_user (
    level VARCHAR(20),              
    state VARCHAR(100),
    year INT,
    quarter INT,
    entity_name VARCHAR(150),     
    registered_users BIGINT,
    PRIMARY KEY (level, state, year, quarter, entity_name)
);

CREATE TABLE user_district (
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(150),
    registered_users BIGINT,
    PRIMARY KEY (state, year, quarter, district)
);

CREATE TABLE user_pincode (
    state VARCHAR(100),
    year INT,
    quarter INT,
    pincode INT,
    registered_users BIGINT,
    PRIMARY KEY (state, year, quarter, pincode)
);
SELECT DISTINCT year, quarter 
FROM aggregated_user
ORDER BY year DESC;