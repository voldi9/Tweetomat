import psycopg2, globalvals
from twython import Twython, TwythonError
from datetime import datetime, timedelta
import re

#if we succeed in getting fresh user_timeline, we can delete rows connected with him from 
#the database
def clearuser(login):
	conn = psycopg2.connect(globalvals.dbcommand)
	cur = conn.cursor()
	cur.execute("UPDATE Users SET tweets = 0, lasttweetid = 1 WHERE login = %s", (login,))
	conn.commit()

	lowerrates(login)

	cur.execute("DELETE FROM Tweet WHERE userid = %s", (login,))
	conn.commit()
	cur.close()
	conn.close()

#when user gets enabled, we increase his keyword's rates
def addrates(login):
	conn = psycopg2.connect(globalvals.dbcommand)
	cur = conn.cursor()
	cur.execute("SELECT * FROM Tweet WHERE userid = %s", (login,))
	user_tweets = cur.fetchall()

	for tweet in user_tweets:
		timeago = tweet[globalvals.tlastup] - tweet[globalvals.tdate]

		allkeywords = [m.start() for m in re.finditer(' ', tweet[globalvals.tcontent])]
		prev = 0

		#add tags' and user_mentions' grade
		for keyw in allkeywords:
			updtag(tweet[globalvals.tcontent][prev:keyw], timeago.days*24 + float(timeago.seconds)/3600, \
			tweet[globalvals.tfavs], tweet[globalvals.trets], tweet[globalvals.tid], 1)
			prev = keyw + 1

	conn.commit()
	cur.close()
	conn.close()		

#when user gets disabled, but not deleted, we need to decrease his keyword's rates
#without deleting any rows from database
def lowerrates(login):
	conn = psycopg2.connect(globalvals.dbcommand)
	cur = conn.cursor()
	cur.execute("SELECT * FROM Tweet WHERE userid = %s", (login,))
	user_tweets = cur.fetchall()

	for tweet in user_tweets:
		timeago = tweet[globalvals.tlastup] - tweet[globalvals.tdate]

		allkeywords = [m.start() for m in re.finditer(' ', tweet[globalvals.tcontent])]
		prev = 0

		#lower tags' and user_mentions' grade
		for keyw in allkeywords:
			updtag(tweet[globalvals.tcontent][prev:keyw], timeago.days*24 + float(timeago.seconds)/3600, \
			tweet[globalvals.tfavs], tweet[globalvals.trets], tweet[globalvals.tid], -1)
			prev = keyw + 1

	conn.commit()
	cur.close()
	conn.close()	

#delete user, his tweets and their keywords from database
def deleteuser(login):
	conn = psycopg2.connect(globalvals.dbcommand)
	cur = conn.cursor()
	cur.execute("UPDATE Users SET active = false WHERE login = %s", (login,))
	conn.commit()
	clearuser(login)
	cur.close()
	conn.close()

#mark user as active
def enableuser(login):
	conn = psycopg2.connect(globalvals.dbcommand)
	cur = conn.cursor()
	cur.execute("UPDATE Users SET active = true WHERE login = %s", (login,))
	conn.commit()
	updateuser(login)
	cur.close()
	conn.close()

#get user's recent tweets and update keywords and their rates
def updateuser(login):
	tweets = 0
	lasttweetid = 1
	conn = psycopg2.connect(globalvals.dbcommand)
	cur = conn.cursor()

	try:
		twitter = Twython(globalvals.APP_KEY, access_token = globalvals.ACCESS_TOKEN)
	except TwythonError as e:
		print e

	try:
		user_timeline = twitter.get_user_timeline(screen_name = login, since_id = lasttweetid + 1)
		#delete user's tweet from database only if we succeeded in getting his timeline!
		clearuser(login)
	except TwythonError as e: #otherwise end updating
		print e
		return None

	for tweet in user_timeline:
		tweets = tweets + 1
		if tweets == 1:
			lasttweetid = tweet['id']

		cur.execute("SELECT current_timestamp;")
		acttime = cur.fetchone()[0]
		acttime = acttime.replace(tzinfo = None)

		cur.execute("SELECT %s - %s;", (acttime, tweet['created_at']))
		
		#check if the tweet is older than 14 days
		timeago = cur.fetchone()[0]
		if timeago > timedelta(days=globalvals.daysstored):
			break
		
		cur.execute("INSERT INTO Tweet VALUES (%s, %s, %s, %s, %s, %s, %s);", (tweet['id'], '', \
		login, tweet['created_at'], acttime, tweet['favorite_count'], tweet['retweet_count']))
		conn.commit()
		content = ''

		#update tags' and user_mentions' grade
		for tag in tweet['entities']['hashtags']:
			content += '#' + tag['text'].lower() + ' '
			updtag('#' + tag['text'].lower(), timeago.days*24 + float(timeago.seconds)/3600, \
			tweet['favorite_count'], tweet['retweet_count'], tweet['id'], 1)
		for usrmen in tweet['entities']['user_mentions']:
			content += '@' + usrmen['screen_name'].lower() + ' '
			updtag('@' + usrmen['screen_name'].lower(), timeago.days*24 + float(timeago.seconds)/3600, \
			tweet['favorite_count'], tweet['retweet_count'], tweet['id'], 1)

		cur.execute("UPDATE Tweet SET content = %s WHERE id = %s", (content, tweet['id']))
	
	cur.execute("UPDATE Users SET tweets = tweets + %s, lasttweetid = %s WHERE login = %s", \
	(tweets, lasttweetid, login))
	conn.commit()
	cur.close()
	conn.close()

#adds certain value to the keyword's rate if occ == 1, otherwise 
#decreases the rate by value
def updtag(tag, hrs, favs, rets, tweetid, occ):
	conn = psycopg2.connect(globalvals.dbcommand);
	cur = conn.cursor()

	#equation used in order to increase the keyword's rates
	addrate = (favs+rets)*(favs+2*rets)/hrs

	cur.execute("SELECT * FROM Keyword WHERE content = %s", (tag,))

	if cur.rowcount > 0:
		cur.execute("""UPDATE Keyword SET occurences = occurences + %s, rate = rate + %s
					   WHERE content = %s""", (occ, occ * addrate, tag))
	else:
		if occ == 1:
			cur.execute("INSERT INTO Keyword VALUES (%s, %s, %s);", (tag, 1, addrate))

	if occ == -1:
		cur.execute("SELECT occurences FROM Keyword WHERE content = %s", (tag,))
		if cur.rowcount > 0:
			if cur.fetchone()[0] < 1:
				cur.execute("DELETE FROM Keyword WHERE content = %s", (tag,))

	conn.commit()
	cur.close()
	conn.close()