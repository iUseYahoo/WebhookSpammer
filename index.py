import requests
from time import sleep

getwebhook = str(input("Webhook Example: https://discord.com/api/webhooks/123456789/abcdefghi\nEnter the webhooks URL: "))
sendmessage = input("Enter the message for the webhook to send: ")


sendconfig = {
    "content": str(sendmessage)
}

senddata = requests.post(getwebhook, data=sendconfig)

if senddata.status_code == 200 or 204:
    print("The data was sent to the webhook successfully.")
else:
    print(f"There was an error sending to the webhook. Status Code: {senddata.status_code}, Content: {senddata.content}")
