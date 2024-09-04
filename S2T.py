import speech_recognition as sr
import googletrans

r = sr.Recognizer()

def speech_to_text():
    # Use the microphone as source for input
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        # Adjust the recognizer sensitivity to ambient noise
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Please speak now.")

        # Listen for the user's input
        audio = r.listen(source)

        try:
            # Use Google Web Speech API to recognize the speech
            text = r.recognize_google(audio, language='en')  # For Spanish, use 'es'
            print("You said: " + text)

            # Save the recognized text to a file
            with open("recognized_text.txt", "w") as file:
                file.write(text)
            print("Text has been saved to 'recognized_text.txt'.")

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

        except sr.UnknownValueError:
            print("Could not understand the audio")


# Call the function
speech_to_text()
