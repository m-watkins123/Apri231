import unittest
import requests
import json
from unittest.mock import patch, Mock
from pprint import pprint
from github import Github
def get_todos():
    Response = requests.get(f"https://api.github.com/repos/m-watkins123/helloWorld/commits")
    print(response.ok)
    username = "m-watkins123"
    url = f"https://api.github.com/repos/m-watkins123/helloWorld/commits"
    print(url + commits)
