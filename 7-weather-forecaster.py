import time
import adafruit_ssd1306
import requests
from board import SDA, SCL
import busio

from PIL import Image, ImageDraw, ImageFont

# Idea to extend this project:
# Traffic , Tweets, Latest news, Stock prices, Current bitcoin exchange rate

def clear_display(display):
    display.fill(0)
    display.show()

i2c = busio.I2C(SCL, SDA)

display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

open_weather_map_url = "https://api.openweathermap.org/data/2.5/weather?q=south%20old%20bridge,USA&APPID=f2c5088da636b92ee1f1c5200acf4a00"

while True:
    #display.clear()
    #display.display()

    clear_display(display)

    width = display.width
    height = display.height
    image = Image.new('1', (width, height))

    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    padding = 2
    top = padding

    x = padding

    font = ImageFont.load_default()

    weather_data = requests.get(open_weather_map_url)

    location = weather_data.json().get('name') + '-' + weather_data.json().get('sys').get('country')
    draw.text((x, top), location, font=font, fill=200)

    # text doesn't work for all displays
    # display.text('Hello', 0, 0)

    description = 'Desc ' + weather_data.json().get('weather')[0].get('main')
    draw.text((x, top + 10), description, font=font, fill=100)

    raw_temperature = weather_data.json().get('main').get('temp')-273.15
    temperature = 'Temperature ' + str(round(raw_temperature,2)) + "*C"
    draw.text((x, top + 20), temperature, font=font, fill=255)

    pressure = 'Pressure ' + str(weather_data.json().get('main').get('pressure')) + 'hPa'
    draw.text((x, top + 30), pressure, font=font, fill=255)

    humidity = 'Humidity ' + str(weather_data.json().get('main').get('humidity')) + '%'
    draw.text((x, top + 40), humidity, font=font, fill=255)

    wind = 'Wind ' + str(weather_data.json().get('wind').get('speed')) + 'mps' + str(weather_data.json().get('wind').get('deg')) + "*"
    draw.text((x, top + 50), wind, font=font, fill=255)

    display.image(image)
    display.show()

    time.sleep(30)

    # clear_display(display)    

    # break

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
# display.fill(0)

# display.show()

# Set a pixel in the origin 0,0 position.
# display.pixel(0, 0, 1)
# Set a pixel in the middle 64, 16 position.
# display.pixel(64, 16, 1)
# Set a pixel in the opposite 127, 31 position.
# display.pixel(127, 31, 1)
#display.show()
