
//Automatically grabs and displays the employees name in the top left corner.
(function addEmployeeName(){
    let aName = window.sessionStorage.getItem("name");
    document.getElementById("employeeName").innerHTML = aName
})()


//Grabs the list of the employee's reimbursements.
//Will need to call every time there is a change in reimbursements.
async function grabEmployeeReimbursements(){
    employeeId = window.sessionStorage.getItem("employeeId")
    console.log(employeeId)
    let url = "http://127.0.0.1:5000//" + employeeId
    let the_reimbursements = await fetch(url).then(response => {return response.json()});
    console.log(the_reimbursements)
}
grabEmployeeReimbursements()//the initial call


//The function to get the data from the reimbursement submit form.
function createReimbursement(){

}

//The function to repopulate the pending reimbursement form.

//The function to repopulate the previous reimbursements.

//The function to logout and delete session data.

//The statistical functions will be in their own dedicated javascript.