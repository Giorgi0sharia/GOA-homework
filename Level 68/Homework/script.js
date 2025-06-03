// 1. Create an object with your name, age, and city.
let person = {
  name: "Alex",
  age: 25,
  city: "New York"
};

// 2. Access the value of a property in an object.
console.log(person.name); // Output: "Alex"

// 3. Add a new property to an existing object.
person.job = "Developer";
console.log(person.job); // Output: "Developer"

// 4. Create a nested object (an object inside another object).
person.contact = {
  email: "alex@example.com",
  phone: "123-456-7890"
};
console.log(person.contact.email); // Output: "alex@example.com"

// 5. Change the value of an existing property in an object.
person.age = 26;
console.log(person.age); // Output: 26

// 6. Check if two numbers are both greater than 10.
let a = 15, b = 12;
console.log(a > 10 && b > 10); // Output: true

// 7. Check if at least one of two conditions is true.
console.log(a > 20 || b > 10); // Output: true

// 8. Use the NOT operator to invert a boolean value.
let isAvailable = false;
console.log(!isAvailable); // Output: true

// 9. Combine multiple logical operations in a single expression.
let x = 5, y = 20, z = 15;
console.log((x < 10 && y > 15) || z === 10); // Output: true

// 10. Convert a number to a string using String().
let num = 123;
console.log(String(num)); // Output: "123"

// 11. Convert a boolean value to a string using String().
let flag = true;
console.log(String(flag)); // Output: "true"

// 12. Convert a string containing a number to a number using Number().
let strNum = "456";
console.log(Number(strNum)); // Output: 456

// 13. Use Number() to convert a boolean to a number.
console.log(Number(true));  // Output: 1
console.log(Number(false)); // Output: 0

// 14. Check what happens when you use Number() on a non-numeric string.
console.log(Number("hello")); // Output: NaN
