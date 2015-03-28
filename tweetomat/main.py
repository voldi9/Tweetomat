import os, psycopg2, globalvals, run

globalvals.init()

import os, psycopg2, globalvals, run

#check if our tables already exist
conn = psycopg2.connect(globalvals.dbcommand)
cur = conn.cursor()
cur.execute("SELECT * FROM information_schema.tables WHERE table_name=%s", ('keyword',))

#if table don't exist, create them
if cur.rowcount == 0: 
	#add tables
	f = open('tmtables.sql', 'r')
	cur.execute(f.read())
	#add popular example users
	f = open('tmbasic.sql', 'r')
	cur.execute(f.read())
	conn.commit()

cur.close()
conn.close()

run.start()
