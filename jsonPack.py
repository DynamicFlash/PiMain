import json
from dateTimeMonth import getTimeData
from readJson import readJSONFile
import os

def readOnly(filePath):
	with open(filePath, 'r') as fp:
    		old_data = json.load(fp)
    		print old_data['E']
    		return old_data['E']


def packet():
	data={}
	date =getTimeData();
	mid = {
	"date" : date[0],
	"month": date[1],
	"time" : date[2]
	}

	data["A"] = {}
	data["A"].update(mid)
	mide = readJSONFile('pack','ecep')
	midm = readJSONFile('pack','machp')
	midc = readJSONFile('pack','compp')
	data.update(mide)
	data.update(midm)
	data.update(midc)
	with open('./pack/pack.json', 'w') as fp:
		json.dump(data, fp)
    

	return data

def check(uid):
	with open('./today.json','r') as fp:
		data =json.load(fp)
		for j in data['users']:
			if j.get('uid') == uid:
				return [True,j.get('time')]
	return False

def ecePack():
	with open('./user/ece.json', 'r') as fp1:
		datae =json.load(fp1)
		for i in datae['E']:
			data = check(i.get('uid'))
			if data == False:
				dat ={ }
				dat['uid'] = i.get('uid')
				dat['time'] = 'Late'
				E =[ ]
				E.append(dat)
				datap={}
				datap['E'] = E
				print datap
				filePathNameWExt = './pack/ecep.json'
				if os.path.isfile(filePathNameWExt)== True:
					if os.stat(filePathNameWExt).st_size == 0 :
						with open(filePathNameWExt, 'w') as fp:
							json.dump(datap, fp)
					else:
						with open(filePathNameWExt, 'r') as fp:
							old_data = json.load(fp)
							data=old_data['E'].append(dat)
							# print old_data
						with open(filePathNameWExt, 'w') as fp:
							json.dump(old_data, fp)
				else :
					with open(filePathNameWExt, 'w') as fp:
						json.dump(datap	, fp)

			else :
				dat ={ }
				dat['uid'] = i.get('uid')
				dat['time'] =data[1]
				E =[ ]
				E.append(dat)
				datap={}
				datap['E'] = E
				print datap
				filePathNameWExt = './pack/ecep.json'
				if os.path.isfile(filePathNameWExt)== True:
					if os.stat(filePathNameWExt).st_size == 0 :
						with open(filePathNameWExt, 'w') as fp:
							json.dump(datap, fp)
					else:
						with open(filePathNameWExt, 'r') as fp:
							old_data = json.load(fp)
							data=old_data['E'].append(dat)
							# print old_data
						with open(filePathNameWExt, 'w') as fp:
							json.dump(old_data, fp)
				else :
					with open(filePathNameWExt, 'w') as fp:
						json.dump(datap	, fp)


def machPack():
	with open('./user/mach.json', 'r') as fp1:
		datae =json.load(fp1)
		for i in datae['M']:
			data = check(i.get('uid'))
			if data == False:
				dat ={ }
				dat['uid'] = i.get('uid')
				dat['time'] = 'Late'
				M =[ ]
				M.append(dat)
				datap={}
				datap['M'] = M
				print datap
				filePathNameWExt = './pack/machp.json'
				if os.path.isfile(filePathNameWExt)== True:
					if os.stat(filePathNameWExt).st_size == 0 :
						with open(filePathNameWExt, 'w') as fp:
							json.dump(datap, fp)
					else:
						with open(filePathNameWExt, 'r') as fp:
							old_data = json.load(fp)
							data=old_data['M'].append(dat)
							# print old_data
						with open(filePathNameWExt, 'w') as fp:
							json.dump(old_data, fp)
				else :
					with open(filePathNameWExt, 'w') as fp:
						json.dump(datap	, fp)

			else :
				dat ={ }
				dat['uid'] = i.get('uid')
				dat['time'] =data[1]
				M =[ ]
				M.append(dat)
				datap={}
				datap['M'] = M
				print datap
				filePathNameWExt = './pack/machp.json'
				if os.path.isfile(filePathNameWExt)== True:
					if os.stat(filePathNameWExt).st_size == 0 :
						with open(filePathNameWExt, 'w') as fp:
							json.dump(datap, fp)
					else:
						with open(filePathNameWExt, 'r') as fp:
							old_data = json.load(fp)
							data=old_data['M'].append(dat)
							# print old_data
						with open(filePathNameWExt, 'w') as fp:
							json.dump(old_data, fp)
				else :
					with open(filePathNameWExt, 'w') as fp:
						json.dump(datap	, fp)


def compPack():
	with open('./user/comp.json', 'r') as fp1:
		datae =json.load(fp1)
		for i in datae['C']:
			data = check(i.get('uid'))
			if data == False:
				dat ={ }
				dat['uid'] = i.get('uid')
				dat['time'] = 'Late'
				C =[ ]
				C.append(dat)
				datap={}
				datap['C'] = M
				print datap
				filePathNameWExt = './pack/compp.json'
				if os.path.isfile(filePathNameWExt)== True:
					if os.stat(filePathNameWExt).st_size == 0 :
						with open(filePathNameWExt, 'w') as fp:
							json.dump(datap, fp)
					else:
						with open(filePathNameWExt, 'r') as fp:
							old_data = json.load(fp)
							data=old_data['C'].append(dat)
							# print old_data
						with open(filePathNameWExt, 'w') as fp:
							json.dump(old_data, fp)
				else :
					with open(filePathNameWExt, 'w') as fp:
						json.dump(datap	, fp)

			else :
				dat ={ }
				dat['uid'] = i.get('uid')
				dat['time'] =data[1]
				C =[ ]
				C.append(dat)
				datap={}
				datap['C'] = C
				print datap
				filePathNameWExt = './pack/compp.json'
				if os.path.isfile(filePathNameWExt)== True:
					if os.stat(filePathNameWExt).st_size == 0 :
						with open(filePathNameWExt, 'w') as fp:
							json.dump(datap, fp)
					else:
						with open(filePathNameWExt, 'r') as fp:
							old_data = json.load(fp)
							data=old_data['C'].append(dat)
							# print old_data
						with open(filePathNameWExt, 'w') as fp:
							json.dump(old_data, fp)
				else :
					with open(filePathNameWExt, 'w') as fp:
						json.dump(datap	, fp)



ecePack()
machPack()
compPack()
print(packet())