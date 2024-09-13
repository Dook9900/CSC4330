def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
number = 7
result = is_even_or_odd(number)
print(f"The number {number} is {result}")
