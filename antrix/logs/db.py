import datetime
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "dbname": "test",
    "user": "postgres",
    "password": os.getenv("db_password"),
    "host": "localhost",
    "port": "5432"
}

conn = None
cursor = None

def get_connection():
    global conn, cursor
    if conn is None or cursor is None:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            cursor = conn.cursor()
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None, None
    return conn, cursor

def save_log(company, email, brochure, result, retries):
    c, cur = get_connection()
    if cur is None:
        print(f"Warning: Could not save log for {company}")
        return
    try:
        company_name = company if isinstance(company, str) else company.get("company_name", company)
        
        # Extract values with proper types matching schema
        score = result.get("score", 0)
        if score is None or score == "":
            score = 0
        else:
            try:
                score = int(score)
            except (ValueError, TypeError):
                score = 0
        
        status = result.get("status", "unknown")
        feedback = result.get("feedback", "")
        
        cur.execute("""
            INSERT INTO poc_logs (company_name, email_output, brochure_output, review_score, review_feedback, status, retries, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            company_name,
            email,
            brochure,
            score,
            feedback,
            status,
            retries,
            datetime.datetime.now()
        ))
        c.commit()
        print(f"✓ Logged: {company_name}")
    except Exception as e:
        print(f"Error saving log for {company_name}: {e}")
        c.commit()
    except Exception as e:
        print(f"Error saving log: {e}")