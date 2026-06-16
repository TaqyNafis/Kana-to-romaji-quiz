import Kana_dictionary as kd
import hiragana as hira
import katakana as kata

def main():
    while True:
        mode = input("1.  Hiragana quiz\n2.  Katakana Quiz\n3.  Hiragana to romaji\n4.  Katakana to romaji\n0.  To quit\nInput number for which mode:\n")

        if mode =="0":
            break
        elif mode == "1":
            hira.kana_quiz()
        elif mode == "2":
            kata.kana_quiz()
        elif mode == "3":
            hira.to_romaji_quiz()
        elif mode == "4":
            kata.to_romaji_quiz()
        else:
            print("invalid input\n")

if __name__ == "__main__":
    main()