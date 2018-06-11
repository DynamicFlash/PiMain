from dateTimeMonth import getTimeData
import json
import os

def getInfo(data):
	timeDate=getTimeData();
	timeNow =timeDate[2]
	with open('allUsers.json', 'r') as fp:
		datarfid = json.load(fp)
		for i in datarfid:
			print i
		# index = str(data)
		uid = datarfid[data]
		filePathNameWExt = './' + 'today' + '.json'
		datat = { }
		datat['uid']=uid;
		datat['time']=timeNow;
		users = [ ]
		users.append(datat)
		datae = { }
		datae ['users'] = users	
		if os.path.isfile(filePathNameWExt)== True:
			if os.stat(filePathNameWExt).st_size == 0 :
				with open(filePathNameWExt, 'w') as fp:
					json.dump(datae, fp)
			else:
				with open(filePathNameWExt, 'r') as fp:
					old_data = json.load(fp)
					data=old_data['users'].append(datat)
					# print old_data
				with open(filePathNameWExt, 'w') as fp:
					json.dump(old_data, fp)

		else :
			with open(filePathNameWExt, 'w') as fp:
				json.dump(datae, fp)


getInfo('84')
