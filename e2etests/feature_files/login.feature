Feature: Employee Login

  Scenario: As an employee I want to login so that I can manage my reimbursements
    Given the employee is on the login page
    When the employee enters their username in the username input box
    When the employee enters their password in the password input box
    When the employee clicks the login button
    Then the employee should be logged in and redirected to the employee home page

  Scenario: As a manager I want to login so that I can manage my reimbursements
    Given the manager is on the login page
    When the manager enters their username in the username input box
    When the manager enters their password in the password input box
    When the manager clicks the login button
    Then the manager should be logged in and redirected to the manager home page

  Scenario: as the system, I should reject failed login attempts
    Given the employee is on the login page
    When the employee enters their username in the username input box
    When the employee enters a faulty password
    When the employee clicks the login button
    Then a login error pops



