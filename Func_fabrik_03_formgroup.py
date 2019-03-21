""" ****************************************************************************
Script to CREATE Joomla Fabrik formgroup record
Copyright (C) AB Janse van Rensburg 20190311
*****************************************************************************"""

def Fabrik_formgroup(s_input="F",s_gr="0",s_fo="0",s_db="Web_ia_joomla",s_tb="ianwu_fabrik_formgroup"):

    """ PARAMETERS *************************************************************
    s_input = F=do not ask parameters(default) T=ask parameters
    s_gr = Group number
    s_fo = Form number
    s_db = Joomla database
    s_tb = Joomla table name
    *************************************************************************"""

    """ INDEX ******************************************************************
    ENVIRONMENT
    INPUT
    OPEN DATABASE
    INSERT FORMGROUP RECORD
    *************************************************************************"""
    print("FABRIK CREATE FORMGROUP STEP 3")
    print("------------------------------")
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
    s_sql = "" #SQL statements
    
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

    # INPUT THE JOOMLA MYSQL FABRIK GROUP NUMBER
    s_gri = s_gr
    if s_input == "T" or s_gri == "0":
        print("")
        print("Default:"+s_gr)
        while s_gri == "" or s_gri == "0":
            s_gri = input("Fabrik GROUP number? ")
        print("")
        
    # INPUT THE JOOMLA MYSQL FABRIK FORM NUMBER
    s_foi = s_fo
    if s_input == "T" or s_foi == "0":
        print("")
        print("Default:"+s_fo)
        while s_foi == "" or s_foi == "0":
            s_foi = input("Fabrik FORM number? ")
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
    INSERT FORMGROUP RECORD
    *************************************************************************"""
    print("INSERT FORMGROUP RECORD")
    funcfile.writelog("INSERT FORMGROUP RECORD")

    # INSERT GROUP RECORD
    s_sql = "INSERT INTO `" + s_tbi + "` (" + """
    form_id,
    group_id,
    ordering
    """ + ") VALUES (" + """
    %FORM%,
    %GROUP%,
    1
    """ + ");"
    #print(s_sql) # DEBUG
    s_sql = s_sql.replace("%FORM%",s_foi)
    s_sql = s_sql.replace("%GROUP%",s_gri)
    # print(s_sql) # DEBUG
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERT RECORD: " + s_dbi +"."+ s_tbi +": Group:"+ s_gri+" Form:"+ s_foi)

    # GET NEWLY CREATED FORMGROUP NUMBER
    s_sql = "SELECT "+s_tbi+".id FROM "+s_tbi+" WHERE "+s_tbi+".form_id=%FORM% AND "+s_tbi+".group_id=%GROUP%"
    s_sql = s_sql.replace("%FORM%",s_foi)
    s_sql = s_sql.replace("%GROUP%",s_gri)
    # print(s_sql) # DEBUG
    curs.execute(s_sql)
    for row in curs.fetchall():
        print("Formgroup "+str(row[0]))
        i_return = row[0]    

    return i_return
