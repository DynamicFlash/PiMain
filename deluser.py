import json
import os


def delU(data):
	file = ['ece','comp','mach']
	for fileName in file:
		# fileName = 'ece'
		filePathNameWExt = './' + 'user' + '/' + fileName + '.json'
		if fileName == 'ece':
			if os.path.isfile(filePathNameWExt)== True:
				if os.stat(filePathNameWExt).st_size == 0 :
					raise ValueError('No data')
				else:
					with open(filePathNameWExt, 'r') as fp:
						old_data = json.load(fp)
						# print old_data
						for d in old_data['E']:
							if d.get('name') == data:
								uid = d.get('uid')
								filePathNameWExt = './' + '../fingerDb' + '/' + uid + '.json'
								os.remove(filePathNameWExt)
								with open('allUsers.json', 'r') as fp:
									datarfid = json.load(fp)
									ui=0
									for k in datarfid:
										if datarfid[k] == uid:
											ui = k
									del datarfid[ui]
									# print datarfid
									with open('allUsers.json', 'w') as fp:
										json.dump(datarfid, fp)
						old_data['E'] = [d for d in old_data['E'] if d.get('name') != data]
						# print old_data
						filePathNameWExt = './' + 'user' + '/' + fileName + '.json'
						with open(filePathNameWExt, 'w') as fp:
							json.dump(old_data, fp)

		if fileName == 'comp':
			if os.path.isfile(filePathNameWExt)== True:
				if os.stat(filePathNameWExt).st_size == 0 :
					raise ValueError('No data')
				else:
					with open(filePathNameWExt, 'r') as fp:
						old_data = json.load(fp)
						# print old_data
						for d in old_data['C']:
							if d.get('name') == data:
								uid = d.get('uid')
								filePathNameWExt = './' + '../fingerDb' + '/' + uid + '.json'
								os.remove(filePathNameWExt)
								with open('allUsers.json', 'r') as fp:
									datarfid = json.load(fp)
									ui=0
									for k in datarfid:
										if datarfid[k] == uid:
											ui = k
									del datarfid[ui]
									# print datarfid
									with open('allUsers.json', 'w') as fp:
										json.dump(datarfid, fp)
						old_data['C'] = [d for d in old_data['C'] if d.get('name') != data]
						# print old_data
						filePathNameWExt = './' + 'user' + '/' + fileName + '.json'
						with open(filePathNameWExt, 'w') as fp:
							json.dump(old_data, fp)


		if fileName == 'mach':
			if os.path.isfile(filePathNameWExt)== True:
				if os.stat(filePathNameWExt).st_size == 0 :
					raise ValueError('No data')
				else:
					with open(filePathNameWExt, 'r') as fp:
						old_data = json.load(fp)
						# print old_data
						for d in old_data['M']:
							if d.get('name') == data:
								uid = d.get('uid')
								filePathNameWExt = './' + '../fingerDb' + '/' + uid + '.json'
								os.remove(filePathNameWExt)
								with open('allUsers.json', 'r') as fp:
									datarfid = json.load(fp)
									ui=0
									for k in datarfid:
										if datarfid[k] == uid:
											ui = k
									del datarfid[ui]
									# print datarfid
									with open('allUsers.json', 'w') as fp:
										json.dump(datarfid, fp)
						old_data['M'] = [d for d in old_data['M'] if d.get('name') != data]
						# print old_data
						filePathNameWExt = './' + 'user' + '/' + fileName + '.json'
						with open(filePathNameWExt, 'w') as fp:
							json.dump(old_data, fp)


# data = {"depart": "M", "uid": "K3MKT7UyHuZyuPPSGYJWhToENAV2", "name": "Sprite"}
# delU(data['name'])