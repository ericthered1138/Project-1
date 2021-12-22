Feature: Manager approve or deny a reimbursement.
  Scenario: as a manager, I should be able to approve reimbursement requests because they are legitimate
    Given the manager is on the manager page
    When the manager clicks the approve radio on one reimbursement
    When the manager clicks the submit button on the table
    Then one reimbursement is approved and sent to the previous reimbursements


  Scenario: as a manager, I should be able to deny reimbursement requests because they are illegitimate
    Given the manager is on the manager page
    When the manager clicks the disapprove radio on one reimbursement
    When the manager clicks the submit button
    Then one reimbursement is disapproved and sent to the previous reimbursements

  Scenario: as a manager, I should be able to leave a comment about my decisions regarding reimbursement
  requests so employees better understand my decisions
    Given the manager is on the manager page
    When the manager clicks the approve radio on the commented reimbursement
    When the manager inputs a comment in the one reimbursement comment box
    When the manager clicks the submit button
    Then the commented reimbursement is approved and sent to the previous reimbursements

