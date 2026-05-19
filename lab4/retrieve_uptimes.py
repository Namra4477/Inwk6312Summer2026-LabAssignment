from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": "22"},
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show version")
    net_connect.disconnect()

    # Uptime
    result = output.find('uptime is')
    begin = int(result)
    end = begin + 38
    print(device['ip'] + " => " + output[begin:end])

    # Config Register
    reg_result = output.find('Configuration register is')
    if reg_result != -1:
        print(device['ip'] + " => " + output[reg_result:reg_result+35])
    print("-"*50)
