from dataclasses import dataclass
import psycopg2
from psycopg2.extras import RealDictCursor
import json


host = ""
username =""
password = ""
database =""

conn = psycopg2.connect(
    host = host,
    database = database,
    user = username,
    password = password
)

def lambda_handler(event, context):
    cur = conn.cursor(cursor_factory = RealDictCursor)
    cur.execute("select * from state")
    results = cur.fetchall()
    json_result = json.dumps(results)
    print(json_result)
    return json_result
    

#lambda_handler()
