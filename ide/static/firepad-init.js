 function init() {
      //// Initialize Firebase.
     const config = {
         apiKey: "AIzaSyA3PEmLbal6m6jFx9OHsmiSDQ7aHi8y6ZE",
         authDomain: "ml-ide.firebaseapp.com",
         databaseURL: "https://ml-ide.firebaseio.com",
         projectId: "ml-ide",
         storageBucket: "ml-ide.appspot.com",
         messagingSenderId: "337288733634",
         appId: "1:337288733634:web:dcb8dc5b5f521e18032c5b",
         measurementId: "G-7H434BFQ1L"
    };
      firebase.initializeApp(config);

      //// Get Firebase Database reference.
      var firepadRef = getExampleRef();

      //// Create CodeMirror (with line numbers and the JavaScript mode).
      var codeMirror = CodeMirror(document.getElementById('firepad-container'), {
        lineNumbers: true,
        mode: 'javascript'
      });

      //// Create Firepad.
      var firepad = Firepad.fromCodeMirror(firepadRef, codeMirror, {
        defaultText: '// JavaScript Editing with Firepad!\nfunction go() {\n  var message = "Hello, world.";\n  console.log(message);\n}'
      });
    }

    // Helper to get hash from end of URL or generate a random one.
    function getExampleRef() {
      var ref = firebase.database().ref();
      var hash = window.location.hash.replace(/#/g, '');
      if (hash) {
        ref = ref.child(hash);
      } else {
        ref = ref.push(); // generate unique location.
        window.location = window.location + '#' + ref.key; // add it as a hash to the URL.
      }
      if (typeof console !== 'undefined') {
        console.log('Firebase data: ', ref.toString());
      }
      return ref;
    }