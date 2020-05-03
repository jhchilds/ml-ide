var timeBetweenKeystrokes = 500;
var timer;
var $editor = $('#firepad-container');

$editor.on('keydown', function () {
    clearTimeout(timer);
});

$editor.on('keyup', function () {
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
        success: function (response){
            console.log(response)
        }
    });
}