const postgres = require('postgres');

const sql = postgres({
    host:'localhost',
        port: 5432,
        user: 'postgres',
        database:'postgres',
        password:'123456'

})
async function getVersion() {
    const reslut = await sql.raw(`select * from products2 `)
    console.log(reslut);
}
getVersion()










// const knex = require('knex');
// const db  = knex({
//     client:'pg',
//     connection: {
//         host:'localhost',
//         port: 5432,
//         user: 'postgres',
//         database:'postgres',
//         password:'123456'
//     }
// });

// // async function getVersion() {
// //     const reslut = await db.raw(`select * from products2 where id = 2`)
// //     console.log(reslut.rows);
// // }
// // getVersion()

// // db('products2')
// // .orderBy('name')
// // .select('price','id','name')

// db(products2)
// // .insert({name:'icar', price:1000},['id'])
// .insert([
//     {name:'samsung s23',price:555},
//     {name:'samsung s24',price:777}
// ],
// ["id" , "name" , "price"]

// )
// .then((data) => {
//     console.log(data);
// })
// .catch((e)=> {
// console.log(e);
// });
