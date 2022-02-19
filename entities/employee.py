class Employee:
    def __init__(self,
                 employee_id=None,
                 manager_if=None,
                 first_name=None,
                 last_name=None,
                 login=None,
                 passcode=None):
        self.employee_id = employee_id
        self.manager_if = manager_if
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.passcode = passcode

    def make_dictionary(self):
        dictionary = {
            "employee_id": self.employee_id,
            "manager_if": self.manager_if,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "login": self.login,
            "passcode": self.passcode}
        return dictionary

    def __str__(self):
        return f"employee_id: {self.employee_id}, " \
               f"manager_if: {self.manager_if}, " \
               f"first_name: {self.first_name}, " \
               f"last_name: {self.last_name}, " \
               f"login: {self.login}, " \
               f"passcode: *****"
