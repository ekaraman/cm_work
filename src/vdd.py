#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 23:00:08 2021

@author: derin
"""

import csv
from packaging import version
import package

def get_vdd_conf(pkg_dict):
    with open('vdd.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            vdd_pkg_name = row[0]
            vdd_pkg_version = row[1]
            if vdd_pkg_name in pkg_dict:
                dict_vdd_version = pkg_dict[vdd_pkg_name].vdd_version
                if dict_vdd_version is None:
                    pkg_dict[vdd_pkg_name].vdd_version = vdd_pkg_version
                else:
                    if version.parse(dict_vdd_version) < version.parse(vdd_pkg_version):
                        pkg_dict[vdd_pkg_name].vdd_version = vdd_pkg_version
            else:
                object = package.Package(pkg_name = vdd_pkg_name, vdd_version = vdd_pkg_version)
                pkg_dict[object.pkg_name] = object
    return pkg_dict