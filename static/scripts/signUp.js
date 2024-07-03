
setTimeout(() => {

    $("#username").focusout(function(){
        $.ajax({
            type: 'GET',
            url: "/checkUserNameExists",
            data: {username: $("#username").val()},
            dataType: "text",
            // success: function(data){
            //     alert("User Exists");
            // },
            // fail: function(data){
            //     alert("User does not exist");
            // }
        }).done(function(data){
            console.log(data)
        });
    });
}, 50);

