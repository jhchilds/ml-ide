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
            console.log(response.errors);

            stdout = response.output;
            stderr = response.errors;

            if (stdout) {
                $("#show-stdout").click();
            } else {
                $("#show-stderr").click();
            }
        }
    });
}