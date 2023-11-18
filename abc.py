import requests

res = requests.get("http://some-url.com")

res2 = requests.post("http://some-other-url.com", body={})

res3 = requests.put("http://yet-another.com", body={})
