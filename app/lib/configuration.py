from uuid import getnode

from decouple import config

pg_username = config("DB_USER", "root")
pg_password = config("DB_PASS", "root")
pg_host = config("DB_HOST", "localhost")
try:
    pg_port = int(config("DB_PORT", "5432"))
except ValueError:
    pg_port = 5432
pg_database = config("DB_DATABASE", "spiderweb")
pg_uri = f"postgresql://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"

session_key = config("SESSION_KEY", str(getnode()))
try:
    # 2880 is 2 days in minutes
    session_lifetime = int(config("SESSION_LIFETIME", "2880"))
except ValueError:
    session_lifetime = 2880
