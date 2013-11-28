#! /usr/bin/python

"""
Script to insert the entries from Squid access.log into a database.

Example of log entry:

1382447026.098    605 127.0.0.1 TCP_MISS/200 1104 CONNECT bugzilla.redhat.com:443 - HIER_DIRECT/10.4.127.4 -

"""


import fileinput
import os
import csv
import hashlib
from peewee import *


# global data base connection, it can use any peewee db connection
db = MySQLDatabase('squid', user='squid', passwd='squid')

class CustomModel(Model):
	class Meta:
		database = db

class Access(CustomModel):
	id = IntegerField()
	uid = CharField()
	time = FloatField()
	timeh = CharField()
	elapse = FloatField()
	remotehost = CharField()
	code = CharField()
	bytes = IntegerField()
	method = CharField()
	url = CharField()
	rfc931 = CharField()
	hierarchy_peerhost = CharField()
	type = CharField()


# convert squid's timestamp to human readable
#def convert_time(utc):
	# to be implemented


# generate a uid with the timestamp, elapsed time and url
def gen_hash(a, b, c):
	return hashlib.md5(a + b + c).hexdigest()

# pick the data from stdin and build two lists: raw and log,
# insert the values into the database
if __name__ == "__main__":
	raw = []
	log = []

	for line in fileinput.input():
		raw.append(line)

	for line in csv.reader(raw, delimiter=" ", skipinitialspace=True):
		log.append(line)

	db.connect()

	for line in log:
		# print(line)
		line_hash = gen_hash(line[0], line[2], line[6])
		
		entry = Access()
		entry.uid = line_hash
		entry.time = line[0]
		# entry.timeh = 
		entry.elapse = line[1]
		entry.remotehost = line[2]
		entry.code = line[3]
		entry.bytes = line[4]
		entry.method = line[5]
		entry.url = line[6]
		entry.rfc931 = line[7]
		entry.hierarchy_peerhost = line[8]
		entry.type = line[9]

		try:
			entry.save()
		except:
			pass

#EOF

