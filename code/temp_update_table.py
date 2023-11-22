from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlite3
from code.models import Country, CountryMatch

engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)
conn = sqlite3.connect('sqlite:///World_cup.sqlite3')
cursor = conn.cursor()

thing = """
Select *
From Country
"""

cursor.execute(thing)
conn.commit()
conn.close()
