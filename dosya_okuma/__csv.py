import csv

with open("turkish_dp.csv",encoding="utf-8")as file:
    csv_reader = csv.DictReader(file)

    for f in csv_reader:
        if f["genres"]=="Action":
            title =f['title'][:20] + '...' if len(f["title"])>20 else f["title"]
            print(f"{title:<25} |")