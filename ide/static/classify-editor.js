var timeBetweenKeystrokes = 500;
var timer;
var $input = $('#firepad-container');

$input.on('keydown', function () {
    clearTimeout(timer);
});

$input.on('keyup', function () {
    clearTimeout(timer);
    timer = setTimeout(sendCode, timeBetweenKeystrokes);
});

function sendCode() {
    $.ajax({
        type: "POST",
        url: "http://localhost:5000/classify/",
        dataType: "json",
        data: {
            code: codeMirror.getValue()
        }
    });
}