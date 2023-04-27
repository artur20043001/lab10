import requests
import json
import random
import vosk
import pyaudio
model = vosk.Model("vosk-model-small-ru-0.4")
response = requests.get(" https://date.nager.at/api/v2/publicholidays/2020/GB")
data = json.loads(response.content)



def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            command = json.loads(rec.Result())
            if command['text']:
                yield command['text']



def means():
    for i in range(len(data)):
        print(data[i]['localName'], end='')
    print()


def date():
    for i in range(len(data)):
        print(data[i]['localName'], data[i]['date'] )
    print()
    print("Курс евро: ", data["rub"]["eur"])


def save_data():
    with open("rates.txt", "w") as f:
        nazv=[]
        for i in range(len(data)):
            nazv.append(data[i]['localName'])
        json.dump(nazv, f)
    print("Данные сохранены в файл rates.txt")


def count():
    print('количество',len(data))
def randomchik():
    chis = random.randint(0,len(data))
    print('дата',data[chis]['localName'],'название', data[chis]['date'])

rec = vosk.KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=16000
)
stream.start_stream()
for text in listen():
    if "перечислить" in text:
        means()
    elif "даты" in text:
        date()
    elif "сохранить" in text:
        save_data()
    elif "количество" in text:
        count()
    elif "любое" in text:
        randomchik()
    elif "выход" in text:
        break
    else:
        print("Не удалось распознать команду")