# import pyttsx3
# # Initialize the TTS engine
# engine = pyttsx3.init()
# # Convert text to speech
# engine.say("I am Saina")
# # Wait for the speech to finish
# engine.runAndWait()
import pyttsx3
engine = pyttsx3.init()
# Get and set the speaking rate
rate = engine.getProperty('rate')
print(f"Current speaking rate: {rate}")
engine.setProperty('rate', 5)
# Get and set the volume level
volume = engine.getProperty('volume')
print(f"Current volume level: {volume}")
engine.setProperty('volume', 20.0)
# Get and set the voice (0 for male, 1 for female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello World!")
engine.say(f"My current speaking rate is {rate}")
engine.runAndWait()