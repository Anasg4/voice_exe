import speech_recognition as sr
import os,winsound,time,sys

suara = sr.Recognizer()

def action():
    #Set your file in here
    os.startfile('C:/Users/Anas/Desktop/xxxxx.exe')
    inti()

def inti():

    with sr.Microphone() as source:

        rekam = suara.listen(source)
    try:
        text = suara.recognize_google(rekam)
        print ("Text: ",text)
        if text == "on":  #Change 'on' word to whatever u want for running your program"
            print ("Running")
            animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                         "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(len(animation)):
                time.sleep(0.2)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
            print("Completed")
            print("\n")
            # time.sleep(3)
            winsound.Beep(700, 300)
            winsound.Beep(800, 500)
            print("sukses")
            action()
        elif text == "stop": #Change 'Stop' word to whatever u want for stopping your program"
            #U can add your own code"
            print ("Cheat Stopped")
            winsound.Beep(400, 300)
            winsound.Beep(300, 300)
        else:
            print("Kata Kunci Salah") #When your voice wrong
            # inti()
    except sr.UnknownValueError:
        # print("Suara Error")
        pass
        # inti()

if __name__ == "__main__":
    print("Auto Run Program with your voice")
    print("Aktif Bilang : on \nNonaktif Bilang : Stop")
    inti()
