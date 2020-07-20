__author__ = "ResearchInMotion"

import findspark
findspark.init()

from pyspark import SparkContext , SparkConf
sparkconf = SparkConf().setMaster("local[*]").setAppName("Sorted Word Count")
sparkcont = SparkContext(conf=sparkconf)
sparkcont.setLogLevel("ERROR")

data = sparkcont.textFile("/Users/sahilnagpal/PycharmProjects/Python/Pyspark/InputData/word_count.text")
wordsplit = data.flatMap(lambda line : line.split(" "))
wordmap = wordsplit.map(lambda line : (line,1))
count = wordmap.reduceByKey(lambda a,b : a+b)
sortedcount = count.sortBy(lambda number : number[1])
for values in sortedcount.collect():
    print(values)