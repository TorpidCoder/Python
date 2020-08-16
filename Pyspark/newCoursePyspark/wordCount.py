__author__ = "ResearchInMotion"

import findspark
findspark.init()

from pyspark import SparkConf , SparkContext
sparkconf = SparkConf().setMaster("local[*]").setAppName("Word Count")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("Error")

data = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/word_count.text")
wordsmap = data.flatMap(lambda word : word.split(" ")).map(lambda word : (word,1)).reduceByKey(lambda a,b : (a+b)).sortBy(lambda vals : vals[1])

for values in wordsmap.collect():
    print(values)