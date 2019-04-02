import cloudbook_service_client_api as capi
import json

# OBJECT CIRCLE EMPTY
circle = capi.get_empty_circle()

# INITIALIZE  CIRCLE
circle["name"] = "Circulo API Cliente"
circle["desc"] = "Este es un circulo de pruebas creado desde el API Cliente"
circle["agent_id"] = "ABCDEFG123456"
circle["url_fs"] = "fs://localhost"


print("CREATE CIRCLE TEST")
response = capi.create_circle(circle)
json_data = json.loads(response.content)
# Save circle_id info
circle["circle_id"] = json_data["circle_id"]
print(json_data)


print("GET CIRCLE TEST")
response = capi.get_circle(circle["agent_id"])
json_data = json.loads(response.content)
print(json_data)


print("GET CIRCLES TEST")
response = capi.get_circles()
json_data = json.loads(response.content)
print(json_data)


print("ATTACH AGENT TEST")
response = capi.attach_agent(circle["agent_id"], circle["circle_id"])
json_data = json.loads(response.content)
print(json_data)


print("MODIFY CIRCLE TEST")
circle["name"] = "Circulo API Cliente MODIFICADO"
response = capi.modify_circle(circle)
json_data = json.loads(response.content)
print(json_data)


print("GET CIRCLE AGENTS TEST")
response = capi.get_circle_agents(circle["circle_id"])
json_data = json.loads(response.content)
print(json_data)