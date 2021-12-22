from abc import ABC, abstractmethod
from entities.employee import Employee


class EmployeeService(ABC):

    @abstractmethod
    def service_check_employee_login(self, employee: Employee) -> Employee:
        """Checks if the entered employee information is correct."""
        pass

    @abstractmethod
    def service_update_information(self, employee: Employee) -> Employee:
        """Updates employee information in the server."""
        pass

    @abstractmethod
    def service_get_employee_reimbursements(self, employee: Employee) -> list:
        """For all employees, grabs the employee's reimbursements."""
        pass

    @abstractmethod
    def service_get_employee_dict(self, manager: Employee) -> dict:
        """For the manager, grabs the employee list for the manager."""
        pass

    @abstractmethod
    def service_get_all_manager_reimbursements(self, manager: Employee) -> dict:
        """For the manager, grabs the reimbursements for the manager."""
        pass

    @abstractmethod
    def service_create_the_stats(self, manager: Employee) -> dict:
        pass

