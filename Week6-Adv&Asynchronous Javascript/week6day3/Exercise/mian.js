// // 🌟 Exercise 1 : Location
// const person = {
//     name: 'John Doe',
//     age: 25,
//     location: {
//         country: 'Canada',
//         city: 'Vancouver',
//         coordinates: [49.2827, -123.1207]
//     }
// }
// const {name, location: {country, city, coordinates: [lat, lng]}} = person;
// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);
// // Output: I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

// // 🌟 Exercise 2: Display Student Info
// function displayStudentInfo(objUser){
//     const {first, last} = objUser;
//     return `Your full name is ${first} ${last}`;
// }
// console.log(displayStudentInfo({first: 'Elie', last:'Schoppik'}));

// // 🌟 Exercise 3: User & Id
// const users = { user1: 18273, user2: 92833, user3: 90315 };
// // Convert object to array
// const userArray = Object.entries(users);
// // Multiply each user's ID by 2
// const modifiedUserArray = userArray.map(([user, id]) => [user, id * 2]);
// console.log(modifiedUserArray);
// // Output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]

// // 🌟Exercise 4 : Person Class
// class Person {
//     constructor(name) {
//       this.name = name;
//     }
//   }
//   const member = new Person('John');
//   console.log(typeof member);
//   // Output: "object"

// // 🌟 Exercise 5: Dog Class
// // Option 2: 
// class Labrador extends Dog {
//     constructor(name, size) {
//       super(name);
//       this.size = size;
//     }
//   };
  
//   🌟 Exercise 6 : Challenges
// True, because they are two different arrays/objects in memory.
// False, because the objects are not the same in memory even though their contents are the same.

// Output:
// 4
// 4
// 5
// Explanation: object1, object2, and object3 all reference the same object in memory, so when object1's number property is changed, it reflects in object2 and object3. object4 is a separate object with its own number property.


// 🌟 Exercise 7: Animal 
// class Animal {
//     constructor(name, type, color) {
//       this.name = name;
//       this.type = type;
//       this.color = color;
//     }
//   }
//   class Mamal extends Animal {
//     sound(noise) {
//       return `Moooo I'm a ${this.type}, named ${this.name} and I'm ${this.color}. ${noise}`;
//     }
//   }
//   const farmerCow = new Mamal('Lily', 'cow', 'brown and white');
//   console.log(farmerCow.sound('Moooo'));
  