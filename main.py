class UserManager:
    def __init__(self):
        self.user = user

    def change_user_name(selfself, user_name):
        self.user = user_name

    def save_user(self):
        file = open("user.txt", "a")
        file.write(self.user)
        file.close()