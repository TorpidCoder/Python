__author__ = "ResearchInMotion"
import findspark
findspark.init()
from pyspark import SparkConf
from pyspark import SparkContext

sparkconf = SparkConf().setAppName("WordCount").setMaster("local[*]")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")

data = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/WordCount.txt")
data = data.flatMap(lambda words :words.split(" "))
wordcount = data.map(lambda word : (word,1)).reduceByKey(lambda a,b : a+b).sortBy(lambda word : word[1])
for words , values in wordcount.collect():
    print("{} {}".format(words,values))
