from util.database_connection import connection


def populate_tables_for_test():
    """Function to populate tables with test data in the database for testing."""
    sql = "insert into employee_table (employee_id, manager, first_name, last_name, login, passcode) " \
          "values ('10000000', 'yes', 'Settra', 'the Imperishable', 'settra', '12345');" \
          "insert into employee_table (employee_id, manager, first_name, last_name, login, passcode) " \
          "values ('10000001', 'yes', 'Karl', 'Sagan', 'KarlSagan888888', 'karlsaganrules');" \
          "insert into employee_table (employee_id, manager, first_name, last_name, login, passcode) " \
          "values ('10000002', 'no', 'Taco', 'MacArthur ', 'passwordistaco', 'taco');" \
          "insert into employee_table (employee_id, manager, first_name, last_name, login, passcode) " \
          "values ('10000003', 'no', 'Mister', 'Eff ', 'iam', 'itsamysterE');" \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('12345', '10000002', '2021-12-10',  '38.23', 'to get on the cloud', 'yes', 'the cloud is very good'); " \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('23456', '10000002', '2021-12-10', '51.78', 'solicit a privates contractor', 'no', 'I see what you did there');" \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('34567', '10000003', '2021-12-10', '28.12', 'a secret mission', 'pending', 'no comment');" \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('34568', '10000003', '2021-12-17', '42.0', 'the secret of life', 'pending', 'no comment');" \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('34569', '10000002', '2021-12-17', '217.53', 'the universe', 'pending', 'no comment');" \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('345670', '10000002', '2021-11-15', '300', 'testing123', 'yes', 'no comment');" \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('345671', '10000003', '2021-10-2', '50000', 'testing123', 'yes', 'no comment');" \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('345672', '10000002', '2021-10-3', '10', 'testing123', 'yes', 'no comment');" \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('345673', '10000002', '2021-10-10', '10', 'testing123', 'yes', 'no comment');" \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, approval, manager_comment) " \
          "values ('345674', '10000002', '2021-10-17', '10', 'testing123', 'yes', 'no comment');" \
          "insert into manager_junction_table values (10000003, 10000001);" \
          "insert into manager_junction_table values (10000002, 10000001);" \
          "insert into manager_junction_table values (10000001, 10000000);"

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


def depopulate_tables_for_test():
    """Function to populate tables with test data in the database for testing."""
    sql = "delete from employee_table where employee_id > 9999999; "

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

# depopulate_tables_for_test()
# populate_tables_for_test()
