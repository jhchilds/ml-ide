var socket = io.connect('http://10.0.0.233:5000');

function getEl(id) {
    return document.getElementById(id)
}
const editor = getEl("codeForm");




editor.addEventListener("keyup", (evt) => {

    var cursorPosBeforeKeyup = editor_for_source_code.getCursor();

    var lineBeforeKeyup = cursorPosBeforeKeyup['line'];
    var charBeforeKeyup = cursorPosBeforeKeyup['ch']-1;

    var cursorPosAfterKeyup = editor_for_source_code.getCursor();
    var lineAfterKeyup = cursorPosAfterKeyup['line'];
    var charAfterKeyup = cursorPosAfterKeyup['ch'];

    var textToReplace = editor_for_source_code.getRange(cursorPosBeforeKeyup, cursorPosAfterKeyup);

    var data = {
        'lineBeforeKeyup': lineBeforeKeyup,
        'charBeforeKeyup': charBeforeKeyup,
        'lineAfterKeyup' :  lineAfterKeyup,
        'charAfterKeyup' :  charAfterKeyup,
        'textToReplace'  :  textToReplace,
    };

    console.log(charBeforeKeyup);

    const text = editor_for_source_code.getValue();
    socket.emit( 'code_text' , text);

});

socket.on('code_text', (data) => {
    editor_for_source_code.setValue(data);
});




