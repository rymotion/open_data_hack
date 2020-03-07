import json


class BackendParser:
    fileDirectory = ''
    def __init__(self, fileLocation):
        self.fileDirectory = fileLocation

    def readJSON(self):
        with open(self.fileDirectory, 'r') as jsonFile:
            reader = json.load(jsonFile)
            #TODO (rpaglinawan): Add data delimeter for json key
            #TODO (rpaglinawan): Add data delimeter for json value
            return reader

    def encodeJSON(self, dataToWrite):
        with open(self.fileDirectory, 'w') as jsonFile:
            json.dump(dataToWrite, jsonFile, sort_keys=True)
            pass