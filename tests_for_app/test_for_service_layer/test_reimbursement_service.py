from custom_exceptions.invalid_reimbursement import InvalidReimbursement
from custom_exceptions.invalid_reimbursement_id import InvalidReimbursementID
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.implementation_classes.reimbursement_service_imp import ReimbursementServiceImp
from entities.reimbursement import Reimbursement
from unittest.mock import MagicMock

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)


def test_service_create_reimbursement_success():
    reimbursement_dao.create_reimbursement = MagicMock(return_value=True)
    test_reimbursement = Reimbursement(employee_id=12345, amount=246.01, reason="some Reason")
    boolean = reimbursement_service.service_create_reimbursement(test_reimbursement)
    print(boolean)
    assert boolean is True


def test_service_create_reimbursement_failure():
    reimbursement_dao.create_reimbursement = MagicMock(return_value=False)
    test_reimbursement = Reimbursement()
    try:
        reimbursement_service.service_create_reimbursement(test_reimbursement)
        assert False
    except InvalidReimbursement as e:
        print(e)
        assert str(e) == 'That reimbursement is not valid.'


def test_service_create_reimbursement_failure_no_amount():
    reimbursement_dao.create_reimbursement = MagicMock(return_value=False)
    test_reimbursement = Reimbursement(employee_id=12345, reason="because")
    try:
        reimbursement_service.service_create_reimbursement(test_reimbursement)
        assert False
    except InvalidReimbursement as e:
        print(e)
        assert str(e) == 'That reimbursement is not valid.'


def test_service_create_reimbursement_failure_alphabetic_amount():
    reimbursement_dao.create_reimbursement = MagicMock(return_value=False)
    test_reimbursement = Reimbursement(employee_id=12345, amount='e', reason="because")
    try:
        reimbursement_service.service_create_reimbursement(test_reimbursement)
        assert False
    except InvalidReimbursement as e:
        print(e)
        assert str(e) == 'That reimbursement is not valid.'


def test_service_create_reimbursement_failure_no_reason():
    reimbursement_dao.create_reimbursement = MagicMock(return_value=False)
    test_reimbursement = Reimbursement(employee_id=12345, amount=500)
    try:
        reimbursement_service.service_create_reimbursement(test_reimbursement)
        assert False
    except InvalidReimbursement as e:
        print(e)
        assert str(e) == 'That reimbursement is not valid.'


def test_service_approve_reimbursement_success():
    """Check to see if the reimbursement is in the database, then forward to the data access layer."""
    reimbursement_dao.approve_reimbursement = MagicMock(return_value=True)
    test_reimbursement = Reimbursement(12345)
    boolean = reimbursement_service.service_approve_reimbursement(test_reimbursement)
    print(boolean)
    assert boolean is True


def test_service_approve_reimbursement_failure():
    """Check to see if the reimbursement is in the database, then forward to the data access layer."""
    reimbursement_dao.approve_reimbursement = MagicMock(return_value=False)
    test_reimbursement = Reimbursement()
    try:
        reimbursement_service.service_approve_reimbursement(test_reimbursement)
        assert False
    except InvalidReimbursementID as e:
        print(e)
        assert str(e) == 'That reimbursement id is not valid.'


def test_service_deny_reimbursement_success():
    """Check to see if the reimbursement is in the database, then forward to the data access layer."""
    reimbursement_dao.deny_reimbursement = MagicMock(return_value=True)
    test_reimbursement = Reimbursement(12345)
    boolean = reimbursement_service.service_deny_reimbursement(test_reimbursement)
    print(boolean)
    assert boolean is True


def test_service_deny_reimbursement_failure():
    """Check to see if the reimbursement is in the database, then forward to the data access layer."""
    reimbursement_dao.approve_reimbursement = MagicMock(return_value=False)
    test_reimbursement = Reimbursement()
    try:
        reimbursement_service.service_deny_reimbursement(test_reimbursement)
        assert False
    except InvalidReimbursementID as e:
        print(e)
        assert str(e) == 'That reimbursement id is not valid.'
