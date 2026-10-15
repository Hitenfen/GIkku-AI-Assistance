import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

def speak(text):
    print("GIKKU:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nGIKKU is listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source, duration=0.6)

        try:
            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=8
            )
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return ""

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower().strip()

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return ""

    except sr.RequestError:
        speak("Speech recognition is unavailable. Check your internet connection.")
        return ""


def handle_command(command):
    if not command:
        return True

    if "hello" in command or "hi gikku" in command:
        speak("Hello! I am Gikku. How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    elif "help" in command:
        speak(
            "You can ask me for the time or date, open Google, "
            "YouTube, or GitHub, or say exit to stop me."
        )

    elif any(word in command for word in [
        "exit", "quit", "stop gikku", "goodbye"
    ]):
        speak("Goodbye! Gikku is shutting down.")
        return False

    else:
        speak("I don't know that command yet. Say help to hear my commands.")

    return True


def main():
    speak("Hello! I am Gikku, your personal voice assistant.")
    speak("Say help to learn my commands.")

    running = True
    while running:
        command = listen()
        running = handle_command(command)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Goodbye!")

# print("Hello! I am Gikku your voice assistant. How can I help you today?")
# while True:
#     command = input("Enter your command::").lower()
#     if command == "hello":
#         print("Hello! How can I assist you?")
#     elif command == "what is the time":
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print("The current time is:", current_time)
#     elif command == "open google":
#         webbrowser.open("https://www.google.com")
#         print("Opening Google...")
#     elif command == "open youtube":
#         webbrowser.open("https://www.youtube.com")
#         print("Opening YouTube...")
    
#     elif command == "help":
#         print("Available commands:")
#         print("- hello: Greet the assistant")
#         print("- what is the time: Get the current time")
#         print("- open google: Open Google in your web browser")
#         print("- open youtube: Open YouTube in your web browser")
#         print("- help: Show available commands")
#         print("- exit: Exit the assistant")
#     elif command == "exit":
#         print("Goodbye whenever you will feel bored do lemme know! Your  Gikku is always here to help you. Have a great day!")
#         break
#     else:
#         print("Sorry, I didn't understand that command. Type 'help' to see available commands.")