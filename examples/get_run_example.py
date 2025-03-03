# Contains a simple python code snippet to get the details of the device with specific id by using the get_device() method and run a small QUBO on the device and print the result

from quanfluence_sdk import QuanfluenceClient

Q = {(0, 0): 1, (0,1): -1, (1,1): 2}

client = QuanfluenceClient()
client.signin('username_here', 'password_here')

device = client.get_device(device_id)
print(device)

result = client.execute_device_qubo_input(device["id"], Q)
print(result)
