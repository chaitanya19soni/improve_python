a = input()
numbers = [int(word) for word in a.split() if word.isdigit()]

print(f"numbers :{numbers}")
print(f"numbers :{len(numbers)}")
