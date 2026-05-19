from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": "22"},
]

loopback_config = [
    "interface Loopback0",
    "description Loopback added by Netmiko",
    "ip address 1.1.1.1 255.255.255.255",
    "no shutdown"
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(loopback_config)
    print("="*60)
    print(f"Device: {device['ip']}")
    print("="*60)
    print(output)
    net_connect.disconnect()
