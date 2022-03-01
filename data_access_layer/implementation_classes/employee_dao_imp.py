from custom_exceptions.login_failed import LoginFailed
from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound

from entities.employee import Employee
from entities.reimbursement import Reimbursement
from util.database_connection import connection
from data_access_layer.abstract_classes.employee_dao_abstract import EmployeeDAO


class EmployeeDaoImp(EmployeeDAO):

    def get_employee(self, employee_id: int) -> Employee:
        """Gets the employee record by employee_id."""
        cursor = connection.cursor()
        sql = "select * from employee_table where employee_id = %(employee_id)s;"
        cursor.execute(sql, {"employee_id": employee_id})
        employee_record = cursor.fetchone()

        # Check to see if there is a record otherwise raise an exception.
        if employee_record:
            current_employee = Employee(*employee_record)
            return current_employee

        raise EmployeeCouldNotBeFound('Employee could not be found.')

    def check_employee_login(self, employee: Employee) -> Employee:
        """Checks if the entered employee information is correct."""
        cursor = connection.cursor()
        sql = "select * from employee_table where login = %(login)s and passcode = %(passcode)s;"
        cursor.execute(sql, {"login": employee.login, "passcode": employee.passcode})
        employee_record = cursor.fetchone()

        # Check to see if there is a record otherwise raise an exception.
        if employee_record:
            current_employee = Employee(*employee_record)
            return current_employee

        raise LoginFailed('Login entered incorrectly')

    def update_information(self, employee: Employee) -> Employee:
        """Updates employee information in the server."""

        # Check if the employee exists by using the get method
        self.get_employee(employee.employee_id)

        # Update in the database.
        sql = "update employee_table set first_name = %(first_name)s, " \
              "last_name = %(last_name)s, login = %(login)s, passcode = %(passcode)s " \
              "where employee_id = %(employee_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "login": employee.login,
            "passcode": employee.passcode,
            "employee_id": employee.employee_id
        })
        connection.commit()

        # Get the record back from the database.
        return self.get_employee(employee.employee_id)

    def get_employee_reimbursements(self, employee: Employee) -> dict:
        """For all employees, grabs the employee's reimbursements."""

        # Check if the employee exists by using the get method
        self.get_employee(employee.employee_id)

        # Get the reimbursements.
        sql = "select * from reimbursement_table where employee_id = %(employee_id)s order by reimbursement_date desc"
        cursor = connection.cursor()
        cursor.execute(sql, {"employee_id": employee.employee_id})
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

        # Check if the employee exists by using the get method
        self.get_employee(manager.employee_id)

        # Get a list of employees
        cursor = connection.cursor()
        sql = "select * from employee_table as et inner join manager_junction_table as mjt " \
              "on et.employee_id = mjt.employee_id where mjt.manager_id = %(employee_id)s;"
        cursor.execute(sql, {"employee_id": manager.employee_id})
        employee_records = cursor.fetchall()

        # Put them into a dictionary using the id as a key
        employee_dict = {}
        for employee in employee_records:
            employee_id, full_name = employee[0], employee[2] + " " + employee[3]
            employee_dict.update({employee_id: full_name})
        return employee_dict

    def get_all_manager_reimbursements(self, manager: Employee) -> dict:
        """For the manager, grabs all reimbursements for employees of the manager."""

        # Check if the employee exists by using the get method
        self.get_employee(manager.employee_id)

        # Get a list of employees
        cursor = connection.cursor()
        sql = f"select * from employee_table as et inner join manager_junction_table as mjt " \
              f"on et.employee_id = mjt.employee_id where mjt.manager_id = %(employee_id)s;"
        cursor.execute(sql, {"employee_id": manager.employee_id})
        employee_records = cursor.fetchall()

        employee_list = []
        for employee in employee_records:
            employee_id = employee[0]
            employee_list.append(employee_id)

        # Create a list of reimbursements and add dictionaries of each reimbursement.
        reimbursement_dict = {}
        for employee in employee_list:
            cursor = connection.cursor()
            sql = "select * from reimbursement_table where employee_id = %(employee_id)s"
            cursor.execute(sql, {"employee_id": employee})
            reimbursement_record = cursor.fetchall()

            # Add all the reimbursements as dictionaries.
            for reimbursement in reimbursement_record:
                current_reimbursement = Reimbursement(*reimbursement)
                reimbursement_dict.update(
                    {current_reimbursement.reimbursement_id: current_reimbursement.make_dictionary()})
        return reimbursement_dict
