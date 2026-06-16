import random
import Kana_dictionary as kd

#note to self
# "temperature" controls the chance for the loop to stop. 
# Each loop, temperature increases, so the longer the text gets, the higher the chance that the random number will be below temperature.
def generate_kana_text(dictionary, max_number = 1001, start_temperature = 1 , temperature_increase = 10):
    text =""
    number = max_number
    temperature = start_temperature
    while number > temperature:
        text += random.choice(list(dictionary))
        
        # Increase stop chance after every added kana
        temperature += temperature_increase

        number = random.randrange(0,max_number)

    return text

if __name__ == "__main__":
    text=generate_kana_text(kd.hiragana)
    print(text)