# This is the version 1.0 of TUlKU: My first personal voice assistant
# Note: Please keep in mind that this is a beginner-level Python project and If you found this helpful and have extra ideas and want to contribute then you are free to do so
''' In this project, I have used the: 
os.system("powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('hello')")
to make my assistant be able to speak and 

If you are using Devian/macOS You can use say:
os.system("say 'hello'")  

For Linux OS:
os.system("espeak 'hello'")

'''
# importing os and time modules
import os,time

if __name__ == '__main__':
    print("Starting TULKU 1.0.....")
    robo = "TULKU 1.0"
    time.sleep(2)
    print("\n----------- Welcome to TULKU 1.0 ----------\n")
    os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('welcome to {robo} your friendly personal assistant')")
    os.system("powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Please enter your name')")
    name = input("Your Name: ")
    
    while True:
        print(f"TULKU 1.0: Hello, {name} please\n           press:\n           c: have conversation with me &\n           d: read what you have entered\n           quit: quit {robo}")
        os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Hello {name} please press c to have conversation with me and press d to read waht you have written and write quit to quit {robo}')")
    
        a = input(f"{name}: ")
    
        # Conversation with TULKU
        if a == 'c':
            print(f"{robo}: {name}, lets have a chat !!")
            os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{name} lets have a chat')")
            print(f"{robo} : Hi, {name}.How are you ?")
            os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Hi {name} how are you')")
            
            while True:
                say = input(f"{name} : ")
                if say == "quit":
                    print("\nDirecting to main tab.......")
                    time.sleep(2)
                    os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{name} you will be directed to main tab ')")
                    print(f"Bye bye{name}")
                    break
                else :
                    print(f"{robo} : Glad to hear that, {name}")
                    os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Glad to hear that {name}')")
                
            
    
        # Read what you entered
        elif a == 'd':
            print(f"\n{robo}: {name}, You have selected to read out loud\n")
            os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{name} You have selected me to read out loud')")
            while True:
                say = input(f"{name} : ")
                os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{say}')")
                print(f"{robo} : {say}")
                if say == "quit":
                    print("\nDirecting to main tab.......")
                    time.sleep(2)
                    print(f"{name}. You will be redirected to main tab.")
                    os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{name} you will be directed to main tab ')")
                    break
            
        elif a == "quit":
            print("\nQuiting TULKU 1.0 .......")
            time.sleep(2)
            print(f"Bye bye {name}. Visit me again")
            os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye bye {name} visit me again')")
            exit()
    
        else :
            print(f"{robo}: {name} you have entered wrong choice")
            os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{name} you have entered wrong choice')")
        