# Decorators modify a function inbuilt or user defined without accessing code of that function.
# Here we are modifying division function so that it can always divide bigger number by smaller number.
def div(a, b):
    print(a / b)


def change(func):  # function takes input as a function
    def swap(a, b):  # swap function
        if a < b:
            a, b = b, a
        return func(a, b)

    return swap


div = change(div)   # links decorator to the desired function
div(8, 2)
div(2, 8)
