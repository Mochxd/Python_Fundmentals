temp=40
while temp >32:
    print("The water is {} degrees.".format(temp))
    temp -= 1

for i in range(1,11):
    if i == 7:
        # print("We are skipping number {}".format(i))
        continue
    print("This is number is {}.".format(i))

for i in range(1,11):
    if i == 7:
        pass
    else:
        print("The number is {}.".format(i))
