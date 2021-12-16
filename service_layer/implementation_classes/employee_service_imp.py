from entities.employee import Employee
from service_layer.abstract_classes.employee_service_abstract import EmployeeService
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp


class EmployeeServiceImp(EmployeeService):
    def __init__(self, employee_dao):
        self.employee_dao: EmployeeDaoImp = employee_dao

    def service_check_employee_login(self, employee: Employee) -> Employee:
        """No checks. Sends to the database layer."""
        return self.employee_dao.check_employee_login(employee)

    def service_update_information(self, employee: Employee) -> Employee:
        """No checks. Sends to the database layer."""
        return self.employee_dao.update_information(employee)

    def service_get_employee_reimbursements(self, employee: Employee) -> dict:
        """No checks. Sends to the database layer."""
        return self.employee_dao.get_employee_reimbursements(employee)

    def service_get_employee_dict(self, manager: Employee) -> dict:
        """No checks. Sends to the database layer."""
        return self.employee_dao.get_employee_dict(manager)
