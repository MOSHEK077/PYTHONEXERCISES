import requests
import time
url ="http://mathworld.wolfram.com/QED.html"
max_retries = 5
retires = 0
success = False
while retires < max_retries and not success:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully retrieved data.")
            success = True
        else:
            retires += 1
            print(f"Failed Attempt {retires}")
            time.sleep
    except requests.exceptions.RequestException as e :
        retires += 1
        print(f"Error:{e},attempt {retires}")
        time.sleep
        