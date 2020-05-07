function runCode() {
    var value = $("#selected-language").val();
    var lang = undefined;
    console.log(value);
    if (value === "predict") {
        lang = currentLang;
    } else {
        lang = value;
    }

    $.ajax({
        type: "POST",
        url: "/run",
        dataType: "json",
        data: {
            code: codeMirror.getValue(),
            lang: lang
        },
        success: function (response) {
            console.log(response.output);
            console.log(response.errors);

            stdout = response.output;
            stderr = response.errors;

            $(".output-box").show();
            if (stdout) {
                $("#show-stdout").click();
            } else {
                $("#show-stderr").click();
            }
        }
    });
}