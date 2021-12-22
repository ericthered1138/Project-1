class Reimbursement:
    def __init__(self,
                 reimbursement_id=0,
                 employee_id=0,
                 reimbursement_date='1997-1-1',
                 amount=0,
                 reason='no reason',
                 if_approved='pending',
                 manager_comment='no comment'):

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
