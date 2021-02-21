#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 00:18:14 2021

@author: derin
"""
import csv
from packaging import version
import package

def get_target_conf(pkg_dict):
    with open('repo_information.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            target_pkg_name = row[0]
            target_pkg_version = row[1]
            if target_pkg_name in pkg_dict:
                dict_target_version = pkg_dict[target_pkg_name].target_version
                if dict_target_version is None:
                    pkg_dict[target_pkg_name].target_version = target_pkg_version
                else:
                    if version.parse(dict_target_version) < version.parse(target_pkg_version):
                        pkg_dict[target_pkg_name].target_version = target_pkg_version
            else:
                object = package.Package(pkg_name = target_pkg_name, target_version = target_pkg_version)
                pkg_dict[object.pkg_name] = object
    return pkg_dict