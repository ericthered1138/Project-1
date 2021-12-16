from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound
from custom_exceptions.that_reimbursement_is_not_pending import ThatReimbursementIsNotPending
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.implementation_classes.reimbursement_service_imp import ReimbursementServiceImp
from entities.reimbursement import Reimbursement
from util.database_generator_for_testing import populate_tables_for_test, depopulate_tables_for_test

employee_dao = EmployeeDaoImp()
reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao, employee_dao)


def test_service_create_reimbursement_failure():
    test_reimbursement = Reimbursement()
    try:
        reimbursement_service.service_create_reimbursement(test_reimbursement)
        assert False
    except EmployeeCouldNotBeFound as e:
        assert str(e) == 'Employee could not be found.'


def test_service_approve_reimbursement_failure():
    """Check to see if the reimbursement is in the database, then forward to the data access layer."""
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_reimbursement = Reimbursement(12345)
    try:
        reimbursement_service.service_approve_reimbursement(test_reimbursement)
        assert False
    except ThatReimbursementIsNotPending as e:
        assert str(e) == 'That reimbursement is not pending.'


def test_service_disapprove_reimbursement():
    """Check to see if the reimbursement is in the database, then forward to the data access layer."""
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_reimbursement = Reimbursement(12345)
    try:
        reimbursement_service.service_disapprove_reimbursement(test_reimbursement)
        assert False
    except ThatReimbursementIsNotPending as e:
        assert str(e) == 'That reimbursement is not pending.'
