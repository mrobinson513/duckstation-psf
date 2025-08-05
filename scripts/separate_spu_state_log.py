import csv, sys, os

LOGFILE = f"{os.getenv('HOME')}/Music/psf_dumps/109 Arise Within You 2025-07-30-20-11-59.csv"

with open(LOGFILE, 'r', newline='') as f:
    data = csv.DictReader(f)
    fieldnames = data.fieldnames

    # Pre-create 24 output files with headers
    for n in range(24):
        voice_file = f"{LOGFILE}.{str(n).zfill(2)}"
        with open(voice_file, "w", newline='') as v:
            writer = csv.DictWriter(v, fieldnames=fieldnames)
            writer.writeheader()

    # Append each row to its corresponding file
    for row in data:
        voice = int(row['Voice'])
        voice_file = f"{LOGFILE}.{str(voice).zfill(2)}"
        with open(voice_file, "a", newline='') as v:
            writer = csv.DictWriter(v, fieldnames=fieldnames)
            writer.writerow(row)