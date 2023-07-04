from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

import requests

# Define the URL of the page you want to scrape
url = 'https://www.mlb.com/stats/'

# Make the request to the website
r = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(r.content, 'html.parser')

# Find the table with the player data. This will depend on the structure of the webpage.
table = soup.find('table')

# Create a database engine
engine = create_engine('sqlite:///mlb_players.db')

# Create a metadata instance
metadata = MetaData()

# Define a new table to store the player data
players = Table('players', metadata,
    Column('name', String),
    Column('team', String),
)

# Create the table
metadata.create_all(engine)

# Get the table rows
rows = table.find_all('tr')

# Iterate over the rows
for row in rows:
    # Get the th and td in this row
    th = row.find('th')#, class_="full-3fV3c9pF"})
    td = row.find('td', {"data-col": "1"})

    if th and td:
        # Extract the player data
        name = th.text
        team = td.text

        # Insert the player data into the database
        insert = players.insert().values(name=name, team=team)
        
        # Get a connection and execute the insert statement
        with engine.connect() as connection:
            connection.execute(insert)
