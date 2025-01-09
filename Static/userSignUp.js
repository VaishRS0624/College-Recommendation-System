function validation(){
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    let flag = 1;

    if(username.value == ""){
        document.getElementById('a').innerHTML = "**Fill the username field";
        flag = 0;
    }
    else{
        document.getElementById('a').innerHTML = " ";
        flag = 1;
    }
    if( password.value == ""){
        document.getElementById('b').innerHTML = "**password field is empty";
        flag = 0;
    }
    
    else if (password.value.length <= 7){
        document.getElementById('b').innerHTML = "**Password must be of min 8 characters";
        flag = 0;
    }
    else{
        document.getElementById('b').innerHTML = " ";
        flag = 1; 
    }

    if(flag){
        return true;
    }else{
        return false;
    }
    
}
function signup() {
    var signupUsername = document.getElementById("signupUsername").value;
    var signupPassword = document.getElementById("signupPassword").value;

    var formData = new FormData();
    formData.append("user", signupUsername);
    formData.append("password", signupPassword);

    fetch("/signUp1", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            // Redirect to the login page after successful signup
            window.location.href = "/login";
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}