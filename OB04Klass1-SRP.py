class User():
    def __init__(self, user):
        self.user = user

class UserNameChanger():
    def __init__(self, user):
        self.user = user
    def change_name(self, new_name):
        self.user = new_name

class SaveUser():
    def __init__(self, user):
        self.user = user
    def save(self):
        file = open("user.txt", "a")
        file.write(self.user)
        file.close()