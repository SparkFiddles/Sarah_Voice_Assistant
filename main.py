import speech_recognition as sr
r = sr.Recogniser()


def record_audio():
   with sr.Microphone() as source:
      print('say something')
      audio = r.listen(source)
      voice_data=''
      try:
        voice_data = r.recognize_google(audio)
        print(voice_data)
      except sr.UnknownValueError:
        print('sorry, I did not get that')
      except sr.RequestError:
        print('Sorry, my speech service is down')
      return voice_data
print('How can I help you')
voice_data=record_audio()
print(voice_data)