// 1. Print numbers from 1 to 20, stop at 13
for (let i = 1; i <= 20; i++) {
  if (i === 13) break;
  console.log("Number:", i);
}

// 2. Loop through colors, stop at "blue"
let colors = ["red", "green", "yellow", "blue", "orange"];
for (let color of colors) {
  if (color === "blue") break;
  console.log("Color:", color);
}

// 3. Count to 50, stop when divisible by 4 and 5
for (let i = 1; i <= 50; i++) {
  if (i % 4 === 0 && i % 5 === 0) break;
  console.log("Count:", i);
}

// 4. Print letters, stop at "a"
let word = "elephant";
for (let letter of word) {
  if (letter === "a") break;
  console.log("Letter:", letter);
}

// 5. Add numbers until sum is 100
let sum = 0;
let n = 1;
while (true) {
  sum += n;
  if (sum >= 100) break;
  n++;
}
console.log("Sum reached 100 at number:", n, "Total sum:", sum);


// ---- 9-13: using continue ----

// 9. Skip 13
for (let i = 1; i <= 20; i++) {
  if (i === 13) continue;
  console.log("Number (skip 13):", i);
}

// 10. Skip "banana"
let fruits = ["apple", "banana", "orange", "grape"];
for (let fruit of fruits) {
  if (fruit === "banana") continue;
  console.log("Fruit:", fruit);
}

// 11. Skip numbers divisible by 3
for (let i = 1; i <= 30; i++) {
  if (i % 3 === 0) continue;
  console.log("Not divisible by 3:", i);
}

// 12. Print letters except "e"
let word2 = "cheese";
for (let letter of word2) {
  if (letter === "e") continue;
  console.log("Letter:", letter);
}

// 13. Skip even numbers from 1 to 50
for (let i = 1; i <= 50; i++) {
  if (i % 2 === 0) continue;
  console.log("Odd number:", i);
}


// ---- 14-18: arrow functions ----

// 14. Add two numbers
const add = (a, b) => a + b;
console.log("Add 5 + 3:", add(5, 3));

// 15. Greeting message
const greet = name => `Hello, ${name}!`;
console.log(greet("John"));

// 16. Double each number in array
const doubleArray = arr => arr.map(num => num * 2);
console.log("Doubled:", doubleArray([1, 2, 3]));

// 17. Check if number is even
const isEven = num => num % 2 === 0;
console.log("Is 4 even?", isEven(4));

// 18. Return string length
const getLength = str => str.length;
console.log("Length of 'hello':", getLength("hello"));
