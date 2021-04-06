"""Example file to show how to use labelbox."""

from labelbox import Client

if __name__ == '__main__':
    API_KEY = """eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
    eyJ1c2VySWQiOiJja214ZmY4dGp2OTNxMDc1N2s2dzRndzY2Ii
    wib3JnYW5pemF0aW9uSWQiOiJja214NWg5Znd0ZzUxMDg0ODdp
    NHZxMDE3IiwiYXBpS2V5SWQiOiJja215eG1qNHR5eThsMDc0N2
    hrdHp3b2ptIiwiaWF0IjoxNjE3Mjg0ODIxLCJleHAiOjIyNDg0
    MzY4MjF9.uJ1wDekRxrYtie31RqpoiM_08tWThlShUZrkqjfCDXI"""
    client = Client(API_KEY)

    project = client.get_project("ckmx5jeqo9u4007902mbiz6k2")
    datasets = project.datasets()
