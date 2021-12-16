from custom_exceptions.login_failed import LoginFailed
from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound

from entities.employee import Employee
from entities.reimbursement import Reimbursement
from util.database_connection import connection
from data_access_layer.abstract_classes.employee_dao_abstract import EmployeeDAO


class EmployeeDaoImp(EmployeeDAO):

    def __init__(self, employee_id_counter=1000):
        self.customer_id_counter = self.max_creator(employee_id_counter) + 1

    @staticmethod
    def max_creator(counter):
        """Static Method sets the new customer id counter by finding the highest."""
        cursor = connection.cursor()
        sql = "select max(employee_id) as highest_customer_id from employee_table"
        cursor.execute(sql)
        highest = cursor.fetchone()
        if highest[0] is None:  # In case the table is empty.
            return counter
        return max(highest[0], counter)

    def get_employee(self, employee_id: int) -> Employee:
        """Gets the employee record by employee_id."""
        cursor = connection.cursor()
        cursor.execute(f"select * from employee_table where employee_id = {employee_id}")
        employee_record = cursor.fetchone()

        # Check to see if there is a record otherwise raise an exception.
        if employee_record:
            current_employee = Employee(*employee_record)
            return current_employee

        raise EmployeeCouldNotBeFound('Employee could not be found.')

    def check_employee_login(self, employee: Employee) -> Employee:
        """Checks if the entered employee information is correct."""
        cursor = connection.cursor()
        sql = f"select * from employee_table where login = '{employee.login}' and passcode = '{employee.passcode}'"
        cursor.execute(sql)
        employee_record = cursor.fetchone()

        # Check to see if there is a record otherwise raise an exception.
        if employee_record:
            current_employee = Employee(*employee_record)
            return current_employee

        raise LoginFailed('Login entered incorrectly')

    def update_information(self, employee: Employee) -> Employee:
        """Updates employee information in the server."""
        # Update in the database.
        sql = f"update employee_table set first_name = '{employee.first_name}', " \
              f"last_name = '{employee.last_name}', login = '{employee.login}', passcode = '{employee.passcode}' " \
              f"where employee_id = '{employee.employee_id}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        # Get the record back from the database.
        cursor.execute(f"select * from employee_table where employee_id = {employee.employee_id}")
        employee_record = cursor.fetchone()
        current_employee = Employee(*employee_record)
        return current_employee

    def get_employee_reimbursements(self, employee: Employee) -> dict:
        """For all employees, grabs the employee's reimbursements."""
        cursor = connection.cursor()
        cursor.execute(f"select * from reimbursement_table where employee_id = {employee.employee_id}")
        reimbursement_record = cursor.fetchall()

        # Create a reimbursement dict and add all the reimbursements as dictionaries
        # where the reimbursement_id is the key.
        reimbursement_dict = {}
        for reimbursement in reimbursement_record:
            current_reimbursement = Reimbursement(*reimbursement)
            reimbursement_dict.update({current_reimbursement.reimbursement_id: current_reimbursement.make_dictionary()})
        return reimbursement_dict

    def get_employee_dict(self, manager: Employee) -> dict:
        """For the manager, grabs the employee dictionary for the manager."""
        cursor = connection.cursor()
        sql = f"select * from employee_table where manager_id = {manager.employee_id}"
        cursor.execute(sql)
        employee_records = cursor.fetchall()

        employee_dict = {}
        for employee in employee_records:
            employee_id, full_name = employee[0], employee[3] + " " + employee[4]
            employee_dict.update({employee_id: full_name})
        return employee_dict

    def get_all_manager_reimbursements(self, manager: Employee) -> list:
        """For the manager, grabs all reimbursements for employees of the manager."""
        cursor = connection.cursor()
        sql = f"select * from employee_table where manager_id = {manager.employee_id}"
        cursor.execute(sql)
        employee_records = cursor.fetchall()

        employee_list = []
        for employee in employee_records:
            employee_id = employee[0]
            employee_list.append(employee_id)

        # Create a list of reimbursements and add dictionaries of each reimbursement.
        reimbursement_list = []
        for employee in employee_list:
            cursor = connection.cursor()
            cursor.execute(f"select * from reimbursement_table where employee_id = {employee}")
            reimbursement_record = cursor.fetchall()

            # Add all the reimbursements as dictionaries.
            for reimbursement in reimbursement_record:
                current_reimbursement = Reimbursement(*reimbursement)
                reimbursement_list.append(current_reimbursement.make_dictionary())
        return reimbursement_list
