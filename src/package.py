#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:56:50 2021

@author: derin
"""

class Package():
        
        def __init__(self,pkg_name, db_version=None, nexus_version=None, target_version=None):
            self.pkg_name = pkg_name
            self.db_version = db_version
            self.nexus_version = nexus_version
            self.target_version = target_version
            
        
        # def get_pkg_name(self):
        #     return self.pkg_name
        
        # def get_db_version(self):
        #     return self.db_version
        
        # def get_nexus_version(self):
        #     return self.nexus_version
        
        # def get_target_version(self):
        #     return self.target_version