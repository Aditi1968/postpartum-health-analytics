import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
from textblob import TextBlob
import os
import uuid

fake = Faker()
random.seed(42)

NUM_USERS = 20000
NUM_CAREGIVERS = 20
MAX_JOURNALS = 10
PHQ_WEEKS = 4
REGIONS = ["Bangalore", "Tumkur", "Mysore", "Chennai", "Hyderabad", "Pune"]
LANGUAGES = ["Kannada", "Hindi", "Tamil", "Telugu", "Marathi", "English"]
RELATIONS = ["Spouse", "Mother", "Father", "Sister", "Brother"]

output_dir = "maatritva_data/data/"
os.makedirs(output_dir, exist_ok=True)

def generate_users():
    users = []
    for i in range(NUM_USERS):
        users.append({
            "user_id": f"U{str(i).zfill(5)}",
            "name": fake.name(),
            "age": random.randint(20, 42),
            "region": random.choice(REGIONS),
            "language": random.choice(LANGUAGES),
            "created_at": fake.date_between(start_date="-1y", end_date="today")
        })
    return pd.DataFrame(users)

def generate_caregivers():
    caregivers = []
    for i in range(NUM_CAREGIVERS):
        caregivers.append({
            "caregiver_id": f"CG{str(i).zfill(4)}",
            "name": fake.name(),
            "contact_email": fake.email(),
            "phone_number": fake.phone_number(),
            "region": random.choice(REGIONS),
            "assigned_count": 0,
            "created_at": fake.date_between(start_date="-1y", end_date="today")
        })
    return pd.DataFrame(caregivers)

def assign_caregivers(users_df, caregivers_df):
    map_data = []
    for _, user in users_df.iterrows():
        caregiver = caregivers_df.sample(1).iloc[0]
        map_data.append({
            "user_id": user["user_id"],
            "caregiver_id": caregiver["caregiver_id"]
        })
    return pd.DataFrame(map_data)

def generate_family_members(users_df):
    families, access = [], []
    for _, user in users_df.iterrows():
        for _ in range(random.choice([0, 1, 2])):
            family_id = f"FM{uuid.uuid4().hex[:6]}"
            families.append({
                "family_id": family_id,
                "name": fake.name(),
                "relationship": random.choice(RELATIONS),
                "email": fake.email(),
                "phone": fake.phone_number(),
                "created_at": fake.date_between(start_date="-1y", end_date="today")
            })
            access.append({
                "user_id": user["user_id"],
                "family_id": family_id,
                "access_type": random.choice(["read-only", "alerts-only"]),
                "granted_at": fake.date_between(start_date="-6m", end_date="today")
            })
    return pd.DataFrame(families), pd.DataFrame(access)

def generate_journals(users_df):
    journals, alerts = [], []
    journal_id = 0
    for _, user in users_df.iterrows():
        neg_count = 0
        for _ in range(random.randint(5, MAX_JOURNALS)):
            date = fake.date_between(start_date="-30d", end_date="today")
            text = fake.sentence(nb_words=12)
            sentiment = TextBlob(text).sentiment.polarity
            emotion = "negative" if sentiment < -0.1 else "positive" if sentiment > 0.1 else "neutral"
            journals.append({
                "journal_id": f"J{journal_id}",
                "user_id": user["user_id"],
                "date": date,
                "text": text,
                "sentiment_score": round(sentiment, 3),
                "emotion": emotion.lower().capitalize()
            })
            if sentiment < -0.1:
                neg_count += 1
            else:
                neg_count = 0

            if neg_count >= 3:
                alerts.append({
                    "alert_id": f"A{uuid.uuid4().hex[:6]}",
                    "user_id": user["user_id"],
                    "type": "Mood",
                    "reason": "3 negative journal entries",
                    "severity": "Medium",
                    "date": date
                })
                neg_count = 0
            journal_id += 1
    return pd.DataFrame(journals), pd.DataFrame(alerts)

def generate_phq_scores(users_df):
    scores, alerts = [], []
    for _, user in users_df.iterrows():
        for week in range(1, PHQ_WEEKS + 1):
            q_scores = [random.randint(0, 3) for _ in range(9)]
            total = sum(q_scores)
            if total <= 4:
                severity = "None"
            elif total <= 9:
                severity = "Mild"
            elif total <= 14:
                severity = "Moderate"
            elif total <= 19:
                severity = "Moderately Severe"
            else:
                severity = "Severe"
            date = (datetime.today() - timedelta(days=(PHQ_WEEKS - week) * 7)).date()
            scores.append({
                "score_id": f"SC{uuid.uuid4().hex[:6]}",
                "user_id": user["user_id"],
                "week": week,
                **{f"q{i+1}": q_scores[i] for i in range(9)},
                "total_score": total,
                "severity": severity,
                "date": date
            })
            if total >= 15:
                alerts.append({
                    "alert_id": f"A{uuid.uuid4().hex[:6]}",
                    "user_id": user["user_id"],
                    "type": "PHQ",
                    "reason": f"High PHQ Score: {total}",
                    "severity": "High" if total > 20 else "Medium",
                    "date": date
                })
    return pd.DataFrame(scores), pd.DataFrame(alerts)

def generate_dim_date():
    base = datetime.today()
    dates = [base - timedelta(days=x) for x in range(365)]
    dim = []
    for d in dates:
        dim.append({
            "date_key": d.date(),
            "day": d.day,
            "month": d.month,
            "month_name": d.strftime("%B"),
            "year": d.year,
            "week": d.isocalendar()[1]
        })
    return pd.DataFrame(dim)

def generate_health_visits(users_df):
    visits = []
    for _, user in users_df.iterrows():
        for _ in range(random.randint(1, 3)):
            visit_date = fake.date_between(start_date="-90d", end_date="today")
            visits.append({
                "visit_id": f"V{uuid.uuid4().hex[:6]}",
                "user_id": user["user_id"],
                "date": visit_date,
                "reason": random.choice(["Follow-up", "Pain", "Fever", "Checkup"]),
                "location": random.choice(["Clinic", "Teleconsultation", "Hospital"]),
                "attended": random.choice([True, True, False])  # Most attended
            })
    return pd.DataFrame(visits)


# === RUN ===
print("Generating Users...")
users = generate_users()
caregivers = generate_caregivers()
print("Assigning Caregivers...")
user_caregiver_map = assign_caregivers(users, caregivers)
print("Generating Family Members...")
family_members, family_access = generate_family_members(users)
print("Generating Journals...")
journals, mood_alerts = generate_journals(users)
print("Generating PHQ Scores...")
phq_scores, phq_alerts = generate_phq_scores(users)
print("Generating Dates...")
dim_date = generate_dim_date()
print("Combining Alerts...")
alerts = pd.concat([mood_alerts, phq_alerts]).drop_duplicates()
print("Generating Visits...")
visits = generate_health_visits(users)
visits.to_csv(output_dir + "visits.csv", index=False)


# === SAVE FILES ===
users.to_csv(output_dir + "users.csv", index=False)
caregivers.to_csv(output_dir + "caregivers.csv", index=False)
user_caregiver_map.to_csv(output_dir + "user_caregiver_map.csv", index=False)
family_members.to_csv(output_dir + "family_members.csv", index=False)
family_access.to_csv(output_dir + "user_family_access.csv", index=False)
journals.to_csv(output_dir + "journals.csv", index=False)
phq_scores.to_csv(output_dir + "phq_scores.csv", index=False)
alerts.to_csv(output_dir + "alerts.csv", index=False)
dim_date.to_csv(output_dir + "dim_date.csv", index=False)

print("✅ All 9 CSVs generated and saved to:", output_dir)
