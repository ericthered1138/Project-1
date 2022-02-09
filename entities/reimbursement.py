class Reimbursement:
    def __init__(self,
                 reimbursement_id=None,
                 employee_id=None,
                 reimbursement_date=None,
                 amount=None,
                 reason=None,
                 if_approved=None,
                 manager_comment=None):
        self.reimbursement_id = reimbursement_id
        self.employee_id = employee_id
        self.reimbursement_date = reimbursement_date
        self.amount = amount
        self.reason = reason
        self.if_approved = if_approved
        self.manager_comment = manager_comment

    def make_dictionary(self):
        dictionary = {
            "reimbursement_id": self.reimbursement_id,
            "employee_id": self.employee_id,
            "reimbursement_date": self.reimbursement_date,
            "amount": self.amount,
            "reason": self.reason,
            "if_approved": self.if_approved,
            "manager_comment": self.manager_comment}
        return dictionary

    def __str__(self):
        return f"reimbursement_id: {self.reimbursement_id}, " \
               f"employee_id: {self.employee_id}, " \
               f"reimbursement_date: {self.reimbursement_date}, " \
               f"amount: {self.amount}, " \
               f"reason: {self.reason}, " \
               f"if_approved: {self.if_approved}," \
               f"manager_comment: {self.manager_comment}"
