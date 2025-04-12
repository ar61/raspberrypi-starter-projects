import smtplib
import os
from email.mime.text import MIMEText
from gpiozero import LED, Button, MotionSensor
from signal import pause
from python_ntfy import NtfyClient

led_status = LED(17)
led_triggered = LED(18)
button = Button(2)
pir = MotionSensor(4)

motion_sensor_status = False
email_sent = False
client = NtfyClient(topic="test")

def arm_motion_sensor():
    global email_sent
    global motion_sensor_status
    if motion_sensor_status == True:
        motion_sensor_status = False
        led_status.off()
        led_triggered.off()
    else:
        motion_sensor_status = True
        email_sent = False
        led_status.on()

def send_email():

    global email_sent
    global motion_sensor_status

    server_env = os.environ.get("NTFY_SERVER")

    if server_env is None:
        print("NTFY_SERVER is not set, exiting app")
        exit(0)

    #email_env = os.environ.get("email")
    #password_env = os.environ.get("password")
    #to_email_env = os.environ.get("to_email")

    #if email_env is None or password_env is None or to_email_env is None:
    #    print("email or password or to email is not set in env variables")
    #    exit(0)

    #from_email_addr = email_env
    #from_email_password = password_env
    #to_email_addr = to_email_env

    #body = 'Motion was detected in your room'
    #msg = MIMEText(body)

    #msg['From'] = from_email_addr
    #msg['To'] = to_email_addr
    #msg['Subject'] = 'INTRUDER ALERT!'

    #server = smtplib.SMTP('smtp.zoho.com', 587)
    #server.starttls()
    #print(f"Trying to login to {from_email_addr}..")
    #server.login(from_email_addr, from_email_password)
    #print(f"Sending email to {to_email_addr}..")
    #server.sendmail(from_email_addr, to_email_addr, msg.as_string())
    #server.quit()
    
    client.send("INTRUDER ALERT")
    print("Ntfy message sent")
    email_sent = True
    led_triggered.on()
    print('Email sent!')


button.when_pressed = arm_motion_sensor
pir.when_motion = send_email

pause()

