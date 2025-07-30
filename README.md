# 🤱 Postpartum Health Intelligence Hub

A capstone-level SQL + Data Engineering project simulating real-world healthcare workflows for detecting postpartum mental health risks, enabling caregiver alerts, and building powerful analytics dashboards.

---

## 🔍 Project Overview

This project mimics the real responsibilities of a **SQL Developer** working in healthcare:
- Integrating multi-source data (real + synthetic)
- Ensuring data integrity and normalization
- Writing complex queries for reporting and alerting
- Building dimension tables for analytics (date, region)
- Supporting stakeholders with daily and ad-hoc reporting

---

## 🧠 Core Features

✅ Synthetic and real data ingestion  
✅ Risk scoring using PHQ-9  
✅ Sentiment analysis from journal entries  
✅ Family member access control  
✅ Real-time alerts (mood, PHQ)  
✅ Date and region dimension tables  
✅ Schema-first approach with ERD & DBML  
✅ Exportable CSVs for dashboards (Power BI / Tableau)

---

## 🗃️ Relational Schema

The database schema models users, caregivers, PHQ-9 scores, family access, journals, alerts, and more.

> Full schema & ER diagram available in [`/schema`](schema)

![ER Diagram](schema/schema.png)

---

## 🏗️ Tech Stack

- **SQL** (MySQL/PostgreSQL compatible)
- **Python** (Faker, TextBlob, Pandas)
- **DBML** for ER design
- **CSV** output for BI
- **ETL-ready** simulated data pipeline

---

## 📂 Folder Structure

```bash
├── data/                  # CSV files (users, scores, journals, etc.)
├── schema/                # SQL, ER diagram, DBML schema
├── notebooks/             # Python notebooks for data generation
└── README.md              # Project overview
