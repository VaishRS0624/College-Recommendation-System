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
document.getElementById("form").addEventListener("submit", function (event) {
    event.preventDefault();
    if (validation()) {
        loginUser();
    }
});

function loginUser() {
    var form = document.getElementById("form");
    var formData = new FormData(form);

    fetch('/login?redirect=/adminDashboard.html', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.status === 405) {
            alert("Method Not Allowed. Please try again.");
            throw new Error("Method Not Allowed");
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            alert(data.message);

            if (data.redirect) {
                window.location.href = data.redirect;
            } else {
                window.location.href = "/adminDashboard.html";
            }
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
