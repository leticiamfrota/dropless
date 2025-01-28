class User:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
        
class Device:
    def __init__(self, mac, user, name):
        self.mac = mac
        self.user = user
        self.name = name
        self.list_port = []

class Port:
    def __init__(self, port_number, port_type, device):
        self.port_number = port_number
        self.port_type = type
        self.device = device

class DataPort:
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
        
class UserPortGroup:
    def __init__(self, port_group, user):
        self.port_group = port_group
        self.user = user
        



    


