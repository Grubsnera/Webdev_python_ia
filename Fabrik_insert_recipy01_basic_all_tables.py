"""*****************************************************************************
Script to INSERT Joomla Fabrik group and form record
Copyright (C) AB Janse van Rensburg 2018-10-28
*****************************************************************************"""

""" FABRIK SETUP STEPS *********************************************************
ENVIRONMENT
OPEN THE DATABASE
CREATE GROUP STEP 1 (create fabrik group and obtain group number)
INSERT FORM STEP 2 (create fabrik form and obtain form number)
INSERT FORMGROUP STEP 3 (create fabrik form group combination)
INSERT LIST STEP 4 (create fabrik list)
INSERT ELEMENT INTERNALID STEP 5 (create fabrik element internalid)
INSERT ELEMENT CREATEDATE STEP 6 (create fabrik element createdate)
INSERT ELEMENT CREATEBY STEP 7 (create fabrik element createby)
INSERT ELEMENT CREATEDATE STEP 8 (create fabrik element editdate)
INSERT ELEMENT EDITBY STEP 9 (create fabrik element editby)
*****************************************************************************"""

"""*****************************************************************************
ENVIRONMENT
*****************************************************************************"""
print("ENVIRONMENT")

# IMPORT SYSTEM OBJECTS
import sys
import pyodbc

# IMPORT FUNCTION FILES
from _my_modules import funcfile
from _my_modules import funcmysql

# DECLARE VARIABLES
sd_database = "Web_ia_joomla"
sd_group = 0
sd_form = 0
s_sql = ""
s_created_by = "854"

print("FABRIK BUILD BASIC TABLE SETUP")
print("------------------------------")

# OPEN THE SCRIPTE LOG FILE
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: FABRIK BUILD BASIC TABLE STRUCTURE")
funcfile.writelog("------------------------------------------")

"""*****************************************************************************
OPEN THE DATABASE
*****************************************************************************"""
print("OPEN THE DATABASE")
funcfile.writelog("OPEN THE DATABASE ")

# SET THE JOOMLA MYSQL FABRIK DATABASE NAME
s_database = ""
print("")
print("Default:"+sd_database)
#s_database = input("Fabrik DATABASE name? ")
if s_database == "":
    s_database = sd_database

# OPEN THE DATABASE
cnxn = funcmysql.mysql_open(s_database)
curs = cnxn.cursor()
print("Database opened "+s_database)
funcfile.writelog("%t OPEN DATABASE: " + s_database)

"""*****************************************************************************
CREATE GROUP STEP 1 (create fabrik group and obtain group number)
*****************************************************************************"""
print("CREATE GROUP")
funcfile.writelog("CREATE GROUP")

# SET THE JOOMLA MYSQL FABRIK TABLE NAME
s_table = ""
sd_table = "ianwu_fabrik_groups"
print("")
print("Default:"+sd_table)
#s_table = input("Fabrik TABLE name? ")
if s_table == "":
    s_table = sd_table

# SET THE JOOMLA MYSQL FABRIK GROUP LABEL
s_label = ""
sd_label = "New GROUP to setup"
print("")
print("Default:"+sd_label)
s_label = input("Fabrik GROUP label? ")
if s_label == "":
    s_label = sd_label
print("")

# ADD THE GROUP RECORD
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

# Display the group number
curs.execute("SELECT "+s_table+".id, "+s_table+".name FROM "+s_table+" WHERE "+s_table+".name = '" + s_label +"'")
for row in curs.fetchall():
    print("1. Build group " + str(row[0]))
    sd_group = row[0]

funcfile.writelog("%t INSERT GROUP: " + s_database +"."+ s_table +":"+ s_label + " " + str(sd_group))

""" INSERT FORM STEP 2 (create fabrik form and obtain form number)
*****************************************************************************"""

# Input the joomla mysql fabrik TABLE name
s_table = ""
sd_table = "ianwu_fabrik_forms"
print("")
print("Default:"+sd_table)
#s_table = input("Fabrik TABLE name? ")
if s_table == "":
    s_table = sd_table

# Input the joomla mysql fabrik FORM name
s_label = ""
sd_label = "New FORM to setup"
print("")
print("Default:"+sd_label)
s_label = input("Fabrik FORM label? ")
if s_label == "":
    s_label = sd_label
print("")

# Insert a FORM record
s_sql = "INSERT INTO " + s_table + "(" + """
label,
record_in_database,
error,
intro,
created,
created_by,
created_by_alias,
reset_button_label,
submit_button_label,
form_template,
view_only_template,
published,
params
""" + ") VALUES (" + """
"%LABEL%",
1,
"Some parts of your form have not been correctly filled in",
"",
NOW(),
%CREATED_BY%,
"Python",
"Reset",
"Save",
"bootstrap",
"bootstrap",
1,
'{
"show-title":"0",
"goback_button":"1",
"submit_on_enter":"1"
}'
""" + ");"
#print(s_sql)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
curs.execute(s_sql)
cnxn.commit()

# Display the form number
curs.execute("SELECT "+s_table+".id, "+s_table+".label FROM "+s_table+" WHERE "+s_table+".label = '" + s_label +"'")
for row in curs.fetchall():
    print("2. Build form " + str(row[0]))
    sd_form = row[0]    

funcfile.writelog("%t INSERT FORM: " + s_database +"."+ s_table +":"+ s_label + " " + str(sd_form))


""" INSERT FORMGROUP STEP 3 (create fabrik form group combination)
*****************************************************************************"""

# Input the joomla mysql fabrik TABLE name
s_table = ""
sd_table = "ianwu_fabrik_formgroup"
print("")
print("Default:"+sd_table)
#s_table = input("Fabrik TABLE name? ")
if s_table == "":
    s_table = sd_table

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
s_sql = s_sql.replace("%FORM%",str(sd_form))
s_sql = s_sql.replace("%GROUP%",str(sd_group))
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t INSERT FORM: " + s_database +"."+ s_table +": FormGroup " + str(sd_form) + " " + str(sd_group))


""" INSERT LIST STEP 4 (create fabrik list)
*****************************************************************************"""

# Input the joomla mysql fabrik TABLE name
s_table = ""
sd_table = "ianwu_fabrik_lists"
print("")
print("Default:"+sd_table)
#s_table = input("Fabrik TABLE name? ")
if s_table == "":
    s_table = sd_table

# Input the joomla mysql fabrik FORM name
s_label = ""
sd_label = "New LABEL to setup"
print("")
print("Default:"+sd_label)
s_label = input("Fabrik LIST label? ")
if s_label == "":
    s_label = sd_label
print("")

# Input the joomla mysql fabrik FORM number
s_form = str(sd_form)

# Input the joomla mysql target TABLE name
print("")
s_target = ""
while s_target == "":
    s_target = input("List target TABLE name? ")

# Input the joomla mysql target KEY FIELD
print("")
s_key = ""
while s_key == "":
    s_key = input("List KEY field? ")

# Add default FINDING RATE data 1
s_sql = "INSERT INTO " + s_table + "(" + """
label,
introduction,
form_id,
db_table_name,
db_primary_key,
auto_inc,
connection_id,
created,
created_by,
created_by_alias,
published,
access,
rows_per_page,
template,
order_by,
order_dir,
filter_action,
params
""" + ") VALUES (" + """
"%LABEL%",
"",
%FORM%,
"%TABLE_TARGET%",
"%TABLE_TARGET%.%KEY_FIELD%",
1,
2,
NOW(),
%CREATED_BY%,
"Python",
1,
9,
10,
"bootstrap",
'[""]',
'["ASC"]',
"onchange",
'{"showall-records":"1",
"show-total":"1",
"bootstrap_condensed_class":"1",
"allow_view_details":"9",
"allow_edit_details":"9",
"allow_add":"10",
"allow_delete":"10",
"allow_drop":"6"}'
""" + ");"
#print(s_sql)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
s_sql = s_sql.replace("%FORM%",s_form)
s_sql = s_sql.replace("%TABLE_TARGET%",s_target)
s_sql = s_sql.replace("%KEY_FIELD%",s_key)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t INSERT LIST: " + s_database +"."+ s_table +":"+ s_label)


""" INSERT ELEMENT INTERNALID STEP 5 (create fabrik element internalid)
*****************************************************************************"""

# Start the element counter
n_coun = 1


# Input the joomla mysql fabrik TABLE name
s_table = ""
sd_table = "ianwu_fabrik_elements"
print("")
print("Default:"+sd_table)
#s_table = input("Fabrik TABLE name? ")
if s_table == "":
    s_table = sd_table

# Input the joomla mysql fabrik GROUP number
s_group = str(sd_group)

# Input the joomla mysql fabrik element FIELD name
s_name = s_key

# Input the joomla mysql fabrik element LABEL name
s_label = s_key

# Input the joomla mysql fabrik element ORDER number
s_auto = str(n_coun)
n_coun = n_coun + 1

# Add default FINDING RATE data 1
s_sql = "INSERT INTO " + s_table + "(" + """
name,
group_id,
plugin,
label,
created,
created_by,
created_by_alias,
width,
height,
ordering,
show_in_list_summary,
filter_exact_match,
published,
access,
params
""" + ") VALUES (" + """
"%NAME%",
%GROUP%,
"internalid",
"%LABEL%",
NOW(),
%CREATED_BY%,
"Python",
11,
6,
%ORDERING%,
0,
1,
1,
1,
'{
"custom_link_indetails":"0",
"include_in_list_query":"0",
"inc_in_adv_search":"0"
}'
""" + ");"
#print(s_sql)
s_sql = s_sql.replace("%NAME%",s_name)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%GROUP%",s_group)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
s_sql = s_sql.replace("%ORDERING%",s_auto)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t INSERT LIST: " + s_database +"."+ s_table +":"+ s_label)

""" INSERT ELEMENT CREATEDATE STEP 6 (create fabrik element createdate)
*****************************************************************************"""

# Input the joomla mysql fabrik TABLE name
s_table = sd_table

# Input the joomla mysql fabrik GROUP number
s_group = str(sd_group)

# Input the joomla mysql fabrik element FIELD name
print("")
s_name = ""
while s_name == "":
    s_name = input("Fabrik element createdate FIELD name? ")

# Input the joomla mysql fabrik element LABEL name
print("")
s_label = ""
while s_label == "":
    s_label = input("Fabrik element createdate LABEL name? ")

# Input the joomla mysql fabrik element ORDER number
s_auto = str(n_coun)
n_coun = n_coun + 1

# Insert the element
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
"jdate",
"%LABEL%",
NOW(),
%CREATED_BY%,
"Python",
1,
%ORDERING%,
0,
1,
1,
10,
'{
"bootstrap_class":"input-medium",
"jdate_showtime":"0",
"jdate_time_format":"H:i:s",
"jdate_time_24":"1",
"jdate_store_as_local":"1",
"jdate_table_format":"Y-m-d",
"jdate_form_format":"Y-m-d H:i:s",
"jdate_defaulttotoday":"1",
"jdate_alwaystoday":"0",
"jdate_allow_typing_in_field":"0",
"jdate_show_week_numbers":"0",
"jdate_csv_offset_tz":"0",
"rollover":"The date on which the element was created.",
"tiplocation":"right",
"edit_access":"10",
"view_access":"9",
"list_view_access":"1",
"store_in_db":"1",
"default_on_copy":"1",
"can_order":"1"
}'
""" + ");"
s_sql = s_sql.replace("%NAME%",s_name)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%GROUP%",s_group)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
s_sql = s_sql.replace("%ORDERING%",s_auto)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t INSERT LIST: " + s_database +"."+ s_table +":"+ s_label)


""" INSERT ELEMENT CREATEBY STEP 7 (create fabrik element createby)
*****************************************************************************"""

# Input the joomla mysql fabrik TABLE name
s_table = sd_table

# Input the joomla mysql fabrik GROUP number
s_group = str(sd_group)

# Input the joomla mysql fabrik element FIELD name
print("")
s_name = ""
while s_name == "":
    s_name = input("Fabrik element createby FIELD name? ")

# Input the joomla mysql fabrik element LABEL name
print("")
s_label = ""
while s_label == "":
    s_label = input("Fabrik element createby LABEL name? ")

# Input the joomla mysql fabrik element ORDER number
s_auto = str(n_coun)
n_coun = n_coun + 1

# Insert the element
s_sql = "INSERT INTO " + s_table + "(" + """
name,
group_id,
plugin,
label,
created,
created_by,
created_by_alias,
hidden,
eval,
ordering,
show_in_list_summary,
filter_exact_match,
published,
access,
params
""" + ") VALUES (" + """
"%NAME%",
%GROUP%,
"user",
"%LABEL%",
NOW(),
%CREATED_BY%,
"Python",
1,
0,
%ORDERING%,
0,
1,
1,
1,
'{
"custom_link_indetails":"0",
"include_in_list_query":"0",
"inc_in_adv_search":"0",
"my_table_data":"id",
"update_on_edit":"0",
"update_on_copy":"1"
}'
""" + ");"

s_sql = s_sql.replace("%NAME%",s_name)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%GROUP%",s_group)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
s_sql = s_sql.replace("%ORDERING%",s_auto)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t INSERT LIST: " + s_database +"."+ s_table +":"+ s_label)


""" INSERT ELEMENT EDITDATE STEP 8 (create fabrik element editdate)
*****************************************************************************"""

# Input the joomla mysql fabrik TABLE name
s_table = sd_table

# Input the joomla mysql fabrik GROUP number
s_group = str(sd_group)

# Input the joomla mysql fabrik element FIELD name
print("")
s_name = ""
while s_name == "":
    s_name = input("Fabrik element editdate FIELD name? ")

# Input the joomla mysql fabrik element LABEL name
print("")
s_label = ""
while s_label == "":
    s_label = input("Fabrik element editdate LABEL name? ")

# Input the joomla mysql fabrik element ORDER number
s_auto = str(n_coun)
n_coun = n_coun + 1

# Insert the element
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
"jdate",
"%LABEL%",
NOW(),
%CREATED_BY%,
"Python",
1,
%ORDERING%,
0,
1,
1,
10,
'{
"bootstrap_class":"input-medium",
"jdate_showtime":"0",
"jdate_time_format":"H:i:s",
"jdate_time_24":"1",
"jdate_store_as_local":"1",
"jdate_table_format":"Y-m-d",
"jdate_form_format":"Y-m-d H:i:s",
"jdate_defaulttotoday":"1",
"jdate_alwaystoday":"0",
"jdate_allow_typing_in_field":"0",
"jdate_show_week_numbers":"0",
"jdate_csv_offset_tz":"0",
"rollover":"The date on which the element was created.",
"tiplocation":"right",
"edit_access":"10",
"view_access":"9",
"list_view_access":"1",
"store_in_db":"1",
"default_on_copy":"1",
"can_order":"1"
}'
""" + ");"
s_sql = s_sql.replace("%NAME%",s_name)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%GROUP%",s_group)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
s_sql = s_sql.replace("%ORDERING%",s_auto)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t INSERT LIST: " + s_database +"."+ s_table +":"+ s_label)

""" INSERT ELEMENT EDITBY STEP 9 (create fabrik element editby)
*****************************************************************************"""

# Input the joomla mysql fabrik TABLE name
s_table = sd_table

# Input the joomla mysql fabrik GROUP number
s_group = str(sd_group)

# Input the joomla mysql fabrik element FIELD name
print("")
s_name = ""
while s_name == "":
    s_name = input("Fabrik element editby FIELD name? ")

# Input the joomla mysql fabrik element LABEL name
print("")
s_label = ""
while s_label == "":
    s_label = input("Fabrik element editby LABEL name? ")

# Input the joomla mysql fabrik element ORDER number
s_auto = str(n_coun)
n_coun = n_coun + 1

# Insert the element
s_sql = "INSERT INTO " + s_table + "(" + """
name,
group_id,
plugin,
label,
created,
created_by,
created_by_alias,
hidden,
eval,
ordering,
show_in_list_summary,
filter_exact_match,
published,
access,
params
""" + ") VALUES (" + """
"%NAME%",
%GROUP%,
"user",
"%LABEL%",
NOW(),
%CREATED_BY%,
"Python",
1,
0,
%ORDERING%,
0,
1,
1,
1,
'{
"custom_link_indetails":"0",
"include_in_list_query":"0",
"inc_in_adv_search":"0",
"my_table_data":"id",
"update_on_edit":"0",
"update_on_copy":"1"
}'
""" + ");"

s_sql = s_sql.replace("%NAME%",s_name)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%GROUP%",s_group)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
s_sql = s_sql.replace("%ORDERING%",s_auto)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t INSERT LIST: " + s_database +"."+ s_table +":"+ s_label)


# Script log file
funcfile.writelog("---------------------------------------")
funcfile.writelog("COMPLETED: FABRIK BUILD BASIC STRUCTURE")
