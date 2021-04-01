from labelbox import Client

if __name__ == '__main__':
    API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja214ZmY4dGp2OTNxMDc1N2s2dzRndzY2Iiwib3JnYW5pemF0aW9uSWQiOiJja214NWg5Znd0ZzUxMDg0ODdpNHZxMDE3IiwiYXBpS2V5SWQiOiJja215eG1qNHR5eThsMDc0N2hrdHp3b2ptIiwiaWF0IjoxNjE3Mjg0ODIxLCJleHAiOjIyNDg0MzY4MjF9.uJ1wDekRxrYtie31RqpoiM_08tWThlShUZrkqjfCDXI"
    client = Client(API_KEY)

    # projects = client.get_projects()
    # for project in projects:
    #     print(project.name, project.uid)
    project = client.get_project("ckmx5jeqo9u4007902mbiz6k2")
    datasets = project.datasets()
