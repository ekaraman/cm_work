#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:56:48 2021

@author: derin
"""

import mysql.connector
from mysql.connector import errorcode
import package


def check_connection():
    config = {
        'user': 'root',
        'password': '010817',
        'host': 'localhost',
        'database': 'scm_db',
        'raise_on_warnings': True
        }

    try:
        connection = mysql.connector.connect(**config)
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def get_platform_conf(project, platform, cms_version):
    config = {
        'user': 'root',
        'password': '010817',
        'host': 'localhost',
        'database': 'scm_db',
        'raise_on_warnings': True
        }
    
    try:
        connection = mysql.connector.connect(**config)
        
        sql_query = """Select pkg_name, pkg_version from platform_pkg_version WHERE 
                        project_name = %s AND platform_name = %s AND cms_version = %s;"""
        
                       
        if connection.is_connected():
            
            cursor = connection.cursor()

            cursor.execute(sql_query,(project,platform,cms_version))

            result = cursor.fetchall()

            #for x in result:
            #    print(x)
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return result
        
def get_scm_db_conf(project, platform, cms_version):
    check_connection()
    scm_db_conf = get_platform_conf(project, platform,cms_version)
    pkg_dict = {}
    for i in range(len(scm_db_conf)):
        pkg_name = scm_db_conf[i][0]
        scm_db_version = scm_db_conf[i][1] 
        object = package.Package(pkg_name,scm_db_version)
        pkg_dict[object.pkg_name] = object
        
    return pkg_dict