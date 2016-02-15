import os.path

def loadFile(filePath):	
	if os.path.isfile(filePath) :
		inputFile = open (filePath)
		fileContent = inputFile.read()
	else :
		fileContent	= 'NULL'
	return fileContent

def encodeData(fileContent):
	content = fileContent.split("\n")
	headers = content[0].split(" ")
	records = content[1:len(fileContent)]
	
	#Encode headers on numerical scale
	encodedHeaders = []
	headerCount = 1
	for index in range(len(headers)):
		if(headers[index] <> "") :
			encodedHeaders.append(headerCount)
			headerCount = headerCount + 1
	
	#Encode records on numerical scale
	values = []
	valueSet = set()
	for i in range(len(records)) :
		record = records[i]
		items = record.split(" ")		
		for j in range(len(items)) :
			item = items[j]
			if item <> "" :								
				values.append(item)
				valueSet.add(item)
				
	encodedRecords = []
	counter = 0
	for i in range(len(values)) :		
		if counter < headerCount - 1:			
			counter = counter + 1		
		else :
			counter = 1		
		temp = str(counter) + "." + getEncodedIndex(values[i],valueSet)
		encodedRecords.append(temp)
			
	encodedData = []
	i = 0
	j = 0
	while i < len(encodedRecords) :
		j = i - 1 + headerCount
		temp = encodedRecords[i:j]
		encodedData.append(temp)
		i = j
	return encodedData

def getEncodedIndex(inputString,inputSet) :
	encodedString = '0'
	i = 1
	for item in inputSet :
		if item == inputString :
			encodedString = str(i)
			break
		i = i + 1
	return encodedString

def decodeData(frequentItemSetDict,fileContent) :
	content = fileContent.split("\n")
	headers = content[0].split(" ")
	records = content[1:len(fileContent)]
	
	#Encode headers on numerical scale
	enumHeaders = []
	headerCount = 1
	for index in range(len(headers)):
		if(headers[index] <> "") :
			enumHeaders.append(headers[index])
			headerCount = headerCount + 1
	
	#Encode records on numerical scale	
	valueSet = set()	
	for i in range(len(records)) :
		record = records[i]
		items = record.split(" ")		
		for j in range(len(items)) :
			item = items[j]
			if item <> "" :												
				valueSet.add(item)
	
	enumValues = []
	valueCount = 1
	for item in valueSet :		
		enumValues.append(item)
		valueCount = valueCount + 1
		
	decodedItemSetDict = dict()
	for itemSets in frequentItemSetDict :
		itemSet = itemSets.split(".")
		i = 0
		tempStr = ""
		for i in range(len(enumHeaders)) :
			if item[0] == str(i+1) :
				tempStr = enumHeaders[i]							
		j = 0
		for j in range(len(enumValues)) :
			if item[1] == str(j+1) :
				decodedItemSetDict[tempStr+" => "+ enumValues[j]] = frequentItemSetDict[items]
	return decodedItemSetDict