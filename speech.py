import speech_recognition as sr


r=sr.Recognizer()
with sr.Microphone() as src:
    audio=r.listen(src)
    voice=r.recognize_google(audio)
    print(voice)