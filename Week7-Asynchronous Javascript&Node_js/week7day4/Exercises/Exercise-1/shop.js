const products = require('./products.js');

function findProductByName(productName) {
  const product = products.find(prod => prod.name === productName);
  if (product) {
    console.log(`Product found: ${product.name}`);
    console.log(`Price: $${product.price}`);
    console.log(`Category: ${product.category}`);
  } else {
    console.log(`Product '${productName}' not found.`);
  }
}
// Test the function
findProductByName("Laptop");
findProductByName("Chair");
findProductByName("Tablet");
