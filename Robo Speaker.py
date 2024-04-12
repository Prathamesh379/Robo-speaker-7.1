import pyttsx3

if __name__ =="__main__": # main cod start form this line

    print("Robo Speaker 7.1")

    engine = pyttsx3.init() # initially this pyttsx3

    while True :                                               # added Loop 
            
            x = input("Enter what you want me to Speak: ")

            if x == '0':
                engine.say("THANK YOU FOR USING ROBO SPEAKER 7.1")
                engine.runAndWait()
                break

            else:
                engine.setProperty('rate', 145)  
                engine.say(x)
                engine.runAndWait()
