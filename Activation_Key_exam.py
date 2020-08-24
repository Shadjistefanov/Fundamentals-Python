text = input()

com_end = input()
while com_end != 'Generate':
    args = com_end.split('>>>')
    command = args[0]

    if command == 'Contains':
        substring = args[1]
        if substring not in text:
            print('Substring not found!')
        else:
            print(f'{text} contains {substring}')

    elif command == "Flip":
        up_or_low = args[1]
        start_idx = int(args[2])
        end_idx = int(args[3])
        if up_or_low == 'Upper':
            text = text[:start_idx] + text[start_idx:end_idx].upper() + text[end_idx:]
        else:
            text = text[:start_idx] + text[start_idx:end_idx].lower() + text[end_idx:]
        print(text)

    elif command == 'Slice':
        start_idx = int(args[1])
        end_idx = int(args[2])
        text = text.replace(text[start_idx:end_idx], '')
        print(text)


    com_end = input()
print(f'Your activation key is: {text}')