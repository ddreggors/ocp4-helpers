# DHCP Builder
A script to read a terraform.tfvars file and build a generic dhcpd.conf file for cluster install on VMWare vSphere hosts.



## Pre-requisites

* A set of variables in tfvars identifying required data for script
  * machine cidr
  * bootstrap ip and name
    * `bootstrap_name = "bootstrap-0"`
    * `bootstrap_ip = "10.111.111.100"`
  * A mac vendor id prefix and a separate cluster id
  * nodes names (list of node names named with a `_names` suffix)
    * `master_names = ["master-0", "master-1", "master-2"]`
    * `infra_names = ["infra-0", "infra-1", "infra-2"]`
    * `worker_names = ["worker-0", "worker-1", "worker-2"]`
    * `storage_names = ["storage-0", "storage-1", "storage-2"]`
  * node ips
    * `master_ips = ["10.111.111.101", "10.111.111.102", "10.111.111.103"]`
    * `infra_ips = ["10.111.111.111", "10.111.111.112", "10.111.111.113"]`
    * `compute_ips = ["10.111.111.121", "10.111.111.122", "10.111.111.123"]`
  * node count
    * `master_count = 3`
    * `infra_count = 3`
    * `compute_count = 3`
  * domain_name
    * `domain_name = `
  * search_domains
    * `search_domains = ["search_domain1", "search_domain2", "search_domain3"]`
  * dommain_name_servers
    * `dommain_name_servers = ["10.111.111.254", "10.111.111.253"]`

These variables are read in and used to build the subnet block network and netmask, the pool range, the static ip block hosts/ip/mac addresses, and the `option routers` line.

## The idea
Build a dhcp config file from your terraform config for cluster install. This should help minimize copy/paste errors and reduce human error until CoreOS images can be built with vSphere agent to allow for static ips to be assigned using native terraform ipv4 directives before bootstrap.
