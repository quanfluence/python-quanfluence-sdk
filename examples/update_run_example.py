# Contains a simple python code snippet to update the device with specific configurations using the update_device() method and run a small QUBO on the device and print the result

from quanfluence_sdk import QuanfluenceClient

Q = {(0, 0): 1, (0,1): -1, (1,1): 2}

client = QuanfluenceClient()
client.signin('username_here', 'password_here')

device = client.update_device(device_id, {"alpha": 1, "iters": 1000})
print(device)

result = client.execute_device_qubo_input(device_id, Q)
print(result)
