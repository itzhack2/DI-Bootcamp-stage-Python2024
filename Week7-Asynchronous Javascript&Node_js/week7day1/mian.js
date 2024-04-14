// 🌟 Exercise 1 : Comparison

function compareToTen(num) {
  return new Promise ((resolve,reject)=> {
    if(num < 10){
        resolve('Number is smaller then 10- this is good')
    }else{
        reject('Number is to high - try again')
    }
  });
   
} 
compareToTen(5)
    .then(res => console.log(res))
    .catch(err => console.log(err))


// 🌟 Exercise 2 : Promises
const Promise = new Promise((resolve,reject)=>{
    setTimeout(() => resolve('success'), 4000);
});

Promise
.then((res) => console.log('success.Result:', res))
.catch((err) => console.error('Something went wrong',err))


// 🌟 Exercise 3 : Resolve & Reject

const Promises = Promise.resolve(2);
const Promise2 = Promise.reject('boo');

Promise2.then((res) => console.log(res)).catch((err)=>console.error(err));