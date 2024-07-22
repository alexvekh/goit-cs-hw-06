import asyncio
import json
import websockets
from motor.motor_asyncio import AsyncIOMotorClient
import os

class WebSocketServer:
    def __init__(self, uri):
        self.uri = uri
        self.clients = set()
        self.client = AsyncIOMotorClient('mongodb://mongodb:27017')
        self.db = self.client.messages_db
        self.data_file_path = 'storage/data.json'
        self.init_data_file()

    def init_data_file(self):
        # Ініціалізація файлу даних, якщо він не існує
        if not os.path.exists(self.data_file_path):
            with open(self.data_file_path, 'w') as file:
                json.dump([], file)

    async def ws_handler(self, ws):
        self.clients.add(ws)
        try:
            await self.distribute(ws)
        finally:
            if ws in self.clients:
                self.clients.remove(ws)

    async def distribute(self, ws):
        async for message in ws:
            message_data = json.loads(message)
            await self.db.messages.insert_one(message_data)
            self.save_to_json_file(message_data)
            await self.broadcast(message_data)

    def save_to_json_file(self, message_data):
        # Створення копії даних без поля '_id'
        data_to_save = {k: v for k, v in message_data.items() if k != '_id'}
        with open(self.data_file_path, 'r+') as file:
            data = json.load(file)
            if isinstance(data, list):
                data.append(data_to_save)
            else:
                data = [data_to_save]
            file.seek(0)
            json.dump(data, file, indent=4)

    async def broadcast(self, message_data):
        clients_copy = set(self.clients)
        for client in clients_copy:
            try:
                await client.send(json.dumps(message_data))
            except Exception as e:
                print(f"Failed to send message to a client: {e}")
                self.clients.remove(client)


    async def main(self):
        async with websockets.serve(self.ws_handler, "0.0.0.0", 5000):
            await asyncio.Future()

if __name__ == "__main__":
    server = WebSocketServer('ws://localhost:5000')
    asyncio.run(server.main())
