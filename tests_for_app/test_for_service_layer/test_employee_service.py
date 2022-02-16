import datetime
from decimal import Decimal

from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound
from custom_exceptions.employee_information_invalid import EmployeeInformationInvalid
from custom_exceptions.login_failed import LoginFailed
from custom_exceptions.the_employee_id_is_not_numeric import TheEmployeeIDIsNotNumeric
from entities.employee import Employee
from service_layer.implementation_classes.employee_service_imp import EmployeeServiceImp
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp
from unittest.mock import MagicMock

employee_dao = EmployeeDaoImp()
employee_service = EmployeeServiceImp(employee_dao)


def test_service_check_employee_login_success():
    employee_dao.check_employee_login = MagicMock(return_value=True)
    test_employee = Employee(login='KarlSagan', passcode='karlsaganrules')
    boolean = employee_service.service_check_employee_login(test_employee)
    print(boolean)
    assert boolean


def test_service_update_information_success():
    employee_dao.update_information = MagicMock(return_value=True)
    a_test_employee = Employee(employee_id=42, login='placeholder', passcode='placeholder', first_name='placeholder',
                               last_name='placeholder')
    boolean = employee_service.service_update_information(a_test_employee)
    print(boolean)
    assert boolean


def test_service_update_information_failure_not_numeric():
    employee_dao.update_information = MagicMock(return_value=False)
    a_test_employee = Employee(employee_id="fourtytwo")
    try:
        employee_service.service_update_information(a_test_employee)
        assert False
    except TheEmployeeIDIsNotNumeric as e:
        print(e)
        assert str(e) == 'That employee ID is not numeric.'


def test_service_update_information_failure_length():
    employee_dao.update_information = MagicMock(return_value=False)
    a_test_employee = Employee(employee_id=42, login='1', passcode='123456789012345678901')
    try:
        employee_service.service_update_information(a_test_employee)
        assert False
    except EmployeeInformationInvalid as e:
        print(e)
        assert str(e) == 'That employee information is invalid.'


def test_service_get_employee_reimbursements_success():
    employee_dao.get_employee_reimbursements = MagicMock(return_value=True)
    a_test_employee = Employee(employee_id=42)
    boolean = employee_service.service_get_employee_reimbursements(a_test_employee)
    print(boolean)
    assert boolean


def test_service_get_employee_dict_success():
    employee_dao.get_employee_dict = MagicMock(return_value=True)
    a_test_employee = Employee(employee_id=42)
    boolean = employee_service.service_get_employee_dict(a_test_employee)
    print(boolean)
    assert boolean


def test_service_get_all_manager_reimbursements_success():
    employee_dao.get_all_manager_reimbursements = MagicMock(return_value=True)
    a_test_employee = Employee(employee_id=42)
    boolean = employee_service.service_get_all_manager_reimbursements(a_test_employee)
    print(boolean)
    assert boolean


def test_service_create_the_stats_success():
    employee_dao.get_employee_dict = MagicMock(return_value={10000001: 'Karl Sagan'})
    employee_dao.get_employee_reimbursements = MagicMock(return_value={
        12345: {'reimbursement_id': 12345, 'employee_id': 10000001,
                'reimbursement_date': datetime.datetime(2021, 12, 10, 0, 0), 'amount': Decimal('38.23'),
                'reason': 'to get on the cloud', 'if_approved': 'yes', 'manager_comment': 'the cloud is very good'}})
    a_test_manager = Employee(employee_id=42)
    dictionary_to_return = employee_service.service_create_the_stats(a_test_manager)
    print(dictionary_to_return)
    assert dictionary_to_return == {
        '10000001': {'number_of_reimbursements': 1, 'acceptance_rate': 100, 'average_reimbursement_cost': 38,
                     'monthly_total': 0, 'total': 38}}
