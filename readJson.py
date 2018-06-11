import json


def readJSONFile(path, fileName):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'r') as fp:
    	data = json.load(fp)
        return data



# Example
# data = {}
# data['key'] = 'value'

# data =	{
#         	"uid" :"PZlo8r9eQwdmo1SFolxnfF9MyaZ2",
#         	"time":"7:58:00"
#         }


# filename = 'Example'
# data = readJSONFile('./',filename)