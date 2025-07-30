-- Users Table
CREATE TABLE users (
    user_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    region VARCHAR(50),
    language VARCHAR(50),
    created_at DATE,
    risk_flag VARCHAR(10)  -- Low, Medium, High
);

-- Caregivers Table
CREATE TABLE caregivers (
    caregiver_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    contact_email VARCHAR(100),
    phone_number VARCHAR(20),
    region VARCHAR(50),
    assigned_count INT,
    created_at DATE
);

-- Mapping between Users and Caregivers
CREATE TABLE user_caregiver_map (
    user_id VARCHAR(10),
    caregiver_id VARCHAR(10),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (caregiver_id) REFERENCES caregivers(caregiver_id)
);

-- Family Members
CREATE TABLE family_members (
    family_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    relationship VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    created_at DATE
);

-- User-Family Access Mapping
CREATE TABLE user_family_access (
    user_id VARCHAR(10),
    family_id VARCHAR(10),
    access_type VARCHAR(20),  -- read-only / alerts-only
    granted_at DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (family_id) REFERENCES family_members(family_id)
);

-- Journals
CREATE TABLE journals (
    journal_id VARCHAR(20) PRIMARY KEY,
    user_id VARCHAR(10),
    date DATE,
    text TEXT,
    sentiment_score FLOAT,
    emotion VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- PHQ-9 Scores
CREATE TABLE phq_scores (
    score_id VARCHAR(20) PRIMARY KEY,
    user_id VARCHAR(10),
    week INT,
    q1 INT, q2 INT, q3 INT, q4 INT, q5 INT, q6 INT, q7 INT, q8 INT, q9 INT,
    total_score INT,
    severity VARCHAR(30),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Health Visits
CREATE TABLE visits (
    visit_id VARCHAR(20) PRIMARY KEY,
    user_id VARCHAR(10),
    date DATE,
    reason VARCHAR(100),
    location VARCHAR(50),
    attended BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Alerts
CREATE TABLE alerts (
    alert_id VARCHAR(20) PRIMARY KEY,
    user_id VARCHAR(10),
    type VARCHAR(20),       -- PHQ or Mood
    reason VARCHAR(100),
    severity VARCHAR(20),   -- Medium, High
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Time Dimension
CREATE TABLE dim_date (
    date_key DATE PRIMARY KEY,
    day INT,
    month INT,
    month_name VARCHAR(20),
    year INT,
    week INT
);

-- Region Dimension
CREATE TABLE dim_region (
    region VARCHAR(50) PRIMARY KEY,
    state VARCHAR(50)
);
