import websockets
import asyncio

async def hello():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        name = input("What's your name? ")
        
        await websocket.send(name)
        print(f"Client Sent: {name}")
        
        greeting = await websocket.recv()
        print(f"Client Received: {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())