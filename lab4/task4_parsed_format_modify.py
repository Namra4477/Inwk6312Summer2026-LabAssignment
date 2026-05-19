from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": "22"},
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show ip route", use_textfsm=True)
    net_connect.disconnect()
    print("="*60)
    print(f"Device: {device['ip']}")
    print("="*60)
    if isinstance(output, list):
        for route in output:
            print(f"Protocol: {route['protocol']} | Network: {route['network']} | Distance: {route['distance']} | Metric: {route['metric']}")
    else:
        print("No routes found")
    print("-"*50)
