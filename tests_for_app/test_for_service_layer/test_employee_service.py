from entities.employee import Employee
from service_layer.implementation_classes.employee_service_imp import EmployeeServiceImp
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp

employee_dao = EmployeeDaoImp()
employee_service = EmployeeServiceImp(employee_dao)


def test_service_check_employee_login():
    """Nothing to check, yet."""
    pass


def test_service_update_information():
    """Nothing to check, yet."""
    pass


def test_service_get_employee_reimbursements():
    """Nothing to check, yet."""
    pass


def test_service_get_employee_dict():
    """Nothing to check, yet."""
    pass


def test_service_create_the_stats():
    manager = Employee(employee_id=10000001)
    dictionary_to_return = employee_service.service_create_the_stats(manager)
    print(dictionary_to_return)
    assert dictionary_to_return
