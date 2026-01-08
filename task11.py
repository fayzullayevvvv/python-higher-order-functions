nums = list(range(1, 21))

even_square = list(
    map(lambda num:num ** 2, filter(lambda num:num % 2 == 0, nums))
)

print(even_square)