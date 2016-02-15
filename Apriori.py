def generateFrequentOneItemSet(dataTable,minSupPercent) :
	dataSet = set()
	
	for row in dataTable :
		for rowItem in row :
			dataSet.add(rowItem)			
	
	candidateItemSetDict = dict()
	for item in dataSet :
		candidateItemSetDict[item] = 0
		for row in dataTable :
			for rowItem in row :
				if item == rowItem:					
					candidateItemSetDict[item] = candidateItemSetDict[item] + 1
	
	minSup = (minSupPercent * len(dataTable)) / 100	
	frequentItemSetDict = dict()
	for key in candidateItemSetDict :
		if candidateItemSetDict[key] >= minSup :				
			frequentItemSetDict[key] = candidateItemSetDict[key]
	generateFrequentKItemSet(frequentItemSetDict, (minSupPercent * len(dataTable)) / 100, 3, 2, dataTable)
	
def generateFrequentKItemSet(frequentItemSetDict,minSup,kValue,kCounter,dataTable) :	
	if kCounter > kValue :
		pass
	else :
		if kCounter == 2 :			
			kItemSetA = set()
			kItemSetB = set()			
			candidateKItemSet = set()			
			for item in frequentItemSetDict :
				kItemSetA.add(item)
				kItemSetB.add(item)
			for i in kItemSetA :				
				for j in kItemSetB :
					if i <> j :
						subStrA = i.split(".")
						subStrB = j.split(".")
						if subStrA[0] <> subStrB[0] :
							tempStr = str(j) +","+str(i)
							if tempStr not in candidateKItemSet :
								candidateKItemSet.add(str(i) + "," + str(j))
								
			frequentKItemSetDict = dict()
			for candidateItem in candidateKItemSet :				
				frequentKItemSetDict[candidateItem] = 0
				kItemSets = candidateItem.split(",")				
				for row in dataTable :
					flag = 0
					matchCount = 0
					for rowItem in row :
						for eachKItem in kItemSets :					
							if rowItem == eachKItem :
								matchCount = matchCount + 1
							if matchCount == len(kItemSets) :
								frequentKItemSetDict[candidateItem] = frequentKItemSetDict[candidateItem] + 1								
								flag = 1
								break
						if flag == 1 :
							break
				if frequentKItemSetDict[candidateItem] <= minSup :
					del frequentKItemSetDict[candidateItem]
			kCounter = kCounter + 1
			generateFrequentKItemSet(frequentKItemSetDict,minSup,kValue,kCounter,dataTable)
		else :			
			kItemSetA = set()
			kItemSetB = set()			
			candidateKItemSet = set()			
			for item in frequentItemSetDict :
				kItemSetA.add(item)
				kItemSetB.add(item)
			for i in kItemSetA :				
				for j in kItemSetB :
					if i <> j :
						subSetA = i.split(",")
						subSetB = j.split(",")
						tempSetC = subSetA
						resultSet = set()
						subSetA.intersection(subSetB)
						if len(tempSetC) - len(subSetA) == 1 :
							resultSet.add(subSetA)
								#
								#
								#	CONTINUE FROM HERE
								#
								#
								
						
						
			print candidateKItemSet
			kCounter = kCounter + 1
			

def generateCandidateRules(frequentItemSetDict,dataTable) :
	pass