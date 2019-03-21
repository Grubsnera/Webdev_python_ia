""" ****************************************************************************
Script to CREATE Joomla Fabrik list record
Copyright (C) AB Janse van Rensburg 20190319
*****************************************************************************"""

def Fabrik_listcreate(s_input="F",s_lb="New LIST to setup",s_fo="0",s_tt="0",s_kf="0",s_db="Web_ia_joomla",s_tb="ianwu_fabrik_lists"):

    """ PARAMETERS *************************************************************
    s_input = F=do not ask parameters(default) T=ask parameters
    s_lb = List label
    s_db = Joomla database
    s_tb = Joomla table name
    *************************************************************************"""

    """ INDEX ******************************************************************
    ENVIRONMENT
    INPUT
    OPEN DATABASE
    INSERT LIST RECORD
    *************************************************************************"""
    print("FABRIK CREATE LIST STEP 4")
    print("--------------------------")
    print("ENVIRONMENT")

    # IMPORT SYSTEM OBJECTS
    import sys

    # OWN MODULE PATH
    sys.path.append('S:/_my_modules')

    # IMPORT PYTHON OBJECTS
    import pyodbc

    # IMPORT FUNCTIONS
    import funcfile
    import funcmysql

    # DECLARE VARIABLES
    s_sql = ""
    s_created_by = "854"

    """*************************************************************************
    INPUT
    *************************************************************************"""
    print("INPUT")

    # INPUT THE JOOMLA MYSQL FABRIK DATABASE NAME
    s_dbi = s_db
    if s_input == "T":
        print("")
        print("Default:"+s_db)
        s_dbi = input("Fabrik DATABASE name? ")
        if s_dbi == "":
            s_dbi = s_db

    # INPUT THE JOOMLA MYSQL TABLE NAME
    s_tbi = s_tb
    if s_input == "T":
        print("")
        print("Default:"+s_tb)
        s_tbi = input("Fabrik TABLE name? ")
        if s_tbi == "":
            s_tbi = s_tb

    # INPUT THE JOOMLA MYSQL FABRIK LIST LABEL
    s_lbi = s_lb
    if s_input == "T":
        print("")
        print("Default:"+s_lb)
        s_lbi = input("Fabrik LIST label? ")
        if s_lbi == "":
            s_lbi = s_lb
        print("")

    # INPUT THE JOOMLA MYSQL FABRIK FORM NUMBER
    s_foi = s_fo
    if s_input == "T" or s_foi == "0":
        print("")
        print("Default:"+s_fo)
        while s_foi == "" or s_foi == "0":
            s_foi = input("Fabrik FORM number? ")
        print("")        

    # INPUT THE JOOMLA MYSQL FABRIK LIST TARGET TABLE NAME
    s_tti = s_tt
    if s_input == "T" or s_tti == "0":
        print("")
        print("Default:"+s_tt)
        while s_tti == "" or s_tti == "0":
            s_tti = input("Fabrik LIST target table name? ")
        print("")        

    # INPUT THE JOOMLA MYSQL FABRIK LIST KEY FIELD
    s_kfi = s_kf
    if s_input == "T" or s_kfi == "0":
        print("")
        print("Default:"+s_kf)
        while s_kfi == "" or s_kfi == "0":
            s_kfi = input("Fabrik LIST key field? ")
        print("")        

    """*************************************************************************
    OPEN DATABASE
    *************************************************************************"""
    print("OPEN DATABASE")
    funcfile.writelog("OPEN DATABASE")

    # Connect to the oracle database
    cnxn = funcmysql.mysql_open(s_dbi)
    curs = cnxn.cursor()
    funcfile.writelog("%t OPEN DATABASE: " + s_dbi)

    """*************************************************************************
    INSERT LIST RECORD
    *************************************************************************"""
    print("INSERT LIST RECORD")
    funcfile.writelog("INSERT LIST RECORD")

    # INSERT LIST RECORD
    s_sql = "INSERT INTO `" + s_tbi + "` (" + """
    `label`,
    `introduction`,
    `form_id`,
    `db_table_name`,
    `db_primary_key`,
    `auto_inc`,
    `connection_id`,
    `created`,
    `created_by`,
    `created_by_alias`,
    `modified`,
    `modified_by`,
    `checked_out`,
    `checked_out_time`,
    `published`,
    `publish_up`,
    `publish_down`,
    `access`,
    `hits`,
    `rows_per_page`,
    `template`,
    `order_by`,
    `order_dir`,
    `filter_action`,
    `group_by`,
    `private`,
    `params`
    """ + ") VALUES (" + """    
    '%LABEL%',
    '',
    %FORM%,
    '%TABLE_TARGET%',
    '%TABLE_TARGET%.%KEY_FIELD%',
    1,
    2,
    NOW(),
    %CREATED_BY%,
    'Python',
    '0000-00-00 00:00:00',
    0,
    0,
    '0000-00-00 00:00:00',
    1,
    '0000-00-00 00:00:00',
    '0000-00-00 00:00:00',
    1,
    0,
    10,
    'bootstrap',
    '[\"\"]',
    '[\"ASC\"]',
    'onchange',
    '',
    0,
    '{
    \"show-table-filters\":\"1\",
    \"advanced-filter\":\"0\",
    \"advanced-filter-default-statement\":\"=\",
    \"search-mode\":\"0\",
    \"search-mode-advanced\":\"0\",
    \"search-mode-advanced-default\":\"all\",
    \"search_elements\":\"\",
    \"list_search_elements\":\"null\",
    \"search-all-label\":\"All\",
    \"require-filter\":\"0\",
    \"filter-dropdown-method\":\"0\",
    \"toggle_cols\":\"0\",
    \"list_filter_cols\":\"1\",
    \"empty_data_msg\":\"\",
    \"outro\":\"\",
    \"list_ajax\":\"0\",
    \"show-table-add\":\"1\",
    \"show-table-nav\":\"1\",
    \"show_displaynum\":\"1\",
    \"showall-records\":\"1\",
    \"show-total\":\"1\",
    \"sef-slug\":\"\",
    \"show-table-picker\":\"1\",
    \"admin_template\":\"\",
    \"show-title\":\"1\",
    \"pdf\":\"\",
    \"pdf_template\":\"\",
    \"pdf_orientation\":\"portrait\",
    \"pdf_size\":\"a4\",
    \"bootstrap_stripped_class\":\"1\",
    \"bootstrap_bordered_class\":\"0\",
    \"bootstrap_condensed_class\":\"1\",
    \"bootstrap_hover_class\":\"1\",
    \"responsive_elements\":\"\",
    \"responsive_class\":\"\",
    \"list_responsive_elements\":\"null\",
    \"tabs_field\":\"\",
    \"tabs_max\":\"10\",
    \"tabs_all\":\"1\",
    \"list_ajax_links\":\"0\",
    \"actionMethod\":\"default\",
    \"detailurl\":\"\",
    \"detaillabel\":\"\",
    \"list_detail_link_icon\":\"search\",
    \"list_detail_link_target\":\"_self\",
    \"editurl\":\"\",\"editlabel\":\"\",
    \"list_edit_link_icon\":\"edit\",
    \"checkboxLocation\":\"end\",
    \"addurl\":\"\",
    \"addlabel\":\"\",
    \"list_add_icon\":\"plus\",
    \"list_delete_icon\":\"delete\",
    \"popup_width\":\"\",
    \"popup_height\":\"\",
    \"popup_offset_x\":\"\",
    \"popup_offset_y\":\"\",
    \"note\":\"\",
    \"alter_existing_db_cols\":\"default\",
    \"process-jplugins\":\"1\",
    \"cloak_emails\":\"0\",
    \"enable_single_sorting\":\"default\",
    \"collation\":\"utf8_general_ci\",
    \"force_collate\":\"\",
    \"list_disable_caching\":\"0\",
    \"distinct\":\"1\",
    \"group_by_raw\":\"1\",
    \"group_by_access\":\"1\",
    \"group_by_order\":\"\",
    \"group_by_template\":\"\",
    \"group_by_order_dir\":\"ASC\",
    \"group_by_start_collapsed\":\"0\",
    \"group_by_collapse_others\":\"0\",
    \"group_by_show_count\":\"1\",
    \"menu_module_prefilters_override\":\"1\",
    \"prefilter_query\":\"\",
    \"join-display\":\"default\",
    \"delete-joined-rows\":\"0\",
    \"show_related_add\":\"0\",
    \"show_related_info\":\"0\",
    \"rss\":\"0\",
    \"feed_title\":\"\",
    \"feed_date\":\"\",
    \"feed_image_src\":\"\",
    \"rsslimit\":\"150\",
    \"rsslimitmax\":\"2500\",
    \"csv_import_frontend\":\"3\",
    \"csv_export_frontend\":\"2\",
    \"csvfullname\":\"0\",
    \"csv_export_step\":\"100\",
    \"newline_csv_export\":\"nl2br\",
    \"csv_clean_html\":\"leave\",
    \"csv_custom_qs\":\"\",
    \"csv_frontend_selection\":\"0\",
    \"incfilters\":\"0\",\"csv_format\":\"0\",
    \"csv_which_elements\":\"selected\",
    \"show_in_csv\":\"\",
    \"csv_elements\":\"null\",
    \"csv_include_data\":\"1\",
    \"csv_include_raw_data\":\"1\",
    \"csv_include_calculations\":\"0\",
    \"csv_filename\":\"\",
    \"csv_encoding\":\"\",
    \"csv_double_quote\":\"1\",
    \"csv_local_delimiter\":\"\",
    \"csv_end_of_line\":\"n\",
    \"open_archive_active\":\"0\",
    \"open_archive_set_spec\":\"\",
    \"open_archive_timestamp\":\"\",
    \"open_archive_license\":\"http:\\/\\/creativecommons.org\\/licenses\\/by-nd\\/2.0\\/rdf\",
    \"dublin_core_element\":\"\",
    \"dublin_core_type\":\"dc:description.abstract\",
    \"raw\":\"0\",
    \"open_archive_elements\":\"null\",
    \"search_use\":\"0\",
    \"search_title\":\"\",
    \"search_description\":\"\",
    \"search_date\":\"\",
    \"search_link_type\":\"details\",
    \"dashboard\":\"0\",
    \"dashboard_icon\":\"\",
    \"allow_view_details\":\"1\",
    \"allow_edit_details\":\"1\",
    \"allow_edit_details2\":\"\",
    \"allow_add\":\"1\",
    \"allow_delete\":\"2\",
    \"allow_delete2\":\"\",
    \"allow_drop\":\"3\",
    \"isview\":\"0\"
    }'
    """ + ");"
    print(s_sql) # DEBUG
    s_sql = s_sql.replace("%LABEL%",s_lbi)
    s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
    s_sql = s_sql.replace("%FORM%",s_foi)
    s_sql = s_sql.replace("%TABLE_TARGET%",s_tti)
    s_sql = s_sql.replace("%KEY_FIELD%",s_kfi)    
    print(s_sql) # DEBUG
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERT RECORD: "+s_dbi+"."+s_tbi+": "+s_lbi)

    # LIST DEFAULT PARAMETERS
    """
    (38,
    'TEST List',
    '',
    38,
    'ia_finding_6',
    'ia_finding_6.ia_find_auto',
    1,
    2,
    '2019-03-19 22:00:00',
    0,
    '',
    '2019-03-20 05:14:28',
    842,
    0,
    '0000-00-00 00:00:00',
    1,
    '0000-00-00 00:00:00',
    '0000-00-00 00:00:00',
    1,
    0,
    10,
    'bootstrap',
    '[\"\"]',
    '[\"ASC\"]',
    'onchange',
    '',
    0,
    '{
    \"show-table-filters\":\"1\",
    \"advanced-filter\":\"0\",
    \"advanced-filter-default-statement\":\"=\",
    \"search-mode\":\"0\",
    \"search-mode-advanced\":\"0\",
    \"search-mode-advanced-default\":\"all\",
    \"search_elements\":\"\",
    \"list_search_elements\":\"null\",
    \"search-all-label\":\"All\",
    \"require-filter\":\"0\",
    \"filter-dropdown-method\":\"0\",
    \"toggle_cols\":\"0\",
    \"list_filter_cols\":\"1\",
    \"empty_data_msg\":\"\",
    \"outro\":\"\",
    \"list_ajax\":\"0\",
    \"show-table-add\":\"1\",
    \"show-table-nav\":\"1\",
    \"show_displaynum\":\"1\",
    \"showall-records\":\"0\",
    \"show-total\":\"0\",
    \"sef-slug\":\"\",
    \"show-table-picker\":\"1\",
    \"admin_template\":\"\",
    \"show-title\":\"1\",
    \"pdf\":\"\",
    \"pdf_template\":\"\",
    \"pdf_orientation\":\"portrait\",
    \"pdf_size\":\"a4\",
    \"bootstrap_stripped_class\":\"1\",
    \"bootstrap_bordered_class\":\"0\",
    \"bootstrap_condensed_class\":\"0\",
    \"bootstrap_hover_class\":\"1\",
    \"responsive_elements\":\"\",
    \"responsive_class\":\"\",
    \"list_responsive_elements\":\"null\",
    \"tabs_field\":\"\",
    \"tabs_max\":\"10\",
    \"tabs_all\":\"1\",
    \"list_ajax_links\":\"0\",
    \"actionMethod\":\"default\",
    \"detailurl\":\"\",
    \"detaillabel\":\"\",
    \"list_detail_link_icon\":\"search\",
    \"list_detail_link_target\":\"_self\",
    \"editurl\":\"\",\"editlabel\":\"\",
    \"list_edit_link_icon\":\"edit\",
    \"checkboxLocation\":\"end\",
    \"addurl\":\"\",
    \"addlabel\":\"\",
    \"list_add_icon\":\"plus\",
    \"list_delete_icon\":\"delete\",
    \"popup_width\":\"\",
    \"popup_height\":\"\",
    \"popup_offset_x\":\"\",
    \"popup_offset_y\":\"\",
    \"note\":\"\",
    \"alter_existing_db_cols\":\"default\",
    \"process-jplugins\":\"1\",
    \"cloak_emails\":\"0\",
    \"enable_single_sorting\":\"default\",
    \"collation\":\"utf8_general_ci\",
    \"force_collate\":\"\",
    \"list_disable_caching\":\"0\",
    \"distinct\":\"1\",
    \"group_by_raw\":\"1\",
    \"group_by_access\":\"1\",
    \"group_by_order\":\"\",
    \"group_by_template\":\"\",
    \"group_by_order_dir\":\"ASC\",
    \"group_by_start_collapsed\":\"0\",
    \"group_by_collapse_others\":\"0\",
    \"group_by_show_count\":\"1\",
    \"menu_module_prefilters_override\":\"1\",
    \"prefilter_query\":\"\",
    \"join-display\":\"default\",
    \"delete-joined-rows\":\"0\",
    \"show_related_add\":\"0\",
    \"show_related_info\":\"0\",
    \"rss\":\"0\",
    \"feed_title\":\"\",
    \"feed_date\":\"\",
    \"feed_image_src\":\"\",
    \"rsslimit\":\"150\",
    \"rsslimitmax\":\"2500\",
    \"csv_import_frontend\":\"3\",
    \"csv_export_frontend\":\"2\",
    \"csvfullname\":\"0\",
    \"csv_export_step\":\"100\",
    \"newline_csv_export\":\"nl2br\",
    \"csv_clean_html\":\"leave\",
    \"csv_custom_qs\":\"\",
    \"csv_frontend_selection\":\"0\",
    \"incfilters\":\"0\",\"csv_format\":\"0\",
    \"csv_which_elements\":\"selected\",
    \"show_in_csv\":\"\",
    \"csv_elements\":\"null\",
    \"csv_include_data\":\"1\",
    \"csv_include_raw_data\":\"1\",
    \"csv_include_calculations\":\"0\",
    \"csv_filename\":\"\",
    \"csv_encoding\":\"\",
    \"csv_double_quote\":\"1\",
    \"csv_local_delimiter\":\"\",
    \"csv_end_of_line\":\"n\",
    \"open_archive_active\":\"0\",
    \"open_archive_set_spec\":\"\",
    \"open_archive_timestamp\":\"\",
    \"open_archive_license\":\"http:\\/\\/creativecommons.org\\/licenses\\/by-nd\\/2.0\\/rdf\",
    \"dublin_core_element\":\"\",
    \"dublin_core_type\":\"dc:description.abstract\",
    \"raw\":\"0\",
    \"open_archive_elements\":\"null\",
    \"search_use\":\"0\",
    \"search_title\":\"\",
    \"search_description\":\"\",
    \"search_date\":\"\",
    \"search_link_type\":\"details\",
    \"dashboard\":\"0\",
    \"dashboard_icon\":\"\",
    \"allow_view_details\":\"1\",
    \"allow_edit_details\":\"1\",
    \"allow_edit_details2\":\"\",
    \"allow_add\":\"1\",
    \"allow_delete\":\"2\",
    \"allow_delete2\":\"\",
    \"allow_drop\":\"3\",
    \"isview\":\"0\"
    }');
    """

    # GET NEWLY CREATED LIST NUMBER
    curs.execute("SELECT "+s_tbi+".id, "+s_tbi+".label FROM "+s_tbi+" WHERE "+s_tbi+".label = '" + s_lbi +"'")
    for row in curs.fetchall():
        print("Created list "+str(row[0]))
        funcfile.writelog("%t LIST CREATED: "+str(row[0]))
        i_return = row[0]

    # RETURN NEWLY CREATED GROUP NUMBER
    return i_return
