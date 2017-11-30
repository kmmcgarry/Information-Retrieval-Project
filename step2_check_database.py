import sqlite3 as sqlite

if __name__ == "__main__":
	with sqlite.connect('../test.db') as con:
		cur = con.cursor()
		cur.execute('select count(*) from clinical_trials')
		print (cur.fetchall())
		cur.execute('select minimum_age from clinical_trials limit 1000')
		print (cur.fetchall())

	






