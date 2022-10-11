/**
 * login_function.js
 * This file contains the functions for the login system.
 */


/**
 * Login()
 * Allows the user to log in to the website with an email and password.
 */
function Login()
{
    // Get login details from form.
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    let url = "/users";
    let response = "Error while retrieving.";
    let xhttp = new XMLHttpRequest();
   
    xhttp.onreadystatechange = function() 
    {
        if (xhttp.readyState == 4 && xhttp.status == 200)
        {
            response = JSON.parse(xhttp.responseText);
            let users = response.result;

            for (let i = 0; i < users.length; i++)
            {
                // Compare inputted values to stored credentials
                if (users[i].email == email)
                {
                    if (users[i].password == password)
                    {
                        CreateCookie(users[i].userId);
                        window.location.href="/";
                        break;
                    }
                }
            }
        }
    }
    xhttp.open("GET", url, true);
    xhttp.send();
}