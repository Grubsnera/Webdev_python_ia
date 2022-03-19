"""
Script to test various MYSQL Functions
Copyright (c) Albert B Janse van Rensburg, 1 Nov 2018
"""

""" Listing of TABLES created

FINDING (Table to store findings)
PEOPLE (Table to store people) See python B001_people_lists
USER (Table to store users)
ASSIGNMENT (Table to store the assignments)
ASSIGNMENT_CATEGORY (Table to store assignment categories)
ASSIGNMENT_TYPE (Table to store the assignment types)
ASSIGNMENT_STATUS (Table to store the assignment status)
ASSIGNMENT_ORIGIN (Table to store assignment origins)
ASSIGNMENT_SITE (Table to store the assignment site or location)
ASSIGNMENT_REPORT (Table to store assignment report to whom)
FINDING_RATE (Impact ratings for each audit finding)
FINDING_STATUS (Status for each audit finding)
FINDING_RESPONSE (Audit finding responses)

"""

# Define python system objects
import sys

# Add own module path
sys.path.append('S:/_my_modules')

# Import python objects
import pyodbc

# Define Functions
import funcmysql
import funcfile

# Declare variables
sd_database = "Web_ia_nwu"
sd_droptable = "n"
sd_addfields = "n"
s_sql = "" #SQL statements

print("WEB_IA_NWU INPUTS")
print("-----------------")

# Input the ia DATABASE name
print("")
print("Default:"+sd_database)
s_database = input("IA DATABASE name? ")
if s_database == "":
    s_database = sd_database

# Input the whether tables must be overwritten
print("")
print("Default:"+sd_droptable)
s_droptable = input("DROP Tables (y/n)? ")
if s_droptable == "":
    s_droptable = sd_droptable

# Input the whether default fields should be added
print("")
print("Default:"+sd_addfields)
s_addfields = input("ADD default fields (y/n)? ")
if s_addfields == "":
    s_addfields = sd_addfields

# Script log file
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: WEB_IA_NWU")
funcfile.writelog("------------------")

# Connect to the oracle database
cnxn = funcmysql.mysql_open(s_database)
curs = cnxn.cursor()
funcfile.writelog("%t OPEN DATABASE: " + s_database)






# Create FINDING table ************************************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_finding")
    funcfile.writelog("%t DROPPED TABLE: FINDING(ia_finding)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_finding (
`ia_find_auto` int(11) NOT NULL,
`ia_assi_auto` int(11) NOT NULL,
`ia_user_numb` int(11) NOT NULL,
`ia_find_date` datetime NOT NULL,
`ia_find_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_pare` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_list` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_disp` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_edit` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_detl` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_findstat_auto` int(11) NOT NULL,
`ia_findrate_auto` int(11) NOT NULL,
`ia_find_stat` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_stattext` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_mailfrom` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_updated` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_updatedate` datetime DEFAULT NULL,
`ia_find_cron` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_desc` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_criteria` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_condition` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_effect` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_cause` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_risk` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_recommend` text COLLATE utf8mb4_unicode_ci NOT NULL,
`ia_find_r1_mailflag` text COLLATE utf8mb4_unicode_ci,
`ia_find_r1_maildate` datetime DEFAULT NULL,
`ia_find_r1_mailto` int(11) DEFAULT NULL,
`ia_find_r1_send` text COLLATE utf8mb4_unicode_ci,
`ia_find_r1_opendate` datetime DEFAULT NULL,
`ia_find_r1_respauto` int(11) DEFAULT NULL,
`ia_find_r1_respcomm` text COLLATE utf8mb4_unicode_ci,
`ia_find_r1_respresp` text COLLATE utf8mb4_unicode_ci,
`ia_find_r1_respacti` text COLLATE utf8mb4_unicode_ci,
`ia_find_r1_respactd` datetime DEFAULT NULL,
`ia_find_r1_respdate` datetime DEFAULT NULL,
`ia_find_r1_audicomm` text COLLATE utf8mb4_unicode_ci,
`ia_find_createdate` datetime NOT NULL,
`ia_find_createby` int(11) NOT NULL,
`ia_find_editdate` datetime NOT NULL,
`ia_find_editby` int(11) NOT NULL,
PRIMARY KEY (`ia_find_auto`),
INDEX `fb_order_ia_find_date_INDEX` (`ia_find_date`),
INDEX `fb_order_ia_find_name_INDEX` (`ia_find_name`),
INDEX `fb_groupby_ia_assi_auto_INDEX` (`ia_assi_auto`),
INDEX `fb_prefilter_ia_find_stat_INDEX` (`ia_find_stat`(10)),
INDEX `fb_prefilter_ia_find_r1_maildate_INDEX` (`ia_find_r1_maildate`)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store audit findings'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: USER(ia_finding)")

# Insert FINDING data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_finding` (`ia_find_auto`, `ia_assi_auto`, `ia_user_numb`, `ia_find_date`, `ia_find_name`, `ia_find_pare`, `ia_find_list`, `ia_find_disp`, `ia_find_edit`, `ia_find_detl`, `ia_findstat_auto`, `ia_findrate_auto`, `ia_find_stat`, `ia_find_stattext`, `ia_find_mailfrom`, `ia_find_updated`, `ia_find_updatedate`, `ia_find_cron`, `ia_find_desc`, `ia_find_criteria`, `ia_find_condition`, `ia_find_effect`, `ia_find_cause`, `ia_find_risk`, `ia_find_recommend`, `ia_find_r1_mailflag`, `ia_find_r1_maildate`, `ia_find_r1_mailto`, `ia_find_r1_send`, `ia_find_r1_opendate`, `ia_find_r1_respauto`, `ia_find_r1_respcomm`, `ia_find_r1_respresp`, `ia_find_r1_respacti`, `ia_find_r1_respactd`, `ia_find_r1_respdate`, `ia_find_r1_audicomm`, `ia_find_createdate`, `ia_find_createby`, `ia_find_editdate`, `ia_find_editby`) VALUES
    (1, 4, 855, '2018-01-01 00:00:00', 'Employee list (detail)', '', '{\"label\":\"Parent list of all findings\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\"}', '{\"label\":\"Audit finding detail\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\\/details\\/21\\/1\"}', '{\"label\":\"reply to audit finding\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\\/form\\/21\\/1\"}', '{\"label\":\"Employee list (detail)\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-repo\\/menu-repo-peop\\/menu-repo-peop-empl-detl\"}', 2, 1, '5', '5 Comment', '1', '1', '2018-12-07 03:51:59', '1', 'List of North-West University employees with personal detail.', 'Alle employees updated every 24 hours.', '', '', '', '', 'None!\r\n\r\nThis finding / list is for information purposes only. You do not have to comment or take any actions.', '1', '2018-12-06 00:00:00', 855, '0', '0000-00-00 00:00:00', 1, '', '', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '', '2018-01-01 00:00:00', 854, '0000-00-00 00:00:00', 855),
    (2, 4, 855, '2018-01-01 00:00:00', 'Employee list (summary)', '', '{\"label\":\"Parent list of all audit findings\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\"}', '{\"label\":\"Audit finding detail\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\\/details\\/21\\/2\"}', '{\"label\":\"reply to audit finding\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\\/form\\/21\\/2\"}', '{\"label\":\"Employee list\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-repo\\/menu-repo-peop\\/menu-repo-peop-empl-list\"}', 2, 1, '5', '5 Comment', '1', '1', '2018-12-07 03:51:59', '0', 'List of North-West University employees without personal detail.', 'Alle employees updated every 24 hours.', '', '', '', '', 'None!\r\n\r\nThis finding / list is for information purposes only. You do not have comment or take any actions.', '1', '2018-12-06 00:00:00', 855, '0', '0000-00-00 00:00:00', 1, '', '', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '', '2018-01-01 00:00:00', 854, '0000-00-00 00:00:00', 855),
    (3, 4, 855, '2018-01-01 00:00:00', 'Employee birthdays', '', '{\"label\":\"Parent list of all findings\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\"}', '{\"label\":\"Audit finding detail\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\\/details\\/21\\/3\"}', '{\"label\":\"reply to audit finding\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\\/form\\/21\\/3\"}', '{\"label\":\"Employee birthdays\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-repo\\/menu-repo-peop\\/menu-repo-peop-birt\"}', 2, 1, '5', '5 Comment', '1', '1', '2018-12-07 00:00:00', '0', 'A list of employees whos birthday anniversary is today.', 'All current employees born today.', '', '', '', '', 'None!\r\n\r\nThis finding / list is for information purposes only. You do not have to comment or take any actions.', '1', '2018-12-07 00:00:00', 873, '1', '0000-00-00 00:00:00', 0, '', '', '', '2018-12-05 00:00:00', '2018-12-05 00:00:00', '', '2018-01-01 00:00:00', 854, '0000-00-00 00:00:00', 855),
    (4, 4, 855, '2018-01-01 00:00:00', 'Employee hierarchy', '', '{\"label\":\"Parent list of all findings\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\"}', '{\"label\":\"Audit finding detail\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\\/details\\/21\\/4\"}', '{\"label\":\"reply to audit finding\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-admi\\/menu-admi-finding\\/form\\/21\\/4\"}', '{\"label\":\"Employee hierarchy\",\"link\":\"http:\\/\\/ia-nwu.co.za\\/index.php\\/menu-repo\\/menu-repo-peop\\/menu-repo-peop-empl-hier\"}', 2, 1, '5', '5 Comment', '1', '1', '2018-12-07 03:52:38', '0', 'The current employee hierarchy.', 'All current employees.', '', '', '', '', 'None!\r\n\r\nThis finding / list is for information purposes only. You do not have to comment or take any actions.', '1', '2018-12-06 00:00:00', 855, '0', '0000-00-00 00:00:00', 1, '', '', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '', '2018-01-01 00:00:00', 854, '0000-00-00 00:00:00', 855)
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: USER(ia_user)")





# Create USER table ************************************************************
if s_droptable == "x":
    curs.execute("DROP TABLE IF EXISTS ia_user")
    funcfile.writelog("%t DROPPED TABLE: USER(ia_user)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_user (
ia_user_id INT(11) NOT NULL AUTO_INCREMENT,
ia_user_sysid INT(11) NOT NULL,
ia_user_empl VARCHAR(150) NOT NULL,
ia_user_numb VARCHAR(150) NOT NULL,
ia_user_name VARCHAR(150) NOT NULL,
ia_user_pass VARCHAR(100) NOT NULL,
ia_user_mail VARCHAR(100) NOT NULL,
ia_user_block TINYINT(4) NOT NULL,
ia_user_group TEXT NOT NULL,
ia_user_position VARCHAR(150) NOT NULL,
ia_user_active TEXT NOT NULL,
ia_user_from DATETIME NOT NULL,
ia_user_to DATETIME NOT NULL,
ia_user_createdate DATETIME NOT NULL,
ia_user_createby INT(11) NOT NULL,
ia_user_editdate DATETIME NOT NULL,
ia_user_editby INT(11) NOT NULL,
PRIMARY KEY (ia_user_id),
INDEX fb_order_ia_user_name_INDEX (ia_user_name),
INDEX fb_order_ia_user_from_INDEX (ia_user_from)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store users'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: USER(ia_user)")

# Insert USER data
if s_addfields == "x":
    s_sql = """
    INSERT INTO `ia_user`
    (`ia_user_sysid`, `ia_user_empl`, `ia_user_numb`, `ia_user_name`, `ia_user_pass`, `ia_user_mail`, `ia_user_block`, `ia_user_group`, `ia_user_position`, `ia_user_active`, `ia_user_from`, `ia_user_to`, `ia_user_createdate`, `ia_user_createby`, `ia_user_editdate`, `ia_user_editby`)
    VALUES
    (855, '21162395', '21162395', 'Albert', '', '21162395@nwu.ac.za', 0, '4', 'NWU Internal Audit: Senior Internal Auditor', '1', '2007-08-01 00:00:00', '2099-12-31 00:00:00', '2018-01-01 00:00:00', 854, '2018-11-27 09:53:44', 855),
    (871, '12119180', '12119180', 'Nicolene', '', '12119180@nwu.ac.za', 0, '4', 'NWU Internal Audit: Audit Manager', '1', '2008-02-01 00:00:00', '2099-12-31 00:00:00', '2018-01-01 00:00:00', 854, '2018-11-27 09:53:10', 855),
    (864, '12788074', '12788074', 'Yolandie', '', '12788074@nwu.ac.za', 0, '4', 'NWU Internal Audit: Senior Internal Auditor', '1', '2012-09-01 00:00:00', '2099-12-31 00:00:00', '2018-01-01 00:00:00', 854, '2018-11-27 09:53:25', 855),
    (870, '13000063', '13000063', 'MNR AL PRINSLOO', '', '13000063@@nwu.ac.za', 0, '3', '', '1', '2012-09-01 00:00:00', '2099-12-31 00:00:00', '2018-01-01 00:00:00', 854, '2018-01-01 00:00:00', 854)
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: USER(ia_user)")

# Create ASSIGNMENT table ************************************************************
if s_droptable == "x":
    curs.execute("DROP TABLE IF EXISTS ia_assignment")
    funcfile.writelog("%t DROPPED TABLE: ASSIGNMENT(ia_assignment)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_assignment (
ia_assi_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_assi_loaddate DATETIME NOT NULL,
ia_assi_year INT(4) NOT NULL,
ia_assitype_auto INT(11) NOT NULL,
ia_assiorig_auto INT(11) NOT NULL,
ia_assisite_auto INT(11) NOT NULL,
ia_assicate_auto INT(11) NOT NULL,
ia_assirepo_auto INT(11) NOT NULL,
ia_assistat_auto INT(11) NOT NULL,
ia_user_numb INT(11) NOT NULL,
ia_assi_priority TEXT NOT NULL,
ia_assi_name VARCHAR(150) NOT NULL,
ia_assi_desc TEXT,
ia_assi_report TEXT,
ia_assi_startdate DATETIME,
ia_assi_completedate DATETIME,
ia_assi_findingdate DATETIME,
ia_assi_proofdate DATETIME,
ia_assi_commentdate DATETIME,
ia_assi_finishdate DATETIME,
ia_assi_createdate DATETIME,
ia_assi_createby VARCHAR(50),
ia_assi_editdate DATETIME,
ia_assi_editby VARCHAR(50),
PRIMARY KEY (ia_assi_auto),
INDEX fb_order_ia_user_numb_INDEX (ia_user_numb),
INDEX fb_order_ia_assi_year_INDEX (ia_assi_year),
INDEX fb_order_ia_assi_name_INDEX (ia_assi_name),
INDEX fb_order_ia_assi_startdate_INDEX (ia_assi_startdate)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store assignments'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: ASSIGNMENT(ia_assignment)")    

# Create ASSIGNMENT_CATEGORY table *********************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_assignment_category")
    funcfile.writelog("%t DROPPED TABLE: ASSIGNMENT_CATEGORY(ia_assignment_category)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_assignment_category (
ia_assicate_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_assicate_name VARCHAR(50) NOT NULL,
ia_assicate_desc TEXT,
ia_assicate_active TEXT NOT NULL,
ia_assicate_private TEXT NOT NULL,
ia_assicate_from DATETIME NOT NULL,
ia_assicate_to DATETIME NOT NULL,
ia_assicate_createdate DATETIME,
ia_assicate_createby VARCHAR(50),
ia_assicate_editdate DATETIME,
ia_assicate_editby VARCHAR(50),
PRIMARY KEY (ia_assicate_auto),
INDEX fb_order_ia_assicate_name_INDEX (ia_assicate_name),
INDEX fb_order_ia_assicate_from_INDEX (ia_assicate_from)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store assignment categories'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: ASSIGNMENT_CATEGORY(ia_assignment_category)")

# Insert ASSIGNMENT_CATEGORY data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_assignment_category`
    (`ia_assicate_name`, `ia_assicate_desc`, `ia_assicate_active`, `ia_assicate_private`, `ia_assicate_from`, `ia_assicate_to`, `ia_assicate_createdate`, `ia_assicate_createby`)
    VALUES
    ('Assignment', 'Audit assignment', '1', '0', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Administration', 'Office administration', '1', '0', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Private', 'Private work', '1', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Consultation', 'Consultation work', '1', '0', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Development', 'Software development', '1', '0', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python')
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: ASSIGNMENT_CATEGORY(ia_assignment_category)")

# Create ASSIGNMENT_TYPE table ***********************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_assignment_type")
    funcfile.writelog("%t DROPPED TABLE: ASSIGNMENT_STATUS(ia_assignment_type)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_assignment_type (
ia_assitype_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_assicate_auto INT(11) NOT NULL,
ia_assitype_file VARCHAR(20),
ia_assitype_name VARCHAR(50) NOT NULL,
ia_assitype_desc TEXT,
ia_assitype_active TEXT NOT NULL,
ia_assitype_from DATETIME NOT NULL,
ia_assitype_to DATETIME NOT NULL,
ia_assitype_createdate DATETIME,
ia_assitype_createby VARCHAR(50),
ia_assitype_editdate DATETIME,
ia_assitype_editby VARCHAR(50),
PRIMARY KEY (ia_assitype_auto),
INDEX fb_order_ia_assitype_name_INDEX (ia_assitype_name),
INDEX fb_order_ia_assitype_from_INDEX (ia_assitype_from),
INDEX fb_groupby_ia_assicate_auto_INDEX (ia_assicate_auto)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store the assignment types'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: ASSIGNMENT_STATUS(ia_assignment_type)")

# Insert ASSIGNMENT_TYPE data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_assignment_type`
    (`ia_assicate_auto`, `ia_assitype_file`, `ia_assitype_name`, `ia_assitype_desc`, `ia_assitype_active`, `ia_assitype_from`, `ia_assitype_to`, `ia_assitype_createdate`, `ia_assitype_createby`)
    VALUES
    (1, '2.9.3.3.', 'Followup audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '2.9.3.4.', 'Assurance audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '2.9.3.5.', 'Adhoc audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '2.9.3.6.', 'Special Investigation audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '2.9.3.7.', 'Compliance audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '2.9.3.8.', 'Verification audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '2.9.3.9.', 'Yearend audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '2.9.3.10.', 'Significant Finding audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '2.9.3.12.', 'Continuous audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '2.9.3.13.', 'IT audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Collegue support', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Event organization', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'File review', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Filing', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Finance', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'General', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Hardware support', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Leave afternoon', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Leave all other', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Management review', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Meeting management', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Meeting office', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Social', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Software support', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Training prepare', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Training present', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Training receive', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Travel', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '', 'Tender', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Afternoon', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Break', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Family', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Leave', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Lunch', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Medical', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Other', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Private', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Social', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, '', 'Telephone', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, '', 'External', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, '', 'Internal', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '', 'Audit tests', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '', 'Data manipulation', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '', 'Software inhouse', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '', 'Software audit', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python')
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: ASSIGNMENT_STATUS(ia_assignment_type)")

# Create ASSIGNMENT_STATUS table ***********************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_assignment_status")
    funcfile.writelog("%t DROPPED TABLE: ASSIGNMENT_STATUS(ia_assignment_status)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_assignment_status (
ia_assistat_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_assicate_auto INT(11) NOT NULL,
ia_assistat_name VARCHAR(50) NOT NULL,
ia_assistat_desc TEXT,
ia_assistat_active TEXT NOT NULL,
ia_assistat_from DATETIME NOT NULL,
ia_assistat_to DATETIME NOT NULL,
ia_assistat_createdate DATETIME,
ia_assistat_createby VARCHAR(50),
ia_assistat_editdate DATETIME,
ia_assistat_editby VARCHAR(50),
PRIMARY KEY (ia_assistat_auto),
INDEX fb_order_ia_assistat_name_INDEX (ia_assistat_name),
INDEX fb_order_ia_assistat_from_INDEX (ia_assistat_from),
INDEX fb_groupby_ia_assicate_auto_INDEX (ia_assicate_auto)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store the assignment status'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: ASSIGNMENT_STATUS(ia_assignment_status)")

# Insert ASSIGNMENT_STATUS data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_assignment_status`
    (`ia_assicate_auto`, `ia_assistat_name`, `ia_assistat_desc`, `ia_assistat_active`, `ia_assistat_from`, `ia_assistat_to`, `ia_assistat_createdate`, `ia_assistat_createby`)
    VALUES
    (1, '00 Deferred', 'Assignment deferred to a later period.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '00 Not started', 'Assignment not yet started.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '01 In progress', 'Assignment started and is in progress.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '10 Planning', 'Assignment in planning phase.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '50 Fieldwork phase', 'Assignment at fieldwork phase.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '80 Draft report', 'Assignment at draft report stage.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '85 Awaiting client', 'Waiting for client for reason specified in notes.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '90 Management comment', 'Waiting for client to deliver management comments.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '95 Client Satisfaction Survey', 'Waiting for client to complete client satisfaction survey.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, '99 Completed', 'Assignment completed.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '0 Deferred', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '0 Not started', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '1 Planning', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '2 Meeting', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '3 Fieldwork', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '4 Reporting', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, '9 Completed', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, 'Private', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, '0 Deferred', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, '0 Not started', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, '1 Planning', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, '2 Meeting', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, '3 Fieldwork', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, '4 Reporting', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, '9 Completed', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '0 Deferred', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '0 Not started', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '1 Administration', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '2 Planning', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '3 Fieldwork', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '4 Reporting', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, '9 Completed', '', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python')
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: ASSIGNMENT_STATUS(ia_assignment_status)")

# Create ASSIGNMENT_ORIGIN table ***********************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_assignment_origin")
    funcfile.writelog("%t DROPPED TABLE: ASSIGNMENT_ORIGIN(ia_assignment_origin)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_assignment_origin (
ia_assiorig_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_assiorig_name VARCHAR(50) NOT NULL,
ia_assiorig_desc TEXT,
ia_assiorig_active TEXT NOT NULL,
ia_assiorig_from DATETIME NOT NULL,
ia_assiorig_to DATETIME NOT NULL,
ia_assiorig_createdate DATETIME,
ia_assiorig_createby VARCHAR(50),
ia_assiorig_editdate DATETIME,
ia_assiorig_editby VARCHAR(50),
PRIMARY KEY (ia_assiorig_auto),
INDEX fb_order_ia_assiorig_name_INDEX (ia_assiorig_name),
INDEX fb_order_ia_assiorig_from_INDEX (ia_assiorig_from)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store assignment origins'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: ASSIGNMENT_ORIGIN(ia_assignment_origin)")

# Insert ASSIGNMENT_ORIGIN data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_assignment_origin`
    (`ia_assiorig_name`, `ia_assiorig_desc`, `ia_assiorig_active`, `ia_assiorig_from`, `ia_assiorig_to`, `ia_assiorig_createdate`, `ia_assiorig_createby`)
    VALUES
    ('Adhoc', 'Adhoc assignments', '1','2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Administration', 'Admin tasks', '1','2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Audit plan', 'Audit plan tasks', '1','2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Other', 'Non audit tasks', '1','2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Management', 'Tasks requested by management', '1','2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Anonymous', 'Reporting box', '1','2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Risk', 'Risk register', '1','2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python')
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: ASSIGNMENT_ORIGIN(ia_assignment_origin)")

# Create ASSIGNMENT_SITE table ***********************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_assignment_site")
    funcfile.writelog("%t DROPPED TABLE: ASSIGNMENT_SITE(ia_assignment_site)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_assignment_site (
ia_assisite_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_assisite_name VARCHAR(50) NOT NULL,
ia_assisite_desc TEXT,
ia_assisite_active TEXT NOT NULL,
ia_assisite_from DATETIME NOT NULL,
ia_assisite_to DATETIME NOT NULL,
ia_assisite_createdate DATETIME,
ia_assisite_createby VARCHAR(50),
ia_assisite_editdate DATETIME,
ia_assisite_editby VARCHAR(50),
PRIMARY KEY (ia_assisite_auto),
INDEX fb_order_ia_assisite_name_INDEX (ia_assisite_name),
INDEX fb_order_ia_assisite_from_INDEX (ia_assisite_from)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store the assignment site or location'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: ASSIGNMENT_SITE(ia_assignment_site)")

# Insert ASSIGNMENT_SITE data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_assignment_site`
    (`ia_assisite_name`, `ia_assisite_desc`, `ia_assisite_active`, `ia_assisite_from`, `ia_assisite_to`, `ia_assisite_createdate`, `ia_assisite_createby`)
    VALUES
    ('Nwu', 'NWU Organization', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Nwu Potchefstroom', 'Potchefstroom Campus', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Nwu Mafikeng', 'Mafikeng Campus', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Nwu Vaal', 'Vaal Triangle Campus', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python')    
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: ASSIGNMENT_SITE(ia_assignment_site)")

# Create ASSIGNMENT_REPORT table ***********************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_assignment_report")
    funcfile.writelog("%t DROPPED TABLE: ASSIGNMENT_REPORT(ia_assignment_report)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_assignment_report (
ia_assirepo_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_assirepo_name VARCHAR(50) NOT NULL,
ia_assirepo_desc TEXT,
ia_assirepo_active TEXT NOT NULL,
ia_assirepo_from DATETIME NOT NULL,
ia_assirepo_to DATETIME NOT NULL,
ia_assirepo_createdate DATETIME,
ia_assirepo_createby VARCHAR(50),
ia_assirepo_editdate DATETIME,
ia_assirepo_editby VARCHAR(50),
PRIMARY KEY (ia_assirepo_auto),
INDEX fb_order_ia_assirepo_name_INDEX (ia_assirepo_name),
INDEX fb_order_ia_assirepo_from_INDEX (ia_assirepo_from)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store assignment report to whom'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: ASSIGNMENT_REPORT(ia_assignment_report)")

# Insert ASSIGNMENT_REPORT data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_assignment_report`
    (`ia_assirepo_name`, `ia_assirepo_desc`, `ia_assirepo_active`, `ia_assirepo_from`, `ia_assirepo_to`, `ia_assirepo_createdate`, `ia_assirepo_createby`)
    VALUES
    ('Client', 'Report to client', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Audit committee', 'Report to audit committee', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Management', 'Report to institutional management', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    ('Line manager', 'Report to line manager', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python')
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: ASSIGNMENT_REPORT(ia_assignment_report)")

# Create FINDING_RATE ***********************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_finding_rate")
    funcfile.writelog("%t DROPPED TABLE: FINDING_RATE(ia_finding_rate)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_finding_rate (
ia_findrate_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_findrate_impact TEXT NOT NULL,
ia_findrate_name VARCHAR(50) NOT NULL,
ia_findrate_desc TEXT,
ia_findrate_active TEXT NOT NULL,
ia_findrate_from DATETIME NOT NULL,
ia_findrate_to DATETIME NOT NULL,
ia_findrate_createdate DATETIME,
ia_findrate_createby VARCHAR(50),
ia_findrate_editdate DATETIME,
ia_findrate_editby VARCHAR(50),
PRIMARY KEY (ia_findrate_auto),
INDEX fb_order_ia_findrate_name_INDEX (ia_findrate_name),
INDEX fb_order_ia_findrate_from_INDEX (ia_findrate_from)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store finding status'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: FINDING_RATE(ia_finding_rate)")

# Insert FINDING_RATE data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_finding_rate`
    (`ia_findrate_impact`, `ia_findrate_name`, `ia_findrate_desc`, `ia_findrate_active`, `ia_findrate_from`, `ia_findrate_to`, `ia_findrate_createdate`, `ia_findrate_createby`)
    VALUES
    (0, 'No rating', 'No rating.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, 'Positive', 'No findings based on the results of audit performed.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, 'Housekeeping', 'Negligible impact on the business.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, 'Minor', 'Minor impact on the business.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (4, 'Significant', 'Significant impact on the business.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, 'Critical', 'Critical impact on the business. Report to audit committee.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python');
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: FINDING_RATE(ia_finding_rate)")

# Create FINDING_STATUS ********************************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_finding_status")
    funcfile.writelog("%t DROPPED TABLE: FINDING_STATUS(ia_finding_status)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_finding_status (
ia_findstat_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_findstat_stat TEXT NOT NULL,
ia_findstat_name VARCHAR(50) NOT NULL,
ia_findstat_desc TEXT,
ia_findstat_active TEXT NOT NULL,
ia_findstat_from DATETIME NOT NULL,
ia_findstat_to DATETIME NOT NULL,
ia_findstat_createdate DATETIME,
ia_findstat_createby VARCHAR(50),
ia_findstat_editdate DATETIME,
ia_findstat_editby VARCHAR(50),
PRIMARY KEY (ia_findstat_auto),
INDEX fb_order_ia_findstat_name_INDEX (ia_findstat_name),
INDEX fb_order_ia_findstat_from_INDEX (ia_findstat_from)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store finding statuses'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: FINDING_STATUS(ia_finding_status)")

# Insert FINDING_STATUS data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_finding_status`
    (`ia_findstat_stat`, `ia_findstat_name`, `ia_findstat_desc`, `ia_findstat_active`, `ia_findstat_from`, `ia_findstat_to`, `ia_findstat_createdate`, `ia_findstat_createby`)
    VALUES
    (0, 'No status', 'No status.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (1, 'Compile', 'Compiling the audit finding.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (2, 'Check', 'Sent for approval.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (3, 'Approved', 'Approved by supervisor.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (5, 'Comment', 'Sent for commenting to responsible person.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (6, 'Review', 'For review and finalization.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python'),
    (9, 'Closed', 'Finalised for reporting.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', NOW(), 'Python')
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: FINDING_STATUS(ia_finding_status)")

# Create FINDING_RESPONSE ********************************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_finding_response")
    funcfile.writelog("%t DROPPED TABLE: FINDING_RESPONSE(ia_finding_response)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_finding_response (
ia_findresp_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_findresp_name VARCHAR(50) NOT NULL,
ia_findresp_desc TEXT,
ia_findresp_active TEXT NOT NULL,
ia_findresp_from DATETIME NOT NULL,
ia_findresp_to DATETIME NOT NULL,
ia_findresp_flagcomm TEXT,
ia_findresp_labecomm TEXT,
ia_findresp_flagresp TEXT,
ia_findresp_laberesp TEXT,
ia_findresp_flagacti TEXT,
ia_findresp_labeacti TEXT,
ia_findresp_flagactd TEXT,
ia_findresp_labeactd TEXT,
ia_findresp_createdate DATETIME,
ia_findresp_createby INT(11),
ia_findresp_editdate DATETIME,
ia_findresp_editby INT(11),
PRIMARY KEY (ia_findresp_auto),
INDEX fb_order_ia_findresp_name_INDEX (ia_findresp_name),
INDEX fb_order_ia_findresp_from_INDEX (ia_findresp_from)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store finding responses'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: FINDING_RESPONSE(ia_finding_response)")

# Insert FINDING_RESPONSE data
if s_addfields == "y":
    s_sql = """
    INSERT INTO `ia_finding_response`
    (`ia_findresp_name`, `ia_findresp_desc`, `ia_findresp_active`, `ia_findresp_from`, `ia_findresp_to`, `ia_findresp_flagcomm`, `ia_findresp_labecomm`, `ia_findresp_flagresp`, `ia_findresp_laberesp`, `ia_findresp_flagacti`, `ia_findresp_labeacti`, `ia_findresp_flagactd`, `ia_findresp_labeactd`, `ia_findresp_createdate`, `ia_findresp_createby`, `ia_findresp_editdate`, `ia_findresp_editby`)
    VALUES
    ('No comment', 'No comment.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', '0', 'Comment', '0', 'Person responsible', '0', 'Action plan', '0', 'Action date', '2018-01-01 00:00:00', 855, '2018-11-20 08:41:24', 855),
    ('Please read auditors comment', 'Auditor left a note.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', '1', 'Comment', '0', '', '1', 'Action', '0', '', '2018-01-01 00:00:00', 855, '2018-01-01 00:00:00', 855),
    ('Action will be taken', 'Action will be taken to rectify. Please specify action plan, who will be responsible, and by what date.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', '1', 'Possible reason', '1', 'Person responsible', '1', 'Action plan', '1', 'Action date', '2018-01-01 00:00:00', 855, '2018-11-20 08:41:24', 855),
    ('Already rectified', 'The finding was already rectified.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', '1', 'Possible reason', '0', '', '1', 'Rectification proof', '1', 'Date rectified', '2018-01-01 00:00:00', 855, '2018-01-01 00:00:00', 855),
    ('False positive', 'A false positive is an error in some evaluation process in which a condition tested for is mistakenly found to have been detected.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', '1', 'How to prevent', '0', '', '0', '', '0', '', '2018-01-01 00:00:00', 855, '2018-01-01 00:00:00', 855),
    ('Noted', 'Took note.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', '1', 'Comment', '0', '', '1', 'Action', '0', '', '2018-01-01 00:00:00', 855, '2018-01-01 00:00:00', 855),
    ('Other', 'Any other response.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', '1', 'Comment', '0', '', '1', 'Action', '0', '', '2018-01-01 00:00:00', 855, '2018-01-01 00:00:00', 855),
    ('System error reported', 'A system error is the cause of this finding. It was reported.', '1', '2018-01-01 00:00:00', '2099-12-31 00:00:00', '1', 'Possible reason', '1', 'Reported to whom', '1', 'System request', '1', 'Date reported', '2018-01-01 00:00:00', 855, '2018-11-20 08:33:06', 855)
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: FINDING_RESPONSE(ia_finding_response)")

# Create FINDING_ATTACH ********************************************************
if s_droptable == "y":
    curs.execute("DROP TABLE IF EXISTS ia_finding_attach")
    funcfile.writelog("%t DROPPED TABLE: FINDING_ATTACH(ia_finding_attach)")
s_sql = """
CREATE TABLE IF NOT EXISTS ia_finding_attach (
ia_findatta_auto INT(11) NOT NULL AUTO_INCREMENT,
ia_find_auto INT(11) NOT NULL,
ia_findatta_acce INT(1) NOT NULL,
ia_findatta_date DATETIME NOT NULL,
ia_findatta_name VARCHAR(150) NOT NULL,
ia_findatta_desc TEXT,
ia_findatta_atta TEXT NOT NULL,
ia_findatta_createdate DATETIME,
ia_findatta_createby INT(11),
ia_findatta_editdate DATETIME,
ia_findatta_editby INT(11),
PRIMARY KEY (ia_findatta_auto),
INDEX fb_order_ia_findatta_date_INDEX (ia_findatta_date),
INDEX fb_order_ia_findatta_name_INDEX (ia_findatta_name)
)
ENGINE = InnoDB
CHARSET=utf8mb4
COLLATE utf8mb4_unicode_ci
COMMENT = 'Table to store finding attachments'
""" + ";"
curs.execute(s_sql)
funcfile.writelog("%t CREATED TABLE: FINDING_ATTACH(ia_finding_attach)")

# Insert FINDING_RESPONSE data
if s_addfields == "x":
    s_sql = """
    INSERT INTO `ia_finding_attach`
    VALUES
    """ + ";"
    curs.execute(s_sql)
    cnxn.commit()
    funcfile.writelog("%t INSERTED DATA: FINDING_ATTACH (ia_finding_attach)")




# ******************************************************************************

# Script log file
funcfile.writelog("---------------------")
funcfile.writelog("COMPLETED: WEB_IA_NWU")
