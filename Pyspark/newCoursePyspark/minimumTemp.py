__author__ = "ResearchInMotion"

import findspark
findspark.init()

from pyspark import SparkConf , SparkContext
sparkconf = SparkConf().setMaster("local[*]").setAppName("minimum temperature")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")

def columnData(line):
    field = line.split(",")
    location = field[0]
    temptype = field[2]
    temp = int(field[3])
    return location , temptype , temp

data = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/newCoursePyspark/inputData/1800.csv")
requiredData = data.map(columnData)
filteredTempmin = requiredData.filter(lambda line : "TMIN" in line[1])
filteredTempdata = filteredTempmin.map(lambda line : (line[0],line[2]))
minTemp = filteredTempdata.reduceByKey(lambda x , y : min(x,y))

for results in minTemp.collect():
    print(results)

filteredTempmax = requiredData.filter(lambda line : "TMAX" in line[1])
filteredTempdatamax = filteredTempmax.map(lambda line : (line[0],line[2]))
maxTemp = filteredTempdatamax.reduceByKey(lambda x , y : max(x,y))

for resultsmax in maxTemp.collect():
    print(resultsmax)


