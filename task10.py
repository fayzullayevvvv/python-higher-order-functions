text = ["apple", "34", "banana", "100", "abc", "75"]

numbers = list(filter(lambda i:i.isdigit() == True, text))

print(numbers)