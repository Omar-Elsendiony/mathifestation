setTimeout(() => {

    $("#post").click(function() {
        var content = document.getElementsByClassName("content")[0].textContent;
        document.getElementById("answer_submit").value = content;
        var check = prompt("Are you sure you want to submit?");
        if (check == null || check == "") {
            return false;
        }
        

        $('.form_content').submit();
        // return false;
    });
}, 100);
