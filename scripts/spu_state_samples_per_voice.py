import csv
from collections import Counter
import sys

filename = sys.argv[1]
column_name = sys.argv[2]

with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    counts = Counter(row[column_name] for row in reader)

for value, count in counts.items():
    print(f"{value}: {count}")