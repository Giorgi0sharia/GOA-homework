

// 2.1 - Function that prints all arguments using a loop
function printArguments(...args) {
  for (let arg of args) {
    console.log(arg);
  }
}
printArguments("hello", 5, true, null);

// 2.2 - Function that counts how many arguments were passed
function countArguments(...args) {
  console.log("Number of arguments:", args.length);
}
countArguments("a", "b", 3, 4);

// 2.3 - Function that adds numeric arguments and prints the total
function sumNumericArgs(...args) {
  let total = 0;
  for (let arg of args) {
    if (typeof arg === "number") total += arg;
  }
  console.log("Total of numeric arguments:", total);
}
sumNumericArgs(1, "hi", 3, true, 5);


// 7.1 - Anonymous function assigned to a variable that multiplies two numbers
const multiply = function (a, b) {
  return a * b;
};
console.log("Multiply 3 * 4 =", multiply(3, 4));

// 7.2 - Anonymous function in setInterval (stops after 6 seconds)
let interval = setInterval(function () {
  console.log("This message shows every 2 seconds");
}, 2000);
setTimeout(() => clearInterval(interval), 6000); // Stop after 6 sec

// 7.3 - Anonymous function as an event listener for a button click
const button = document.createElement("button");
button.textContent = "Click Me!";
document.body.appendChild(button);
button.addEventListener("click", function () {
  alert("Button was clicked!");
});


// 10.1 - IIFE that prints “Hello, world!”
(function () {
  console.log("Hello, world!");
})();

// 10.2 - IIFE that calculates square of a number
(function (num) {
  console.log("Square of", num, "is", num * num);
})(5);

// 10.3 - IIFE that sums array elements
(function (arr) {
  let sum = 0;
  for (let num of arr) sum += num;
  console.log("Sum of array:", sum);
})([1, 2, 3, 4, 5]);

// 11 - Function that stops printing at value 0 using break
function stopAtZero(...args) {
  for (let arg of args) {
    if (arg === 0) break;
    console.log(arg);
  }
}
stopAtZero(1, 2, 3, 0, 4, 5);

// 12 - Function that skips strings using continue
function printOnlyNumbers(...args) {
  for (let arg of args) {
    if (typeof arg === "string") continue;
    console.log(arg);
  }
}
printOnlyNumbers(1, "hello", true, 3, "world");



// 13 - Local variable scope example
function testScope() {
  let localVar = "I'm local!";
}
testScope();

// 14 - Nested functions with outer scope variable
function outerFunction() {
  let message = "Original";
  console.log("Before inner function:", message);

  function innerFunction() {
    message = "Modified by inner function";
  }

  innerFunction();
  console.log("After inner function:", message);
}
outerFunction();

// 15 - var, let, and const scope demonstration
function scopeDemo() {
  if (true) {
    var x = 10;
    let y = 20;
    const z = 30;
    console.log("Inside block: x =", x, "y =", y, "z =", z);
  }

  console.log("Outside block: x =", x); 
}
scopeDemo();
