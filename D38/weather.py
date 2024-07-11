import win32com.client as wc
import requests,json,time

if __name__ == '__main__':
    speak = wc.Dispatch("SAPI.SpVoice")
    print("Starting my app.....")
    time.sleep(2)
    robo = "TULKU 1.1"
    print("\n----------- Weather App using python ----------\n")
    speak.Speak("Welcome to simple weather app using python")
    speak.Speak("Please Enter your city name")
    city = input("Your city: ")
    
    url = f"https://api.weatherapi.com/v1/current.json?key=8b4872d58b024d1e9f1170105240906&q={city}"
    
    req = requests.get(url)
    #print(req.text) # this is in str type
    
    #now lets change req.text to dictionary and display the local time
    intoDict = json.loads(req.text)
    ltime = intoDict["location"] ["localtime"]
    temp = intoDict["current"] ["temp_c"]
    print("Local time: ",ltime,"\nTemp: ",temp,"deg/celsius")
    speak.Speak(f"Local time on {city} is {ltime} and the temperature is {temp} degree celsius")
    print("Bye bye...")
    speak.Speak("Thank you for using this app ")
    speak.Speak("Bye bye see you next time")