# file = open('test.txt')
# print(file.read())
# file.close()

# lines = file.readlines()
# for line in lines:
#     print(line)
# while line!="":
#     print(line)
#     line=file.readline()

# file.close()

with open("test.txt","r") as file:
    content = file.readlines()
    reversed(content)
    with open("test.txt","w") as writer:
        for line in reversed(content):
            writer.write(line)
