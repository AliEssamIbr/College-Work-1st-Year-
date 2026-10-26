from xmlrpc.server import SimpleXMLRPCServer
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def floordiv(a,b):
    return(a//b)
def sub(a,b):
    return a-b
def square(a):
    return a*a

server = SimpleXMLRPCServer(("localhost",8000))
server.register_function(add,"add")
server.register_function(mul,"multiplication")
server.register_function(div,"division")
server.register_function(floordiv,"floor division")
server.register_function(sub,"subtraction")
server.register_function(square,"square")
print("RPC server listening on port 8000...")
server.serve_forever()