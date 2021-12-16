class Employee:
    def __init__(self,
                 employee_id=0,
                 manager_id=0,
                 manager_if='no',
                 first_name='first',
                 last_name='last',
                 login='username',
                 passcode='password'):

        self.employee_id = employee_id
        self.manager_id = manager_id
        self.manager_if = manager_if
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.passcode = passcode

    def make_dictionary(self):
        dictionary = {
            "employee_id": self.employee_id,
            "manager_id": self.manager_id,
            "manager_if": self.manager_if,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "login": self.login,
            "passcode": self.passcode}
        return dictionary
