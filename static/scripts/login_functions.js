/*import { getAuth, onAuthStateChanged, createUserWithEmailAndPassword, signInWithEmailAndPassword, 
  GoogleAuthProvider, signInWithPopup, signOut, signInWithRedirect} from "firebase/auth";
*/
'use strict';

/**
 * Login()
 * Allows the user to log in to the website with an email and password and also using Google.
 * It uses FirebaseUI as a backend authentication service to sign-in and authenticate users.
 */

window.addEventListener('load', function() {
  document.getElementById('sign-out').onclick = function() {
    firebase.auth().signOut();
  };

  // FirebaseUI config.
  var uiConfig = {
    signInSuccessUrl: '/',
    signInOptions: [
        // Comment out any lines corresponding to providers you did not check in          
        // the Firebase console.
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        firebase.auth.EmailAuthProvider.PROVIDER_ID,
    ],
    // Terms of service url.
    tosUrl: '<your-tos-url>'
  };
  firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
      // User is signed in, so display the "sign out" button and login info.
      document.getElementById('sign-out').hidden = false;          
      document.getElementById('reset-password').hidden = false;
      document.getElementById('before-login').hidden = true;
      document.getElementById('login-welcome').innerHTML = 'Welcome ' + user.displayName + '!';

      console.log(`Signed in as ${user.displayName} (${user.email})`);
      
      user.getIdToken().then(function(token) {
      // Add the token to the browser's cookies. The server will then be
      // able to verify the token against the API.
      // SECURITY NOTE: As cookies can easily be modified, only put the
      // token (which is verified server-side) in a cookie; do not add other
      // user information.
      document.cookie = "token=" + token;
    });
    } else {
      // User is signed out.
      // Initialize the FirebaseUI Widget using Firebase.

      var ui = new firebaseui.auth.AuthUI(firebase.auth());
      
      // Show the Firebase login button.
      ui.start('#firebaseui-auth-container', uiConfig);
      
      // Update the login state indicators.
      document.getElementById('sign-out').hidden = true;
      document.getElementById('login-welcome').innerHTML = 'Welcome!';
      
      // Clear the token cookie.
      document.cookie = "token=";
      }
  }, function(error) {
      console.log(error);
      alert('Unable to log in: ' + error)
  });
});
