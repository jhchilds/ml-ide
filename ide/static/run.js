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


            var out = "";
            if (response.output === ""){
                out = response.errors;
                console.log(response.errors);
            }
            else{
                out = response.output;
                console.log(response.output);
            }
            document.getElementById("output-box").innerText = out
        }
    });
}