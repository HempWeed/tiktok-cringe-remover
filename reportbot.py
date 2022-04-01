import requests
import random
from os import name, system

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
id = str(input("enter the video ID: "))
while id == "":
    print("please input an ID")
print(id + "\n")

i = "0"
count = 0

try:
    while True:
        i = str(random.randint(1,1000))
        url = "https://www.tiktok.com/aweme/v1/aweme/feedback/?object_id=" + id + "&priority_region=True&reason=" + i + "&report_type=video&target=" + id + "&video_id=" + id
        response = requests.get(url)
        if response.status_code != 200:
            print("Error: " + str(response.status_code))
        else:
            print(str(response.status_code) + u"\u001b[34;1m sucessful report!\u001b[0m")
            count += 1

except KeyboardInterrupt:
    print("\n\nTotal reports: " + str(count))
    exit()
