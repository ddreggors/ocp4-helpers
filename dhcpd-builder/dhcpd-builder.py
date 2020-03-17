#!/usr/bin/env python3

import hcl
import json
from netaddr import IPAddress, IPNetwork
from jinja2 import Environment, FileSystemLoader
import pprint

with open('terraform.tfvars', 'r') as fp:
    vars = hcl.load(fp)

# Base Variables
types = {"master": "1", "worker": "2", "storage": "3", "infra": "4"}
cluster_nodes = {}
netprefx = "/23"
counts = {}
machine_cidr = vars["machine_cidr"]
macprefix = vars["macprefix"]
cluster_mac_id = vars["cluster_mac_id"]
domain = vars["base_domain"]
domain_name_servers = vars["domain_name_servers"]
search_domains = vars["search_domains"]
pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(vars)

# Bootstrap node
bootstrap_name = vars["bootstrap_name"]
bootstrap_ip = vars["bootstrap_ip"]
bootstrap_mac = macprefix + ":" + cluster_mac_id + ":" + "00"

# Gather base network details  from bootstrap helper
network = IPNetwork(bootstrap_ip + netprefx)

# Cluster nodes
cluster_nodes[bootstrap_name] = {"name": bootstrap_name, "typeid": "bootstrap-00", "ip": bootstrap_ip, "mac": bootstrap_mac}
for type in types:
    count_key = type + "_count"
    name_key = type + "_names"
    ip_key = type + "_ips"
    if not count_key in vars:
        continue

    count = vars[count_key]
    for i in range(count):
        host = vars[name_key][i]
        machine_cidr = vars["machine_cidr"]
        mac = macprefix + ":" + cluster_mac_id + ":" + types[type] + str(i)
        cluster_nodes[host] = {"name": host, "typeid": type + "-0" + str(i), "ip": vars[ip_key][i], "mac": mac}


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('dhcpd.j2')
routers = str(network.network + 1)
range = str(network.network + 250) + " " + str(network.network + 251)
output = template.render(nodes=cluster_nodes, network=network, routers=routers, range=range, domain=domain, search_domains=search_domains, dommain_name_servers=domain_name_servers)
print(output)
