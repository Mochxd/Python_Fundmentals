greeting = input("Good morning\n")

if greeting.lower() == "morning":
    print("Condition matches")
else:
    print("condition is not matched")

greeting2 = input("What is the type of women?\n")
if greeting2 == "evils":
    print("yes u are right.thank u")
else:
    print("no, they are evils. thank u")

obj = [1,2,3,4,5]
for i in obj:
    print(i*2)

summation=0
for o in range(0, 6):
    summation += o
    print(summation)

print("#################################")
"""
in case if u have only upper, lower bounds and step
it will start with lower and end with index -1
"""
for k in range(10,16,2):
    print(k)
print("#################################")
"""
in case if u have only upper bound it will start with 0
and end with index -1
"""
for z in range(5):
    print(z)

soso=5
while soso<10:
    print(soso)
    soso+=1

toto=10
while toto>1:
    if toto == 9:
        toto = toto-1
        continue
    if toto == 3:
        break
    print(toto)
    toto = toto - 1
