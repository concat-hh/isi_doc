
from __future__ import print_function
from pprint import pprint
import time
import urllib3
import json
import platform
import subprocess
from datetime import datetime
from datetime import date
import isi_sdk_8_2_2
import isi_sdk_9_0_0
from airium import Airium
from isi_sdk_8_2_2.rest import ApiException
from isi_sdk_9_0_0.rest import ApiException

import os
import csv

urllib3.disable_warnings()

# enviroment variables
now = datetime.now()
today = date.today()
Cluster = '192.168.222.170'
lnn = 1 # Node LNN
zone = 'System' # str | Specifies which access zone to use. (optional)
scope = 'user'
dir = 'ASC'
sort = 'description'
limit = 10
hosts = '192.168.222.170'
google = "8.8.8.8"

# configure cluster connection: basicAuth
configuration = isi_sdk_8_2_2.Configuration()
configuration.host = 'https://192.168.222.170:8080'
configuration.username = 'root'
configuration.password = 'a'
configuration.verify_ssl = False
API_VERSION = '3'

# create an instance of the API class

# 8_2_2 instances
api_client = isi_sdk_8_2_2.ApiClient(configuration)
api_instance_protocols = isi_sdk_8_2_2.ProtocolsApi(api_client)
api_instance_node = isi_sdk_8_2_2.ClusterNodesApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_network = isi_sdk_8_2_2.NetworkApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_zones = isi_sdk_8_2_2.ZonesApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_auth_ad = isi_sdk_8_2_2.AuthApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_auth_ldap = isi_sdk_8_2_2.AuthApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_license = isi_sdk_8_2_2.LicenseApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_event = isi_sdk_8_2_2.EventApi(isi_sdk_8_2_2.ApiClient(configuration))

# 9_0_0 instances
api_instance_onefs = isi_sdk_9_0_0.ClusterApi(isi_sdk_9_0_0.ApiClient(configuration))


# +---------------------------------------+
# + All functions to get data from Isilon +
# +---------------------------------------+

# Get OneFS Version
try:
    api_response_onefsversion = api_instance_onefs.get_cluster_version()
except ApiException as e:
    print("Exception when calling ProtocolsApi->Cluster Version: %s\n" % e)
# Get Cluster Information
try:
    api_response_onefs = api_instance_onefs.get_cluster_nodes()
except ApiException as e:
    print("Exception when calling ProtocolsApi->Cluster Version: %s\n" % e)
# Get Cluster Config
try:
    api_response_clusterconfig = api_instance_onefs.get_cluster_config()
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_config: %s\n" % e)
# Get Cluster Identity
try:
     api_response_identity = api_instance_onefs.get_cluster_identity()
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_identity: %s\n" % e)





# Format output in CSV
with open('output.csv', 'w') as csvfile:
    fieldnames = ['onefsversion']
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow({'onefs_version', api_response_onefsversion.nodes[0].version})
    print("ONEFS check")
# Write if cluster is in compliance mode
    writer.writerow({'cluster_compliance_mode', api_response_clusterconfig.is_compliance})
    print("COMPLIANCE check")
# Write Cluster Name
    writer.writerow({'cluster_identity', api_response_identity.name})
    print("GET NAME check")
# Write Node Serial Number

# Write Node Count
    writer.writerow({'node_count', api_response_onefs.total})
    print("GET NODE NR check")
