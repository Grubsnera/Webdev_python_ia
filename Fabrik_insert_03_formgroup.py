"""
Script to INSERT Joomla Fabrik form record
Copyright: AB Janse van Rensburg on 2018-10-28
"""

import sys

# Add own module path
sys.path.append('S:/_my_modules')

# Import python objects
import pyodbc

# Define Functions
import funcfile
import funcmysql

# Declare variables
sd_database = "Web_ia_joomla"
sd_table = "ianwu_fabrik_formgroup"
s_sql = "" #SQL statements

print("FABRIK INSERT FORMGROUP STEP 3")
print("------------------------------")

# Input the joomla mysql fabrik DATABASE name
print("")
print("Default:"+sd_database)
s_database = input("Fabrik DATABASE name? ")
if s_database == "":
    s_database = sd_database

# Input the joomla mysql fabrik TABLE name
print("")
print("Default:"+sd_table)
s_table = input("Fabrik TABLE name? ")
if s_table == "":
    s_table = sd_table
    
# Input the joomla mysql fabrik GROUP number
print("")
s_group = ""
while s_group == "":
    s_group = input("Fabrik GROUP number? ")

# Input the joomla mysql fabrik FORM number
print("")
s_form = ""
while s_form == "":
    s_form = input("Fabrik FORM number? ")

# Script log file
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: FABRIK_INSERT_03_FORMGROUP")
funcfile.writelog("----------------------------------")

# Connect to the oracle database
cnxn = funcmysql.mysql_open(s_database)
curs = cnxn.cursor()
funcfile.writelog("%t OPEN DATABASE: " + s_database)

# Add default FINDING RATE data 1
s_sql = "INSERT INTO " + s_table + "(" + """
form_id,
group_id,
ordering
""" + ") VALUES (" + """
%FORM%,
%GROUP%,
1
""" + ");"
#print(s_sql)
s_sql = s_sql.replace("%FORM%",s_form)
s_sql = s_sql.replace("%GROUP%",s_group)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t ADD DATA: " + s_database +"."+ s_table +":"+ "FormGroup")

# Script log file
funcfile.writelog("-------------------------------------")
funcfile.writelog("COMPLETED: FABRIK_INSERT_03_FORMGROUP")
