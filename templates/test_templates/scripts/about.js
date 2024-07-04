
setTimeout(() => {

    window.SineWave = SineWave = function() {
        this.css = function(p) {
            s = Math.sin((p-1)*500);  // 1
            x = (5000 - p*5000) * 10; // 2
            y = s * 100 + 150;
            return {top: y + "px", left: x + "px"};
        } 
    }
    
    $(".objectFloating").stop().animate(
        {path: new SineWave}, 
        50000, // 3
        "linear"
    );
    

    function leftToRight() {
        $("#animateMe").animate({ left: ['+=10%', 'linear'], top: ['+=5%', 'swing'] }, 1000, function() {
            $(this).animate({ left: ['+=10%', 'linear'], top: ['-=5%', 'swing'] }, 1000, function() {
                $(this).animate({ left: ['+=10%', 'linear'], top: ['+=5%', 'swing'] }, 1000, function() {
                    $(this).animate({ left: ['+=10%', 'linear'], top: ['-=5%', 'swing'] }, 1000, function() {
                        animateElement(); // Call the function again to loop the animation
                    });
                });
            });
        });
    }

    function rightToLeft() {
        $("#animateMe").animate({ left: ['-=10%', 'linear'], top: ['+=5%', 'swing'] }, 1000, function() {
            $(this).animate({ left: ['-=10%', 'linear'], top: ['-=5%', 'swing'] }, 1000, function() {
                $(this).animate({ left: ['-=10%', 'linear'], top: ['+=5%', 'swing'] }, 1000, function() {
                    $(this).animate({ left: ['-=10%', 'linear'], top: ['-=5%', 'swing'] }, 1000, function() {
                        animateElement(); // Call the function again to loop the animation
                    });
                });
            });
        });
    }
    var start = true
    var direction = "right";
    function animateElement() {
        var element = document.getElementById('animateMe');
        var position = element.getBoundingClientRect();
        var x = position.left;
        var y = position.top;
        // console.log(x, y);
        // console.log(screen.width);
        if (start == true) {
            start = false;
            leftToRight();
        }
        else{
            // console.log("else")
            if (x >= 0.6 * screen.width ) {
                direction = "left";
                // rightToLeft();
            }
            if (x <= 0.2 * screen.width) {
                direction = "right"
                // leftToRight();
            }
            if (direction == "right") {
                leftToRight();
            }
            else{
                rightToLeft();
            }

        }
        
    }
    
    // Start the animation
    animateElement();



}, 50);

