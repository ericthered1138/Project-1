from flask import Flask, request, jsonify
from flask_cors import CORS

from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound
from custom_exceptions.login_failed import LoginFailed
from entities.employee import Employee
from entities.reimbursement import Reimbursement

from util.database_generator_for_testing import depopulate_tables_for_test, populate_tables_for_test
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp
from service_layer.implementation_classes.employee_service_imp import EmployeeServiceImp
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.implementation_classes.reimbursement_service_imp import ReimbursementServiceImp

import logging
logging.basicConfig(filename="records.log", level=logging.DEBUG,
                    format="[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d")
app: Flask = Flask(__name__)
CORS(app)

depopulate_tables_for_test()  # Eliminates possible test data in the database, so that it doesn't interfere.
populate_tables_for_test()

employee_dao = EmployeeDaoImp()
employee_service = EmployeeServiceImp(employee_dao)
reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao, employee_dao)


# test to see if on
@app.get("/")
def on():
    return "I am on."


@app.post("/login")
def service_check_employee_login():
    info = request.get_json()

    if info:
        employee_username = info["employeeUsername"]
        employee_passcode = info["employeePasscode"]
    else:
        return {"manager_if": "incorrectly entered"}

    try:
        employee_to_return = Employee(login=employee_username, passcode=employee_passcode)
        employee_as_object = employee_service.service_check_employee_login(employee_to_return)
        employee_as_dict = employee_as_object.make_dictionary()
        employee_as_json = jsonify(employee_as_dict)
        return employee_as_json
    except LoginFailed:
        return {"manager_if": "login failed"}


@app.patch("/employee")
def update_information():
    info = request.get_json()
    employee_username = info["employeeUsername"]
    employee_passcode = info["employeePasscode"]
    employee_employee_id = info["employeeId"]
    employee_manager_id = info["managerId"]
    employee_manager_if = info["managerIf"]
    employee_first_name = info["employeeFirstName"]
    employee_last_name = info["employeeLastName"]
    employee_to_return = Employee(login=employee_username, passcode=employee_passcode,
                                  employee_id=employee_employee_id, manager_id=employee_manager_id,
                                  manager_if=employee_manager_if, first_name=employee_first_name,
                                  last_name=employee_last_name)
    return employee_service.service_update_information(employee_to_return)


@app.get("/<employeeId>")
def get_employee_reimbursements(employeeId):
    """Returns a list."""
    employee_to_return = Employee(employee_id=employeeId)
    reimbursements_as_dict = employee_service.service_get_employee_reimbursements(employee_to_return)
    reimbursements_as_json = jsonify(reimbursements_as_dict)
    return reimbursements_as_json


@app.post("/reimbursement")
def service_create_reimbursement():

    try:
        info = request.get_json()
        reimbursement_to_return = Reimbursement(
            employee_id=info["employeeId"], amount=info["amount"], reason=info["reason"])
        new_reimbursement = reimbursement_service.service_create_reimbursement(reimbursement_to_return)
        reimbursement_as_dict = new_reimbursement.make_dictionary()
        reimbursement_as_json = jsonify(reimbursement_as_dict)
        return reimbursement_as_json
    except EmployeeCouldNotBeFound:
        return "The Employee could not be found."


@app.patch("/reimbursement/approve/<reimbursement_id>")
def service_approve_reimbursement(reimbursement_id):
    reimbursement_to_return = Reimbursement(reimbursement_id)
    return reimbursement_service.service_approve_reimbursement(reimbursement_to_return)


@app.patch("/reimbursement/disapprove/<reimbursement_id>")
def service_disapprove_reimbursement(reimbursement_id):
    reimbursement_to_return = Reimbursement(reimbursement_id)
    return reimbursement_service.service_disapprove_reimbursement(reimbursement_to_return)


# def get_employee_dict():
#     """No checks. Sends to the database layer."""
#     return self.employee_dao.get_employee_dict(manager)

app.run()

