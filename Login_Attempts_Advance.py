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

user01.increment_login_attempts()
user01.increment_login_attempts()
# user01.increment_login_attempts()

if user01.login_attempts >= 3:
    print("30 min wait to login!")
else:
    print("Login Successfully")