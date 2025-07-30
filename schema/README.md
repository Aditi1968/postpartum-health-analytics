# 🧱 Database Schema – Postpartum Health Intelligence Hub

This folder contains all database artifacts used in the postpartum mental health risk analytics project.

---

## 📚 Description

This schema was designed to simulate a real-world healthcare data system where users (mothers) log journal entries and complete weekly PHQ-9 assessments. The data is linked with assigned caregivers, family access permissions, mood tracking, and auto-triggered alerts.

---

## 🔗 Key Relationships

- Every user is assigned to a caregiver (`user_caregiver_map`)
- Journal entries and PHQ scores are tied to individual users
- Family members are granted read-only or alert access
- Alerts are raised if mood or PHQ-9 scores indicate high risk
- `dim_date` and `dim_region` are used for analytical dashboards

---

## 📁 Files

| File                     | Description                             |
|--------------------------|-----------------------------------------|
| `schema.sql`             | Raw SQL CREATE TABLE statements         |
| `dbml_schema.dbml`       | Schema in DBML format for diagrams      |
| `schema.png`             | Visual ER diagram                       |
| `README.md`              | This documentation                      |

---

## 📸 ER Diagram

> Refer to `schema.png` or [View on dbdiagram.io](https://dbdiagram.io/) for live edits.
