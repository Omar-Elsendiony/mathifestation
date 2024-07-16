setTimeout(() => {

    $("#post").click(function() {
        var content = document.getElementsByClassName("content")[0].textContent;
        document.getElementById("answer_submit").value = content;
        // alert(content);
        // question.value = content;

        $('.form_content').submit();
        // return false;
    });
}, 100);
