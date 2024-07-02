
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
    
}, 50);

