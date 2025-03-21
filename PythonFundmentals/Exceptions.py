try:
    with open("soso.txt","r") as file:
        file.read()
except Exception as s:
    print(s)