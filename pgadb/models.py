from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, JSON, Date, UniqueConstraint

metadata = MetaData()

api_requests = Table(
    "api_requests",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("url", String),
    Column("request_dtm", DateTime),
    Column("status_code", Integer),
    Column("response_text", String),
    Column("response_json", JSON)
)

schedule = Table(
    "schedule",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("tournament", String, nullable=False),
    Column("location", String, nullable=False),
    Column("course_name", String, nullable=False),
    Column("tournament_id", String(length=4), nullable=False),
    Column("start_date", Date, nullable=False),
    Column("end_date", Date, nullable=False),
    Column("schedule_year", Integer, nullable=False),
    Column("leaderboard_url", String),
    Column("notes", String),
    UniqueConstraint("tournament_id", "schedule_year")
)
