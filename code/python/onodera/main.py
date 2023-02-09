from fastapi import FastAPI
import queue
from pydantic import BaseModel
import time

class Item(BaseModel):
	command: str
	value: str

app = FastAPI()

game_dict = {}

@app.get("/")
async def root():
	return {"result": "succeed"}
	
@app.get("/{game_name}/{pc_name}")
async def read_command(game_name: str, pc_name: str):
	if game_name not in game_dict:
		game_dict[game_name] = dict()
	pc_dict = game_dict[game_name]
	if pc_name not in pc_dict:
		return {"error" : "not registered"}
	elif "opponent" not in pc_dict[pc_name]:
		return {"error" : "not connected"}	
	else:
		if pc_dict[pc_name]["queue"].empty():
			return {"command" : "none"}
		else:
			command = pc_dict[pc_name]["queue"].get().split("%")
			if len(command) == 1:
				return {"command" : command[0]}
			else:
				return {"command" : command[0], "value" : command[1]}

@app.post("/{game_name}/{pc_name}")
def issue_command(game_name: str, pc_name: str, item: Item):
	if game_name not in game_dict:
		game_dict[game_name] = dict()
	pc_dict = game_dict[game_name]
	if item.command == "register":
		if pc_name in pc_dict:
			if "opponent" in pc_dict[pc_name]:
				del pc_dict[pc_name]["opponent"]
				del pc_dict[pc_dict[pc_name]["opponent"]]["opponent"]
				del pc_dict[pc_dict[pc_name]["opponent"]]["queue"]
		pc_dict[pc_name] = {"name" : item.value}
		return {"result" : "succeed", "command" : item.command, "value" : item.value}
	elif item.command == "quit":
		if pc_name in pc_dict:
			if "opponent" in pc_dict[pc_name]:
				pc_dict[pc_dict[pc_name]["opponent"]]["queue"].put("quit%")
				time.sleep(0.5)
				del pc_dict[pc_dict[pc_name]["opponent"]]
			del pc_dict[pc_name]
		return {"result" : "succeed", "command" : item.command}
	elif pc_name not in pc_dict:
		return {"result" : "error", "reason": "not registered"}
	elif item.command == "opponent":
		if "opponent" in pc_dict[pc_name]:
			return  {"result" : "connected", "opponent" : pc_dict[pc_name]["opponent"], "value" : pc_dict[pc_dict[pc_name]["opponent"]]["name"]}
		rv = {"result" : "succeed"}
		for key, value in pc_dict.items():
			if key == pc_name:
				continue
			if "opponent" not in value:
				rv[key] = value["name"]
		return rv
	elif item.command == "connect":
		if "opponent" in pc_dict[pc_name]:
			return  {"result" : "connected", "opponent" : pc_dict[pc_name]["opponent"], "value" : pc_dict[pc_dict[pc_name]["opponent"]]["name"]}
		if item.value not in pc_dict:
			return {"result" : "error", "reason": item.value + " not exist"}
		if "opponent" not in pc_dict[item.value]:
			pc_dict[pc_name]["opponent"] = item.value
			pc_dict[pc_name]["queue"] = queue.Queue()
			pc_dict[item.value]["opponent"] = pc_name
			pc_dict[item.value]["queue"] = queue.Queue()
#			pc_dict[item.value]["queue"].put("connect"+"%"+pc_name)
			return  {"result" : "succeed", "command" : item.command, "value" : pc_dict[item.value]["name"]}
		else:
			return {"result" : "error", "reason": "already connected"}
	elif "opponent" not in pc_dict[pc_name]:
		return {"result" : "error", "reason": "not connected"}
	else:
		pc_dict[pc_dict[pc_name]["opponent"]]["queue"].put(item.command + "%" + item.value)
		return {"result" : "succeed", "command" : item.command, "value" : item.value}