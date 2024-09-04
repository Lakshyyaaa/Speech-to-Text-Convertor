import speech_recognition as sr
import googletrans

r = sr.Recognizer()

def speech_to_text():
    # Use the microphone as source for input
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Please speak now.")

        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='en')  # Any language can be used by changing the language = 'en' with the code of language                              
            print("You said: " + text)  # A file for other language codes has been provided in the repository

            with open("recognized_text.txt", "w") as file:
                file.write(text)
            print("Text has been saved to 'recognized_text.txt'.")

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

        except sr.UnknownValueError:
            print("Could not understand the audio")


speech_to_text()
