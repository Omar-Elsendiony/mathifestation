
setTimeout(() => {
    var start = true
    var direction = "down";
    function downToUp() {
        $("#floatingRubik").animate({ top: '-=50%' }, 10000, function() {
                animateElement(); 
        })};


    function upToDown() {
        $("#floatingRubik").animate({ top: '+=50%' }, 10000, function() {
                animateElement();
        })};

    function animateElement() {
        var parentElement = document.getElementsByClassName('playing_rubik')[0];
        visibilityParent = parentElement.checkVisibility();
        // console.log(visibilityParent)
        if (visibilityParent == false){
            return
        }

        var element = document.getElementById('floatingRubik');

        console.log(screen.height)
        
        var position = element.getBoundingClientRect();
        var x = position.left;
        var y = position.top;
        console.log(y)
        
        if (start == true) {
            start = false;
            upToDown();
        }
        else{
            // console.log("else")
            if (y >= 0.4 * screen.height ) {
                direction = "up";
                // rightToLeft();
            }
            if (y <= 0.3 * screen.height) {
                direction = "down"
                // leftToRight();
            }
            if (direction == "down") {
                upToDown();
            }
            else{
                downToUp();
            }
        }
    }
    // Start the animation
    animateElement();

}, 50);
