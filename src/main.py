#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 08:47:43 2021

@author: derin
"""
import argparse
import scm_db
import nexus
import target

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Check configuration of target platform against scm database and nexus repo.')
    parser.add_argument('project', metavar='project', help='project name')
    parser.add_argument('platform', metavar='platform', help='platform name')
    parser.add_argument('cms_version', metavar='cms_version',  help='cms version')
    parser.add_argument('target_repo_info', metavar='target_repo_info', help='target platform repo_information.txt path')
    args = parser.parse_args()
    
    project = args.project
    platform = args.platform
    cms_version = args.cms_version
    tarfget_repo_info = args.target_repo_info
    
    # Get scm db configuration into dictionary
    pkg_dict = scm_db.get_scm_db_conf(project, platform, cms_version)
    
    # Get nexus configuration into dictionary
    pkg_dict = nexus.get_nexus_conf(project, platform, cms_version, pkg_dict)

    # Get target platform configuration into dictionary
    pkg_dict = target.get_target_conf(pkg_dict)
    
