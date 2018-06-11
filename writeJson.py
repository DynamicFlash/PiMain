import json
import os.path

def merge_two_dicts(x, y):
	"""Given two dicts, merge them into a new dict as a shallow copy."""
	z = x.copy()
	z.update(y)
	return z


def writeToPack(path, fileName, data):
	filePathNameWExt = './' + path + '/' + fileName + '.json'
	if fileName == 'ece':
		with open(filePathNameWExt, 'r') as fp:
			old_data = json.load(fp)
			data=old_data["E"].append(data)
			print old_data
		with open(filePathNameWExt, 'w') as fp:
			json.dump(old_data, fp)

	if fileName == 'comp':
		with open(filePathNameWExt, 'r') as fp:
			old_data = json.load(fp)
			data=old_data["C"].append(data)
			print old_data
		with open(filePathNameWExt, 'w') as fp:
			json.dump(old_data, fp)

	if fileName == 'mach':
		with open(filePathNameWExt, 'r') as fp:
			old_data = json.load(fp)
			data=old_data["M"].append(data)
			print old_data
		with open(filePathNameWExt, 'w') as fp:
			json.dump(old_data, fp)


def writeUser(path, fileName, data):
	filePathNameWExt = './' + path + '/' + fileName + '.json'

	if fileName == 'ece':
		datae = { }
		E = [ ]
		E.append(data)
		datae ['E'] = E
		if os.path.isfile(filePathNameWExt)== True:
			if os.stat(filePathNameWExt).st_size == 0 :
				with open(filePathNameWExt, 'w') as fp:
					json.dump(datae, fp)
			else:
				with open(filePathNameWExt, 'r') as fp:
					old_data = json.load(fp)
					data=old_data['E'].append(data)
					# print old_data
				with open(filePathNameWExt, 'w') as fp:
					json.dump(old_data, fp)

		else :
			datae = { }
			E = [ ]
			E.append(data)
			datae ['E'] = E
			with open(filePathNameWExt, 'w') as fp:
				json.dump(datae, fp)

	if fileName == 'comp':
		datac = { }
		C = [ ]
		C.append(data)
		datac ['C'] = C		
		if os.path.isfile(filePathNameWExt)== True:
			if os.stat(filePathNameWExt).st_size == 0 :
				with open(filePathNameWExt, 'w') as fp:
					json.dump(datac, fp)
			else:
				with open(filePathNameWExt, 'r') as fp:
					old_data = json.load(fp)
					data=old_data['C'].append(data)
					# print old_data
				with open(filePathNameWExt, 'w') as fp:
					json.dump(old_data, fp)

		else :
			datac = { }
			C = [ ]
			C.append(data)
			datac ['C'] = C			
			with open(filePathNameWExt, 'w') as fp:
				json.dump(datac, fp)


	if fileName == 'mach':
		datam = { }
		M = [ ]
		M.append(data)
		datam ['M'] = M	
		if os.path.isfile(filePathNameWExt)== True:
			if os.stat(filePathNameWExt).st_size == 0 :
				with open(filePathNameWExt, 'w') as fp:
					json.dump(datam, fp)
			else:
				with open(filePathNameWExt, 'r') as fp:
					old_data = json.load(fp)
					data=old_data['M'].append(data)
					# print old_data
				with open(filePathNameWExt, 'w') as fp:
					json.dump(old_data, fp)

		else :
			datam = { }
			M = [ ]
			M.append(data)
			datam ['M'] = M	
			with open(filePathNameWExt, 'w') as fp:
				json.dump(datam, fp)





# Example
# data = {}
# data['key'] = 'value'

# data =	{
# 			"name":"RR",
# 			"uid" :"s31lDmLCJDWTE0NgnNKWBozujd82"
# 		}


# filename = 'Example'
# writeUser('../','ece',data)
# './' represents the current directory so the directory save-file.py is in
# 'test' is my file name
