import asyncio
from asyncio import StreamReader, StreamWriter

REMOTE_ADDRESS = '127.0.0.1'
REMOTE_PORT = 5050


async def echo_server(reader: StreamReader, writer: StreamWriter):
    while True:
        message = await reader.read(100)  # Max byte to read.
        message = message.decode('utf8').strip()
        if not message:
            break
        sender_address, sender_port = writer.get_extra_info('peername')
        print(f'<{sender_address} on {sender_port}>: {message}')

        writer.write('testing'.encode('utf8'))
        await writer.drain()
    writer.close()


async def main(host: str, port: int):
    print(f'Listening to {REMOTE_ADDRESS} on port: {REMOTE_PORT}')
    server = await asyncio.start_server(echo_server, host, port)
    await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.run(main(REMOTE_ADDRESS, REMOTE_PORT))
    except KeyboardInterrupt:
        pass
