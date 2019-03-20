class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name + ".")
        print("Restaurant type is " + self.cuisine_type + '.')

    def open_restaurant(self):
        print("Restaurant is open in 3PM")
    
    def set_number_served(self, increment):
        self.number_served += increment



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
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

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


restaurent = Restaurant('ABC', 'Tea')
print(restaurent.number_served)
restaurent.number_served = 10
print("Served" + str(restaurent.number_served))
restaurent.set_number_served(20)
print("Served (Updated): " + str(restaurent.number_served))


user02 = User('Buksh', 'Ali Shah', 'male', 20)
user02.increment_login_attempts()
user02.increment_login_attempts()
user02.increment_login_attempts()
print("Login Attempts: " + str(user02.login_attempts))
user02.reset_login_attempts()
print("Reset Attempts: " + str(user02.login_attempts))