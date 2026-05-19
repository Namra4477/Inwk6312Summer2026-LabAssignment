import yaml
import logging
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

# Setup Logger
logging.basicConfig(
    filename='lab_exercise.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load hosts from YAML
hosts = yaml.load(open('lab_hosts.yml'), Loader=yaml.SafeLoader)

# Setup Jinja2
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, autoescape=False)
template = env.get_template('lab_interfaces.j2')

# Push config to each device
for host in hosts["hosts"]:
    try:
        # Render config for this host
        config = template.render(host=host)

        print("="*60)
        print(f"Connecting to {host['name']} ({host['hostname']})")
        print("="*60)
        print("Config to be pushed:")
        print(config)
        print("-"*60)

        # Connect via Netmiko
        net_connect = Netmiko(
            host=host["name"],
            username=host["username"],
            password=host["password"],
            port=host["port"],
            device_type=host["type"]
        )

        logger.info(f"Successfully connected to {host['name']}")
        print(f"Logged into {host['name']} successfully")

        # Push config
        output = net_connect.send_config_set(config.split("\n"))
        print(f"Config pushed to {host['name']} successfully")
        print(output)
        logger.info(f"Config pushed to {host['name']} successfully")

        net_connect.disconnect()
        logger.info(f"Disconnected from {host['name']}")

    except Exception as e:
        logger.error(f"Error connecting to {host['name']}: {str(e)}")
        print(f"ERROR on {host['name']}: {str(e)}")

print("="*60)
print("All devices configured successfully!")
print("Check lab_exercise.log for details")
