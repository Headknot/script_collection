# -*- coding: utf-8 -*

import ipaddress
from textwrap import dedent

def create_dhcp_scopes_from_supernet(supernet: str, subnet_size: int) -> bool:
    '''Subnet a supernet into target network size and generate DHCP scopes for all of them.
    The scopes are saved into a text file.
    
    :param supernet:    ex. "10.25.0.0/16"
    :param subnet_size: ex. 29
    :rtype: bool
    '''
    supernet = ipaddress.ip_network(supernet)
    subnets = list(supernet.subnets(new_prefix=subnet_size))
    
    with open('dhcp_scopes.txt', 'a') as f:
        for network in subnets:
            hosts = list(network.hosts())
            
            f.write(dedent(f'''
            subnet {network} netmask {network.netmask} {{
            option routers {hosts[0]};
            option domain-name-servers 8.8.8.8, 8.8.4.4;
            option broadcast-address {network.broadcast_address};
            pool {{
                failover peer "failover-partner";
                range {hosts[1]} {hosts[-1]};
            }}
            }}'''))
        
    return True
    
def create_dhcp_scope(network_address: str) -> bool:
    '''Create a DHCP scope to match target network.
    The scope is printed out to terminal.
    
    :param network_address:     ex. '192.168.1.0/24'
    :rtype: bool
    '''
    
    network = ipaddress.ip_network(network_address)
    hosts = list(network.hosts())
    
    template = f'''
    subnet {network} netmask {network.netmask} {{
    option routers {hosts[0]};
    option domain-name-servers 8.8.8.8, 8.8.4.4;
    option broadcast-address {network.broadcast_address};
    pool {{
        failover peer "failover-partner";
        range {hosts[1]} {hosts[-1]};
    }}
    }}'''
    
    print(dedent(template))
        
    return True

if __name__ == '__main__':
    create_dhcp_scopes_from_supernet('10.32.0.0/16', 27)
    #create_dhcp_scope('192.168.1.0/24')
    print('Finished!')
