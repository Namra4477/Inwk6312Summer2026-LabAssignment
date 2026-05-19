from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": "22"},
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show ip interface brief", use_textfsm=True)
    net_connect.disconnect()
    print("="*60)
    print(f"Device: {device['ip']}")
    print("="*60)
    for interface in output:
        print(f"Interface: {interface['interface']} | IP: {interface['ip_address']} | Status: {interface['status']} | Protocol: {interface['proto']}")
