import asyncio

REMOTE_ADDRESS = '127.0.0.1'
REMOTE_PORT = 5050


async def main():
    try:
        reader, writer = await asyncio.open_connection(REMOTE_ADDRESS, REMOTE_PORT)
        while True:
            message = input('type a message:')
            writer.write(message.encode('utf8'))
            await writer.drain()
    except ConnectionRefusedError:
        print(f'Failed to connect to {REMOTE_ADDRESS}:{REMOTE_PORT}')
    except ConnectionResetError:
        print(f'Server is down')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
