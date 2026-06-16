import random
import Kana_dictionary as kd
text =""
max_number = 1001

# "temperature" controls the chance for the loop to stop.
# Each loop, temperature increases, so the longer the text gets,
# the higher the chance that the random number will be below temperature.
temperature = 2
temperature_increase = 1

number = max_number
while number > temperature:
    text += random.choice(kd.hiragana_all)
    
    # Increase stop chance after every added kana
    temperature += temperature_increase

    number = random.randrange(0,max_number)

print(temperature, number)
print(text)
