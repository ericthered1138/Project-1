from custom_exceptions.invalid_reimbursement import InvalidReimbursement
from custom_exceptions.invalid_reimbursement_id import InvalidReimbursementID
from custom_exceptions.that_reimbursement_is_not_pending import ThatReimbursementIsNotPending
from entities.reimbursement import Reimbursement
from service_layer.abstract_classes.reimbursement_service_abstract import ReimbursementService
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp


class ReimbursementServiceImp(ReimbursementService):
    def __init__(self, reimbursement_dao):
        self.reimbursement_dao: ReimbursementDAOImp = reimbursement_dao

    @staticmethod
    def is_float(number):
        """A method to check whether the input is a float."""
        try:
            float(number)
            return True
        except ValueError:
            return False

    def service_create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """Check to make sure the reimbursement is valid"""
        # Raise an error if the reimbursement reason or amount is empty.
        if not reimbursement.amount or not reimbursement.reason:
            raise InvalidReimbursement('That reimbursement is not valid.')

        if not (str(reimbursement.employee_id).isnumeric() and
                self.is_float(reimbursement.amount) and
                20000 >= int(reimbursement.amount) > 0 and
                len(reimbursement.reason) <= 280):
            raise InvalidReimbursement('That reimbursement is not valid.')

        # Make sure the correct format is being used
        reimbursement.employee_id = int(reimbursement.employee_id)
        reimbursement.amount = float(reimbursement.amount)
        reimbursement.reason = str(reimbursement.reason)

        return self.reimbursement_dao.create_reimbursement(reimbursement)

    def service_approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """Check to make sure the reimbursement id is valid."""
        if not (str(reimbursement.reimbursement_id).isnumeric()):
            raise InvalidReimbursementID('That reimbursement id is not valid.')
        return self.reimbursement_dao.approve_reimbursement(reimbursement)

    def service_deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """Check to make sure the reimbursement id is valid."""
        if not (str(reimbursement.reimbursement_id).isnumeric()):
            raise InvalidReimbursementID('That reimbursement id is not valid.')
        return self.reimbursement_dao.deny_reimbursement(reimbursement)
