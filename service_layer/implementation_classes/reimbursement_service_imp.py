from custom_exceptions.that_reimbursement_is_not_pending import ThatReimbursementIsNotPending
from entities.reimbursement import Reimbursement
from service_layer.abstract_classes.reimbursement_service_abstract import ReimbursementService
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp


class ReimbursementServiceImp(ReimbursementService):
    def __init__(self, reimbursement_dao, employee_dao):
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
        """Checking to make sure that the employee is in the database before forwarding to the data access layer."""
        employee_id = reimbursement.employee_id
        self.employee_dao.get_employee(employee_id)
        return self.reimbursement_dao.create_reimbursement(reimbursement)

    def service_approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """Check to see if the reimbursement is in the database and pending, then forward to the data access layer."""
        a_reimbursement = self.reimbursement_dao.get_reimbursement(reimbursement)
        if a_reimbursement.if_approved == 'pending':
            return self.reimbursement_dao.approve_reimbursement(reimbursement)
        raise ThatReimbursementIsNotPending('That reimbursement is not pending.')

    def service_disapprove_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """Check to see if the reimbursement is in the database and pending, then forward to the data access layer."""
        a_reimbursement = self.reimbursement_dao.get_reimbursement(reimbursement)
        if a_reimbursement.if_approved == 'pending':
            return self.reimbursement_dao.disapprove_reimbursement(reimbursement)
        raise ThatReimbursementIsNotPending('That reimbursement is not pending.')
