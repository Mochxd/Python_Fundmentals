import random

class Person:
    def __init__(self, firstname, lastname, health, status):
        self.firstName = firstname
        self.lastName = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hello, My name is {} {}".format(self.firstName, self.lastName))

    def emote(self):
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print("{} is happy".format(self.firstName))
        elif emotion == 2:
            print("{} is sad".format(self.firstName))

    def health_status(self):
        if self.health == 100:
            print("{} is too old".format(self.firstName))
        elif self.health >= 75:
            print("{} is old".format(self.firstName))
        elif self.health >= 51:
            print("{} is good".format(self.firstName))
        elif self.health >= 40:
            print("{} is very good".format(self.firstName))
        else:
            print("{} is so cool".format(self.firstName))

# Creating instances
maria = Person("Maria", "Mostafa", 66, True)
soso = Person("Soso", "Hamed", health=31, status=True)

# Checking status correctly
print("{} is my friend? {}".format(maria.firstName, "Yes" if maria.status else "No"))
print("{} is my friend? Yes, and she is {} so it is {}".format(soso.firstName, soso.health, soso.status))

maria.introduce()

class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname,lastname,health,status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, You are tired and weak" .format(self.firstName))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!" .format(other.firstName))
        if other.status == True:
            other.status = False

Alex = Enemy("rock","Alex", "Wayne", 75, status= False)
Alex.hurt(maria) 

