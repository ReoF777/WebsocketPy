import asyncio
import websockets

async def listen():
    url = "ws://127.0.0.1:8000"
    async with websockets.connect(url) as websocket:
        while True:
            try:
                message = websocket.recv()
                print(f"Client Received: {message}")
            except websockets.ConnectionClosed:
                print("Connection Closed")
                break

if __name__ == "__main__":
    try:
        asyncio.run(listen())
    except KeyboardInterrupt:
        print("Client Stopped")