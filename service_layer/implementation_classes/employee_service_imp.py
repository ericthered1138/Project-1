import datetime

from custom_exceptions.employee_information_invalid import EmployeeInformationInvalid
from custom_exceptions.the_employee_id_is_not_numeric import TheEmployeeIDIsNotNumeric
from entities.employee import Employee
from service_layer.abstract_classes.employee_service_abstract import EmployeeService
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp


class EmployeeServiceImp(EmployeeService):

    def __init__(self, employee_dao):
        self.employee_dao: EmployeeDaoImp = employee_dao
        self.error_message = 'That employee ID is not numeric.'

    @staticmethod
    def is_float(number):
        """A method to check whether the input is a float."""
        try:
            float(number)
            return True
        except ValueError:
            return False

    def service_check_employee_login(self, employee: Employee) -> Employee:
        """Converts all input to a string before sending to the database layer."""
        employee.login = str(employee.login)
        employee.passcode = str(employee.passcode)
        return self.employee_dao.check_employee_login(employee)

    def service_update_information(self, employee: Employee) -> Employee:
        """Function is not being used. Kept for potential expansion."""

        # Make sure that the employee id is numeric.
        if not str(employee.employee_id).isnumeric():
            raise TheEmployeeIDIsNotNumeric(self.error_message)

        # Make sure that string lengths are viable.
        if not (len(employee.login) <= 40 and
                len(employee.passcode) <= 20 and
                len(employee.first_name) <= 20 and
                len(employee.last_name) <= 20):
            raise EmployeeInformationInvalid('That employee information is invalid.')

        return self.employee_dao.update_information(employee)

    def service_get_employee_reimbursements(self, employee: Employee) -> dict:
        """Service layer method to get a dictionary of an employee's reimbursements."""
        # Make sure that the employee id is numeric.
        if not str(employee.employee_id).isnumeric():
            raise TheEmployeeIDIsNotNumeric(self.error_message)

        return self.employee_dao.get_employee_reimbursements(employee)

    def service_get_employee_dict(self, manager: Employee) -> dict:
        """Service layer method to get all of a manager's employees."""
        # Make sure that the employee id is numeric.
        if not str(manager.employee_id).isnumeric():
            raise TheEmployeeIDIsNotNumeric(self.error_message)

        return self.employee_dao.get_employee_dict(manager)

    def service_get_all_manager_reimbursements(self, manager: Employee) -> dict:
        """Service layer method to get all reimbursements by manager id."""
        # Make sure that the employee id is numeric.
        if not str(manager.employee_id).isnumeric():
            raise TheEmployeeIDIsNotNumeric(self.error_message)

        return self.employee_dao.get_all_manager_reimbursements(manager)

    def service_create_the_stats(self, manager: Employee) -> dict:
        """Takes in information from the data access layer and creates the statistics to send to main."""
        # Make sure that the employee id is numeric.
        if not str(manager.employee_id).isnumeric():
            raise TheEmployeeIDIsNotNumeric(self.error_message)

        # get the employees dict
        employees_dict = self.employee_dao.get_employee_dict(manager)

        employees_by_name_dict = {}
        # loop through the employees getting each employee's reimbursement stats
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
                    if a_reimbursement["reimbursement_date"] + datetime.timedelta(30) > datetime.datetime.now():
                        monthly_total += int(a_reimbursement["amount"])
                elif a_reimbursement["if_approved"] == 'no':
                    number_of_no += 1

            average_reimbursement_cost = total // number_of_yes if number_of_yes != 0 else 0
            acceptance_rate = round((number_of_yes / (number_of_yes + number_of_no)) * 100) if total != 0 else 0
            employees_by_name_dict.update({str(an_employee): {
                "number_of_reimbursements": number_of_yes,
                "acceptance_rate": acceptance_rate,
                "average_reimbursement_cost": average_reimbursement_cost,
                "monthly_total": monthly_total,
                "total": total
            }})

        return employees_by_name_dict
