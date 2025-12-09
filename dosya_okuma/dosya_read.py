# f = open("log.txt",encoding="utf-8",)
# print(f.read(10))
# print(f"""
# {f.tell()}
# {f.seek(10)}

# {f.readlines()}
# """)# {f.seek()}
with open("log.txt") as f:
    print(f.read())