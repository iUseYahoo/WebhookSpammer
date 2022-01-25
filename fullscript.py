import requests

def webhook_tester():
    webhookurl = str(input("Enter webhook URL to test: "))
    testwebhook = requests.get(webhookurl, allow_redirects=False)

    if testwebhook.status_code != 200:
        print("This webhook didn't return with status code 200, This webhook may be dead.")
    elif testwebhook.status_code == 200:
        print("This webhook returned status code 200. This webhook is alive.")
    else:
        print(f"Status Code: {testwebhook.status_code}\nContent: {testwebhook.content}\nText: {testwebhook.text}")

def webhook_sender():
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

pickscript = int(input("Scriptsn\n[1] - Test Webhooks\n[2] - Webhook Sender\nEnter scipts number: "))

if pickscript == 1:
    webhook_tester()
elif pickscript == 2:
    webhook_sender()
else:
    print(f"{pickscript} is not a valid option. Please use script 1 or 2.\nExiting.")
    quit()
