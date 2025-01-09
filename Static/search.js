//making request to fetch recommendations.
    function searchColleges() {
        var combination = document.querySelector('input[name="combination"]:checked');
        var criteria = Array.from(document.querySelectorAll('input[name="criteria"]:checked')).map(cb => cb.value);
        var department = document.getElementById("depts").value;

        // Preparing the data to send in the request body
        var data = {
            combination: combination ? combination.value : null,
            criteria: criteria,
            department: department
        };

        // Performing the  request using the fetch API
        fetch('/backend_endpoint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // we can Process the response data here
            console.log("Recommendations:", data);
            // if needed we can update the DOM with the received recommendations or perform other actions
        })
        .catch(error => {
            console.error('Error:', error);
        });

        // Perform actions with the selected values
        console.log("Selected Combination:", combination ? combination.value : "Not selected");
        console.log("Selected Criteria:", Array.from(criteria).map(cb => cb.value).join(", ") || "None selected");
        console.log("Selected Department:", department || "Not selected");
    }
