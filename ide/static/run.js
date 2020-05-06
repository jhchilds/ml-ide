function runCode() {
    $.ajax({
        type: "POST",
        url: "/run",
        dataType: "json",
        data: {
            code: codeMirror.getValue(),
            lang: currentLang
        },
        success: function (response) {
            console.log(response.output);
        }
    });
}