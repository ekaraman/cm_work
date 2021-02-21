#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 08:17:23 2021

@author: derin
"""

import requests
from packaging import version
import package

USERNAME = 'admin'
PASSWORD = '010817'
NEXUS_BASE_URL = 'http://localhost:8081/service/rest/v1'

def get_components_response(params):
    return requests.get(f'{NEXUS_BASE_URL}/components', auth=(USERNAME, PASSWORD), params=params).json()

def delete_component(component):
    response = requests.delete(f'{NEXUS_BASE_URL}/components/{component["id"]}', auth=(USERNAME, PASSWORD))
    response.raise_for_status() # or print(response.status_code)

# Get all components of a project
def get_components(repository):    
    response = get_components_response({'repository': repository})
    components = response['items']

    while response['continuationToken']:
        response = get_components_response({'repository': repository, 'continuationToken': response['continuationToken']})
        components.extend(response['items'])

    return components

#Get nexus configuration
def get_nexus_conf(project, platform, cms_version, pkg_dict):
    components = get_components(project)
    path = platform + "/" + cms_version
    length = len(components)
    for i in range(length):
        # Get only requested platform and cms version configuration. 
        # Nexus project repo contains packagaes for all platforms and all cms versions. 
        if path in components[i]['assets'][0]['path']:
            # Check if pkg in dictionary (scm db configuration).
            # If pkg exists:
            if components[i]['name'] in pkg_dict:
                dict_nexus_version = pkg_dict[components[i]['name']].nexus_version
                nexus_version = components[i]['version']
                # If pkg exists in dictionary and nexus_version equals None, set nexus_version.
                if dict_nexus_version is None:
                    pkg_dict[components[i]['name']].nexus_version = nexus_version
                #   If pkg exists in dictionary and nexus_version is not None, compare dictionary
                # nexus version and component nexus version to find which one is the biggest.
                else:
                    if version.parse(dict_nexus_version) < version.parse(nexus_version):
                        pkg_dict[components[i]['name']].nexus_version = nexus_version
            # If pkg not exists add it to dicitionary.
            else:
                object = package.Package(pkg_name = components[i]['name'],nexus_version = components[i]['version'])
                pkg_dict[object.pkg_name] = object
    return pkg_dict