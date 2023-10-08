from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

def get_prod_cats(spark, prod_df, cat_df):

  exploded_cats_df = cat_df.select("pid", explode("cats").alias("cat"))   

  result_df = prod_df.join(exploded_cats_df,  
                           prod_df["pid"] == exploded_cats_df["pid"],
                           "left_outer")

  result_df = result_df.select(prod_df["pname"], exploded_cats_df["cat"])

  return result_df


if __name__ == "__main__":

  spark = SparkSession.builder.appName("test").getOrCreate()   

  prod_df = spark.read.json("products.json")
  cat_df = spark.read.json("categories.json")

  result_df = get_prod_cats(spark, prod_df, cat_df)

  result_df.write.json("results.json")

  spark.stop()
