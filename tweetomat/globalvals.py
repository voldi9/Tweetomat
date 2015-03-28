def init():
	#values used in multiple modules
	global dbcommand, ulasttweetid
	global ulogin, uactive, ucategoryname
	global uadded, utweets, daysstored
	global APP_KEY, APP_SECRET, ACCESS_TOKEN
	global tid, tcontent, tuserid, tdate
	global tlastup, tfavs, trets
	#user constants
	ulogin = 0
	uactive = 1
	ucategoryname = 2
	uadded = 3
	utweets = 4
	ulasttweetid = 5
	#tweet constants
	tid = 0
	tcontent = 1
	tuserid = 2
	tdate = 3
	tlastup = 4
	tfavs = 5
	trets = 6

	daysstored = 14
	dbcommand = """dbname=bd host=labdb user=fk337266 password=dupadupa"""
	APP_KEY = 'XTkiPEZoW7Uz9EwPoiqQ'
	APP_SECRET = 'YVdqiE8FTBO9uDl1ezZvPHSJPAykRkFAQP4sYHk5vU'
	ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKG9VwAAAAAA0LGhWYgfwhYrGO%2FZ6gSCxd71THk%3DND6XIzqG0H8iW3eQz592Ai95tFex7ag9314SC7tuZsST4106rQ'
