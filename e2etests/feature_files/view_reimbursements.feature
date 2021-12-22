Feature: View Reimbursements
  Scenario: as an employee, I should be able to review my reimbursement requests so I can know if they are approved or denied
    Given the employee is on the employee page
    Then the employee should see the past reimbursments table

  Scenario: as a manager, I should be able to view pending reimbursement requests so I can make decisions about them
    Given the manager is on the manager page
    Then the manager should see the pending reimbursement table

  Scenario: as a manager, I should be able to view past reimbursement requests so I can check previous decisions
    Given the manager is on the manager page
    Then the manager should see the past reimbursement table