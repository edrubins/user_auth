class Friend():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return self.first_name + " " + self.last_name

if __name__ == "__main__":

    frankie = Friend('Frankie', "Jones", "fjones@mymail.com")

    print(frankie)