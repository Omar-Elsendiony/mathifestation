#!/usr/bin/node


setTimeout(() => {
    const elements = document.querySelectorAll('.btn');

    content_element = document.querySelectorAll('.content')[0];
    // console.log(content_element);

    // $(document).on('keyup', function(){
    //     content_element.setAttribute("contenteditable","false")
    //     var $newChild=$('hello'); 
    //     $('.content').append($newChild);
    // });

    // elements.forEach(element => {
    //     element.addEventListener('click', () => {
    //         let command = 'em';
    //         content_element.innerHTML += '<' + command + '></' + command + '>';
    //         content_element.innerHTML += 'added';
    //     });
    // });
}, 50);




// content_element = document.querySelectorAll('.content');

// console.log(elements);
// content_element.addEventListener('focus', () => {
//     alert('htghththet');
// });

// elements.forEach(element => {
//     element.addEventListener('click', () => {
//         // let command = element.dataset('element');
//         // content_element.innerHTML += '<' + command + '></' + command + '>';
//         // content_element.innerHTML += 'hyhrhh';
//         console.log('htghththet');
//         alert('htghththet');
//     });
// });
