""" FUNCMYSQL ******************************************************************
MYSQL Functions
Copyright (c) AB Janse v Rensburg 2018-10-27
**************************************************************************** """

# Import the system objects
import pyodbc

""" Short description of functions *********************************************
mysql_open 		Open a MYSQL database and return the connection string
**************************************************************************** """


def mysql_open(s_database):
    """
    Open a MYSQL database via ODBC
    :param s_database: Name of the database
    :return: Connection string
    """
    global cnxn
    if s_database == "Web_ia_nwu":
        cnxn = pyodbc.connect("DSN=Web_ia_nwu; PWD=+C8+amXnmdo; Use Procedure Bodies=false;")
    elif s_database == "Web_ia_joomla":
        cnxn = pyodbc.connect("DSN=Web_ia_joomla; PWD=WbNpdPtDd0Q36pfIbXSHv8cAETPY0Ohd;")
    elif s_database == "Mysql_ia_server":
        cnxn = pyodbc.connect("DSN=Mysql_ia_server; PWD=aAbB2957;")
    return cnxn  # Connection


def get_colnames_sqlite_text(os_cur, s_table, s_prefix):
    """
    Function to obtain MYSQL database table column names
    :param os_cur: ODBC Source cursor
    :param s_table: Data table name
    :param s_prefix: Table prefix
    :return: Column headers in text format
    """
    s_data = ""
    for row in os_cur.execute("PRAGMA table_info(" + s_table + ")").fetchall():
        s_data = s_data + "`" + s_prefix + row[1].lower() + "`, "

    return s_data  # Return column headers in text format


def get_coltypes_mysql_list(os_cur, s_schema, s_table):
    """
    Function to obtain MYSQL database table column names
    :param os_cur: ODBC Source cursor
    :param s_schema: Database name
    :param s_table: Data table name
    :return: Column headers in text format
    """

    # print(s_schema)
    # print(s_table)

    a_data = []
    for row in os_cur.execute("SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '"+s_schema+"' AND TABLE_NAME = '"+s_table+"';").fetchall():
        a_data.append(row[0])

    return a_data  # Return column headers in text format


def convert_sqlite_mysql(r_row, a_colt, i_key=1, i_coun=1):
    """
    Function to convert Sqlite field types to Mysql field types
    :param r_row: Schema table row object
    :param a_colt: Table column types
    :param i_key: Key column value
    :param i_coun: Counter value
    :return:
    """

    s_data = "("+str(i_key)+", "
    for member in r_row:
        if type(member) == str and a_colt[i_coun] == "varchar":
            # print("str-varchar")
            s_data = s_data + "'" + member + "', "
        elif type(member) == str and a_colt[i_coun] == "int":
            # print("str-int")
            if member == '':
                s_data = s_data + "0, "
            else:
                s_data = s_data + member + ", "
        elif type(member) == str and a_colt[i_coun] == "decimal":
            # print("str-decimal")
            if member == '':
                s_data = s_data + "0, "
            else:
                s_data = s_data + member + ", "
        elif type(member) == str and a_colt[i_coun] == "date":
            # print("str-date")
            if member == '':
                s_data = s_data + "'0', "
            else:
                s_data = s_data + "'" + member + "', "
        elif type(member) == str and a_colt[i_coun] == "datetime":
            # print("str-datetime")
            if member == '':
                s_data = s_data + "'0', "
            else:
                s_data = s_data + "'" + member + "', "
        elif type(member) == int and a_colt[i_coun] == "int":
            # print("int-int")
            s_data = s_data + str(member) + ", "
        elif type(member) == int and a_colt[i_coun] == "varchar":
            # print("int-varchar")
            s_data = s_data + "'" + str(member) + "', "
        elif type(member) == float and a_colt[i_coun] == "decimal":
            # print("float-decimal")
            s_data = s_data + str(member) + ", "
        elif member is None and a_colt[i_coun] == "varchar":
            # print("none-varchar")
            s_data = s_data + "'', "
        elif member is None and a_colt[i_coun] == "int":
            # print("none-int")
            s_data = s_data + "0, "
        elif member is None and a_colt[i_coun] == "decimal":
            # print("none-decimal")
            s_data = s_data + "0, "
        elif member is None and a_colt[i_coun] == "date":
            # print("none-date")
            s_data = s_data + "'0', "
        elif member is None and a_colt[i_coun] == "datetime":
            # print("none-datetime")
            s_data = s_data + "'0', "
        else:
            print(type(member))
            print(member)
            print(a_colt[i_coun])
            s_data = s_data + "'', "
        # print(member)
        i_coun = i_coun + 1
    s_data = s_data.rstrip(", ") + ")"

    return s_data
