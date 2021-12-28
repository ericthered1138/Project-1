from custom_exceptions.reimbursement_could_not_be_found import ReimbursementCouldNotBeFound
from datetime import date, datetime

from data_access_layer.abstract_classes.reimbursement_dao_abstract import ReimbursementDAO
from entities.reimbursement import Reimbursement
from util.database_connection import connection


class ReimbursementDAOImp(ReimbursementDAO):
    def __init__(self, reimbursement_counter=1000):
        self.reimbursement_id_counter = self.max_creator(reimbursement_counter) + 1

    @staticmethod
    def max_creator(counter):
        """Static Method sets the new customer id counter by finding the highest."""
        cursor = connection.cursor()
        sql = "select max(reimbursement_id) as highest_reimbursement_id from reimbursement_table"
        cursor.execute(sql)
        highest = cursor.fetchone()
        if highest[0] is None:  # In case the table is empty.
            return counter
        return max(highest[0], counter)

    def get_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """To get a reimbursement."""
        cursor = connection.cursor()
        cursor.execute(f"select * from reimbursement_table where reimbursement_id = {reimbursement.reimbursement_id}")
        reimbursement_record = cursor.fetchone()

        # Check to see if there is a record otherwise raise an exception.
        if reimbursement_record:
            current_reimbursement = Reimbursement(*reimbursement_record)
            return current_reimbursement

        raise ReimbursementCouldNotBeFound('The reimbursement could not be found.')

    def create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For employees, to create reimbursements."""
        reimbursement.reimbursement_id = self.reimbursement_id_counter
        self.reimbursement_id_counter += 1

        sql = f"insert into reimbursement_table (reimbursement_id, employee_id, reimbursement_date, amount, " \
              f"reason, approval, manager_comment) " \
              f"values ('{reimbursement.reimbursement_id}', '{reimbursement.employee_id}', " \
              f"'{datetime.now()}', '{reimbursement.amount}', '{reimbursement.reason}', " \
              f"'{reimbursement.if_approved}', '{reimbursement.manager_comment}');"

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return self.get_reimbursement(reimbursement)

    def approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For managers, to approve a reimbursement."""
        sql = f"update reimbursement_table set approval = 'yes' " \
              f"where reimbursement_id = {reimbursement.reimbursement_id};" \
              f"update reimbursement_table set manager_comment = '{reimbursement.manager_comment}' " \
              f"where reimbursement_id = {reimbursement.reimbursement_id}"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return self.get_reimbursement(reimbursement)

    def disapprove_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        """For managers, to disapprove a reimbursement."""
        sql = f"update reimbursement_table set approval = 'no' " \
              f"where reimbursement_id = {reimbursement.reimbursement_id};" \
              f"update reimbursement_table set manager_comment = '{reimbursement.manager_comment}' " \
              f"where reimbursement_id = {reimbursement.reimbursement_id}"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return self.get_reimbursement(reimbursement)
