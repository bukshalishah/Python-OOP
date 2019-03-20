class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name + ".")
        print("Restaurant type is " + self.cuisine_type + '.')

    def open_restaurant(self):
        print("Restaurant is open in 3PM")
    
restaurent = Restaurant('01 Restaurent', 'Coffe')
restaurent.describe_restaurant()
restaurent.open_restaurant()

restaurent_2 = Restaurant('02 Restaurent', 'BBQ')
restaurent_3 = Restaurant('03 Restaurent', 'Fast Food')
restaurent_2.describe_restaurant()
restaurent_3.describe_restaurant()

class User():
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        full_name = self.first_name.title() + " "  + self.last_name
        print("~~~User Information~~~")
        print("User is " + str(self.age) + ' Years old!')
        print("User is "  + self.gender + ".")
        print("User name: " + full_name)

    def greet_user(self):
        print("Welcome " + self.first_name + " " + self.last_name + '.')

user01 = User("Buksh", "Ali Shah", 'Male', 20)
user01.greet_user()
user01.describe_user()