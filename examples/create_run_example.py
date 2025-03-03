#Contains a simple python code snippet to create a device and run a small QUBO on the device and print the result

from quanfluence_sdk import QuanfluenceClient

Q = {(0, 0): 1, (0,1): -1, (1,1): 2}

client = QuanfluenceClient()
client.signin('username_here', 'password_here')

device = client.create_device(title="Device 1",
    description="A device for testing QUBO problems",
    type="aws",    # Always set to this default value
    iters=10000,     # Number of iterations
    runs=5,        # Number of runs per problem
    alpha=2.0,     # Alpha parameter
    beta=0.333,      # Beta parameter
    beta_decay=0.1,  # Beta decay rate
    noise_stdev=0.0,  # Standard deviation of noise
    runtime=0,     # Default value
    trials=1       # Number of trials
    'private_ipv4_address': 'http://172.31.12.198:5050'
    'public_ipv4_address': ''
)
print(device["id"])

result = client.execute_device_qubo_input(device["id"], Q)
print(result)
