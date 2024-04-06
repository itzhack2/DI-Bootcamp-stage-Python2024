//Exercise 1 : Scope 
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }console.log( funcOne());
// #1.1 - run in the console:
//funcOne() 
// #1.2 What will happen if the variable is declared 
// with const instead of let ?
// function funcOne() {
//     const a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }
// Uncaught TypeError
// //#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
// // #2.2 What will happen if the variable is declared 
// // with const instead of let ?


// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared 
// with const instead of let ?

// 🌟 Exercise 2 : Ternary Operator
// function winBattle(){
//     return true;
// }
// const winBattle = () => true;
// let experiencePoints;
// experiencePoints = winBattle() ? 10 : 1
// console.log("experiencePoints:",experiencePoints);


// 🌟 Exercise 3 : Is It A String ?
// const isString = (arg) => typeof arg === "string";
// console.log(isString("hello")); //true
// console.log("isString([1,2,4,0])); //false


// 🌟Exercise 4 : Find The Sum
// const sum = (a, b) => a + b;
// console.log(sum(5, 3)); // Output: 8

// 🌟 Exercise 5 : Kg And Grams
// function kgToGramsDeclaration(kg) {
//     return kg * 1000;
// }
// console.log(kgToGramsDeclaration(2)); // Output: 2000
// const kgToGramsExpression = function(kg) {
//     return kg * 1000;
// };
// console.log(kgToGramsExpression(2)); // Output: 2000
// const kgToGramsArrow = (kg) => kg * 1000;
// console.log(kgToGramsArrow(2)); // Output: 2000

// 🌟 Exercise 6 : Fortune Teller
// (function(numberOfChildren, partnerName, geographicLocation, jobTitle) {
//     const message = `You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnerName} with ${numberOfChildren} kids.`;
//     document.getElementById('fortune').innerText = message;
// })(2, 'Emma', 'Paris', 'software engineer');


// 🌟 Exercise 7 : Welcome
// (function(username) {
//     const navbar = document.getElementById('navbar');
//     navbar.innerHTML = `<div>Welcome, ${username} <img src="profile.jpg" alt="Profile Picture"></div>`;
// })('John');

// 🌟 Exercise 8 : Juice Bar
// function makeJuice(size) {
//     const ingredients = [];
//     function addIngredients(ingredient1, ingredient2, ingredient3) {
//         ingredients.push(ingredient1, ingredient2, ingredient3);
//     }
//     function displayJuice() {
//         const message = `The client wants a ${size} juice, containing ${ingredients.join(', ')}.`;
//         console.log(message);
//     }
//     addIngredients('apple', 'banana', 'orange');
//     addIngredients('strawberry', 'mango', 'pineapple');
//     displayJuice();
// }
// makeJuice('medium');
