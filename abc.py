import requests

res = requests.get("http://some-url.com")

res2 = requests.post("http://some-other-url.com", body={})

res3 = requests.post("http://yet-some-other-url.com", body={})
