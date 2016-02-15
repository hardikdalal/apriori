from ReadDB import loadFile
from ReadDB import encodeData
from Apriori import generateFrequentOneItemSet
from ReadDB import decodeData
import sys

#path = raw_input("Enter file path: ")
#fileName = raw_input("Enter file name: ")
#fileContent = loadFile(path+fileName)
fileContent = loadFile("data1")
if fileContent == 'NULL' :
	print 'ERROR: File do not exist'
	sys.exit(1)
#minSup = raw_input("Enter minimum support count (in percentage): ")
minSupPercent = 30

if minSupPercent < 0 | minSupPercent > 100 :
	print "ERROR: Percent must be greater than 0 and less than 100"
	sys.exit(1)

encodedData = encodeData(fileContent)

frequentEncodedData = generateFrequentOneItemSet(encodedData,minSupPercent)

#print frequentEncodedData
#decodedFrequentItemSet = decodeData(frequentEncodedData,fileContent)

#print "Frequent Itemset => Support Count / Support Percent"

#for item in decodedFrequentItemSet :
#	print item + " {" + str(decodedFrequentItemSet[item]) + "} "