//import { getAuth, onAuthStateChanged, createUserWithEmailAndPassword, signInWithEmailAndPassword, 
//  GoogleAuthProvider, signInWithPopup, signOut, signInWithRedirect, sendPasswordResetEmail} from "firebase/auth";
'use strict';

/**
 * Allows the user to log in to the website with an email/password and also using Google.
 * It uses FirebaseUI as a backend authentication service to sign-in and authenticate users.
 * 
 * If user is new, then it automatically registers the user
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
    tosUrl: 'https://www.privacypolicygenerator.org/live.php?token=5RL7wPYDaYFwiyTwS89vrqVdIVOaa0ec'
  };
  //firebase.auth().onAuthStateChanged(function(user) {
  firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
      // User is signed in, so display the "sign out" button and login info.
      document.getElementById('sign-out').hidden = false;          
      document.getElementById('reset-password').hidden = false;
      document.getElementById('delete-user').hidden = false;
      document.getElementById('before-login').hidden = true;
      document.getElementById('login-welcome').innerHTML = 'Welcome ' + user.displayName + '!';

      // console.log(`Signed in as ${user.displayName} (${user.email})`); // only for debugging
      
      user.getIdToken().then(function(token) {
      // Add the token to the browser's cookies. The server will then be
      // able to verify the token against the API.
      // SECURITY NOTE: As cookies can easily be modified, only put the
      // token (which is verified server-side) in a cookie; do not add other
      // user information.
      document.cookie = "token=" + token;
      
      document.getElementById('reset-password').onclick = function() { // sends password reset email
        firebase.auth().sendPasswordResetEmail(user.email)
        .then(() => {
          alert("Password reset email sent!")
        })
        .catch(() => {
          const errorCode = error.code;
          const errorMessage = error.message;   
          console.log(errorCode, errorMessage)   
        })
      }

      document.getElementById('delete-user').onclick = function() { // deletes the user's account and signs out
        firebase.auth().deleteUser(user)
          .then(() => {
            // User is signed out.
            // Initialize the FirebaseUI Widget using Firebase.

            var ui = new firebaseui.auth.AuthUI(firebase.auth());
            
            // Show the Firebase login button.
            ui.start('#firebaseui-auth-container', uiConfig);
            
            alert("User has been deleted, you are now signed out")
          })
          .catch(() => {
            const errorCode = error.code;
            const errorMessage = error.message;   
            console.log(errorCode, errorMessage)   
          })
      }
    });
    } else {
      // User is signed out.
      // Initialize the FirebaseUI Widget using Firebase.

      var ui = new firebaseui.auth.AuthUI(firebase.auth());
      
      // Show the Firebase login button.
      ui.start('#firebaseui-auth-container', uiConfig);

      // alert("You have been signed out!")
      
      // Update the login state indicators.
      document.getElementById('sign-out').hidden = true;
      document.getElementById('reset-password').hidden = true;
      document.getElementById('delete-user').hidden = true;
      document.getElementById('login-welcome').innerHTML = 'Welcome!';
      
      // Clear the token cookie.
      document.cookie = "token=";
      }
  }, function(error) {
      console.log(error);
      alert('Unable to log in: ' + error)
  });
});
