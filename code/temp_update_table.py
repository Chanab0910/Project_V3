from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlite3
from code.models import Country, CountryMatch

engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)
conn = sqlite3.connect("../World_cup.sqlite")
cursor = conn.cursor()

thing = """
Select *
From country
"""

cursor.execute(thing)
conn.commit()
conn.close()
