class Patient():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    #Method 1
    def say_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return(full_name)
    #Method 2
    def change_last_name(self, update_lastname):
        self.last_name = update_lastname
    #Method 3
    def change_first_name(self, update_first_name):
        self.first_name = update_first_name
    #Method 4
    def change_age(self, update_age):
        self.age = update_age

#  Create instance         
pid01 = Patient("Buksh", "Ali", 20)
print(pid01.age)
print(pid01.say_full_name())
pid01.change_last_name("Ali Shah")
print(pid01.say_full_name())