import ray
import os
import modin.pandas as pd

RAY_HEAD_HOST = os.environ.get("RAY_CLUSTER_HEAD_HOST")
RAY_HEAD_PORT = os.environ.get("RAY_CLUSTER_HEAD_PORT", 10001)

print(f"Connecting to Ray at ray://{RAY_HEAD_HOST}:{RAY_HEAD_PORT}")
ray.init(f"ray://{RAY_HEAD_HOST}:{RAY_HEAD_PORT}")

df = pd.read_csv("https://tinyurl.com/googleplaystorecsv")

print("Running group operation on google play store items by category")
print(df.groupby("Category")["App"].count())
