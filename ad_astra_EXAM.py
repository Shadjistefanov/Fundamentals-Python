import re
pattern = r'(\||#)([A-Za-z]+ *[A-Za-z]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1'
text = input()
calories_count = 0
CALORY_FOR_DAY = 2000
matches = re.findall(pattern, text)
days = 0
for match in matches:
    if match != []:


        food = match[1]
        time = match[2]
        calories = int(match[3])
        calories_count += calories
#print(calories_count)
while calories_count >= CALORY_FOR_DAY:
    calories_count -= 2000
    days += 1
#print(matches)
print(f'You have food to last you for: {days} days!')
for match in matches:

    print(f'Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}')