class Hero():
    def __init__(self, level, job) -> None:
        self.level = level
        self.job = job
        self.items = []
        self.magic = []
    def set_item(self, inv):
        self.items.append(inv)
    def get_item(self):
        print(self.items)
    def set_magic(self, spell):
        self.magic.append(spell)
    def get_magic(self):
        print(self.magic)


#encapsulation - fundamental attributes cannot be changed or modified by other objects
#abstaction - doesn't need to know why it works, just that it does work
#inheritence - inherit attributes from one object to another, saving time not needing to custom code every object
#polymorphism - extension of inheritence, but enables each child object to implement the Start method