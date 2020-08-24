command = input()
dictionaries = {}
while command != 'stop':
    value = int(input())
    #for ch in command:
    if command not in dictionaries:
        dictionaries[command] = 0

    dictionaries[command] += value

    command = input()
for key, value in dictionaries.items():
    print(f'{key} -> {value}')