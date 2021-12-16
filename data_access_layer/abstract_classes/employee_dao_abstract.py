from abc import ABC, abstractmethod
from entities.employee import Employee


class EmployeeDAO(ABC):

    @abstractmethod
    def get_employee(self, employee_id: int) -> Employee:
        """Gets the employee record by employee_id."""
        pass

    @abstractmethod
    def check_employee_login(self, employee: Employee) -> Employee:
        """Checks if the entered employee information is correct."""
        pass

    @abstractmethod
    def update_information(self, employee: Employee) -> Employee:
        """Updates employee information in the server."""
        pass

    @abstractmethod
    def get_employee_reimbursements(self, employee: Employee) -> list:
        """For all employees, grabs the employee's reimbursements."""
        pass

    @abstractmethod
    def get_employee_dict(self, manager: Employee) -> dict:
        """For the manager, grabs the employee list for the manager."""
        pass

    @abstractmethod
    def get_all_manager_reimbursements(self, manager: Employee) -> list:
        """For the manager, grabs all reimbursements for employees of the manager."""
        pass
