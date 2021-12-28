from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound
from custom_exceptions.login_failed import LoginFailed
from entities.employee import Employee
from service_layer.implementation_classes.employee_service_imp import EmployeeServiceImp
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp
from util.database_generator_for_testing import depopulate_tables_for_test, populate_tables_for_test

employee_dao = EmployeeDaoImp()
employee_service = EmployeeServiceImp(employee_dao)


def test_service_check_employee_login_failure():
    depopulate_tables_for_test()
    populate_tables_for_test()
    try:
        test_employee = Employee(login='KarlSagan', passcode='karlsaganrules')
        employee_service.service_check_employee_login(test_employee)
        assert False
    except LoginFailed as e:
        assert str(e) == 'Login entered incorrectly'


def test_service_update_information_failure():
    a_test_employee = Employee(employee_id=-50)
    print(a_test_employee.employee_id)
    try:
        employee_service.service_update_information(a_test_employee)
        assert False
    except EmployeeCouldNotBeFound as e:
        assert str(e) == 'Employee could not be found.'


def test_service_get_employee_reimbursements_failure():
    a_test_employee = Employee(employee_id=-50)
    print(a_test_employee.employee_id)
    try:
        employee_service.service_update_information(a_test_employee)
        assert False
    except EmployeeCouldNotBeFound as e:
        assert str(e) == 'Employee could not be found.'


def test_service_get_employee_dict_failure():
    a_test_employee = Employee(employee_id=-50)
    print(a_test_employee.employee_id)
    try:
        employee_service.service_update_information(a_test_employee)
        assert False
    except EmployeeCouldNotBeFound as e:
        assert str(e) == 'Employee could not be found.'


def test_service_get_all_manager_reimbursements_failure():
    a_test_employee = Employee(employee_id=-50)
    print(a_test_employee.employee_id)
    try:
        employee_service.service_update_information(a_test_employee)
        assert False
    except EmployeeCouldNotBeFound as e:
        assert str(e) == 'Employee could not be found.'


def test_service_create_the_stats_success():
    manager = Employee(employee_id=10000001)
    dictionary_to_return = employee_service.service_create_the_stats(manager)
    print(dictionary_to_return)
    assert dictionary_to_return
