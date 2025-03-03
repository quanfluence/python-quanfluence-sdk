# Contains python code to sample a BQM on the Ising machine by using dimod to convert it into a QUBO and prints the result

import sys
import dimod
from quanfluence_sdk import QuanfluenceClient

# ******* Signing in *************

client = QuanfluenceClient()
client.signin(Username, Password)   #Update your username and password here


# ********** INSERT CODE FOR CREATING YOUR QUBO FROM HERE **************
# ***** An example QUBO is inlcuded in the following code remove if required

Q = {(0, 0): 1, (0,1): -1, (1,1): 2}

bqm=dimod.BinaryQuadraticModel.from_qubo(Q)


# ****** End of user code **********

# Converting QUBO to dictionary format

Q_tuple = bqm.to_qubo()

QUBO64 = Q_tuple[0]

# Converting QUBO values from Float 64 to Float

def convert_dict_values_to_float(input_dict): 
 return {key: float(value) for key, value in input_dict.items()}
QUBO = convert_dict_values_to_float(QUBO64)

# Sending QUBO in Dictionary format to Quanfluence Ising Machine 

result = client.execute_device_qubo_input(device_id, QUBO) # Update your device id here
print(result)
