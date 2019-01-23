"""
Script to INSERT Joomla Fabrik form record
Copyright: AB Janse van Rensburg on 2018-10-28
"""

# Import python system object
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
sd_table = "ianwu_fabrik_forms"
sd_label = "New FORM to setup"
s_sql = "" #SQL statements
s_created_by = "854"

print("FABRIK INSERT FORM STEP 2")
print("-------------------------")

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

# Input the joomla mysql fabrik FORM name
print("")
print("Default:"+sd_label)
s_label = input("Fabrik FORM label? ")
if s_label == "":
    s_label = sd_label
print("")

# Script log file
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: FABRIK_INSERT_02_FORM")
funcfile.writelog("-----------------------------")

# Connect to the oracle database
cnxn = funcmysql.mysql_open(s_database)
curs = cnxn.cursor()
funcfile.writelog("%t OPEN DATABASE: " + s_database)

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
"goback_button":"1",
"submit_on_enter":"1"
}'
""" + ");"
#print(s_sql)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t ADD DATA: " + s_database +"."+ s_table +":"+ s_label)

# Form param default
"""
{
"outro":"",
"reset_button":"0",
"reset_button_label":"Reset",
"reset_button_class":"btn-warning",
"reset_icon":"",
"reset_icon_location":"before",
"copy_button":"0",
"copy_button_label":"Save as copy",
"copy_button_class":"",
"copy_icon":"",
"copy_icon_location":"before",
"goback_button":"0",
"goback_button_label":"Go back",
"goback_button_class":"",
"goback_icon":"",
"goback_icon_location":"before",
"apply_button":"0",
"apply_button_label":"Apply",
"apply_button_class":"",
"apply_icon":"",
"apply_icon_location":"before",
"delete_button":"0",
"delete_button_label":"Delete",
"delete_button_class":"btn-danger",
"delete_icon":"",
"delete_icon_location":"before",
"submit_button":"1",
"submit_button_label":"Save",
"save_button_class":"btn-primary",
"save_icon":"",
"save_icon_location":"before",
"submit_on_enter":"0",
"labels_above":"0",
"labels_above_details":"0",
"pdf_template":"admin",
"pdf_orientation":"portrait",
"pdf_size":"letter",
"show_title":"1",
"print":"",
"email":"",
"pdf":"",
"admin_form_template":"",
"admin_details_template":"",
"note":"",
"show_referring_table_releated_data":"0",
"tiplocation":"tip",
"process_jplugins":"2",
"ajax_validations":"0",
"ajax_validations_toggle_submit":"0",
"submit_success_msg":"",
"suppress_msgs":"0",
"show_loader_on_submit":"0",
"spoof_check":"1",
"multipage_save":"0"
}
"""

# Display the form number
curs.execute("SELECT "+s_table+".id, "+s_table+".label FROM "+s_table+" WHERE "+s_table+".label = '" + s_label +"'")
for row in curs.fetchall():
    print(row)

# Script log file
funcfile.writelog("--------------------------------")
funcfile.writelog("COMPLETED: FABRIK_INSERT_02_FORM")
