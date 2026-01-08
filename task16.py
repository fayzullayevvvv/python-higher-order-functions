data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

result = list(
    map(
        lambda word:word,
        filter(lambda word:isinstance(word, str) and len(word) > 5, data)
    )
)


print(result)