import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"{url} - Status Code: {response.status_code}")

urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org"
]


threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
