// ---------🌟 Exercise 1 : Find The Numbers Divisible By 23---------
// Create a function call displayNumbersDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.
// function displayNumbersDivisible(){
// let sum = 0 ;
// for ( let i = 0; i <= 500; i++){
//     if(i % 23 === 0 ){
//         console.log(i);
//         sum += i;
//     }
//  }
//  console.log("Sum:", sum);
// } 
// displayNumbersDivisible()

// ------------🌟 Exercise 2 : Shopping List-----------------

// Add the stock and prices objects to your js file.
// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
// Create a function called myBill() that takes no parameters.
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 
// const shoppingList = [ 'banana', 'orange', 'apple' ]
// function myBill(){
//     let totalPrice = 0;
//     for(const i of shoppingList){
//         if(i in stock && stock[i] > 0 ){
//             totalPrice += prices[i];
//             // stock[i];
//         }else {
//             console.log(`Sorry, ${item} is out of stock`);
//         }
//         return totalPrice
//     }
// } 
// console.log("shopping list total price:", myBill())

// Exercise 3: What’s In My Wallet ?
function changeEnough(itemPrice, amountOfChange) {
    const changeValues = [0.25, 0.1, 0.05, 0.01];
    let totalChange = 0;

    for (let i = 0; i < changeValues.length; i++) {
        totalChange += amountOfChange[i] * changeValues[i];
    }

    return totalChange >= itemPrice;
}

console.log(changeEnough(14.11, [2, 100, 0, 0])); // false
console.log(changeEnough(0.75, [0, 0, 20, 5])); // true

// Exercise 4: Vacations Costs
function hotelCost() {
    let nights = prompt("How many nights would you like to stay in the hotel?");
    while (isNaN(nights)) {
        nights = prompt("Please enter a valid number of nights:");
    }
    return nights * 140;
}

function planeRideCost(destination) {
    let cost;
    switch (destination.toLowerCase()) {
        case "london":
            cost = 183;
            break;
        case "paris":
            cost = 220;
            break;
        default:
            cost = 300;
    }
    return cost;
}

function rentalCarCost() {
    let days = prompt("How many days would you like to rent the car?");
    while (isNaN(days)) {
        days = prompt("Please enter a valid number of days:");
    }
    let cost = days * 40;
    if (days > 10) {
        cost *= 0.95; // 5% discount for more than 10 days
    }
    return cost;
}

function totalVacationCost() {
    const hotel = hotelCost();
    const destination = prompt("Where is your destination?");
    const planeTicket = planeRideCost(destination);
    const rentalCar = rentalCarCost();
    return `The hotel cost: $${hotel}, the plane tickets cost: $${planeTicket}, the car rental cost: $${rentalCar}`;
}

console.log(totalVacationCost());

// Exercise 5: Users
const container = document.getElementById("container");
console.log(container);

const lists = document.querySelectorAll(".list");
lists.forEach(list => {
    list.firstElementChild.textContent = "Your Name";
});

const firstUL = document.querySelector("ul");
firstUL.classList.add("student_list", "university", "attendance");

const secondLI = firstUL.lastElementChild;
secondLI.style.border = "2px solid black";

const body = document.querySelector("body");
body.style.fontSize = "18px";

// Bonus
if (container.style.backgroundColor === "lightblue") {
    alert("Hello x and y");
}

// Exercise 6: Change The Navbar
const navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

const newLi = document.createElement("li");
const textNode = document.createTextNode("Logout");
newLi.appendChild(textNode);
const ul = navBar.querySelector("ul");
ul.appendChild(newLi);

const firstLi = ul.firstElementChild;
const lastLi = ul.lastElementChild;
console.log(firstLi.textContent, lastLi.textContent);

// Exercise 7: My Book List
const section = document.querySelector(".listBooks");

const allBooks = [
    { title: "Book 1", author: "Author 1", image: "https://via.placeholder.com/100", alreadyRead: true },
    { title: "Book 2", author: "Author 2", image: "https://via.placeholder.com/100", alreadyRead: false }
];

allBooks.forEach(book => {
    const div = document.createElement("div");
    div.innerHTML = `<p>Title: ${book.title}</p><p>Author: ${book.author}</p>`;
    const image = document.createElement("img");
    image.src = book.image;
    image.style.width = "100px";
    if (book.alreadyRead) {
        div.style.color = "red";
    }
    div.appendChild(image);
    section.appendChild(div);
});
