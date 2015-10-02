import asyncio

class SimpleEchoProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        print('Connection Received !')
        self.transport = transport

    def data_received(self, data):
        print(data)
        self.transport.write(b'echo:')
        self.transport.write(data)

    def connection_lost(self, exc):
        print('Connection lost ! Closing Server !')
        

loop = asyncio.get_event_loop()
server = loop.run_until_complete(loop.create_server(SimpleEchoProtocol, 'localhost', 2222))
loop.run_until_complete(server.wait_closed())
