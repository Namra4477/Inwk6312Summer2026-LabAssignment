from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "secret": "cisco", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "secret": "cisco", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "secret": "cisco", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "secret": "cisco", "port": "22"},
]

for device in devices:
    net_connect = Netmiko(**device)
    print(f"Default prompt: {net_connect.find_prompt()}")
    net_connect.send_command_timing("disable")
    print(f"Disable command: {net_connect.find_prompt()}")
    net_connect.enable()
    print(f"Enable command: {net_connect.find_prompt()}")
    net_connect.disconnect()
    print("-"*50)
