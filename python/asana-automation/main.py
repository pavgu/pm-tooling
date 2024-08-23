import os
import requests
import json


def beautify(text):
    return json.dumps(text, sort_keys=True, indent=2)


def get_xxx_workspace():
    url = 'https://app.asana.com/api/1.0/workspaces'
    auth_header = 'Bearer ' + asana_token
    headers = {'Accept': 'application/json', 'Authorization': auth_header}
    r = requests.get(url, headers=headers)
    results = r.json()['data']
    for result in results:
        if result['name'] == 'XXX':
            return result['gid']


def create_team():
    # Creating a team
    url = 'https://app.asana.com/api/1.0/teams'
    auth_header = 'Bearer ' + asana_token
    headers = {'Content-Type': 'application-json', 'Accept': 'application/json', 'Authorization': auth_header}

    data = {"data": {"description": "XXX Team",
                     "html_description": "<body>All active XXX Team members.</body>",
                     "name": "XXX Team",
                     "organization": xxx_workspace
                     }
            }
    data_json = json.dumps(data)
    r = requests.post(url, data=data_json, headers=headers)
    result = r.json()['data']
    return result['gid']


def add_team_members():
    team = ["t1@xxx.com",
            "t2@xxx.com",
            "t3@xxx.com"]
    url = "https://app.asana.com/api/1.0/teams/" + team_gid + "/addUser"
    auth_header = 'Bearer ' + asana_token
    headers = {'Content-Type': 'application-json',
               'Accept': 'application/json',
               'Authorization': auth_header}

    for team_member in team:
        data = {"data": {"user": team_member}}
        team_member_json = json.dumps(data)
        r = requests.post(url, data=team_member_json, headers=headers)


def create_project():
    url = "https://app.asana.com/api/1.0/projects"
    auth_header = 'Bearer ' + asana_token
    headers = {'Content-Type': 'application-json',
               'Accept': 'application/json',
               'Authorization': auth_header}
    data = {
      "data": {
        "archived": "false",
        "color": "light-green",
        "current_status": {
          "author": {
            "name": "XXX"
          },
          "color": "green",
          "created_by": {
            "name": "XXX"
          },
          "html_text": "<body>The project is created to ...</body>",
          "modified_at": "null",
          "text": "",
          "title": ""
        },
        "default_view": "calendar",
        "due_date": "202x-xx-xx",
        "due_on": "202x-xx-xx",
        "followers": "",
        "html_notes": "<body>Initial Project</body>",
        "is_template": "false",
        "name": "Initial Project",
        "notes": "Project",
        "owner": project_owner_gid,
        "public": "false",
        "start_on": "2021-01-11",
        "team": team_gid
      }
    }

    data_json = json.dumps(data)
    r = requests.post(url, data=data_json, headers=headers)
    print("Project creation result: ")
    print(beautify(r.text))
    result = r.json()['data']
    return result['gid']


if __name__ == '__main__':
    asana_token = os.environ['ASANA_PTA']

    # Different Asana entities
    xxx_workspace = get_xxx_workspace()
    project_owner_gid = 'xxxxxxxxxxx' 

    # Creating team and adding members
    # team_gid = create_team()
    team_gid = 'xxxxxxxxxxx'
    # add_team_members()

    # Creating project
    me_project_gid = create_project()
