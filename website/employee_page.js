//Automatically grabs and displays the employees name in the top left corner.
(function addEmployeeName(){
    let aName = window.sessionStorage.getItem("name");
    document.getElementById("employeeName").innerHTML = aName
})()

let employeeId = window.sessionStorage.getItem("employeeId")

//The function to repopulate the pending reimbursement form.
async function createPendingReimbursementForm(){
    //clear the table
    let pendingTable = document.getElementById("pendingReimbursementTable");
    pendingTable.innerHTML = ''

    let url = "http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000//" + employeeId
    const the_reimbursements = await fetch(url).then(response => {return response.json()});
    for (aReimbursementId in the_reimbursements){
        let aReimbursementObject = the_reimbursements[aReimbursementId]
        let reimbursementStatus = aReimbursementObject.if_approved;
        if (reimbursementStatus == "pending"){
            let reimbursementId = aReimbursementObject.reimbursement_id;
            let amount = aReimbursementObject.amount;
            let reason = aReimbursementObject.reason;
            let reimbursementDate = aReimbursementObject.reimbursement_date;
            
            let pendingTable = document.getElementById("pendingReimbursementTable");
            let row = pendingTable.insertRow();
            let first = row.insertCell(0);
            let second = row.insertCell(1);
            let third = row.insertCell(2);
            let fourth = row.insertCell(3);

            first.innerHTML = reimbursementId;
            second.innerHTML = amount;
            third.innerHTML = reason;
            fourth.innerHTML = reimbursementDate;

            third.setAttribute("id", reason)
        };
    }
}
createPendingReimbursementForm()

//The function to get the data from the reimbursement submit form and send to python.
async function createReimbursement(){
    //grab the information from the page
    let reimbursementReason = document.getElementById("reimbursementReason").value
    let reimbursementAmount = document.getElementById("reimbursementAmount").value
    let employeeId = window.sessionStorage.getItem("employeeId")


        reimbursementJson = JSON.stringify({"employeeId":employeeId, 
            "amount":reimbursementAmount, "reason":reimbursementReason})
        let url = "http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000/reimbursement"
        let the_reimbursement = await fetch(url, {
            method:"POST",
            headers:{'Content-Type': 'application/json'}, 
            body:reimbursementJson}).then(response => {return response.json()});
        
        if (the_reimbursement["if_approved"] == "The amount must be numeric and positive."){
            alert("Invalid Entry: Amounts must be positiver numbers.")
        }else{
            createPendingReimbursementForm()
        }
}

//The function to repopulate the previous reimbursements.
async function createOldReimbursementForm(){
    let url = "http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000//" + employeeId
    const the_reimbursements = await fetch(url).then(response => {return response.json()});
    for (aReimbursementId in the_reimbursements){
        let aReimbursementObject = the_reimbursements[aReimbursementId]
        let reimbursementStatus = aReimbursementObject.if_approved;
        if (reimbursementStatus != "pending"){
            let reimbursementId = aReimbursementObject.reimbursement_id;
            let amount = aReimbursementObject.amount;
            let reason = aReimbursementObject.reason;
            let reimbursementDate = aReimbursementObject.reimbursement_date;
            let approval = aReimbursementObject.if_approved;
            let comment = aReimbursementObject.manager_comment;
            
            let pendingTable = document.getElementById("oldReimbursementTable");
            let row = pendingTable.insertRow();
            let first = row.insertCell(0);
            let second = row.insertCell(1);
            let third = row.insertCell(2);
            let fourth = row.insertCell(3);
            let fifth = row.insertCell(4)
            let sixth = row.insertCell(5)

            first.innerHTML = reimbursementId;
            second.innerHTML = amount;
            third.innerHTML = reason;
            fourth.innerHTML = reimbursementDate;
            fifth.innerHTML = approval;
            sixth.innerHTML = comment;
        };
    }
}
createOldReimbursementForm()


//The function to submit changes in the Pending Reimbursement form.
async function submitEmployeePendingReimbursementForm(){
    let url = "http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000/manager/" + employeeId
    const the_reimbursements = await fetch(url).then(response => {return response.json()});
    for (aReimbursementId in the_reimbursements){
        if (the_reimbursements[aReimbursementId].if_approved === "pending"){
            let pending = document.getElementById(aReimbursementId + "pending");
            let approval = document.getElementById(aReimbursementId + "approval");
            let disapproval = document.getElementById(aReimbursementId + "disapproval");
            console.log(pending)
            console.log(approval)
            console.log(disapproval)
            if (pending.checked){
                continue
            }else if(approval.checked){
                let url = "http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000/reimbursement/approve/" + aReimbursementId
                let the_response = await fetch(url).then(response => {return response.json()});
                console.log(the_response)
            }else if(disapproval.checked){
                let url = "http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000/reimbursement/disapprove/" + aReimbursementId
                let the_response = await fetch(url).then(response => {return response.json()});
                console.log(the_response)
            }
        }
    }
    createEmployeePendingReimbursementForm()
    createEmployeeOldReimbursementForm()
}

function logout(){
    localStorage.clear();
    sessionStorage.clear();
    window.location.href = "login_page.html"
}


//select and option to make a drop down list