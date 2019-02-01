"""
Script to INSERT Joomla Fabrik group and form record
Copyright (C) AB Janse van Rensburg 2018-10-28
"""

# Import system objects
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
sd_table = "ianwu_fabrik_groups"
sd_label = "New GROUP to setup"
s_sql = ""
s_created_by = "854"

print("FABRIK INSERT GROUP STEP 1")
print("--------------------------")

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

# Input the joomla mysql fabrik GROUP label
print("")
print("Default:"+sd_label)
s_label = input("Fabrik GROUP label? ")
if s_label == "":
    s_label = sd_label
print("")

# Script log file
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: FABRIK_INSERT_01_GROUP")
funcfile.writelog("------------------------------")

# Connect to the oracle database
cnxn = funcmysql.mysql_open(s_database)
curs = cnxn.cursor()
funcfile.writelog("%t OPEN DATABASE: " + s_database)

# Add a GROUP record
s_sql = "INSERT INTO `" + s_table + "` (" + """
`name`,
`css`,
`label`,
`published`,
`created`,
`created_by`,
`created_by_alias`,
`modified`,
`modified_by`,
`checked_out`,
`checked_out_time`,
`is_join`,
`private`,
`params`
""" + ") VALUES (" + """
'%LABEL%',
'',
'Add/Edit %LABEL%',
1,
NOW(),
%CREATED_BY%,
'Python',
'0000-00-00 00:00:00',
0,
0,
'0000-00-00 00:00:00',
0,
0,
'{
\"split_page\":\"0\",
\"list_view_and_query\":\"1\",
\"access\":\"1\",
\"intro\":\"\",
\"outro\":\"\",
\"repeat_group_button\":\"0\",
\"repeat_template\":\"repeatgroup\",
\"repeat_max\":\"\",
\"repeat_min\":\"\",
\"repeat_num_element\":\"\",
\"repeat_error_message\":\"\",
\"repeat_no_data_message\":\"\",
\"repeat_intro\":\"\",
\"repeat_add_access\":\"1\",
\"repeat_delete_access\":\"1\",
\"repeat_delete_access_user\":\"\",
\"repeat_copy_element_values\":\"0\",
\"group_columns\":\"1\",
\"group_column_widths\":\"\",
\"repeat_group_show_first\":\"1\",
\"random\":\"0\",
\"labels_above\":\"-1\",
\"labels_above_details\":\"-1\"
}'
""" + ");"
#print(s_sql)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t ADD DATA: " + s_database +"."+ s_table +":"+ s_label)

# GROUP default params
"""
'{
\"split_page\":\"0\",
\"list_view_and_query\":\"1\",
\"access\":\"1\",
\"intro\":\"\",
\"outro\":\"\",
\"repeat_group_button\":\"0\",
\"repeat_template\":\"repeatgroup\",
\"repeat_max\":\"\",
\"repeat_min\":\"\",
\"repeat_num_element\":\"\",
\"repeat_error_message\":\"\",
\"repeat_no_data_message\":\"\",
\"repeat_intro\":\"\",
\"repeat_add_access\":\"1\",
\"repeat_delete_access\":\"1\",
\"repeat_delete_access_user\":\"\",
\"repeat_copy_element_values\":\"0\",
\"group_columns\":\"1\",
\"group_column_widths\":\"\",
\"repeat_group_show_first\":\"1\",
\"random\":\"0\",
\"labels_above\":\"-1\",
\"labels_above_details\":\"-1\"
}'
"""

# Display the group number
curs.execute("SELECT "+s_table+".id, "+s_table+".name FROM "+s_table+" WHERE "+s_table+".name = '" + s_label +"'")
for row in curs.fetchall():
    print(row)

# Script log file
funcfile.writelog("---------------------------------")
funcfile.writelog("COMPLETED: FABRIK_INSERT_01_GROUP")
