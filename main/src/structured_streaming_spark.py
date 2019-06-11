from pyspark.sql import SparkSession
import os


def main():
    os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.11:2.4.3,' \
                                        'org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3,' \
                                        'org.apache.kafka:kafka-clients:2.0.0' \
                                        ' pyspark-shell'
    spark = SparkSession.builder.appName('structured_streaming').getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel('ERROR')
    port = 'localhost:9092'

    df = read_stream(spark, 'test-topic', port)
    print(type(df))
    df.printSchema()

    df_sql = df.selectExpr('CAST(value AS STRING)')
    console_output = write_stream(df_sql)
    print(type(console_output))
    console_output.awaitTermination()


def read_stream(spark, topic, port):
    return spark.readStream.format('kafka') \
        .option('kafka.bootstrap.servers', port) \
        .option('subscribe', topic) \
        .option('startingOffsets', 'earliest') \
        .load()


def write_stream(df_sql):
    return df_sql \
        .writeStream \
        .queryName('console') \
        .outputMode('append') \
        .format('console') \
        .option('truncate', False)\
        .start()
    # .format('json') \
    # .option("path", "resources/output/") \
    # .option("checkpointLocation", "resources/chkpoint_dir")\


if __name__ == '__main__':
    main()
