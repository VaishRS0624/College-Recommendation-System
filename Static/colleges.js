function validateAndSave() {
    // Create FormData object
    var formData = new FormData(document.getElementById("addCollegesForm"));

    // Validate input 

    // Validate that the required fields are not empty
    if (!formData.get("instituteCode") || !formData.get("instituteName") ||
        !formData.get("instituteStatus") || !formData.get("totalIntake")) {
        alert("Please fill in all required fields.");
        return;
    }

    // Validate Institute Code is a number
    if (isNaN(formData.get("instituteCode"))) {
        alert("Institute Code must be a number.");
        return;
    }

    // Validate Intake is a number
    if (isNaN(formData.get("totalIntake"))) {
        alert("Total Intake must be a number.");
        return;
    }
     var formData = new FormData();
    formData.append("instituteCode", instituteCode);
    formData.append("instituteName", instituteName);
    formData.append("instituteStatus", instituteStatus);
    formData.append("totalIntake", totalIntake);

    // Fetch API to send a POST request to the Flask server
    fetch("/addColleges", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        console.log(data);
        // You can add more logic here to handle the response on the client side if needed
    })
    .catch(error => {
        console.error("Error:", error);
    });
}