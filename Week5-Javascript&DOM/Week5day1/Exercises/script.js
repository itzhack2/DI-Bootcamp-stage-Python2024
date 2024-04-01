// 🌟 Exercise 1 : List Of People
// Part I - Review About Arrays
// const people = ["Greg", "Mary", "Devon", "James"];
// people.shift()
// people[3] = "jaosn"
// people.push("itzhack")
// console.log(people.indexOf("Mary"))
// new_Pepole=people.slice(1)
// console.log(new_Pepole);
// console.log(people);
// const index = people.indexOf("Foo");
// console.log(index);//The reason it returns -1 is because "Foo" does not exist in the people array.
// let last = people[people.length -1]
// console.log(last);

// Part II - Loops
// for (let i = 0; i < people.length; i++){
//     console.log(people[i]);
// if(people[i] === "Devon")
//     break;
// }
// 🌟 Exercise 2 : Your Favorite Colors
// const colors = ["blue", "red", "green", "yellow", "purple"];

// for (let i = 0; i < colors.length; i++) {
//     console.log(`My #${i + 1} choice is ${colors[i]}`);
// }
// 🌟 Exercise 3 : Repeat The Question
// 1.Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
// const user = prompt('"Please enter your Number:')
// const inputType = typeof user;
// console.log("The data type of the input is:", inputType);
// 2.While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// let userInput;
// while (true) {
//     userInput = prompt("Please enter a number:");
//     const number = parseFloat(userInput);
//     if (isNaN(number)) {
//         alert("Please enter a valid number.");
//         continue;
//     }
//     if (number < 10) {
//         break;
//     } else {
//         alert("The number should be smaller than 10. Please try again.");
//     }
// }
// console.log("The number is smaller than 10:", userInput);

// 🌟 Exercise 4 : Building Management
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor:{
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log();







// 🌟 Exercise 5 : Family




// 🌟 Exercise 6 : Rudolf
// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
//   }



// 🌟 Exercise 7 : Secret Group
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];