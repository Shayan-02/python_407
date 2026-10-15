import requests
import time


def fetch_url(url):
    response = requests.get(url)
    print(f"URL: {url}, length: {len(response.text)}")


start_time = time.time()
urls = [
    "https://www.digikala.com/",
    "https://snapp.ir/",
    "https://www.aparat.com/",
    "https://divar.ir/",
    "https://shaparak.ir/",
    "https://namnak.com/",
    "https://www.digikala.com/",
    "https://snapp.ir/",
    "https://www.aparat.com/",
    "https://divar.ir/",
    "https://shaparak.ir/",
    "https://namnak.com/",
]


for url in urls:
    result = fetch_url(url)
end_time = time.time()

execution_time = end_time - start_time

print(f"time:  {execution_time} s")