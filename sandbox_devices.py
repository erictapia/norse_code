from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.data import load_yaml

def show_inventory(task):
    task.run(netmiko_send_command, command_string="show inventory", use_textfsm=True)

def get_serial_number(platform, data):
    # Generic function to build the real function name from the platform
    function = globals().get(f'get_{platform}_serial_number')

    if not function:
        raise NotImplementedError(f'Function get_{platform}_serial_number is not implemented.')
    
    return function(data)

def get_cisco_ios_serial_number(data):
    # Cisco IOS specific function to get the serial number from data created by the textfsm structure
    serial_number = None

    for inv in data:
        if inv['name'] in ['Chassis', 'Rack 0']:
            serial_number = inv['sn']

    return serial_number

def get_cisco_nxos_serial_number(data):
    # Cisco NXOS specific function to get the serial number from data created by the textfsm structure
    serial_number = None

    for inv in data:
        if inv['name'] == 'Chassis':
            serial_number = inv['sn']

    return serial_number

if __name__ == '__main__':
    nr = InitNornir(config_file='config.yaml')

    result = nr.run(task=show_inventory)

    #print_result(result)

    # Nornir results: Dict.List.List[dict, dict, ...]
    # when using netmiko and textfsm

    for host in result.keys():
        if not result[host][1].failed:
            serial_number = get_serial_number(nr.inventory.hosts[host].platform, result[host][1].result)
            
            print('='*79)
            print(f'{host}')
            print('='*79)
            print(f'\thostname: {nr.inventory.hosts[host].hostname}')
            print(f'\tserial number: {serial_number}')
            print()
        else:
            print('='*79)
            print(f'{host}')
            print('='*79)
            print(f'\thostname: {nr.inventory.hosts[host].hostname}')
            print('\tconnection: failed')
            print()
