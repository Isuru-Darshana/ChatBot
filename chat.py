import os
from dotenv import load_dotenv
import google.generativeai as genai
import pyttsx3 as tx
import speech_recognition as sr

load_dotenv()


def bot():
    bot = tx.init()
    bot.setProperty('rate', 150)
    bot.say("Hello I'm Rashmin. What can I do for you")
    bot.runAndWait()


def speech():
    try:
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source2:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio = r.listen(source2)
                txt = r.recognize_google(audio)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Voice is not clear try again...")
        r = sr.Recognizer()


def chat():
    genai.configure(api_key=os.getenv("API_KEY"))
    config = {"temperature": 0.9, "top_p": 1,
              "top_k": 1, "max_output_tokens": 500}

    model = genai.GenerativeModel("gemini-pro", generation_config=config)

    test = input("text: ")
    response = model.generate_content(test)

    text_content = ' '.join([part.text for part in response.parts])

    print(text_content)


speech()
