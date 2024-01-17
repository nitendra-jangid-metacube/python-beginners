class InvalidPasswordException(Exception):
    def __init__(self, message):
        self.message = message
    def get_message(self):
        return self.message

def check_password_length(password):
    if len(password) < 8:
        raise InvalidPasswordException("Password should be at least 8 characters long")

try:
    password = input("Enter a password: ")
    check_password_length(password)
    print("Valid password")
except InvalidPasswordException as e:
    print(e.get_message())