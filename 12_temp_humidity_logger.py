import adafruit_dht
import time
import board

sensor = adafruit_dht.DHT22(board.D4)

running = True

file = open("sensor_readings.txt", "w")
file.write("time and date, temperature, humidity")

while running:
    try:
        temperature_C = sensor.temperature
        humidity = sensor.humidity

        temperature_F = temperature_C * 9/5.0 + 32

        if humidity is not None and temperature_C is not None:
            print('Temperature = ' + str(temperature_C) + 'C, Humidity = ' + str(humidity))
            file.write(time.strftime('%H:%M:%S %d:%m:%Y') + ', ' + str(temperature_C) + 'C, ' + str(humidity) + '\n')
        else:
            print('failed to get reading, Try again!')
        time.sleep(2)
    except KeyboardInterrupt:
        print('Program Stopped')
        running = False
        file.close()

