var timeBetweenKeystrokes = 200;
var timer;
var editor = $('#firepad-container');
var currentLang;

$( document ).ready(function() {
    sendCode();
});

editor.on('keydown', function () {
    clearTimeout(timer);
});

editor.on('keyup', function () {
    clearTimeout(timer);
    timer = setTimeout(sendCode, timeBetweenKeystrokes);
});

function sendCode() {
    $.ajax({
        type: "POST",
        url: "/classify",
        dataType: "json",
        data: {
            code: codeMirror.getValue()
        },
        success: function (response) {
            console.log(response.lang);
            var mime;
            var mode;
            var url = "https://codemirror.net/2/mode/%N/%N.js";

            switch (response.lang) {
                case "py":
                    mime = "text/x-python";
                    mode = "python";
                    break;
                case "c":
                    mime = "text/x-csrc";
                    mode = "clike";
                    break;
                case "js":
                    mime = "text/javascript";
                    mode = "javascript";
                    break;
                case "java":
                    mime = "text/x-java";
                    mode = "clike";
                    break;
                case "swift":
                    mime = "text/x-swift";
                    mode = "swift";
                    url = "https://codemirror.net/mode/%N/%N.js"
                    break;
                case "hs":
                    mime = "text/x-haskell";
                    mode = "haskell";
                    break;
                default:
                    mime = undefined;
                    mode = undefined;
            }

            if (mime !== undefined && mode !== undefined) {
                CodeMirror.modeURL = url;
                codeMirror.setOption("mode", mime);
                CodeMirror.autoLoadMode(codeMirror, mode);
                console.log(response.lang);
                currentLang = response.lang;
            } else {
                console.log("unknown lang");
            }
        }
    });
}

