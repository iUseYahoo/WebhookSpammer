import requests

webhookurl = str(input("Enter webhook to test: "))

testwebhook = requests.get(webhookurl, allow_redirects=False)

if testwebhook.status_code != 200:
    print("This webhook didn't return with status code 200, This webhook may be dead.")
elif testwebhook.status_code == 200:
    print("This webhook returned status code 200. This webhook is alive.")
else:
    print(f"Status Code: {testwebhook.status_code}\nContent: {testwebhook.content}\nText: {testwebhook.text}")

