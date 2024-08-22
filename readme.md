# Before you run the script, make sure you have the pywhatkit library installed. You can install it via pip

pip install pywhatkit

----------------------------------------
Python Script

import pywhatkit as kit
import time

with open('message.txt', 'r') as file:
    message = file.read().strip()

with open('numbers.txt', 'r') as file:
    numbers = [line.strip() for line in file]

def send_message(number, message):
    kit.sendwhatmsg_instantly(f"+{number}", message)
    time.sleep(10)  

for number in numbers:
    send_message(number, message)
    print(f"Message sent to {number}")

print("All messages sent!")

----------------------------------------

Explanation
message.txt: This file should contain the message you want to send.

numbers.txt: This file should contain the list of phone numbers, each on a new line. Include the country code without the + sign (e.g., 911234567890 for an Indian number).

send_message function: This function sends the message to the specified number using the pywhatkit.sendwhatmsg_instantly method.

Delay: There is a 10-second delay between sending messages to avoid being flagged by WhatsApp.

Notes: 
Ensure that WhatsApp Web is logged in on your default browser, as pywhatkit will open WhatsApp Web and send the messages from there.
This script assumes that you are sending messages in quick succession. If you need to send messages at a specific time, you can modify the script accordingly.
Running the Script
Simply run the script after placing your message.txt and numbers.txt in the same directory as the Python file.

python send_whatsapp_messages.py
