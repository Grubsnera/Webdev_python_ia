""" ****************************************************************************
Script to CREATE Joomla Fabrik group record
Copyright (C) AB Janse van Rensburg 20190308
*****************************************************************************"""

def Fabrik_groupcreate(s_input="F",s_lb="New GROUP to setup",s_db="Web_ia_joomla",s_tb="ianwu_fabrik_groups"):

    """ PARAMETERS *************************************************************
    s_input = F=do not ask parameters(default) T=ask parameters
    s_lb = Group label
    s_db = Joomla database
    s_tb = Joomla table name
    *************************************************************************"""

    """ INDEX ******************************************************************
    ENVIRONMENT
    INPUT
    OPEN DATABASE
    INSERT GROUP RECORD
    *************************************************************************"""
    print("FABRIK CREATE GROUP STEP 1")
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

    # Input the joomla mysql fabrik DATABASE name
    s_dbi = s_db
    if s_input == "T":
        print("")
        print("Default:"+s_db)
        s_dbi = input("Fabrik DATABASE name? ")
        if s_dbi == "":
            s_dbi = s_db

    # Input the joomla mysql fabrik TABLE name
    s_tbi = s_tb
    if s_input == "T":
        print("")
        print("Default:"+s_tb)
        s_tbi = input("Fabrik TABLE name? ")
        if s_tbi == "":
            s_tbi = s_tb

    # Input the joomla mysql fabrik GROUP label
    s_lbi = s_lb
    if s_input == "T":
        print("")
        print("Default:"+s_lb)
        s_lbi = input("Fabrik GROUP label? ")
        if s_lbi == "":
            s_lbi = s_lb
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
    INSERT GROUP RECORD
    *************************************************************************"""
    print("INSERT GROUP RECORD")
    funcfile.writelog("INSERT GROUP RECORD")

    # INSERT GROUP RECORD
    s_sql = "INSERT INTO `" + s_tbi + "` (" + """
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
    #print(s_sql) # DEBUG
    s_sql = s_sql.replace("%LABEL%",s_lbi)
    s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERT RECORD: "+s_dbi+"."+s_tbi+": "+s_lbi)

    # GROUP DEFAULT PARAMETERS
    """
    (
    92,
    'TEST List',
    '',
    'TEST List',
    1,
    '2019-03-20 05:14:04',
    842,
    'Albertjvr',
    '0000-00-00 00:00:00',
    0,
    0,
    '0000-00-00 00:00:00',
    0,
    0,
    '{
    \"split_page\":\"0\",
    \"list_view_and_query\":\"1\",
    \"access\":\"1\",\"intro\":\"\",
    \"outro\":\"\",
    \"repeat_group_button\":0,
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
    \"repeat_group_show_first\":1,
    \"random\":\"0\",
    \"labels_above\":\"-1\",
    \"labels_above_details\":\"-1\"
    }'
    );
    """

    # GET NEWLY CREATED GROUP NUMBER
    curs.execute("SELECT "+s_tbi+".id, "+s_tbi+".name FROM "+s_tbi+" WHERE "+s_tbi+".name = '" + s_lbi +"'")
    for row in curs.fetchall():
        print("Created group "+str(row[0]))
        funcfile.writelog("%t GROUP CREATED: "+str(row[0]))
        i_return = row[0]

    # RETURN NEWLY CREATED GROUP NUMBER
    return i_return
