from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.implementation_classes.reimbursement_service_imp import ReimbursementServiceImp
from entities.reimbursement import Reimbursement
from unittest.mock import MagicMock

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)


def test_service_create_reimbursement_success():
    reimbursement_dao.create_reimbursement = MagicMock(return_value=True)
    test_reimbursement = Reimbursement()
    reimbursement_service.service_create_reimbursement(test_reimbursement)


def test_service_approve_reimbursement_success():
    """Check to see if the reimbursement is in the database, then forward to the data access layer."""
    test_reimbursement = Reimbursement(12345)
    reimbursement_service.service_approve_reimbursement(test_reimbursement)


def test_service_disapprove_reimbursement():
    """Check to see if the reimbursement is in the database, then forward to the data access layer."""
    test_reimbursement = Reimbursement(12345)
    reimbursement_service.service_deny_reimbursement(test_reimbursement)
