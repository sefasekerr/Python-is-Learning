import csv

with open("list_methods(Sayfa1).csv")as file:
    csv_reader = csv.reader(file,)
    print(csv_reader)
    for a in csv_reader:
        print(a[1])
    # f = file.readlines()
    # print(f)
    # for a in f:
    #     print(a)
    
    
