#import mysql.connector
import sqlite3
import json
connection = sqlite3.connect('yzsuSQL.db')
newtable = connection.cursor()
newtable.execute('''CREATE TABLE airports(code text, lat text, lon text, name text, city text, state text, 
		country text, woeid text, tz text, phone text, type text, email, text 
		url text, runway_length text, elev text, icao text, direct_flights text, carriers text)''')
with open('airports.json') as json_file:
	new_json = json.loads(json_file.read())
	for info in new_json:
		items = []
		itemsValue  = info.values()
		for i in itemsValue:
			items.append(i)
		newtable.execute("INSERT INTO airports VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
		(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8], 
			items[9], items[10], items[11], items[12], items[13], items[14], items[15], items[16], items[17]))
connection.commit()
newtable.close()
connection.close()