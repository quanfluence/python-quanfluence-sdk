# python-quanfluence-sdk
Quanfluence Developer Kit for Python

<div>
🚀 <a href="#getting-started">Getting started</a> - 💻 <a href="#api-reference">API reference</a> - 📚 <a href="#examples">Examples</a> - 💬 <a href="#feedback">Feedback</a>
</div>


Learn how to solve complex problems with Quanfluence using Python.

## Getting started
### Installation
You can install the Quanfluence Python SDK using the following command.
```
pip install quanfluence-sdk
```

> Requires Python 3.0 or higher.

# Usage
## Initialize QuanfluenceClient

Once the package is installed, you can import the library using import or require approach.

```python
from quanfluence_sdk import QuanfluenceClient

client = QuanfluenceClient()

```

## Perform Authentication

Quanfluence APIs are access contolled, you need valid user crendentials to invoke any module methods. Use below method for authentication.

```python
try:
    login = client.signin(USERNAME, PASSWORD)
except Error:
    print(Error)
```
> You can use valid quanfluence client's USERNAME & PASSWORD

## API references
Quanfluence comprises various ising devices to execute complex problems. Use below methods to interact with Quanfluence APIs.

### Device Management
#### Create a Device
```python
from quanfluence_sdk import QuanfluenceClient

device = Device(...)
response = client.create_device(device)
```
> Use Device model with required attributes

#### Update a Device
```python
from quanfluence_sdk import QuanfluenceClient

device = Device(...)
response = client.update_device(device)
```
> Use Form model with id or uuid & other required attributes

#### Get a Device
```python
from quanfluence_sdk import QuanfluenceClient

response: Device = QuanfluenceClient.get(ID)
```
> ID is unique device identifier

#### Upload a Qubo file to Device
```python
from quanfluence_sdk import QuanfluenceClient

response = QuanfluenceClient.upload_device_qubo(ID, FILE_PATH)
```
> ID is unique device identifier
> FILE_PATH is qubo file path


### Device Execution
#### Execute Device with QUBO as input
```python
from quanfluence_sdk import QuanfluenceClient

Q = {(0, 0): 1, (0,1): -1, (1,1): 2}
response = client.execute_device_qubo_input(ID, Q)
```
> ID is unique device identifier

#### Execute Device with QUBO as file
```python
from quanfluence_sdk import QuanfluenceClient

response = client.execute_device_qubo_file(ID, FILE_NAME)
```
> ID is unique submission identifier
> FILE_NAME is unique file identifier created using Upload a Qubo file to Device


## Examples
- [Examples](https://github.com/quanfluence/python-quanfluence-sdk/blob/main/EXAMPLES.md) - explore our examples docs and learn more about using sdk.


### Feedback

---

If you get stuck, we’re here to help. The following are the best ways to get assistance working through your issue:

Use our [GitHub Issue Tracker][gh-issues] for reporting bugs or requesting features.
Visit the [Quanfluence Community][quanfluence-community] for getting help using Quanfluence Developer Kit for Python or just generally bond with your fellow Quanfluence developers.

<!-- Markdown links -->