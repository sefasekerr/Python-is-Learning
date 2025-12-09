from collections import Counter

with open("log.txt","r",encoding="utf-8") as f:
    saat = []
    for lines in f:
        if "attribute" in lines:
            continue
        elif "---saat" in lines:
            hour = lines.split("---")
            saat.append(hour[0].strip())

print(saat)           
counter = Counter(saat)
print(counter)
if counter:
    liste = counter.most_common(1)[0]
    print(f"en çok geçen saat {liste[0]} {liste[1]} kez geçyor.")