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
sd_table = "ianwu_fabrik_lists"
sd_label = "New LIST to setup"
sd_form = "1"
sd_target = "ia_finding_rate"
sd_key = "ia_findrate_auto"
s_sql = ""
s_created_by = "854"

print("FABRIK INSERT LIST STEP 4")
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

# Input the joomla mysql fabrik LIST label
print("")
print("Default:"+sd_label)
s_label = input("Fabrik LIST label? ")
if s_label == "":
    s_label = sd_label

# Input the joomla mysql fabrik FORM number
print("")
s_form = ""
while s_form == "":
    s_form = input("Fabrik FORM number? ")

# Input the joomla mysql target TABLE name
print("")
s_target = ""
while s_target == "":
    s_target = input("List TABLE name? ")

# Input the joomla mysql target KEY FIELD
print("")
s_key = ""
while s_key == "":
    s_key = input("List KEY field? ")

# Script log file
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: FABRIK_INSERT_04_LISTS")
funcfile.writelog("------------------------------")

# Connect to the oracle database
cnxn = funcmysql.mysql_open(s_database)
curs = cnxn.cursor()
funcfile.writelog("%t OPEN DATABASE: " + s_database)

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
funcfile.writelog("%t ADD DATA: " + s_database +"."+ s_table +":"+ s_label)

# LIST param defaults
"""
{
"show-table-filters":"1",
"advanced-filter":"0",
"advanced-filter-default-statement":"=",
"search-mode":"0",
"search-mode-advanced":"0",
"search-mode-advanced-default":"all",
"search_elements":"",
"list_search_elements":"null",
"search-all-label":"All",
"require-filter":"0",
"filter-dropdown-method":"0",
"toggle_cols":"0",
"list_filter_cols":"1",
"empty_data_msg":"",
"outro":"",
"list_ajax":"0",
"show-table-add":"1",
"show-table-nav":"1",
"show_displaynum":"1",
"showall-records":"0",
"show-total":"0",
"sef-slug":"",
"show-table-picker":"1",
"admin_template":"",
"show-title":"1",
"pdf":"",
"pdf_template":"",
"pdf_orientation":"portrait",
"pdf_size":"a4",
"bootstrap_stripped_class":"1",
"bootstrap_bordered_class":"0",
"bootstrap_condensed_class":"0",
"bootstrap_hover_class":"1",
"responsive_elements":"",
"responsive_class":"",
"list_responsive_elements":"null",
"tabs_field":"",
"tabs_max":"10",
"tabs_all":"1",
"list_ajax_links":"0",
"actionMethod":"default",
"detailurl":"",
"detaillabel":"",
"list_detail_link_icon":"search",
"list_detail_link_target":"_self",
"editurl":"",
"editlabel":"",
"list_edit_link_icon":"edit",
"checkboxLocation":"end",
"addurl":"",
"addlabel":"",
"list_add_icon":"plus",
"list_delete_icon":"delete",
"popup_width":"",
"popup_height":"",
"popup_offset_x":"",
"popup_offset_y":"",
"note":"",
"alter_existing_db_cols":"default",
"process-jplugins":"1",
"cloak_emails":"0",
"enable_single_sorting":"default",
"collation":"utf8_general_ci",
"force_collate":"",
"list_disable_caching":"0",
"distinct":"1",
"group_by_raw":"1",
"group_by_access":"1",
"group_by_order":"",
"group_by_template":"",
"group_by_order_dir":"ASC",
"group_by_start_collapsed":"0",
"group_by_collapse_others":"0",
"group_by_show_count":"1",
"menu_module_prefilters_override":"1",
"prefilter_query":"",
"join-display":"default",
"delete-joined-rows":"0",
"show_related_add":"0",
"show_related_info":"0",
"rss":"0",
"feed_title":"",
"feed_date":"",
"feed_image_src":"",
"rsslimit":"150",
"rsslimitmax":"2500",
"csv_import_frontend":"3",
"csv_export_frontend":"2",
"csvfullname":"0",
"csv_export_step":"100",
"newline_csv_export":"nl2br",
"csv_clean_html":"leave",
"csv_custom_qs":"",
"csv_frontend_selection":"0",
"incfilters":"0",
"csv_format":"0",
"csv_which_elements":"selected",
"show_in_csv":"",
"csv_elements":"null",
"csv_include_data":"1",
"csv_include_raw_data":"1",
"csv_include_calculations":"0",
"csv_filename":"",
"csv_encoding":"",
"csv_double_quote":"1",
"csv_local_delimiter":"",
"csv_end_of_line":"n",
"open_archive_active":"0",
"open_archive_set_spec":"",
"open_archive_timestamp":"",
"open_archive_license":"http:\/\/creativecommons.org\/licenses\/by-nd\/2.0\/rdf",
"dublin_core_element":"",
"dublin_core_type":"dc:description.abstract",
"raw":"0",
"open_archive_elements":"null",
"search_use":"0",
"search_title":"",
"search_description":"",
"search_date":"",
"search_link_type":"details",
"dashboard":"0",
"dashboard_icon":"",
"allow_view_details":"1",
"allow_edit_details":"1",
"allow_edit_details2":"",
"allow_add":"1",
"allow_delete":"2",
"allow_delete2":"",
"allow_drop":"3",
"isview":"0"
}
"""

# Script log file
funcfile.writelog("---------------------------------")
funcfile.writelog("COMPLETED: FABRIK_INSERT_04_LISTS")
