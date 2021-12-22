import datetime
from datetime import date

from entities.employee import Employee
from service_layer.abstract_classes.employee_service_abstract import EmployeeService
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp


class EmployeeServiceImp(EmployeeService):

    def __init__(self, employee_dao):
        self.employee_dao: EmployeeDaoImp = employee_dao

    def service_check_employee_login(self, employee: Employee) -> Employee:
        """No checks necessary the data access layer is the function."""
        return self.employee_dao.check_employee_login(employee)

    def service_update_information(self, employee: Employee) -> Employee:
        """Function is not being used"""
        return self.employee_dao.update_information(employee)

    def service_get_employee_reimbursements(self, employee: Employee) -> dict:
        """Check to make sure the employee is in the database."""
        self.employee_dao.get_employee(employee.employee_id) # raises employee not found error if employee not found
        return self.employee_dao.get_employee_reimbursements(employee)

    def service_get_employee_dict(self, manager: Employee) -> dict:
        """Check to make sure the employee is in the database."""
        self.employee_dao.get_employee(manager.employee_id)  # raises employee not found error if employee not found
        return self.employee_dao.get_employee_dict(manager)

    def service_get_all_manager_reimbursements(self, manager: Employee) -> dict:
        """Check to make sure the employee is in the database."""
        self.employee_dao.get_employee(manager.employee_id)  # raises employee not found error if employee not found
        return self.employee_dao.get_all_manager_reimbursements(manager)

    def service_create_the_stats(self, manager: Employee) -> dict:
        """Takes in information from the data access layer and creates the statistics to send to the frontend."""
        # get the employees dict
        employees_dict = self.employee_dao.get_employee_dict(manager)

        employees_by_name_dict = {}
        # loop through the employees getting each employees reimbursement stats
        for an_employee in employees_dict.keys():
            employee_object = Employee(employee_id=an_employee)
            reimbursements_dict = self.employee_dao.get_employee_reimbursements(employee_object)

            # Acceptance Rate
            number_of_yes = 0
            number_of_no = 0

            # Total
            total = 0
            monthly_total = 0
            for a_reimbursement in reimbursements_dict.values():
                if a_reimbursement["if_approved"] == 'yes':
                    total += int(a_reimbursement["amount"])
                    number_of_yes += 1
                    if a_reimbursement["reimbursement_date"] + datetime.timedelta(30) > date.today():
                        monthly_total += int(a_reimbursement["amount"])
                elif a_reimbursement["if_approved"] == 'no':
                    number_of_no += 1

            average_reimbursement_cost = total//number_of_yes if number_of_yes != 0 else 0
            acceptance_rate = round((number_of_yes / (number_of_yes + number_of_no)) * 100) if total != 0 else 0
            employees_by_name_dict.update({str(an_employee): {
                "number_of_reimbursements": number_of_yes,
                "acceptance_rate": acceptance_rate,
                "average_reimbursement_cost": average_reimbursement_cost,
                "monthly_total": monthly_total,
                "total": total
            }})

        return employees_by_name_dict
