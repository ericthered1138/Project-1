from abc import ABC, abstractmethod
from entities.reimbursement import Reimbursement


class ReimbursementService(ABC):

    @abstractmethod
    def service_create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For employees, to create reimbursements."""
        pass

    @abstractmethod
    def service_approve_reimbursement(self, reimbursement: Reimbursement) -> bool:
        """For managers, to approve a reimbursement."""
        pass

    @abstractmethod
    def service_deny_reimbursement(self, reimbursement: Reimbursement) -> bool:
        """For managers, to disapprove a reimbursement."""
        pass
