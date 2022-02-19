from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound
from custom_exceptions.reimbursement_could_not_be_found import ReimbursementCouldNotBeFound

from custom_exceptions.that_reimbursement_is_not_pending import ThatReimbursementIsNotPending
from data_access_layer.abstract_classes.reimbursement_dao_abstract import ReimbursementDAO
from entities.reimbursement import Reimbursement
from util.database_connection import connection


class ReimbursementDAOImp(ReimbursementDAO):

    def get_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        """To get a reimbursement."""
        sql = "select * from reimbursement_table where reimbursement_id = %(reimbursement_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"reimbursement_id": reimbursement_id})
        reimbursement_record = cursor.fetchone()

        # Check to see if there is a record otherwise raise an exception.
        if reimbursement_record:
            current_reimbursement = Reimbursement(*reimbursement_record)
            return current_reimbursement

        raise ReimbursementCouldNotBeFound('The reimbursement could not be found.')

    def create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For employees, to create reimbursements."""
        # Check if the employee actually exists.
        cursor = connection.cursor()
        sql = "select * from employee_table where employee_id = %(employee_id)s;"
        cursor.execute(sql, {"employee_id": reimbursement.employee_id})
        employee_record = cursor.fetchone()
        if not employee_record:
            raise EmployeeCouldNotBeFound("Employee could not be found.")

        # Create the reimbursement.
        sql = "insert into reimbursement_table (reimbursement_id, employee_id, amount, reason) " \
              "values (default, %(employee_id)s, %(amount)s, %(reason)s) returning reimbursement_id;"

        cursor.execute(sql, {"employee_id": reimbursement.employee_id,
                             "amount": reimbursement.amount,
                             "reason": reimbursement.reason
                             })
        connection.commit()
        reimbursement_id = cursor.fetchone()[0]
        return self.get_reimbursement(reimbursement_id)

    def approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For managers, to approve a reimbursement."""

        # Check the reimbursement in the database to make sure that it exists and is pending.
        checked_reimbursement = self.get_reimbursement(reimbursement.reimbursement_id)
        if checked_reimbursement.if_approved != 'pending':
            raise ThatReimbursementIsNotPending('That reimbursement is not pending.')

        # Approve the reimbursement.
        sql = f"update reimbursement_table set approval = 'yes', manager_comment = %(manager_comment)s " \
              f"where reimbursement_id = %(reimbursement_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"manager_comment": reimbursement.manager_comment,
                             "reimbursement_id": reimbursement.reimbursement_id})
        connection.commit()
        return self.get_reimbursement(reimbursement.reimbursement_id)

    def deny_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For managers, to disapprove a reimbursement."""

        # Check the reimbursement in the database to make sure that it exists and is pending.
        checked_reimbursement = self.get_reimbursement(reimbursement.reimbursement_id)
        if checked_reimbursement.if_approved != 'pending':
            raise ThatReimbursementIsNotPending('That reimbursement is not pending.')

        # Deny the reimbursement.
        sql = f"update reimbursement_table set approval = 'no', manager_comment = %(manager_comment)s " \
              f"where reimbursement_id = %(reimbursement_id)s;"
        cursor = connection.cursor()
        cursor.execute(sql, {"manager_comment": reimbursement.manager_comment,
                             "reimbursement_id": reimbursement.reimbursement_id})
        connection.commit()
        return self.get_reimbursement(reimbursement.reimbursement_id)
