import requests
import tkinter
from tkinter import PhotoImage


from mtranslate import translate



def translate_to_turkish(english_word):
    turkish_word = translate(english_word, 'tr', 'en')
    return turkish_word



'''def translate_to_turkish(english_text):
    translator = Translator(to_lang="tr")
    translation = translator.translate(english_text)
    return translation'''
def butona_tiklandiginda():
    # API anahtarınızı buraya ekleyin
    api_key = "f39b38a7fc574fc0e66fb98ea888bbf2"

    # Hava durumu almak istediğiniz şehir adını burada belirtin
    city_name = entry1.get()

    # API isteği için URL oluşturun
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    # API isteğini gönderin
    response = requests.get(url)

    # Cevabı JSON formatında alın
    data = response.json()

    # Hava durumu verilerini işleme
    if response.status_code == 200:
        
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        ceviri=translate_to_turkish(weather)
        
        sehir=f"{entry1.get()}"
        celcius=f"{int(temperature - 273.15)}°C "

        label2.config(text=sehir,font=("Sans Serif", 20))
        label3.config(text=celcius,font=("Bold", 20))
        label4.config(text=ceviri,font=("Sans Serif", 20))




        '''print(f"Hava Durumu: {ceviri}")
        print(f"Sıcaklık: {temperature} Kelvin")
        print(f"Nem: {humidity}%")'''
    else:
        print("Hava durumu verileri alınamadı.")




#gui



ekran=tkinter.Tk()

ekran.geometry("200x500")

photo = PhotoImage(file="logo.png")

logo_label=tkinter.Label(image=photo)
logo_label.pack(pady=10)

label1=tkinter.Label(text="şehir ismini giriniz",font=("Arial", 15))
label1.pack(pady=5)

entry1=tkinter.Entry(width=25)
entry1.pack(pady=10)

buton1=tkinter.Button(text="arama",font=("Arial", 15),background="#00BFFF",command=butona_tiklandiginda)

buton1.pack(pady=10)



label2=tkinter.Label(text="")
label2.pack()

label3=tkinter.Label(text="")
label3.pack()

label4=tkinter.Label(text="")
label4.pack()


ekran.mainloop()

