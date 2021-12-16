from util.database_connection import connection


def create_tables():
    """Function to create tables in the database."""
    sql = "create table employee_table(employee_id int, manager_id int, manager varchar(3), first_name varchar(20), " \
          "last_name varchar(20), login varchar(40), passcode varchar(20), primary key (employee_id));" \
          "create table reimbursement_table(reimbursement_id int, employee_id int, reimbursement_date date, " \
          "amount decimal, reason varchar(280), approval varchar(20), primary key (reimbursement_id), " \
          "foreign key (employee_id) references employee_table(employee_id));"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


def populate_tables_for_test():
    """Function to populate tables with test data in the database for testing."""
    sql = "insert into employee_table (employee_id, manager_id, manager, first_name, last_name, login, passcode) " \
          "values ('10000001',Null, 'yes', 'Karl', 'Sagan', 'KarlSagan888888', 'karlsaganrules');"\
          "insert into employee_table (employee_id, manager_id, manager, first_name, last_name, login, passcode) " \
          "values ('10000002','10000001', 'no', 'Taco', 'MacArthur ', 'passwordistaco', 'taco');"\
          "insert into employee_table (employee_id, manager_id, manager, first_name, last_name, login, passcode) " \
          "values ('10000003','10000001', 'no', 'Mister', 'Eff ', 'iam', 'itsamysterE');"\
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval) " \
          "values ('12345', '10000002', '2021-12-10',  '38.23', 'to get on the cloud', 'yes'); " \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval) " \
          "values ('23456', '10000002', '2021-12-10', '51.78', 'solicit a privates contractor', 'no');"\
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval) " \
          "values ('34567', '10000003', '2021-12-10', '28.12', 'a secret mission', 'pending');"

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


def depopulate_tables_for_test():
    """Function to populate tables with test data in the database for testing."""
    sql = "delete from reimbursement_table where employee_id > 9999999;"\
          "delete from employee_table where employee_id > 9999999; "

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


# create_tables()
# depopulate_tables_for_test()
# populate_tables_for_test()
