let client = "John";
const groceries = {
    fruits: ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice: "20$",
    other: {
        paid: true,
        meansOfPayment: ["cash", "creditCard"]
    }
}
const displayGroceries = () => {
    groceries.fruits.forEach(fruit => console.log(fruit));
}
const cloneGroceries = () => {
    let user = client; 
    client = "Betty"; 
    let shopping = {...groceries};
    shopping.totalPrice = "35$";
    shopping.other.paid = false; 
    console.log(user); 
    console.log(shopping.totalPrice); 
    console.log(shopping.other.paid); 
}
cloneGroceries();