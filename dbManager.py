from tinydb import TinyDB, Query
import utils, time

db = TinyDB('./db/cloudbook.json')

#Circle json/data definition
BaseCircle = {"name": "",
          "circle_id": "",
          "desc": "",
          "num_attached_agents": 0,
          "url_fs": "",
          "status": ""}

AgentCircle = {"agent_id": "",
               "circle_id": "",
               "attach_time": 0}


def create_circle(json_circle):
    if check_circle_name_exist(json_circle['name']) == 0:
        tmp_circle = BaseCircle
        tmp_circle['name'] = json_circle['name']
        tmp_circle['desc'] = json_circle['desc']
        tmp_circle['url_fs'] = json_circle['url_fs']
        tmp_circle['status'] = "make on going"
        tmp_circle['circle_id'] = utils.id_generator()
        tmp_circle['num_attached_agents'] = 1
        print(tmp_circle)
        table_circle = db.table('circles')
        table_circle.insert(tmp_circle)

        tmp_agent_circle = AgentCircle
        tmp_agent_circle['agent_id'] = json_circle['agent_id']
        tmp_agent_circle['circle_id'] = tmp_circle['circle_id']
        tmp_agent_circle['attach_time'] = str(time.time())
        table_agent_circle = db.table('agent_circle')
        table_agent_circle.insert(tmp_agent_circle)
    else:
        tmp_circle = {"status": "CIRCLE EXIST"}
    return tmp_circle


def get_circles_by_agent(agent_id):
    table = db.table('circles')
    table_agent_circle = db.table('agent_circle')
    query = Query()
    circle_ids_list = table_agent_circle.search(query.agent_id == agent_id)
    circle_list = []
    for circle in circle_ids_list:
        circle_list.append(table.search(query.circle_id == circle['circle_id']))
    return circle_list


def attach_agent_to_circle(json_data):
    tmp_agent_circle = AgentCircle
    if check_circle_id_exist(json_data['circle_id']) > 0:
        tmp_agent_circle['agent_id'] = json_data['agent_id']
        tmp_agent_circle['circle_id'] = json_data['circle_id']
        tmp_agent_circle['attach_time'] = str(time.time())
        table_agent_circle = db.table('agent_circle')
        if table_agent_circle.search((Query().circle_id == tmp_agent_circle['circle_id'])
                                     & (Query().agent_id == tmp_agent_circle['agent_id'])):
            return "Agent Already Attached"
        else:
            table_agent_circle.insert(tmp_agent_circle)
            update_circle_agents(tmp_agent_circle['circle_id'], 1)

        return "Agent Attach"
    else:
        return "Circle Not Exist"


def update_circle_agents(circle_id, num):
    table = db.table('circles')
    circle_query = Query()
    circle = table.search(circle_query.circle_id == circle_id)[0]
    circle['num_attached_agents'] = int(circle['num_attached_agents']) + num
    table.upsert(circle, circle_query.circle_id == circle_id)


def get_circle_by_id(circle_id):
    table = db.table('circles')
    circle_query = Query()
    circle = table.search(circle_query.circle_id == circle_id)[0]
    return circle


def get_all_circles():
    table = db.table('circles')
    return table.all()


def get_agents_by_circle(circle_id):
    table_agent_circle = db.table('agent_circle')
    query = Query()
    agent_ids_list = table_agent_circle.search(query.circle_id == circle_id)
    return agent_ids_list


def update_circle(json_circle):
    # CIRCLE EXIST
    if check_circle_id_exist(json_circle['circle_id']) > 0:
        tmp_circle = get_circle_by_id(json_circle['circle_id'])
        tmp_circle['name'] = json_circle['name']
        tmp_circle['desc'] = json_circle['desc']
        if tmp_circle['num_attached_agents'] < 1:
            tmp_circle['url_fs'] = json_circle['url_fs']
        tmp_circle['status'] = "make on going"
        print(tmp_circle)
        table_circle = db.table('circles')
        query = Query()
        table_circle.upsert(tmp_circle, query.circle_id == json_circle['circle_id'])
    else:
        tmp_circle = {"status": "CIRCLE NOT EXIST"}
    return tmp_circle


def check_circle_name_exist(circle_name):
    table = db.table('circles')
    circle_query = Query()
    return len(table.search(circle_query.name == circle_name))


def check_circle_id_exist(circle_id):
    table = db.table('circles')
    circle_query = Query()
    return len(table.search(circle_query.circle_id == circle_id))