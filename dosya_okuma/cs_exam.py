import csv
with open("onlinefoods.csv","r") as file:
    # count = 0
    # for line in file.readlines():
    #     count+=1
    # print(count-1)
    # ya da 
    csv_reader = csv.DictReader(file)
    sonuc = list(csv_reader)
    print(len(sonuc))
# with open("onlinefoods.csv","r") as file:
#     line_reader = csv.DictReader(file)
#     students = [line for line in line_reader if line["Occupation"]=="Student" and line["Gender"]=="Male" and line["Marital Status"]=="Married"]
#     for student in students:
#         print(student.values())
        
# with open("onlinefoods.csv","r") as file:
#     line_reader = csv.DictReader(file)
#     students = [(float(line["latitude"]),float(line["longitude"])) for line in line_reader if 20<int(line["Age"])<30]
#     for student in students:
#         print(f"enlem:{student[0]:<10}| boylam: {student[1]:>6}")