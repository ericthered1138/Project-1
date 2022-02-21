from flask import Flask, request, jsonify
from flask_cors import CORS

from custom_exceptions.employee_could_not_be_found import EmployeeCouldNotBeFound
from custom_exceptions.invalid_reimbursement import InvalidReimbursement
from custom_exceptions.invalid_reimbursement_id import InvalidReimbursementID
from custom_exceptions.login_failed import LoginFailed
from custom_exceptions.that_reimbursement_is_not_pending import ThatReimbursementIsNotPending
from custom_exceptions.the_employee_id_is_not_numeric import TheEmployeeIDIsNotNumeric
from entities.employee import Employee
from entities.reimbursement import Reimbursement

from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDaoImp
from service_layer.implementation_classes.employee_service_imp import EmployeeServiceImp
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.implementation_classes.reimbursement_service_imp import ReimbursementServiceImp
from util.database_generator_for_testing import populate_tables_for_test, depopulate_tables_for_test

import logging

app: Flask = Flask(__name__)
CORS(app)

# logging.basicConfig(filename="records.log", level=logging.DEBUG,
#                     format="[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d")

employee_dao = EmployeeDaoImp()
employee_service = EmployeeServiceImp(employee_dao)
reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)

# Setup test data
depopulate_tables_for_test()
populate_tables_for_test()


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
        return "Error: Username or Password not entered.", 400

    try:
        employee_to_return = Employee(login=employee_username, passcode=employee_passcode)
        employee_as_object = employee_service.service_check_employee_login(employee_to_return)
        employee_as_dict = employee_as_object.make_dictionary()
        employee_as_json = jsonify(employee_as_dict)
        return employee_as_json
    except LoginFailed as e:
        return str(e), 400


@app.get("/<manager_id>")
def get_employee_reimbursements(manager_id):
    """Returns a dictionary of all an employee's reimbursements."""
    try:
        employee_to_return = Employee(employee_id=manager_id)
        reimbursements_as_dict = employee_service.service_get_employee_reimbursements(employee_to_return)
        reimbursements_as_json = jsonify(reimbursements_as_dict)
        return reimbursements_as_json
    except TheEmployeeIDIsNotNumeric as e:
        return str(e), 400
    except EmployeeCouldNotBeFound as e:
        return str(e), 400


@app.get("/manager/<manager_id>")
def get_manager_reimbursements(manager_id):
    """Returns a dictionary of all a manager's reimbursements."""
    try:
        employee_to_return = Employee(employee_id=manager_id)
        reimbursements_as_dict = employee_service.service_get_all_manager_reimbursements(employee_to_return)
        reimbursements_as_json = jsonify(reimbursements_as_dict)
        return reimbursements_as_json
    except TheEmployeeIDIsNotNumeric as e:
        return str(e), 400
    except EmployeeCouldNotBeFound as e:
        return str(e), 400


@app.post("/reimbursement")
def service_create_reimbursement():
    try:
        info = request.get_json()
        reimbursement_to_return = Reimbursement(
            employee_id=info["employeeId"], amount=info["amount"], reason=str(info["reason"]))
        new_reimbursement = reimbursement_service.service_create_reimbursement(reimbursement_to_return)
        reimbursement_as_dict = new_reimbursement.make_dictionary()
        reimbursement_as_json = jsonify(reimbursement_as_dict)
        return reimbursement_as_json
    except EmployeeCouldNotBeFound as e:
        return str(e), 400
    except InvalidReimbursement as e:
        return str(e), 400


@app.post("/reimbursement/approve")
def service_approve_reimbursement():
    try:
        reimbursement_info = request.get_json()
        reimbursement_id = int(reimbursement_info["reimbursementId"])
        reimbursement_comment = reimbursement_info["managerComment"]
        reimbursement_to_return = Reimbursement(reimbursement_id=reimbursement_id,
                                                manager_comment=reimbursement_comment)
        new_reimbursement = reimbursement_service.service_approve_reimbursement(reimbursement_to_return)
        reimbursement_as_dict = new_reimbursement.make_dictionary()
        reimbursement_as_json = jsonify(reimbursement_as_dict)
        return reimbursement_as_json
    except InvalidReimbursementID as e:
        return str(e), 400
    except ThatReimbursementIsNotPending as e:
        return str(e), 400


@app.post("/reimbursement/disapprove")
def service_disapprove_reimbursement():
    try:
        reimbursement_info = request.get_json()
        reimbursement_id = int(reimbursement_info["reimbursementId"])
        reimbursement_comment = reimbursement_info["managerComment"]
        reimbursement_to_return = Reimbursement(reimbursement_id=reimbursement_id,
                                                manager_comment=reimbursement_comment)
        new_reimbursement = reimbursement_service.service_deny_reimbursement(reimbursement_to_return)
        reimbursement_as_dict = new_reimbursement.make_dictionary()
        reimbursement_as_json = jsonify(reimbursement_as_dict)
        return reimbursement_as_json
    except InvalidReimbursementID as e:
        return str(e), 400
    except ThatReimbursementIsNotPending as e:
        return str(e), 400


@app.get("/stats/<manager_id>")
def get_employee_dict(manager_id):
    try:
        manager = Employee(employee_id=manager_id)
        stats_dict_to_return = employee_service.service_create_the_stats(manager)
        stats_json = jsonify(stats_dict_to_return)
        return stats_json
    except EmployeeCouldNotBeFound as e:
        return str(e), 400
    except TheEmployeeIDIsNotNumeric as e:
        return str(e), 400


app.run(host='0.0.0.0')
