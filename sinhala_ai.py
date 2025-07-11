import pyttsx3

def sinhala_speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    sinhala_speak("ආයුබෝවන්! මම සිංහල AI බොට් එක.")
