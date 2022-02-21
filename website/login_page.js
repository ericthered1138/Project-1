async function loginAttempt(){
    //grab the sign in data from the webpage
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value

    //put it in a json and post it to http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000//login
    loginJson = JSON.stringify({"employeeUsername":username, "employeePasscode":password})
    let url = "http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000//login"
    let the_request = await fetch(url, {
        method:"POST",
        headers:{'Content-Type': 'application/json'}, 
        body:loginJson}).then(response => {return response.json()});

    //store the information for the session
    window.sessionStorage.setItem("name", the_request["first_name"] +" "+ the_request["last_name"]);
    window.sessionStorage.setItem("employeeId", the_request["employee_id"]);
    
    //3 possibilities to check for before logging in
    if (the_request["manager_if"] === false){//go to the employee page
        window.location.href = "employee_page.html";
    }else if(the_request["manager_if"] === true){//go to the manager page
        window.location.href = "manager_page.html";
    }else{//pop up an error message for the attempt
        alert("Username or password entered incorrectly.");
    }
}