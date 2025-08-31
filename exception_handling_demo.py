
class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age must be >= 18.")
try:
    age = 16
    if age < 18:
        raise InvalidAgeError(age)
except InvalidAgeError as ex:
    print(ex)

    """
    Write a custom exception handler that raises InsufficentFundError for bank.
    """


