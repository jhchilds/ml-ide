function init() {

    var credentials = fetch('../static/credentials.json')
                .then(res => res.json());
    const config = {
        apiKey:            credentials.apiKey,
        authDomain:        credentials.authDomain,
        databaseURL:       credentials.databaseURL,
        projectId:         credentials.projectId,
        storageBucket:     credentials.storageBucket,
        messagingSenderId: credentials.messagingSenderId,
        appId:             credentials.appId,
        measurementId:     credentials.measurementId
    };

    firebase.initializeApp(config);

    var firepadRef = getExampleRef();
    var codeMirror = CodeMirror(document.getElementById('firepad-container'), {
        lineNumbers: true,
        mode: 'javascript'
    });
    var firepad = Firepad.fromCodeMirror(firepadRef, codeMirror, {
        defaultText: 'Welcome to ML-IDE'
    });
}

function getExampleRef() {
    var ref = firebase.database().ref();
    var hash = window.location.hash.replace(/#/g, '');
    if (hash) {
        ref = ref.child(hash);
    } else {
        ref = ref.push();
        window.location = window.location + '#' + ref.key;
    }
    if (typeof console !== 'undefined') {
        console.log('Firebase data: ', ref.toString());
    }
    return ref;
}