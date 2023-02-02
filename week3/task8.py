class Person:

    count_of_object = 0

    def __init__(
            self,
            first_name,
            last_name,
            age,
            occupation,
            gender,
            nationality
    ):
        Person.count_of_object += 1

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.gender = gender
        self.nationality = nationality

    def year_born(self, cur_year):
        return cur_year - self.age

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_nationality(self):
        return self.nationality

    def get_age(self):
        return self.age

    def get_occupation(self):
        return self.occupation

actor1 = Person(
    first_name="Brad",
    last_name="Pitt",
    age=50,
    occupation="Actor",
    gender="Man",
    nationality="American"
)

# print(Person.count_of_object)

print(actor1.year_born(2023))
print(actor1.get_name())
print(actor1.get_nationality())
print(actor1.get_age())
print(actor1.get_occupation())

