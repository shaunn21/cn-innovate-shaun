


class Person():
    def __init__(self, name, profession, age, height):
        self.name = name
        self.age = self.check_age(age)
        self.profession = profession
        self.height = height
        self.hobbies = []
    def __init__(self, person_hair):
        self.hair = person_hair
    
    def set_hobby(self, hobby):
        self.hobbies.append(hobby)

    def get_hobby(self):
        for hobby in self.hobbies:
            print(hobby)
    
    def set_hair(self, person_hair):
        self.hair = person_hair
    
    def get_hair(self):
        print(self.hair)

# person_x = Person("shaun", 31, "diving", "5'8")

# print(person)

# new_person = Person()
# print(new_person.name)




