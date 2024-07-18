
setTimeout(() => {

    


    document.getElementById('submit').addEventListener('click',
        function(event) {

            var question = document.querySelector('.que_text').value;
            if (question == ""){
                alert("Please fill the question")
                return;
            }
            
            var inputs = document.querySelectorAll('.option input')
            for (let i = 0; i < inputs.length; i++) {
                if (inputs[i].value == "") {
                    alert("Please fill all the options")
                    return;
                }
            }
            questions[question_index] = document.querySelector('.que_text').value
            inputs = document.querySelectorAll('.option input')
            inputs_values = new Array();
            
            for (let i = 0; i < inputs.length; i++) {
                inputs_values.push(inputs[i].value)
            }


            questions_options[question_index] = inputs_values

            if (node_selected == null){
                alert("Please select the correct answer")
                return;
            }

            correct = node_selected.nextElementSibling.value
            correct_choice[question_index] = correct

            /////////// start submitting the content of the question, options and title /////////////
            submitContent()
    });

}, 1000);

















/////////////////////////////////////////////////////
//////////////// ANIMATE RUBIK //////////////////////
////////////////////////////////////////////////////

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

        // console.log(screen.height)
        
        var position = element.getBoundingClientRect();
        var x = position.left;
        var y = position.top;
        // console.log(y)
        
        if (start == true) {
            start = false;
            upToDown();
        }
        else{
            // console.log("else")
            if (y > 0.3 * screen.height ) {
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
