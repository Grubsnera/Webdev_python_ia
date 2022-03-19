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

print("FABRIK INSERT ELEMENT TEXTAREA STEP 5")
print("-------------------------------------")

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
funcfile.writelog("SCRIPT: FABRIK_INSERT_05_ELEMENT_TEXTAREA_255")
funcfile.writelog("---------------------------------------------")

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
"textarea",
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
"bootstrap_class":"input-xxlarge",
"textarea_field_type":"TEXT",
"textarea-showmax":"0",
"textarea-maxlength":"255",
"textarea_limit_type":"word",
"inc_in_adv_search":"1"
}'
""" + ");"
s_sql = s_sql.replace("%NAME%",s_name)
s_sql = s_sql.replace("%LABEL%",s_label)
s_sql = s_sql.replace("%GROUP%",s_group)
s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
s_sql = s_sql.replace("%ORDERING%",s_auto)
curs.execute(s_sql)
cnxn.commit()
funcfile.writelog("%t ADD DATA: " + s_database +"."+ s_table +":"+ s_label)

# Default params
"""
{
"bootstrap_class":"input-xxlarge",
"width":"40",
"height":"6",
"textarea_showlabel":"1",
"textarea_placeholder":"",
"use_wysiwyg":"0",
"wysiwyg_extra_buttons":"1",
"textarea_field_type":"TEXT",
"textarea-showmax":"1",
"textarea-maxlength":"255",
"textarea_limit_type":"char",
"textarea-tagify":"0",
"textarea_tagifyurl":"",
"textarea-truncate-where":"0",
"textarea-truncate-html":"0",
"textarea-truncate":"0",
"textarea-hover":"1",
"textarea_hover_location":"top",
"show_in_rss_feed":"0",
"show_label_in_rss_feed":"0",
"use_as_rss_enclosure":"0",
"rollover":"","tipseval":"0",
"tiplocation":"top-left",
"labelindetails":"0",
"labelinlist":"0",
"comment":"",
"edit_access":"1",
"edit_access_user":"",
"view_access":"1",
"view_access_user":"",
"list_view_access":"1",
"encrypt":"0",
"store_in_db":"1",
"default_on_copy":"0",
"can_order":"0",
"alt_list_heading":"",
"custom_link":"",
"custom_link_target":"",
"custom_link_indetails":"1",
"use_as_row_class":"0",
"include_in_list_query":"1",
"always_render":"0",
"icon_folder":"0",
"icon_hovertext":"1",
"icon_file":"",
"icon_subdir":"",
"filter_length":"20",
"filter_access":"1",
"full_words_only":"0",
"filter_required":"0",
"filter_build_method":"0",
"filter_groupby":"text",
"inc_in_adv_search":"1",
"filter_class":"input-medium",
"filter_responsive_class":"",
"tablecss_header_class":"",
"tablecss_header":"",
"tablecss_cell_class":"",
"tablecss_cell":"",
"sum_on":"0",
"sum_label":"Sum",
"sum_access":"1",
"sum_split":"",
"avg_on":"0",
"avg_label":"Average",
"avg_access":"1",
"avg_round":"0",
"avg_split":"",
"median_on":"0",
"median_label":"Median",
"median_access":"1",
"median_split":"",
"count_on":"0",
"count_label":"Count",
"count_condition":"",
"count_access":"1",
"count_split":"",
"custom_calc_on":"0",
"custom_calc_label":"Custom",
"custom_calc_query":"",
"custom_calc_access":"1",
"custom_calc_split":"",
"custom_calc_php":"",
"validations":[]
}"""

# Script log file
funcfile.writelog("------------------------------------------------")
funcfile.writelog("COMPLETED: FABRIK_INSERT_05_ELEMENT_TEXTAREA_255")
