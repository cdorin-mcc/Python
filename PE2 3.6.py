class Exception:
    pass
class NotNumericError(Exception):
    def __init__(self, message="Input is not a numeric value."):
        self.message = message
        super().__init__(self.message)

#Script for prompting user.
try:
    user_input = input("Please enter a number: ")
    if not user_input.isnumeric():
        raise NotNumericError()
except NotNumericError as e:
    print(e)
else:
    print("The input is valid.")
finally:
    print("End of program execution.")

