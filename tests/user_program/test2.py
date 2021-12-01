df = df.rdd.map(lambda x : (x[1] - x[2],x[3] - x[0])).toDF(["max_price_fluctuation","final_price_change"])
df.show()

# find average price fluctuation
fluctuationDf = df.select(df["max_price_fluctuation"])
fluctuationDf = fluctuationDf.groupBy()
fluctuationDf = fluctuationDf.avg()
fluctuationDf.show()