__author__ = "ResearchInMotion"

import findspark
findspark.init()
from pyspark import SparkConf
from pyspark import SparkContext

sparkconf = SparkConf().setAppName("WordCount").setMaster("local[*]")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")

def hostname(line):
    lines = line.split("\t")
    hostname = lines[0]
    return hostname

julydata = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/nasa_19950701.tsv")
augustdata = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/nasa_19950801.tsv")
julyFirstHosts = julydata.map(lambda line: line.split("\t")[0])
augustFirstHosts = augustdata.map(lambda line: line.split("\t")[0])

intersectionData = julyFirstHosts.intersection(augustFirstHosts)
cleandata = intersectionData.filter(lambda host : host != "host")

print(cleandata.take(5))



