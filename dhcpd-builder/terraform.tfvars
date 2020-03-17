



// The machine_cidr where IP addresses will be assigned for cluster nodes.
// Additionally, IPAM will assign IPs based on the network ID.
machine_cidr = "10.111.111.0/23"




// DNS

// Base domain from which the cluster domain is a subdomain.
base_domain = "mydomain.com"

domain_name_servers = ["10.111.111.254", "10.111.111.253"]
search_domains = ["domain1", "domain2", "domain3"]

// The number of control plane VMs to create. Default is 3.


// The number of compute VMs to create. Default is 3.


// The number of storage VMs to create. Default is 3.




// NODE INFO

// Bootstrap
bootstrap_name = "ocp4-60.mydomain.com"
bootstrap_ip = "10.111.111.15"

// Master nodes
master_count = 3
master_names = ["master-00.mydomain.com", "master-01.mydomain.com", "master-02.mydomain.com"]
master_ips = ["10.111.111.20", "10.111.111.21", "10.111.111.22"]

// Infra nodes
infra_count = 3
infra_names = ["infra-00.mydomain.com","infra-01.mydomain.com","infra-02.mydomain.com"]
infra_ips = ["10.111.111.23","10.111.111.24","10.111.111.25"]


// Worker nodes
worker_count = 6
worker_names = ["worker-00.mydomain.com", "worker-01.mydomain.com", "worker-02.mydomain.com","worker-03.mydomain.com","worker-04.mydomain.com","worker-05.mydomain.com"]
worker_ips = ["10.111.111.26","10.111.111.27","10.111.111.28","10.111.111.29","10.111.111.30","10.111.111.31"]

// Storage nodes
storage_count = 3
storage_names = ["ocp4-64.mydomain.com", "ocp4-65.mydomain.com", "ocp4-66.mydomain.com"]
storage_ips = ["10.111.111.23;", "10.111.111.24;", "10.111.111.25;"]
