//----------- 🌟 Exercise 1 : Change The Article
// const h1 = document.querySelector('h1');
// console.log(h1.textContent);
// const paragraphs = document.querySelectorAll('article p');
// const lastParagraph = paragraphs[paragraphs.length - 1];
// lastParagraph.remove();
// const h2 = document.querySelector('#chocolate');
// h2.addEventListener('click', function() {
//     h2.style.backgroundColor = 'red';
// });
// const h3 = document.querySelector('h3');
// h3.addEventListener('click', function() {
//     h3.style.display = 'none';
// });
// const boldButton = document.getElementById('boldButton');
// boldButton.addEventListener('click', function() {
//     paragraphs.forEach(paragraph => {
//         paragraph.style.fontWeight = 'bold';
//     });
// });
// h1.addEventListener('mouseover', function() {
//     const randomSize = Math.floor(Math.random() * 101);
//     h1.style.fontSize = randomSize + 'px';
// });

// ------------- 🌟Exercise 2: Work With Forms
// const form = document.getElementById('myForm');
// console.log(form);

// const fnameInput = document.getElementById('fname');
// const lnameInput = document.getElementById('lname');
// console.log(fnameInput, lnameInput);

// const firstnameInput = document.querySelector('input[name="firstname"]');
// const lastnameInput = document.querySelector('input[name="lastname"]');
// console.log(firstnameInput, lastnameInput);

// form.addEventListener('submit', function(event) {
//     event.preventDefault();
    
//     const fname = fnameInput.value;
//     const lname = lnameInput.value;
//     // Check if inputs are not empty
//     if (fname && lname) {
//         // Create li elements
//         const firstNameLi = document.createElement('li');
//         firstNameLi.textContent = fname;
//         const lastNameLi = document.createElement('li');
//         lastNameLi.textContent = lname;
//         // Append them to the ul
//         const ul = document.querySelector('.usersAnswer');
//         ul.appendChild(firstNameLi);
//         ul.appendChild(lastNameLi);
//     }
// });

// <!------------------ 🌟 Exercise 3 : Transform The Sentence ------>

// let allBoldItems;
// function getBoldItems() {
//     const boldItems = document.querySelectorAll('strong');
//     allBoldItems = boldItems;
// }
// function highlight() {
//     allBoldItems.forEach(item => {
//         item.style.color = 'blue';
//     });
// }
// function returnItemsToDefault() {
//     allBoldItems.forEach(item => {
//         item.style.color = 'black';
//     });
// }
// const paragraph = document.querySelector('p');
// paragraph.addEventListener('mouseover', highlight);
// paragraph.addEventListener('mouseout', returnItemsToDefault);


//--------------- 🌟 Exercice 4 : Volume Of A Sphere
// let form = document.forms[0]
// console.log(form)
// //adding eventListener to the button
// form.addEventListener('submit', calculateAndOutput)
// //how to avoid the default action (refresh) to happen:
// function getRadius(e){
//     e.preventDefault()
//     console.log(form.elements.radius.value)
//     return form.elements.radius.value
// }
// function calculateVolume(radius){
//     return (4/3 * 3.14 * (radius**3))
// }
// function displayVolume(volume){
//     form.elements.volume.value = volume;
// }
// function calculateAndOutput(e){
//     let radius = getRadius(e)
//     let volume = calculateVolume(radius)
//     displayVolume(volume)
// }
