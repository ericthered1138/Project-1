from abc import ABC, abstractmethod
from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):

    @abstractmethod
    def get_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        """To get a reimbursement."""
        pass

    @abstractmethod
    def create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For employees, to create reimbursements."""
        pass

    @abstractmethod
    def approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For managers, to approve a reimbursement."""
        pass

    @abstractmethod
    def deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For managers, to disapprove a reimbursement."""
        pass
