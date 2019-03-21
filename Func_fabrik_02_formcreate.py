""" ****************************************************************************
Script to CREATE Joomla Fabrik form record
Copyright (C) AB Janse van Rensburg 20190310
*****************************************************************************"""

def Fabrik_formcreate(s_input="F",s_fl="New FORM to setup",s_db="Web_ia_joomla",s_tb="ianwu_fabrik_forms"):

    """ PARAMETERS *************************************************************
    s_input = F=do not ask parameters(default) T=ask parameters
    s_fl = Form label
    s_db = Joomla database
    s_tb = Joomla table name
    *************************************************************************"""

    """ INDEX ******************************************************************
    ENVIRONMENT
    INPUT
    OPEN DATABASE
    INSERT GROUP RECORD
    *************************************************************************"""
    print("FABRIK CREATE FORM STEP 2")
    print("-------------------------")
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

    # Input the joomla mysql fabrik FORM name
    s_fli = s_fl
    if s_input == "T":
        print("")
        print("Default:"+s_fl)
        s_fli = input("Fabrik FORM label? ")
        if s_fli == "":
            s_fli = s_fl
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
    INSERT FORM RECORD
    *************************************************************************"""
    print("INSERT FORM RECORD")
    funcfile.writelog("INSERT FORM RECORD")

    # INSERT FORM RECORD
    s_sql = "INSERT INTO `" + s_tbi + "` (" + """
    `label`,
    `record_in_database`,
    `error`,
    `intro`,
    `created`,
    `created_by`,
    `created_by_alias`,
    `modified`,
    `modified_by`,
    `checked_out`,
    `checked_out_time`,
    `publish_up`,
    `publish_down`,
    `reset_button_label`,
    `submit_button_label`,
    `form_template`,
    `view_only_template`,
    `published`,
    `private`,
    `params`
    """ + ") VALUES (" + """
    '%LABEL%',
    1,
    'Some parts of your form have not been correctly filled in',
    '',
    NOW(),
    %CREATED_BY%,
    'Python',
    '0000-00-00 00:00:00',
    0,
    0,
    '0000-00-00 00:00:00',
    '0000-00-00 00:00:00',
    '0000-00-00 00:00:00',
    'Reset',
    'Save',
    'bootstrap',
    'bootstrap',
    1,
    0,
    '{
    \"outro\":\"\",
    \"reset_button\":\"0\",
    \"reset_button_label\":\"Reset\",
    \"reset_button_class\":\"btn-warning\",
    \"reset_icon\":\"\",
    \"reset_icon_location\":\"before\",
    \"copy_button\":\"0\",
    \"copy_button_label\":\"Save as copy\",
    \"copy_button_class\":\"\",
    \"copy_icon\":\"\",
    \"copy_icon_location\":\"before\",
    \"goback_button\":\"0\",
    \"goback_button_label\":\"Go back\",
    \"goback_button_class\":\"\",
    \"goback_icon\":\"\",
    \"goback_icon_location\":\"before\",
    \"apply_button\":\"0\",
    \"apply_button_label\":\"Apply\",
    \"apply_button_class\":\"\",
    \"apply_icon\":\"\",
    \"apply_icon_location\":\"before\",
    \"delete_button\":\"0\",
    \"delete_button_label\":\"Delete\",
    \"delete_button_class\":\"btn-danger\",
    \"delete_icon\":\"\",
    \"delete_icon_location\":\"before\",
    \"submit_button\":\"1\",
    \"submit_button_label\":\"Save\",
    \"save_button_class\":\"btn-primary\",
    \"save_icon\":\"\",
    \"save_icon_location\":\"before\",
    \"submit_on_enter\":\"0\",
    \"labels_above\":\"0\",
    \"labels_above_details\":\"0\",
    \"pdf_template\":\"admin\",
    \"pdf_orientation\":\"portrait\",
    \"pdf_size\":\"letter\",
    \"show_title\":\"1\",
    \"print\":\"\",
    \"email\":\"\",
    \"pdf\":\"\",
    \"admin_form_template\":\"\",
    \"admin_details_template\":\"\",
    \"note\":\"\",
    \"show_referring_table_releated_data\":\"0\",
    \"tiplocation\":\"tip\",
    \"process_jplugins\":\"2\",
    \"ajax_validations\":\"0\",
    \"ajax_validations_toggle_submit\":\"0\",
    \"submit_success_msg\":\"\",
    \"suppress_msgs\":\"0\",
    \"show_loader_on_submit\":\"0\",
    \"spoof_check\":\"1\",
    \"multipage_save\":\"0\"
    }'
    """ + ");"
    #print(s_sql) # DEBUG
    s_sql = s_sql.replace("%LABEL%",s_fli)
    s_sql = s_sql.replace("%CREATED_BY%",s_created_by)
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERT RECORD: " + s_dbi +"."+ s_tbi +":"+ s_fli)

    # FORM DEFAULT PARAMETERS
    """
    (
    38,
    'TEST List',
    1,
    'Some parts of your form have not been correctly filled in',
    '',
    '2019-03-20 05:14:04',
    842,
    'Albertjvr',
    '0000-00-00 00:00:00',
    0,
    0,
    '0000-00-00 00:00:00',
    '0000-00-00 00:00:00',
    '0000-00-00 00:00:00',
    '',
    'Save',
    'bootstrap',
    'bootstrap',
    1,
    0,
    '{
    \"outro\":\"\",
    \"reset_button\":\"0\",
    \"reset_button_label\":\"Reset\",
    \"reset_button_class\":\"btn-warning\",
    \"reset_icon\":\"\",
    \"reset_icon_location\":\"before\",
    \"copy_button\":\"0\",
    \"copy_button_label\":\"Save as copy\",
    \"copy_button_class\":\"\",
    \"copy_icon\":\"\",
    \"copy_icon_location\":\"before\",
    \"goback_button\":\"0\",
    \"goback_button_label\":\"Go back\",
    \"goback_button_class\":\"\",
    \"goback_icon\":\"\",
    \"goback_icon_location\":\"before\",
    \"apply_button\":\"0\",
    \"apply_button_label\":\"Apply\",
    \"apply_button_class\":\"\",
    \"apply_icon\":\"\",
    \"apply_icon_location\":\"before\",
    \"delete_button\":\"0\",
    \"delete_button_label\":\"Delete\",
    \"delete_button_class\":\"btn-danger\",
    \"delete_icon\":\"\",
    \"delete_icon_location\":\"before\",
    \"submit_button\":\"1\",
    \"submit_button_label\":\"Save\",
    \"save_button_class\":\"btn-primary\",
    \"save_icon\":\"\",
    \"save_icon_location\":\"before\",
    \"submit_on_enter\":\"0\",
    \"labels_above\":\"0\",
    \"labels_above_details\":\"0\",
    \"pdf_template\":\"admin\",
    \"pdf_orientation\":\"portrait\",
    \"pdf_size\":\"letter\",
    \"show_title\":\"1\",
    \"print\":\"\",
    \"email\":\"\",
    \"pdf\":\"\",
    \"admin_form_template\":\"\",
    \"admin_details_template\":\"\",
    \"note\":\"\",
    \"show_referring_table_releated_data\":\"0\",
    \"tiplocation\":\"tip\",
    \"process_jplugins\":\"2\",
    \"ajax_validations\":\"0\",
    \"ajax_validations_toggle_submit\":\"0\",
    \"submit_success_msg\":\"\",
    \"suppress_msgs\":\"0\",
    \"show_loader_on_submit\":\"0\",
    \"spoof_check\":\"1\",
    \"multipage_save\":\"0\"
    }'
    );
    """

    # GET NEWLY CREATED FORM NUMBER
    curs.execute("SELECT "+s_tbi+".id, "+s_tbi+".label FROM "+s_tbi+" WHERE "+s_tbi+".label = '" + s_fli +"'")
    for row in curs.fetchall():
        print("Created list "+str(row[0]))
        funcfile.writelog("%t FORM CREATED: "+str(row[0]))
        i_return = row[0]

    # RETURN NEWLY CREATED FORM NUMBER
    return i_return
