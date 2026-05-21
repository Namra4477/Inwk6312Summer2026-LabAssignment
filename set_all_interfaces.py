import logging
import requests
from requests.auth import HTTPBasicAuth
import json
import yaml

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

USER = 'student'
PASS = 'Meilab123'

def set_interface(host, interface_name, ip, netmask):
    BASE_URL = 'http://{0}/restconf/api/running/'.format(host)
    url = BASE_URL + "interfaces/interface/" + interface_name
    auth = HTTPBasicAuth(USER, PASS)
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }
    data = {
        "ietf-interfaces:interface": {
            "name": interface_name,
            "description": "Changed through Restconf",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": 'true',
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": ip,
                        "netmask": netmask
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }
    response = requests.put(url, auth=auth, headers=headers, data=json.dumps(data))
    if response.status_code == 204:
        logging.info(f"Successfully configured {interface_name} on {host}")
        return "success!"
    else:
        logging.error(f"Error on {host} - {interface_name}, Code: {response.status_code}")
        return response.text

# Load YAML file
with open('routers.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Loop through routers and set interfaces
for router in config['routers']:
    host = router['management_ip']
    print(f"\nConfiguring router {router['name']} ({host})")
    for interface in router['interfaces']:
        result = set_interface(
            host,
            interface['name'],
            interface['ip'],
            interface['netmask']
        )
        print(f"{interface['name']}: {result}")
