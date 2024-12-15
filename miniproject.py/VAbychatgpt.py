import pyttsx3
import speech_recognition as sr

def speak(text):
    """
    Converts text to speech.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """
    Listens to the user's voice and returns the recognized text.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def main():
    speak("Hello! I am your voice assistant. How can I help you today?")

    while True:
        user_input = listen().lower()

        if "stop" in user_input:
            speak("Goodbye!")
            break
        elif "hello" in user_input:
            speak("Hi there! How can I assist you?")
        else:
            speak("I'm not sure how to respond to that. Can you please rephrase or ask another question?")

if __name__ == "__main__":
    main()
