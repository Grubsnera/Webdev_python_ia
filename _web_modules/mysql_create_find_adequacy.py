"""
Copyright (c) Albert B Janse van Rensburg, 15 Mar 2022
"""

# Define python system objects
# import sys
# import pyodbc

# Define Functions
from _my_modules import funcmysql
from _my_modules import funcfile

"""  Index - list of tables created
FINDING_ADEQUACY (Table to store finding adequacy)
"""


def find_adequacy(s_database: str = "", s_drop_table: str = "", s_add_data: str = ""):
    """
    Script to build FINDING ADEQUACY table with contents
    :param s_database: Database in which to create the table
    :param s_drop_table: Should table be dropped? (y/n)
    :param s_add_data: Should default data be added? (y/n)
    :return: Nothing
    """

    # Declare variables
    l_debug: bool = False
    sd_database: str = "Web_ia_nwu"
    sd_drop_table: str = "n"
    sd_add_data: str = "n"

    if l_debug:
        print("WEB_IA_NWU INPUTS")
        print("-----------------")

    # Input the ia DATABASE name
    if l_debug or s_database == "":
        print("")
        print("Default:" + sd_database)
    if s_database == "": 
        s_database = input("IA DATABASE name? ")
    if s_database == "":
        s_database = sd_database

    # Input the whether tables must be overwritten
    if l_debug or s_drop_table == "":
        print("")
        print("Default:" + sd_drop_table)
    if s_drop_table == "":
        s_drop_table = input("DROP Table (y/n)? ")
    if s_drop_table == "":
        s_drop_table = sd_drop_table

    # Input the whether default fields should be added
    if l_debug or s_add_data == "":
        print("")
        print("Default:" + sd_add_data)
    if s_add_data == "":
        s_add_data = input("ADD default fields (y/n)? ")
    if s_add_data == "":
        s_add_data = sd_add_data

    # Script log file
    funcfile.writelog("Now")
    funcfile.writelog("SCRIPT: WEB_IA_NWU")
    funcfile.writelog("------------------")

    # Connect to the oracle database
    cnxn = funcmysql.mysql_open(s_database)
    curs = cnxn.cursor()
    if l_debug:
        print("Open the database...")
    funcfile.writelog("%t OPEN DATABASE: " + s_database)

    # Create FINDING_ADEQUACY table *******************************************
    if s_drop_table == "y":
        curs.execute("DROP TABLE IF EXISTS ia_finding_adequacy_test")
        funcfile.writelog("%t DROPPED TABLE: FINDING_ADEQUACY(ia_finding_adequacy)")
    s_sql: str = """
    CREATE TABLE IF NOT EXISTS ia_finding_adequacy_test (
    ia_findadeq_auto INT(11) NOT NULL AUTO_INCREMENT,
    ia_findadeq_name VARCHAR(50) NOT NULL,
    ia_findadeq_desc TEXT NOT NULL,
    ia_findadeq_active TEXT NOT NULL,
    ia_findadeq_from DATETIME NOT NULL,
    ia_findadeq_to DATETIME NOT NULL,
    ia_findadeq_createdate DATETIME,
    ia_findadeq_createby VARCHAR(50),
    ia_findadeq_editdate DATETIME,
    ia_findadeq_editby VARCHAR(50),
    PRIMARY KEY (ia_findadeq_auto),
    INDEX fb_order_ia_findadeq_name_INDEX (ia_findadeq_name),
    INDEX fb_order_ia_findadeq_from_INDEX (ia_findadeq_from)
    )
    ENGINE = InnoDB
    CHARSET=utf8mb4
    COLLATE utf8mb4_unicode_ci
    COMMENT = 'Table to store finding adequacy lists.'
    """ + ";"
    curs.execute(s_sql)
    funcfile.writelog("%t CREATED TABLE: FINDING_ADEQUACY(ia_finding_adequacy)")

    # Insert FINDING_ADEQUACY data
    if s_add_data == "y":
        s_sql = """
        INSERT INTO `ia_finding_adequacy_test`
        (`ia_findadeq_name`,
        `ia_findadeq_desc`,
        `ia_findadeq_active`,
        `ia_findadeq_from`,
        `ia_findadeq_to`,
        `ia_findadeq_createdate`,
        `ia_findadeq_createby`)
        VALUES
        ('Adequate', 'Control is adequate to mitigate the risk.', '1', NOW(), '2099-12-31 00:00:00', NOW(), 'Python'),
        ('Inadequate', 'Control is not adequate to mitigate the risk.', '1', NOW(), '2099-12-31 00:00:00', NOW(), 'Python')
        """ + ";"
        curs.execute(s_sql)
        cnxn.commit()
        funcfile.writelog("%t INSERTED DATA: FINDING_ADEQUACY(ia_finding_adequacy)")

    # ******************************************************************************

    # Script log file
    funcfile.writelog("---------------------")
    funcfile.writelog("COMPLETED: WEB_IA_NWU")

    return


if __name__ == '__main__':
    try:
        find_adequacy()
        # Test automated function - delete and create new table with data
        # find_adequacy("Web_ia_nwu", "y", "y")
    finally:
        print("")
