import yaml
import logging
from netmiko import Netmiko

# Setup Logger
logging.basicConfig(
    filename='lab_exercise.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load hosts
hosts = yaml.load(open('lab_hosts.yml'), Loader=yaml.SafeLoader)

for host in hosts["hosts"]:
    try:
        print("="*60)
        print(f"Routing Table for {host['name']} ({host['hostname']})")
        print("="*60)

        net_connect = Netmiko(
    host=host["name"],
    username=host["username"],
    password=host["password"],
    port=host["port"],
    device_type=host["type"]
)

        logger.info(f"Connected to {host['name']} for routing table")

        output = net_connect.send_command("show ip route", use_textfsm=True)
        net_connect.disconnect()

        if isinstance(output, list):
            for route in output:
                print(f"Protocol: {route['protocol']} | Network: {route['network']}/{route['prefix_length']} | Distance: {route['distance']} | Metric: {route['metric']} | Next Hop: {route['nexthop_ip']} | Interface: {route['nexthop_if']}")
            logger.info(f"Routing table collected from {host['name']} successfully")
        else:
            print("No routes found or TextFSM parsing failed")
            logger.warning(f"No routes found on {host['name']}")

        print("-"*60)

    except Exception as e:
        logger.error(f"Error on {host['name']}: {str(e)}")
        print(f"ERROR on {host['name']}: {str(e)}")

print("="*60)
print("Done! Check lab_exercise.log for details")
