from netmiko import ConnectHandler

r1 = {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"}
r2 = {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"}
r3 = {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"}
r4 = {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": "22"}

for device in (r1, r2, r3, r4):
    net_connect = ConnectHandler(**device)
    print("="*60)
    print(f"Device: {device['ip']}")
    print("="*60)

    # Show interface description
    output1 = net_connect.send_command("show interface description")
    print("--- Interface Description ---")
    print(output1)

    # Show IP interface brief
    output2 = net_connect.send_command("show ip interface brief")
    print("--- IP Interface Brief ---")
    print(output2)

    # Show version
    output3 = net_connect.send_command("show version")
    print("--- Version ---")
    print(output3)

    net_connect.disconnect()
