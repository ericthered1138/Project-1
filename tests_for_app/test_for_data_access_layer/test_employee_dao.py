from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound
from custom_exceptions.login_failed import LoginFailed
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp
from entities.employee import Employee
import pytest
from util.database_connection import connection

employee_dao = EmployeeDaoImp()


@pytest.fixture
def create_fake_employee():
    sql = "delete from employee_table where employee_id > 9999999;" \
          "insert into employee_table (employee_id, manager, first_name, last_name, login, passcode) " \
          "values ('10000001', 'yes', 'Karl', 'Sagan', 'KarlSagan888888', 'karlsaganrules');"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    yield
    sql = "delete from employee_table where employee_id > 9999999;"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


@pytest.fixture
def create_fake_manager(create_fake_employee):
    sql = "insert into employee_table (employee_id, manager, first_name, last_name, login, passcode) " \
          "values ('10000000', 'yes', 'Settra', 'the Imperishable', 'settra', '12345');" \
          "insert into manager_junction_table values(10000001, 10000000);"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


@pytest.fixture
def create_fake_reimbursement(create_fake_employee):
    sql = "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, " \
          "approval, manager_comment) " \
          "values ('12345', '10000001', '2021-12-10',  '38.23', 'to get on the cloud', 'yes', 'the cloud is very " \
          "good'); "
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


def test_get_employee_success_1(create_fake_employee):
    returned_employee = employee_dao.get_employee(10_000_001)
    print(returned_employee)
    assert str(returned_employee) == "employee_id: 10000001, " \
                                     "manager_if: True, " \
                                     "first_name: Karl, " \
                                     "last_name: Sagan, " \
                                     "login: KarlSagan888888, " \
                                     "passcode: *****"


def test_get_employee_success_2(create_fake_manager):
    returned_employee = employee_dao.get_employee(10000000)
    print(returned_employee)
    assert str(returned_employee) == "employee_id: 10000000, " \
                                     "manager_if: True, " \
                                     "first_name: Settra, " \
                                     "last_name: the Imperishable, " \
                                     "login: settra, " \
                                     "passcode: *****"


def test_get_employee_fail_no_employee():
    try:
        employee_dao.get_employee(10000001)
        assert False
    except EmployeeCouldNotBeFound as e:
        print(e)
        assert str(e) == 'Employee could not be found.'


def test_check_employee_login_success(create_fake_employee):
    test_employee = Employee(login='KarlSagan888888', passcode='karlsaganrules')
    returned_employee = employee_dao.check_employee_login(test_employee)
    print(returned_employee)
    assert str(returned_employee) == "employee_id: 10000001, " \
                                     "manager_if: True, " \
                                     "first_name: Karl, " \
                                     "last_name: Sagan, login: " \
                                     "KarlSagan888888, passcode: *****"


def test_check_employee_login_failure_bad_login():
    try:
        test_employee = Employee(login='KarlSagan888888', passcode='karlsaganrules')
        employee_dao.check_employee_login(test_employee)
        assert False
    except LoginFailed as e:
        print(e)
        assert str(e) == 'Login entered incorrectly'


def test_update_information_success(create_fake_employee):
    test_employee = Employee(employee_id=10000001,
                             manager_if='yes',
                             first_name='Karl',
                             last_name='Sagan',
                             login='KarlSaganebulous',
                             passcode='hammer')
    returned_employee = employee_dao.update_information(test_employee)
    print(returned_employee)
    assert str(returned_employee) == "employee_id: 10000001, " \
                                     "manager_if: True, " \
                                     "first_name: Karl, " \
                                     "last_name: Sagan, " \
                                     "login: KarlSaganebulous, " \
                                     "passcode: *****"


def test_get_employee_reimbursements_success(create_fake_reimbursement):
    test_employee = Employee(employee_id=10000001)
    returned_reimbursements = employee_dao.get_employee_reimbursements(test_employee)
    print(returned_reimbursements)
    assert str(returned_reimbursements) == r"{12345: {'reimbursement_id': 12345, 'employee_id': 10000001, " \
                                           r"'reimbursement_date': datetime.datetime(2021, 12, 10, 0, 0), " \
                                           r"'amount': Decimal('38.23'), 'reason': 'to get on the cloud', " \
                                           r"'if_approved': 'yes', 'manager_comment': 'the cloud is very good'}}"


def test_get_employee_list_success(create_fake_manager):
    test_manager = Employee(employee_id=10000000)
    returned_dictionary = employee_dao.get_employee_dict(test_manager)
    print(returned_dictionary)
    assert str(returned_dictionary) == "{10000001: 'Karl Sagan'}"


def test_get_all_manager_reimbursements_success(create_fake_manager, create_fake_reimbursement):
    test_manager = Employee(employee_id=10000000)
    returned_dictionary = employee_dao.get_all_manager_reimbursements(test_manager)
    print(returned_dictionary)
    assert str(returned_dictionary) == r"{12345: {'reimbursement_id': 12345, 'employee_id': 10000001, " \
                                       r"'reimbursement_date': datetime.datetime(2021, 12, 10, 0, 0), " \
                                       r"'amount': Decimal('38.23'), 'reason': 'to get on the cloud', " \
                                       r"'if_approved': 'yes', 'manager_comment': 'the cloud is very good'}}"
