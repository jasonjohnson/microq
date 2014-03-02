from microrpc import Client

client = Client()

queue = 'my-queue'

client.create(queue)
client.put(queue, "Message 0")
client.put(queue, "Message 1")
client.put(queue, "Message 2")
client.put(queue, "Message 3")
client.put(queue, "Message 4")

print(client.get(queue))
print(client.get(queue))

client.delete(queue)

