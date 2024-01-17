#! /usr/bin/env python3

"""
Current CSE console provides a list of endpoints with installed agents with pretty limited capabilities. 
This script will return the list of all computers from SE console, with a series of choices:
Sort: alphabetically or by last time seen
Filter: Group
More Filter: Time range : Last seen, starting from 2 hours.
Fields shown: Computer Name, Orbital Status, Last Seen, with the ability to add own fields (just leave commend and some notice how to get the field from json value and add it)
"""
import requests
from requests.auth import HTTPBasicAuth
import sys
import argparse


# adds /home to the path to import environment module
sys.path.insert(0, '/home')

# import API key module
import environment as env

# Setting API keys as constant variables:

# Cisco Secure Endpoint
cse_client_id = env.SECURE_ENDPOINT_CLIENT_ID
cse_api_key = env.SECURE_ENDPOINT_API_KEY
cse_host = env.SECURE_ENDPOINT_URL

# Functions

def get_cse_computers(
    group_guid,
    host=cse_host,
    client_id=cse_client_id,
    api_key=cse_api_key,
):
    """Get a list of computers from  Cisco Secure Endpoint."""
    print("\n==> Getting computer list from Cisco Secure Endpoint")
    
    auth=HTTPBasicAuth(client_id, api_key)

    # Construct the URL
    url = f"https://{host}/v1/computers"

    query_params = {
        "group_guid": group_guid
    }

    response = requests.get(url, auth=auth, params=query_params)
    
    # Consider any status other than 2xx an error
    response.raise_for_status()

    computer_list = response.json()["data"]
    
    return computer_list

def get_cse_groups(
    host=cse_host,
    client_id=cse_client_id,
    api_key=cse_api_key
):
    """Get a list of groups from  Cisco Secure Endpoint."""
    print("\n==> Getting groups list from Cisco Secure Endpoint")
    
    auth=HTTPBasicAuth(client_id, api_key)

    # Construct the URL
    url = f"https://{host}/v1/groups"

    response = requests.get(url, auth=auth)
    
    # Consider any status other than 2xx an error
    response.raise_for_status()

    groups_list = response.json()["data"]
    
    return groups_list


# If this script is the "main" script, run...
if __name__ == "__main__":
    
    # Parse program arguments

    parser = argparse.ArgumentParser(description="This script will return the list of all computers from SE console, with a series of choices.")
    parser.add_argument("--get_groups", help="Print out group names to use in --group argument",action='store_true',required=False)
    parser.add_argument("--group", help="Display all computers belonging to the group. Usage: --group='GROUP NAME'",required=False)
    parser.add_argument("--sort", help="Sort alphabetically or by last time seen. Usage: --sort='abc' or  --sort='last_seen'",required=False)

    args = parser.parse_args()

    if args.get_groups:
        groups = get_cse_groups()
        print([g['name'] for g in groups])

    if args.group:
        groups = get_cse_groups()
        #list comprehension example ref https://note.nkmk.me/en/python-dict-list-values/
        guid = [g.get('guid') for g in groups if g.get('name')==args.group]
    
    computers = get_cse_computers(group_guid=guid)
    
    if args.sort=='abc':
        computers = sorted(computers, key=lambda d: d['hostname'])
    
    if args.sort=='last_seen':
        computers = sorted(computers, key=lambda d: d['last_seen'])

    print('{0:20}  {1:35}  {2:10}'.format('Computer Hostname','Connector GUID','Orbital Status')) 

    [print(f'{comp["hostname"]:20}  {comp["connector_guid"]:30}  {comp["orbital"]["status"]:10}') for comp in computers]
