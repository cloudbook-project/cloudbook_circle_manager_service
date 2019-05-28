import requests

# REQUESTS TO MANAGE CIRCLE
url = 'http://127.0.0.1:5002'

circle_data = {
 "name": "",
 "desc": "",
 "agent_id": "",
 "circle_id":"",
 "url_fs": "",
 "status": ""
}


def get_empty_circle():
    return circle_data


# @app.route('/create_circle', methods=['POST'])
def create_circle(p_circle_data):
    response = requests.post(url + "/create_circle", json=p_circle_data)
    print(response.content)
    return response


# @app.route('/get_circle/<agent_id>')
def get_circle(agent_id):
    response = requests.get(url + "/get_circle/"+agent_id)
    print(response.content)
    return response


# @app.route('/get_circles')
def get_circles():
    response = requests.get(url + "/get_circles")
    print(response.content)
    return response


# @app.route('/attach_agent', methods=['POST'])
def attach_agent(p_agent_id, p_circle_id):
    p_attach_data = {"agent_id":p_agent_id, "circle_id":p_circle_id}
    response = requests.post(url + "/attach_agent", json=p_attach_data)
    print(response.content)
    return response


# @app.route('/modify_circle', methods=['POST'])
def modify_circle(p_circle_data):
    response = requests.post(url + "/modify_circle", json=p_circle_data)
    print(response.content)
    return response


# @app.route('/get_circle_agents/<circle_id>')
def get_circle_agents(p_circle_id):
    response = requests.get(url + "/get_circle_agents/"+p_circle_id)
    print(response.content)
    return response

