import { getAuth, onAuthStateChanged, GoogleAuthProvider, signInWithPopup, signOut} from "firebase/auth";



/**
 * Login()
 * Allows the user to log in to the website with an email and password and also using Google.
 * 
 * It uses FirebaseUI as a backend authentication service to sign-in and authenticate users.
 */
function Login() {

    // Initialize the FirebaseUI Widget using Firebase.
    var ui = new firebaseui.auth.AuthUI(firebase.auth());

    var uiConfig = {
        callbacks: {
          signInSuccessWithAuthResult: function(authResult, redirectUrl) {
            // User successfully signed in.
            // Return type determines whether we continue the redirect automatically
            // or whether we leave that to developer to handle.
            return true;
          },
          uiShown: function() {
            // The widget is rendered.
            // Hide the loader.
            document.getElementById('loader').style.display = 'none';
          }
        },
        // Will use popup for IDP Providers sign-in flow instead of the default, redirect.
        signInFlow: 'popup',
        signInSuccessUrl: "{{ url_for('index') }}",
        signInOptions: [
          // Leave the lines as is for the providers you want to offer your users.
          firebase.auth.GoogleAuthProvider.PROVIDER_ID,
          firebase.auth.EmailAuthProvider.PROVIDER_ID,
        ],
        // Terms of service url.
        tosUrl: '<your-tos-url>',
        // Privacy policy url.
        privacyPolicyUrl: '<your-privacy-policy-url>'
      };
    
    
      // The start method will wait until the DOM is loaded.
    ui.start('#firebaseui-auth-container', uiConfig);


    
    
    
    
    /* // Get login details from form.
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
    xhttp.send(); */
}