with open("test.txt", "r", encoding="utf-8") as file:
    for line in file:
        # .strip() removes trailing newlines (\n) and extra whitespace
        print(line.strip())
