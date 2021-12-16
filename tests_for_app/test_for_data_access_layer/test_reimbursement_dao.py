from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from util.database_generator_for_testing import populate_tables_for_test, depopulate_tables_for_test
from entities.reimbursement import Reimbursement

reimbursement_dao = ReimbursementDAOImp(10000)


def test_get_reimbursement_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_reimbursement = Reimbursement(reimbursement_id=12345)
    assert reimbursement_dao.get_reimbursement(test_reimbursement)


def test_create_reimbursement_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_reimbursement = Reimbursement(employee_id=10000003)
    returned_reimbursement = reimbursement_dao.create_reimbursement(test_reimbursement)
    assert reimbursement_dao.get_reimbursement(returned_reimbursement)


def test_approve_reimbursement_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_reimbursement = Reimbursement(reimbursement_id=34567)
    assert reimbursement_dao.approve_reimbursement(test_reimbursement)


def test_disapprove_reimbursement_success():
    depopulate_tables_for_test()
    populate_tables_for_test()
    test_reimbursement = Reimbursement(reimbursement_id=34567)
    assert reimbursement_dao.disapprove_reimbursement(test_reimbursement)
