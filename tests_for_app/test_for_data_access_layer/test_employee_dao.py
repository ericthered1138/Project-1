from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp
from util.database_generator_for_testing import populate_tables_for_test, depopulate_tables_for_test
from entities.employee import Employee

employee_dao = EmployeeDaoImp(12345678)


def test_get_employee_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    assert employee_dao.get_employee(10000001)


def test_check_employee_login_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_employee = Employee(login='KarlSagan888888', passcode='karlsaganrules')
    assert employee_dao.check_employee_login(test_employee)


def test_update_information_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_employee = Employee(employee_id=10000001,
                             manager_id='Null',
                             manager_if='yes',
                             first_name='Karl',
                             last_name='Sagan',
                             login='KarlSaganebulous',
                             passcode='hammer')
    assert employee_dao.update_information(test_employee)


def test_get_employee_reimbursements_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_employee = Employee(employee_id=10000002)
    assert employee_dao.get_employee_reimbursements(test_employee)


def test_get_employee_list_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_manager = Employee(employee_id=10000001)
    assert employee_dao.get_employee_dict(test_manager)


def test_get_all_manager_reimbursements_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_manager = Employee(employee_id=10000001)
    assert employee_dao.get_all_manager_reimbursements(test_manager)
