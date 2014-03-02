from queue import Queue
from microrpc import Server

queues = {}
server = Server()

@server.rpc
def create(name):
    if name not in queues:
        queues[name] = Queue()
        return True
    return False

@server.rpc
def delete(name):
    if not queues.pop(name, False):
        return False
    return True

@server.rpc
def put(name, payload):
    queues[name].put(payload)

@server.rpc
def get(name):
    return queues[name].get()

server.run()

