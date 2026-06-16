import Kana_dictionary as kd
import  generate_kana_text as generate
import random
from termcolor import colored

def kana_quiz():
    while True:
        text = random.choice(kd.hiragana_all)

        print (colored(text, "yellow"))
        input_text = input("Enter the romaji (q to exit): ")
        
        if input_text.lower() == "q":
            break

        if len(text) == 1:
            answer = kd.hiragana[text]
        elif len(text) == 2:
            romaji_comb = kd.hiragana_youon_base[text[0]] + kd.hiragana_youon_small[text[1]]
            answer = romaji_comb 
        
        if input_text == answer:
            print(colored("Correct","green"))
        else:
            print(colored("Wrong!! answer is","red"), colored(answer,"red",attrs=["bold"]))

def hiragana_to_romaji(text):
    romajinized_text = ""
    i = 0

    while i < len(text):
        x = text[i]

        if x in kd.hiragana_youon_base and i + 1 < len(text):
            if text[i+1] in kd.hiragana_youon_small:
                romajinized_text += kd.hiragana_youon_base[x] + kd.hiragana_youon_small[text[i+1]]
                i += 2
                continue

        if x in kd.hiragana:
            romajinized_text += kd.hiragana[x]
        else:
            romajinized_text +=  x
        
        i += 1

    return romajinized_text

def to_romaji_quiz ():
    while True:
        text = generate.generate_kana_text(kd.hiragana_all)
        romajinized_text = hiragana_to_romaji (text)

        print(colored(text,"yellow")) 
        input_text = input ("write romaji of the text above (q to exit): \n")

        if input_text.lower() == "q":
            break

        if romajinized_text == input_text:
            print(colored("Correct","green"))
        else:
            # If both length of input and text are the same
            highlights_mistake = ""
            Answer_with_highlight = ""
            i = 0
            if len(romajinized_text) == len(input_text):
                while i < len(romajinized_text):
                    x = romajinized_text[i]
                    y = input_text[i]

                    if x == y:
                        highlights_mistake += y
                        Answer_with_highlight += x
                    else:
                        highlights_mistake += colored(y, "red",attrs=["reverse"])
                        Answer_with_highlight += colored(x, "green",attrs=["reverse"])
                        
                    i+=1
            #If input length is less than answer
            elif len (romajinized_text) > len(input_text):
                while i < len(input_text):
                    x = romajinized_text[i]
                    y = input_text[i]

                    if x == y:
                        highlights_mistake += y
                        Answer_with_highlight += x
                        
                    else:
                        highlights_mistake += colored(y, "red",attrs=["reverse"])
                        Answer_with_highlight += colored(x, "green",attrs=["reverse"])
                    i+=1
                for x in romajinized_text[i:]:
                    highlights_mistake += colored(" ", "red",attrs=["reverse"])
                    Answer_with_highlight += colored(x, "green",attrs=["reverse"])

            #If input length is more than answer
            elif len (romajinized_text) < len(input_text):
                while i < len(romajinized_text):
                    x = romajinized_text[i]
                    y = input_text[i]

                    if x == y:
                        highlights_mistake += y
                        Answer_with_highlight += x
                        
                    else:
                        highlights_mistake += colored(y, "red",attrs=["reverse"])
                        Answer_with_highlight += colored(x, "green",attrs=["reverse"])
                    i+=1
                for x in input_text[i:len(input_text)-1]:
                    highlights_mistake += colored(x, "red",attrs=["reverse", "strike"])
                    Answer_with_highlight += colored(" ", "green",attrs=["reverse"])

            print(f"\nMistakes highlighted:\n{highlights_mistake}\n\nAnswer:\n{Answer_with_highlight}\n")

    


if __name__ == "__main__":
    kana_quiz()
    #to_romaji_quiz()

