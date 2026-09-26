# Voice Controlled Robot using Python

# Install required libraries:

# pip install SpeechRecognition PyAudio

import speech_recognition as sr

recognizer = sr.Recognizer()

def move_robot(command):
command = command.lower()

```
if "forward" in command:
    print("🤖 Robot moving FORWARD")

elif "backward" in command:
    print("🤖 Robot moving BACKWARD")

elif "left" in command:
    print("🤖 Robot turning LEFT")

elif "right" in command:
    print("🤖 Robot turning RIGHT")

elif "stop" in command:
    print("🛑 Robot STOPPED")

else:
    print("Command not recognized.")
```

def listen_command():
with sr.Microphone() as source:
print("\nListening...")
recognizer.adjust_for_ambient_noise(source, duration=1)

```
    try:
        audio = recognizer.listen(source, timeout=5)
        command = recognizer.recognize_google(audio)

        print("You said:", command)
        move_robot(command)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the command.")

    except sr.RequestError:
        print("Speech recognition service is unavailable.")

    except sr.WaitTimeoutError:
        print("No voice command detected.")
```

while True:
print("\n===== VOICE CONTROLLED ROBOT =====")
print("Say: Forward | Backward | Left | Right | Stop")
print("Say 'Exit' to close the program.")

```
with sr.Microphone() as source:
    print("\nListening...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    try:
        audio = recognizer.listen(source, timeout=5)
        command = recognizer.recognize_google(audio)

        print("You said:", command)

        if command.lower() == "exit":
            print("Voice Controlled Robot Closed.")
            break

        move_robot(command)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the command.")

    except sr.RequestError:
        print("Speech recognition service is unavailable.")

    except sr.WaitTimeoutError:
        print("No command detected.")
```
