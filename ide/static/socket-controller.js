var socket = io.connect('http://10.0.0.233:5000');

function getEl(id) {
    return document.getElementById(id)
}
const editor = getEl("codeForm");

editor.addEventListener("keyup", (evt) => {
    const text = editor_for_source_code.getValue();
    socket.emit( 'code_text' , text);
});

socket.on('code_text', (data) => {
    editor_for_source_code.setValue(data);
});




