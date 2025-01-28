class User:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
        self.devices = []

    def add_devices(self, device):
        self.devices.append(device)

class Device:
    def __init__(self, mac, user, name):
        self.mac = mac
        self.user = user
        self.name = name
        self.list_port = []
    
    def add_port(self, port_number, port_type):
        port = Port(port_number, port_type, self):
        self.list_port.append(port)

class Port:
    def __init__(self, port_number, port_type, device):
        self.port_number = port_number
        self.port_type = type
        self.device = device

class Data:
    def __init__(self, time_stamp, value, std, port):
        self.time_stamp = time_stamp
        self.value = value
        self.std = std
        self.port = port

class UserPortView:
    def __init__(self, user, port, custom_name):
        self.user = user
        self.port = port
        self.custom_name = custom_name




    


