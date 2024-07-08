
setTimeout(() => {

    $("#title").focus(function(){
        $("#number-one").toggleClass("blackWhite", 30000, "linear");
    });

    $("#title").focusout(function(){
        $("#number-one").toggleClass("blackWhite", 30000, "linear");
    });


    $(".content").focus(function(){
        $("#number-two").toggleClass("blackWhite", 30000, "linear");
    });

    $(".content").focusout(function(){
        $("#number-two").toggleClass("blackWhite", 30000, "linear");
    });


    $("#submit").focus(function(){
        $("#number-three").toggleClass("blackWhite", 30000, "linear");
    });

    $("#submit").focusout(function(){
        $("#number-three").toggleClass("blackWhite", 30000, "linear");
    });
    

    $("#submit").click(function() {
        // if ({{ user.is_authenticated }} == false) {

        // }
        var question = document.getElementById("question");
        content = document.getElementById("content").textContent;
        content2 = document.getElementById("title").value;
        console.log(content2);
        console.log(content);
        
        // question.setAttribute('value', content);
        question.value = content;

        $('.form_content').submit();
        // return false;
    });

}, 50);

