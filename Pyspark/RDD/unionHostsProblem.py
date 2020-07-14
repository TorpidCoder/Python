__author__ = "ResearchInMotion"

import findspark
findspark.init()
from pyspark import SparkConf
from pyspark import SparkContext

sparkconf = SparkConf().setAppName("WordCount").setMaster("local[*]")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")

def columns(lines):
    field = lines.split(",")
    country = field[3]
    name = field[1]
    return name,country

julydata = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/nasa_19950701.tsv")
augustdata = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/nasa_19950801.tsv")
julyFirstHosts = julydata.map(lambda line: line.split("\t")[0])
augustFirstHosts = augustdata.map(lambda line: line.split("\t")[0])

unionData = julyFirstHosts.union(augustFirstHosts)
cleandata = unionData.filter(lambda host : host != "host")

print(cleandata.take(5))

