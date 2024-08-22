import pywhatkit as kit
import time

# Read the message from message.txt
with open('message.txt', 'r') as file:
    message = file.read().strip()

# Read the numbers from numbers.txt
with open('numbers.txt', 'r') as file:
    numbers = [line.strip() for line in file]

# Function to send a message to a number
def send_message(number, message):
    kit.sendwhatmsg_instantly(f"+{number}", message)
    time.sleep(20)  # Wait for 20 seconds before sending the next message

# Send message to each number
for number in numbers:
    send_message(number, message)
    print(f"Message sent to {number}")

print("All messages sent!")
