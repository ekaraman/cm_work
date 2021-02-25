#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:17:45 2021

@author: derin
"""

from junit_xml import TestSuite, TestCase

def test_result_writer(pkg_dict, project, platform, cms_version, check_type):
    test_cases = []
    for key in pkg_dict:
        db_version = pkg_dict[key].db_version
        nexus_version = pkg_dict[key].nexus_version
        target_version = pkg_dict[key].target_version
        vdd_version = pkg_dict[key].vdd_version
        if check_type == "vdd":
            if db_version == nexus_version == target_version == vdd_version:
                test_case = TestCase(name=key, status='OK')
                test_cases.append(test_case)
            else:
                test_case = TestCase(name=key, status='NOT OK')
                error_message = "SCM DB Version =  {} {}Nexus Version =  {} Target Version = {} VDD Version = {}".format(db_version, "\n", nexus_version, target_version, vdd_version)
                test_case.add_failure_info(error_message)
                test_cases.append(test_case)
    ts = TestSuite("Configuration Reporter", test_cases)
    print(TestSuite.to_xml_string([ts]))
    with open('output.xml', 'w') as f:
        TestSuite.to_file(f, [ts])
    
    
    
#     tmp_test = TestCase(name='ansible', status='NOT OK')
#     tmp_test.add_error_info("deneme")
#     #tmp_test.add_failure_info("this is failure")
#     test_cases = [tmp_test]
#     ts = TestSuite("Configuration Reporter", test_cases)
# # pretty printing is on by default but can be disabled using prettyprint=False
#     print(TestSuite.to_xml_string([ts]))
#     with open('output.xml', 'w') as f:
#         TestSuite.to_file(f, [ts])