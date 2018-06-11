
from dateTimeMonth import getTimeData
from writeJson import writeUser
import random 
import os.path
import json

def getFilename(department):
	if department=='E':
		return 'ece'
	elif department =='C':
		return 'comp'
	else :
		return 'mach'


def getFinger(uid):
	finger = random.randint(1,11)
	finger = str(finger)
	data = {}
	#-*- coding: future_fstrings -*-
	#filePathNameWExt =
	filePathNameWExt = './' + '../fingerDb' + '/' + uid + '.json'
	with open(filePathNameWExt, 'w') as fp:
		fp.write(finger)



def getRFID(uid):
	RFID = random.randint(1,101)
	data = {}
	data[RFID] = uid	
	if os.path.isfile('allUsers.json')== True:
		if os.stat("allUsers.json").st_size == 0 :
			with open('allUsers.json', 'w') as fp:
				json.dump(data, fp)
		else:
			with open('allUsers.json', 'r') as fp:
				old_data = json.load(fp)
				data=old_data.update(data)
				# print old_data
			with open('allUsers.json', 'w') as fp:
				json.dump(old_data, fp)

	else :
		with open('allUsers.json', 'w') as fp:
			json.dump(data, fp)

	



def regNew(data):
	getRFID(data['uid'])
	getFinger(data['uid'])
	writeUser('user',getFilename(data['depart']),data)

# data = {"name":"7UP","uid":"Js5CyWMhrfO2nsXtW22peZazo2w1","depart" : "M"}

# regNew(data)