from flask import Flask, request
import dbManager, json

application = Flask(__name__)


@application.route('/')
def index():
    return 'Server circle manager Works!'


@application.route('/get_circle/<agent_id>')
def get_circle(agent_id):
    circles = dbManager.get_circles_by_agent(agent_id)
    json_data = json.dumps(circles)
    return json_data


@application.route('/get_circles')
def get_circles():
    circles = dbManager.get_all_circles()
    json_data = json.dumps(circles)
    return json_data


@application.route('/create_circle', methods=['POST'])
def create_circles():
    json_data = request.get_json()
    circle = dbManager.create_circle(json_data)
    json_data = json.dumps(circle)
    return json_data


@application.route('/attach_agent', methods=['POST'])
def attach_agent():
    json_data = request.get_json()
    str_ret = dbManager.attach_agent_to_circle(json_data)
    json_data = json.dumps(str_ret)
    return json_data


@application.route('/modify_circle', methods=['POST'])
def modify_circle():
    json_data = request.get_json()
    updated_circle = dbManager.update_circle(json_data)
    json_data = json.dumps(updated_circle)
    return json_data


@application.route('/get_circle_agents/<circle_id>')
def get_circle_agents(circle_id):
    circles = dbManager.get_agents_by_circle(circle_id)
    json_data = json.dumps(circles)
    return json_data

if __name__ == '__main__':
	application.run(host='0.0.0.0',port=80)
