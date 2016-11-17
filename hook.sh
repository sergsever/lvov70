#!/bin/bash 

curl -X POST -u sergsever --data '{
"id": 1,
"url": "api.github.com/tempesta-tech/tempesta/hooks/1",
"name": "web",
"events": [
"push",
"pull_request"
],
"active": True,
"config": {
"url": "82.196.12.145/cgi-bin/githubhook.py",
"content_type": "json"
}
}' https://api.github.com/repos/sergsever/lvov70/hooks

