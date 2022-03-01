async function loginAttempt(){
    //grab the sign in data from the webpage
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value

    //put it in a json and post it to http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000//login
    let loginJson = JSON.stringify({"employeeUsername":username, "employeePasscode":password})
    let url = "http://ec2-3-135-215-83.us-east-2.compute.amazonaws.com:5000//login"
    let the_request = await fetch(url, {
        method:"POST",
        headers:{'Content-Type': 'application/json'}, 
        body:loginJson});
    
    if (the_request.status == 400){
        alert("Username or password entered incorrectly.");
    }else{
        let response_body = await the_request.json();
        console.log(response_body)
        //store the information for the session
        window.sessionStorage.setItem("name", response_body["first_name"] +" "+ response_body["last_name"]);
        window.sessionStorage.setItem("employeeId", response_body["employee_id"]);

        //2 possibilities to check for before logging in
        if (response_body["manager_if"] === false){//go to the employee page
        window.location.href = "employee_page.html";
        }else if(response_body["manager_if"] === true){//go to the manager page
        window.location.href = "manager_page.html";
    }
    }
    
}