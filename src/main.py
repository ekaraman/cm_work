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
import vdd
import reporter

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Check configuration of target platform against scm database and nexus repo.')
    parser.add_argument('project', metavar='project', help='project name')
    parser.add_argument('platform', metavar='platform', help='platform name')
    parser.add_argument('cms_version', metavar='cms_version',  help='cms version')
    parser.add_argument('target_repo_info', metavar='target_repo_info', help='target platform repo_information.txt path')
    parser.add_argument('check_type', metavar='check_type', help='check target repo or vdd against scm db and nexus. Value can be target or vdd')
    args = parser.parse_args()
    
    project = args.project
    platform = args.platform
    cms_version = args.cms_version
    tarfget_repo_info = args.target_repo_info
    check_type = args.check_type
    
    # Get scm db configuration into dictionary
    pkg_dict = scm_db.get_scm_db_conf(project, platform, cms_version)
    
    
    # Get nexus configuration into dictionary
    pkg_dict = nexus.get_nexus_conf(project, platform, cms_version, pkg_dict)

    # Get target platform configuration into dictionary
    if check_type == 'target' or check_type == 'vdd':
        pkg_dict = target.get_target_conf(pkg_dict)
    
    # Get vdd configuration into dictionary
    if check_type == 'vdd':
        pkg_dict = vdd.get_vdd_conf(pkg_dict)
        
    reporter.test_result_writer(pkg_dict, project, platform, cms_version,check_type)