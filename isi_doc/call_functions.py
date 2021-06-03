
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

# +---------------------------------------+
# + Format output in CSV                  +
# +---------------------------------------+

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# Write OneFS Version
    writer.writerow({'onefs_version', api_response_onefsversion.nodes[0].version})
    print("ONEFS check")
# Write if cluster is in compliance mode
    writer.writerow({'cluster_compliance_mode', api_response_clusterconfig.is_compliance})
    print("COMPLIANCE check")
# Write Cluster Name
    writer.writerow({'cluster_identity', api_response_identity.name})
    print("GET NAME check")
# Write Node Serial Number
    # json_data = json.loads(api_response_onefs.nodes)
    # #print(json_data.get('hardware'))
    # writer.writerow({'Serial Number', ''.join(map(str, api_response_onefs.nodes))})
    # print("SERIAL NUMBER Check")'
# Write Node Count
    writer.writerow({'node_count', api_response_onefs.total})
    print("GET NODE NR check")
