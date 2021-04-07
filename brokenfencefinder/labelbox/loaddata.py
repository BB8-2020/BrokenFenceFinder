"""Example file to show how to use labelbox."""
import requests
from labelbox import Client

if __name__ == '__main__':
    API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
              ".eyJ1c2VySWQiOiJja214ZmY4dGp2OTNxMDc" \
              "1N2s2dzRndzY2Iiwib3JnYW5pemF0aW9uSWQ" \
              "iOiJja214NWg5Znd0ZzUxMDg0ODdpNHZxMDE" \
              "3IiwiYXBpS2V5SWQiOiJja215eG1qNHR5eTh" \
              "sMDc0N2hrdHp3b2ptIiwiaWF0IjoxNjE3Mjg" \
              "0ODIxLCJleHAiOjIyNDg0MzY4MjF9.uJ1wDe" \
              "kRxrYtie31RqpoiM_08tWThlShUZrkqjfCDXI"
    client = Client(API_KEY)

    project = client.get_project("ckmx5jeqo9u4007902mbiz6k2")
    datasets = project.datasets()
    exportUrl = project.export_labels()
    data = requests.get(exportUrl).json()

