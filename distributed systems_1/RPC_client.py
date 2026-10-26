import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000")
result1 = proxy.add(3,5)
print(f"3+5 : {result1}")
result2 = proxy.square(5)
print(f"square(5) = {result2}")