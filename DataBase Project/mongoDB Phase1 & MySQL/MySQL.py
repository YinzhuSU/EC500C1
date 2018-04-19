#import mysql.connector
import sqlite3
import json
connection = sqlite3.connect('yzsuSQL.db')
c = connection.cursor()
c.execute('''CREATE TABLE airports(code text, lat text, lon text, name text, city text, state text, 
		country text, woeid text, tz text, phone text, type text, email, text 
		url text, runway_length text, elev text, icao text, direct_flights text, carriers text)''')
with open('airports.json') as json_file:
	new_json = json.loads(json_file.read())
	for info in new_json:
		List = []
		List_value  = info.values()
		for i in List_value:
			List.append(i)
		c.execute("INSERT INTO airports VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
		(List[0], List[1], List[2], List[3], List[4], List[5], List[6], List[7], List[8], 
			List[9], List[10], List[11], List[12], List[13], List[14], List[15], List[16], List[17]))
connection.commit()
c.close()
connection.close()