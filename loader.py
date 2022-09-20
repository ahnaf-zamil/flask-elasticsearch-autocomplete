from elasticsearch import Elasticsearch

import csv

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])

print(f"Connected to ElasticSearch cluster `{es.info().body['cluster_name']}`")

with open("./Car details v3.csv", "r") as f:
    reader = csv.reader(f)

    for i, line in enumerate(reader):
        document = {
            "name": line[0],
            "engine": line[9],
            "year": line[1],
            "price": line[2],
        }
        es.index(index="cars", document=document)
