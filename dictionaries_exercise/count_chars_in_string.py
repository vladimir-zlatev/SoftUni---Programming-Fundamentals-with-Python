words = input()

chars = {}

for el in words:
    if el != ' ':
        if el in chars:
            chars[el] += 1
        else:
            chars[el] = 1

for key, value in chars.items():
    print(f"{key} -> {value}")