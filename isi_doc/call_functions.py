
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

import requests
from requests.auth import HTTPBasicAuth
import pprint

import os
import csv

urllib3.disable_warnings()

# +---------------------------------------+
# + Authentication Data                   +
# +---------------------------------------+

# configure cluster connection: basicAuth
configuration = isi_sdk_8_2_2.Configuration()
configuration.host = 'https://192.168.222.170:8080'
configuration.username = 'root'
configuration.password = 'a'
configuration.verify_ssl = False
API_VERSION = '3'

# +---------------------------------------+
# + Standard REST Functions               +
# +---------------------------------------+

# GET
def send_get_request(url_string, user, passwd):
    """
    Creates a HTTP GET request
    :param url_string: full URL of PAPI attribute
    :param user: username of user with PAPI rights. Normally root
    :param passwd: password of user specified in user param
    :return: The data returned from cluster
    """
    # print 'URLstring: ' + url_string + '\n'
    try:
        returned_data_from_get_request = requests.get(url_string, auth=HTTPBasicAuth(user, passwd), verify=False)
    except requests.Timeout as e:
        print('Fehler(send_get_request) Timeout')
        print(e)
    except requests.HTTPError as e:
        print('Fehler(send_get_request) HTTPError')
        print(e)
    except requests.ConnectionError as e:
        print('Fehler(send_get_request) Connection Error')
        print(e)
    return returned_data_from_get_request

# POST
def send_post_request(url_string, user, passwd, data):
    """
    Creates a HTTP POST request
     :param url_string: full URL of PAPI attribute
     :param user: username of user with PAPI rights. Normally root
     :param passwd: password of user specified in user param
     :return: The data returned from cluster
     :param data: Data to post in Python format, will be converted to JSON
     :return: The HTTP code of the operation
    """

    header_json = {'content-type': 'application/json'}
    try:
        returncode_from_post_request = requests.post(url_string, auth=HTTPBasicAuth(user, passwd), verify=False,
                                                     data=json.dumps(data),
                                                     headers=header_json)
    except requests.Timeout as e:
        print('Fehler(send_post_request) Timeout')
        print(e)
    except requests.HTTPError as e:
        print('Fehler(send_post_request) HTTPError')
        print(e)
    except requests.ConnectionError as e:
        print('Fehler(send_post_request) Connection Error')
        print(e)
    return returncode_from_post_request

# PUT
def send_put_request(url_string, user, passwd, data):
    """
    Creates a HTTP PUT request
    :param url_string: full URL of PAPI attribute
    :param user: username of user with PAPI rights. Normally root
    :param passwd: password of user specified in user param
    :return: The data returned from cluster
    :param data: Data to post in Python format, will be converted to JSON
    :return: The HTTP code of the operation
   """
    try:
        returncode_from_post_request = requests.put(url_string, auth=HTTPBasicAuth(user, passwd), verify=False,
                                                    data=json.dumps(data))
    except requests.Timeout as e:
        print('Fehler(send_put_request) Timeout')
        print(e)
    except requests.HTTPError as e:
        print('Fehler(send_put_request) HTTPError')
        print(e)
    except requests.ConnectionError as e:
        print('Fehler(send_put_request) Connection Error')
        print(e)
    return returncode_from_post_request

# DELETE
def send_delete_request(url_string, user, passwd):
    """
    Creates a HTTP DELETE request
    :param url_string: full URL of PAPI attribute
    :param user: username of user with PAPI rights. Normally root
    :param passwd: password of user specified in user param
    :return: The data returned from cluster
    """
    header_json = {'content-type': 'application/json'}
    try:
        returncode_from_delete_request = requests.delete(url_string, auth=HTTPBasicAuth(user, passwd), verify=False,
                                                         headers=header_json)
    except requests.Timeout as e:
        print('Fehler(send_delete_request) Timeout')
        print(e)
    except requests.HTTPError as e:
        print('Fehler(send_delete_request) HTTPError')
        print(e)
    except requests.ConnectionError as e:
        print('Fehler(send_delete_request) Connection Error')
        print(e)
    return returncode_from_delete_request

# +---------------------------------------+
# + Instance Creation                     +
# +---------------------------------------+

# 8_2_2 instances
api_client = isi_sdk_8_2_2.ApiClient(configuration)
api_instance_protocols = isi_sdk_8_2_2.ProtocolsApi(api_client)
api_instance_node = isi_sdk_8_2_2.ClusterNodesApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_network = isi_sdk_8_2_2.NetworkApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_zones = isi_sdk_8_2_2.ZonesApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_auth_ad = isi_sdk_8_2_2.AuthApi(isi_sdk_8_2_2.ApiClient(configuration))# gleiche instance wie dadrunter
api_instance_auth_ldap = isi_sdk_8_2_2.AuthApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_license = isi_sdk_8_2_2.LicenseApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_event = isi_sdk_8_2_2.EventApi(isi_sdk_8_2_2.ApiClient(configuration))
api_instance_groupnet_sum = isi_sdk_8_2_2.GroupnetsSummaryApi(isi_sdk_8_2_2.ApiClient(configuration)) #new
api_instance_groupnet_net = isi_sdk_8_2_2.NetworkGroupnetsApi(isi_sdk_8_2_2.ApiClient(configuration)) #new
api_instance_job = isi_sdk_8_2_2.JobApi(isi_sdk_8_2_2.ApiClient(configuration))                       #new
api_instance_sync = isi_sdk_8_2_2.SyncApi(isi_sdk_8_2_2.ApiClient(configuration))                     #new
api_instance_snapshot = isi_sdk_8_2_2.SnapshotApi(isi_sdk_8_2_2.ApiClient(configuration))             #new
api_instance_quotas = isi_sdk_8_2_2.QuotaApi(isi_sdk_8_2_2.ApiClient(configuration))                  #new
api_instance_storagepool = isi_sdk_8_2_2.StoragepoolApi(isi_sdk_8_2_2.ApiClient(configuration))       #new
api_instance_cluster = isi_sdk_8_2_2.ClusterApi(isi_sdk_8_2_2.ApiClient(configuration))               #new
api_instance_protocols2 = isi_sdk_8_2_2.ProtocolsApi(isi_sdk_8_2_2.ApiClient(configuration))          #new
api_instance_snap = isi_sdk_8_2_2.SnapshotApi(isi_sdk_8_2_2.ApiClient(configuration))

# 9_0_0 instances
api_instance_onefs = isi_sdk_9_0_0.ClusterApi(isi_sdk_9_0_0.ApiClient(configuration))
api_instance_network_9_0_0 = isi_sdk_9_0_0.NetworkApi(isi_sdk_9_0_0.ApiClient(configuration))         #new
api_instance_clusternode = isi_sdk_9_0_0.ClusterNodesApi(isi_sdk_9_0_0.ApiClient(configuration))      #new
api_instance_hardware = isi_sdk_9_0_0.HardwareApi(isi_sdk_9_0_0.ApiClient(configuration))             #new
api_instance_remote = isi_sdk_9_0_0.RemotesupportApi(isi_sdk_9_0_0.ApiClient(configuration))          #new

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

#Get Software License                                                                      #new
try:
    api_response_license = api_instance_license.list_license_licenses()
except ApiException as e:
    print("Exception when calling LicenseApi->list_license_licenses: %s\n" % e)

#Get Groupnet Summary                                                                      #new
try:
    api_response_groupnet_sum = api_instance_groupnet_sum.get_groupnets_summary()
except ApiException as e:
    print("Exception when calling GroupnetsSummaryApi->get_groupnets_summary: %s\n" % e)

#Get Groupnet Networks                                                                     #new bei error api_instance_network_9_0_0 versuchen
try:
    api_response_groupnet_net = api_instance_network.list_network_groupnets()
except ApiException as e:
    print("Exception when calling NetworkApi->list_network_groupnets: %s\n" % e)

#Get NTP Server                                                                            #new
try:
    api_response_ntp = api_instance_protocols2.list_ntp_servers()
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_ntp_servers: %s\n" % e)

#Get SNMP Settings                                                                         #new
try:
    api_response_snmp = api_instance_protocols2.get_snmp_settings()
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_snmp_settings: %s\n" % e)

#Get Subnet Information                                                                    #new bei error api_instance_network_9_0_0 versuchen
try:
    api_response_subnet = api_instance_network.get_network_subnets()
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_subnets: %s\n" % e)
#Get IP Pools Interfaces                                                                   #new bei error api_instance_network_9_0_0 versuchen
try:
    api_response_net_interface = api_instance_network.get_network_interfaces()
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_interfaces: %s\n" % e)

#Get IP Pool Information                                                                   #new bei error api_instance_network_9_0_0 versuchen
try:
    api_response_network = api_instance_network.get_network_pools()
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_pools: %s\n" % e)

#Get Authentication Provider                                                               #new
try:
    api_response_auth_ad = api_instance_auth_ad.list_providers_ads()
except ApiException as e:
    print("Exception when calling AuthApi->list_providers_ads: %s\n" % e)

#Get Access Zones                                                                          #new
try:
    api_response_zones = api_instance_zones.list_zones()
except ApiException as e:
    print("Exception when calling ZonesApi->list_zones: %s\n" % e)

#Get Role Based Access                                                                     #new
try:
    api_response_rolelist = api_instance_auth_ad.list_auth_roles()
except ApiException as e:
    print("Exception when calling AuthApi->list_auth_roles: %s\n" % e)

#Get Job Statistic                                                                         #new
try:
    api_response_job = api_instance_job.get_job_statistics()
except ApiException as e:
    print("Exception when calling JobApi->get_job_statistics: %s\n" % e)

#Get Job jobs                                                                              #new
try:
    api_response_joblist = api_instance_job.list_job_jobs()
except ApiException as e:
    print("Exception when calling JobApi->list_job_jobs: %s\n" % e)

#Get SyncIQ Settings                                                                       #new
try:
    api_response_syncIQ = api_instance_sync.list_sync_policies()
except ApiException as e:
    print("Exception when calling SyncApi->list_sync_policies: %s\n" % e)

#Get Snapshot Settings                                                                     #new
try:
    api_response_snapset = api_instance_snap.get_snapshot_settings()
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_settings: %s\n" % e)

#Get Snapshot Schedule                                                                     #new
try:
    api_response_snapschedule = api_instance_snap.list_snapshot_schedules()
except ApiException as e:
    print("Exception when calling SnapshotApi->list_snapshot_schedules: %s\n" % e)

#Get SmartQuotas                                                                           #new
try:
    api_response_quotas = api_instance_quotas.list_quota_quotas()
except ApiException as e:
    print("Exception when calling QuotaApi->list_quota_quotas: %s\n" % e)

#Get Node Pool                                                                             #new
try:
    api_response_nodepool = api_instance_storagepool.list_storagepool_nodepools()
except ApiException as e:
    print("Exception when calling StoragepoolApi->list_storagepool_nodepools: %s\n" % e)

#Get NDMP                                                                                  #new
try:
    api_response_ndmp = api_instance_protocols.get_ndmp_settings_global()
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_settings_global: %s\n" % e)

#Get SMB Share                                                                             #new
try:
    api_response_smb = api_instance_protocols.list_smb_shares()
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_smb_shares: %s\n" % e)

#Get NFS Export                                                                            #new
try:
    api_response_nfs = api_instance_protocols.list_nfs_exports()
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)

#Get SMTP Server                                                                          #new
try:
    api_response_smtp = api_instance_cluster.get_cluster_email()
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_email: %s\n" % e)

#Get SRS

# +---------------------------------------+
# + Format output in CSV                  +
# +---------------------------------------+

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# 1) Write OneFS Version
    writer.writerow({'onefs_version', api_response_onefsversion.nodes[0].version})
    print("ONEFS check")
# 2) Write if cluster is in compliance mode
    writer.writerow({'cluster_compliance_mode', api_response_clusterconfig.is_compliance})
    print("COMPLIANCE check")
# 3) Write Date
    writer.writerow({'date', date.today()})
# 4) Write Cluster Name
    writer.writerow({'cluster_identity', api_response_identity.name})
    print("GET NAME check")
# 5) Write Node-Count
    writer.writerow({'node-count', api_response_onefs.total})
    print("GET NODE NR check")
# 6) Write Node-Types
    writer.writerow({'node-types', api_response_onefs.nodes[0].hardware.family_code})
    print("GET NODE SERIES check")


# 6) Write Node Serial Number
# iteration over nodes to get serial numbers
    serial_numbers = []
    for i in range(api_response_onefs.total):
        serial_numbers.append(api_response_onefs.nodes[i].hardware.serial_number)
# append list elements to single string
    str_serial_numbers = ', '.join(serial_numbers)
    writer.writerow({'Serial Numbers', str_serial_numbers})
    print("SERIAL NUMBER Check")
# 7) Write Backend Switch Information

# 8) Write Software License Information
# iteration over license-list to get all license elements
    licenses = []
    for i in range(api_response_license.total):
        licenses.append(api_response_license.licenses[i].name)
# append list elements to single string
    str_licenses = ', '.join(licenses)
    writer.writerow({'Licenses', str_licenses})
    print("LICENSES Check")
# 9) Write Groupnet Information
    groupnets = []
    for i in range(api_response_groupnet_sum.summary.count):
        groupnets.append(api_response_groupnet_sum.summary.list[i].name)
    str_groupnets = ', '.join(groupnets)
    writer.writerow({'Groupnets', str_groupnets})
    print("Groupnets Check")
