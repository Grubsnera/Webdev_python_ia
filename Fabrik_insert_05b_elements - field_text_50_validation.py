"""
Script to INSERT Joomla Fabrik form record
Copyright: AB Janse van Rensburg on 2018-10-28
"""

# Import python system objects
import sys
import pyodbc

# Define Functions
from _my_modules import funcfile
from _my_modules import funcmysql

# Declare variables
sd_database = "Web_ia_joomla"
sd_table = "ianwu_fabrik_elements"
s_sql = "" #SQL statements
s_created_by = "854"

print("FABRIK INSERT ELEMENT FIELD TEXT STEP 5")
print("---------------------------------------")

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

# Input the joomla mysql fabrik element FIELD name
print("")
s_name = ""
while s_name == "":
    s_name = input("Fabrik element FIELD name? ")

# Input the joomla mysql fabrik element LABEL name
print("")
s_label = ""
while s_label == "":
    s_label = input("Fabrik element LABEL name? ")

# Input the joomla mysql fabrik element ORDER number
print("")
s_auto = ""
while s_auto == "":
    s_auto = input("Fabrik element ORDERING number? ")
   
# Script log file
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: FABRIK_INSERT_05_ELEMENT_FIELD_TEXT")
funcfile.writelog("-------------------------------------------")

# Connect to the oracle database
cnxn = funcmysql.mysql_open(s_database)
curs = cnxn.cursor()
funcfile.writelog("%t OPEN DATABASE: " + s_database)

# Add default FINDING RATE data 1
s_sql = "INSERT INTO " + s_table + "(" + """
name,
group_id,
plugin,
label,
created,
created_by,
created_by_alias,
hidden,
ordering,
show_in_list_summary,
filter_exact_match,
published,
access,
params
""" + ") VALUES (" + """
"%NAME%",
%GROUP%,
"field",
"%LABEL%",
NOW(),
%CREATED_BY%,
"Python",
0,
%ORDERING%,
1,
1,
1,
1,
'{
"maxlength":"50",
"bootstrap_class":"input-xxlarge",
"can_order":"1",
"inc_in_adv_search":"1",
"validations":{"plugin":["notempty"],"Plugin_published":["1"],"validate_hidden":["1"],"show_icon":["0"]
}}'
""" + ");"
s_sql = s_sql.replace("%NAME%",s_name)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%GROUP%",s_group)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
s_sql = s_sql.replace("%ORDERING%",s_auto)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t ADD DATA: " + s_database +"."+ s_table +":"+ s_label)

# Element field text default params
"""
{
"maxlength":"50",
"bootstrap_class":"input-xxlarge",
"text_format":"text",

"link_target_options":"default",
"rel":"","link_title":"",
"show_in_rss_feed":"0",
"show_label_in_rss_feed":"0",
"use_as_rss_enclosure":"0",
"tiplocation":"right",
"store_in_db":"1",
"can_order":"1",
"validations":{"plugin":["notempty"],"plugin_published":["1"],"validate_in":["both"],"validation_on":["both"],"validate_hidden":["1"],"must_validate":["1"],"show_icon":["0"]}
}
"""


# Script log file
funcfile.writelog("----------------------------------------------")
funcfile.writelog("COMPLETED: FABRIK_INSERT_05_ELEMENT_FIELD_TEXT")





