class Person:
    def __init__(
            self,
            name: str,
            fives: int,
            tens: int,
            twenties: int
    ):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def sum_of_money(self):
        return (
                self.fives * 5
                + self.tens * 10
                + self.twenties * 20
        )

def most_money(persons):
    max = 0
    most_rich_person = None

    for person in persons:
        if person.sum_of_money() > max:
            max = person.sum_of_money()
            most_rich_person = person

    return most_rich_person.name

john = Person("John", 2, 2, 0)
alice = Person("Alice", 1, 3, 0)
mike = Person("Mike", 0, 0, 2)

print(most_money([john, alice, mike]))
