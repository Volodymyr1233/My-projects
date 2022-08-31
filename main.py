from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import requests
from bs4 import BeautifulSoup
import sys
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config



url = "https://minfin.com.ua/currency/nbu/"

source = requests.get(url)
text = source.text
soup = BeautifulSoup(text, 'html.parser')



p = soup.find_all("div",{'class':'sc-1x32wa2-10 evFbid'})

def curr_func(item):
    result = item.get_text().strip()[:7].replace(',', '.')
    result = float(result)
    return round(result, 2)

USD = curr_func(p[0])
EUR = curr_func(p[1])
PLN = curr_func(p[2])

config_dict = config.get_default_config()  # операція для зміни мови
config_dict['language'] = 'en'
owm = OWM('98a1db1eb81598f26e532bafd5a30636', config_dict)
mgr = owm.weather_manager()  # підключаємо погоду



class FirstWindow(Screen):
    def exit_app(self):
        sys.exit()



class SecondWindow(Screen):
    def press1(self):
       self.resultat.text = 'Exchange rate for dollar today is ' + str(USD) + " UAH"
       self.resultat.font_size = 40
    def press2(self):
       self.resultat.text = 'Exchange rate for euro today is ' + str(EUR) + " UAH"
       self.resultat.font_size = 40
    def press3(self):
       self.resultat.text = 'Exchange rate for zloty today is ' + str(PLN) + " UAH"
       self.resultat.font_size = 40



class LastWindow(Screen):
    def pressed(self):
        try:
            Text = self.input.text.strip()
            observation = mgr.weather_at_place(Text)  # беремо погоду з нашого інпуту
            w = observation.weather  # обробляємо і дістаємо погоду для нашого користувача

            temp = w.temperature('celsius')["temp"]  # отримуємо температуру і в квадратних дужках вказуємо температуру на даний момент
            wind = w.wind()["speed"]  # отримуємо швидкість вітру
            water = w.humidity  # отримуємо вологість
            status = w.detailed_status  # отримуємо статус хмарно, або наприклад ясно

            self.label1.text = "Status: " + "in city " + Text + " now is " + str(status)
            self.label2.text = "Humidity: " + "in city " + Text + " now is " + str(water) + '%'
            self.label3.text = "Temperature: " + "in city " + Text + " now is " + str(temp) + '°C'
            self.label4.text = "Speed: " + "in city " + Text + " wind speed is " + str(wind) + " м/с"
            self.label1.color = (75 / 255, 220 / 255, 20 / 255, 1)
            self.label2.color = (75 / 255, 220 / 255, 20 / 255, 1)
            self.label3.color = (75 / 255, 220 / 255, 20 / 255, 1)
            self.label4.color = (75 / 255, 220 / 255, 20 / 255, 1)
        except:
            self.label1.text = "Error"
            self.label1.color = (220 / 255, 28 / 255, 20 / 255, 1)
            self.label2.text = "Error"
            self.label2.color = (220 / 255, 28 / 255, 20 / 255, 1)
            self.label3.text = "Error"
            self.label3.color = (220 / 255, 28 / 255, 20 / 255, 1)
            self.label4.text = "Error"
            self.label4.color = (220 / 255, 28 / 255, 20 / 255, 1)



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('my1.kv')


class MyApp(App):
    def build(self):
        return kv




if __name__ == "__main__":
   MyApp().run()

