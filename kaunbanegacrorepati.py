import pyttsx3
def kbc():
    def speak(audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        #print(voices[1].id)
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    speak("Welcome to kbc")
    name = input("Your name:-")
    location = input("Where you from:-")
    speak("here with us")
    speak(name)
    speak("from")
    speak(location)
    speak("India")
    speak("Let's begin today's game")
    question = ["Current Railway Minister of India is","Which god is also known as ‘Gauri Nandan’?","What does not grow on tree according to a popular Hindi saying?","Which city is known as Pink City in India?","Who wrote India's National Anthem?","How many major religions are there in India?","When is the National Hindi Diwas celebrated?","How many states are there in India?","Where in India Gate located?","Who wrote Vande Mataram?","Which one of the following places is famous for the Great Vishnu Temple?","The largest Buddhist Monastery in India is located at"]
    option = ["A Mamta Banarjee  B Ram Vilash  C Ashwini Vaishnaw D Piyush Goyal","A Agni B Indra C Hanuman D Ganesha","A Money B Flowers C Leaves D Fruits","A Banglore B Maysore C Jaipur D Kochi","A Rabindranath Tagore B Lal Bahadur Shastri C Chetan Bhagat D RK Narayan","A 6 B 7 C 8 D 9","A 13 September B 14 September C 14 July D 15 August","A 28 B 29 C 31 D 31","A Agra B Punjab C Mumbai D New Delhi","A Sarat Chandra Chattopadhyay B Rabindranath Tagore C Bankim Chandra Chatterjee D Ishwar Chandra Vidyasagar","A Bordubar Indonesia B Bamiyan Afghanistan C Panja Sahib Pakistan D Ankorvat Cambodia","A Sarnath Uttar Pradesh B Tawang Arunachal Pradesh C Dharmashala Himachal Pradesh D Gangtok Sikkim"]
    speak("Your first question is on your screen")

    print(question[0])
    print(option[0])

    speak(question[0])
    speak(option[0])

    correct_answer = ["C","D","A","C","A","A","B","A","D","C","D","B","quit"]

    your_anwser = input("Enter your Answer:-")
    if your_anwser == correct_answer[0]:
        speak("congratulation that's a right answer you won 10000 ruppes")
        print("Total cash = 10000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming")
        exit()
    else:
        speak("We are really sorry but that's a wrong you were not able to win anything today")
        exit()

    speak("Your second question is on your screen")
    print(question[1])
    print(option[1])
    speak(question[1])
    speak(option[1])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[1]:
        speak("congratulation that's a right answer you won 20000 ruppes")
        print("Total cash = 20000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 10000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 10000 ruppess today")
        exit()

    speak("Your third question is on your screen")
    print(question[2])
    print(option[2])
    speak(question[2])
    speak(option[2])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[2]:
        speak("congratulation that's a right answer you won 40000 ruppes")
        print("Total cash = 40000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 20000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 20000 ruppess today")
        exit()

    speak("Your fourth question is on your screen")
    print(question[3])
    print(option[3])
    speak(question[3])
    speak(option[3])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[3]:
        speak("congratulation that's a right answer you won 80000 ruppes")
        print("Total cash = 80000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 40000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 40000 ruppess today")
        exit()
    speak("Your fifth question is on your screen")
    print(question[4])
    print(option[4])
    speak(question[4])
    speak(option[4])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[4]:
        speak("congratulation that's a right answer you won 160000 ruppes")
        print("Total cash = 160000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 80000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 80000 ruppess today")
        exit()

    speak("Your sixth question is on your screen")
    print(question[5])
    print(option[5])
    speak(question[5])
    speak(option[5])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[5]:
        speak("congratulation that's a right answer you won 320000 ruppes")
        print("Total cash = 320000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 160000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 160000 ruppess today")
        exit()

    speak("Your seventh question is on your screen")
    print(question[6])
    print(option[6])
    speak(question[6])
    speak(option[6])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[6]:
        speak("congratulation that's a right answer you won 640000 ruppes")
        print("Total cash = 640000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 320000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 320000 ruppess today")
        exit()

    speak("Your eighth question is on your screen")
    print(question[7])
    print(option[7])
    speak(question[7])
    speak(option[7])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[7]:
        speak("congratulation that's a right answer you won 1280000 ruppes")
        print("Total cash = 1280000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 640000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 640000 ruppess today")
        exit()

    speak("Your ninth question is on your screen")
    print(question[8])
    print(option[8])
    speak(question[8])
    speak(option[8])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[8]:
        speak("congratulation that's a right answer you won 2560000 ruppes")
        print("Total cash = 2560000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 1280000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 1280000 ruppess today")
        exit()

    speak("Your tenth question is on your screen")
    print(question[9])
    print(option[9])
    speak(question[9])
    speak(option[9])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[9]:
        speak("congratulation that's a right answer you won 5120000 ruppes")
        print("Total cash = 5120000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 2560000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 2560000 ruppess today")
        exit()

    speak("Your elevnth question is on your screen")
    print(question[10])
    print(option[10])
    speak(question[10])
    speak(option[10])
    your_anwser =input("Enter your Answer:-")
    if your_anwser == correct_answer[10]:
        speak("one crore you have won 10240000")
        print("Total cash = 10240000")
    elif your_anwser == correct_answer[12]:
        speak("thank you for coming you won 5120000")
        exit()
    else:
        speak("ohh no that was awrong answer but you have won 5120000 ruppess today")
        exit()

    speak("Do you wanna continue the game")
    choice = ["yes","no"]
    your_choice = input("your choice yes or no:-")
    if your_choice == choice[0]:
        speak("Your twelth question is")
        print(question[11])
        print(option[11])
        speak(question[11])
        speak(option[11])
        your_anwser =input("Enter your Answer:-")
        if your_anwser == correct_answer[11]:
            speak("two crore you have won 20560000")
            print("Total cash = 20560000")
            speak("you have won the game all your answer was you won it all you are champion")
        elif your_anwser == correct_answer[12]:
            speak("thank you for coming you won 10240000")
            exit()
        else:
            speak("ohh no that was a wrong answer but you have won 10240000 ruppess today you are a crorepati now")
            exit()
    else:
        speak("its was a nice game you became a crorepati today")
        exit() 

if __name__ == '__main__':
    kbc()