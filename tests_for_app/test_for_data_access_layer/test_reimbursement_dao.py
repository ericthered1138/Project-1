from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound
from custom_exceptions.reimbursement_could_not_be_found import ReimbursementCouldNotBeFound
from custom_exceptions.that_reimbursement_is_not_pending import ThatReimbursementIsNotPending
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from util.database_generator_for_testing import populate_tables_for_test, depopulate_tables_for_test
from entities.reimbursement import Reimbursement
import pytest
from util.database_connection import connection

reimbursement_dao = ReimbursementDAOImp()


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
          "approval, manager_comment) values ('12345', '10000001', '2021-12-10',  '38.23', 'to get on the cloud', " \
          "'yes', 'the cloud is very good'); " \
          "insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, reason, " \
          "approval, manager_comment) values ('12346', '10000001', '1991-08-06',  '12.34', 'some bad reason', " \
          "'pending', 'some bad reason');"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


def test_get_reimbursement_success(create_fake_reimbursement):
    returned_reimbursement = reimbursement_dao.get_reimbursement(12345)
    print(returned_reimbursement)
    assert returned_reimbursement


def test_get_reimbursement_failure():
    try:
        reimbursement_dao.get_reimbursement(12345)
        assert False
    except ReimbursementCouldNotBeFound as e:
        print(e)
        assert str(e) == 'The reimbursement could not be found.'


def test_create_reimbursement_success(create_fake_employee):
    test_reimbursement = Reimbursement(employee_id=10000001, amount=42.00, reason="because")
    returned_reimbursement = reimbursement_dao.create_reimbursement(test_reimbursement)
    print(returned_reimbursement)
    assert returned_reimbursement


def test_create_reimbursement_failure():
    test_reimbursement = Reimbursement(employee_id=10000001, amount=42.00, reason="because")
    try:
        reimbursement_dao.create_reimbursement(test_reimbursement)
        assert False
    except EmployeeCouldNotBeFound as e:
        print(e)
        assert str(e) == 'Employee could not be found.'


def test_approve_reimbursement_success(create_fake_reimbursement):
    test_reimbursement = Reimbursement(reimbursement_id=12346)
    returned_reimbursement = reimbursement_dao.approve_reimbursement(test_reimbursement)
    print(returned_reimbursement)
    assert returned_reimbursement


def test_approve_reimbursement_failure(create_fake_reimbursement):
    test_reimbursement = Reimbursement(reimbursement_id=12345)
    try:
        reimbursement_dao.approve_reimbursement(test_reimbursement)
        assert False
    except ThatReimbursementIsNotPending as e:
        print(e)
        assert str(e) == 'That reimbursement is not pending.'


def test_deny_reimbursement_success(create_fake_reimbursement):
    test_reimbursement = Reimbursement(reimbursement_id=12346)
    returned_reimbursement = reimbursement_dao.deny_reimbursement(test_reimbursement)
    print(returned_reimbursement)
    assert returned_reimbursement
    

def test_deny_reimbursement_failure(create_fake_reimbursement):
    test_reimbursement = Reimbursement(reimbursement_id=12345)
    try:
        reimbursement_dao.deny_reimbursement(test_reimbursement)
        assert False
    except ThatReimbursementIsNotPending as e:
        print(e)
        assert str(e) == 'That reimbursement is not pending.'
