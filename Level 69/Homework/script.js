let number = Number(prompt("Enter a number:"));

if (number > 0) {
  alert("The number is positive.");
} else if (number < 0) {
  alert("The number is negative.");
} else {
  alert("The number is zero.");
}
let age = Number(prompt("Enter your age:"));

if (age >= 18) {
  alert("You can vote!");
} else {
  alert("You are not eligible to vote.");
}
let num1 = Number(prompt("Enter the first number:"));
let num2 = Number(prompt("Enter the second number:"));

if (num1 > num2) {
  alert("The first number is larger.");
} else if (num2 > num1) {
  alert("The second number is larger.");
} else {
  alert("Both numbers are equal.");
}

//is this a square
function isSquare(n) {
  return Number.isInteger(Math.sqrt(n));
}
//name shuffler
function nameShuffler(str) {
  return str.split(' ').reverse().join(' ');
}
//isogram checker
function isIsogram(str) {
  str = str.toLowerCase();
  return new Set(str).size === str.length;
}
//completing duplicates
function duplicateCount(text) {
  let lower = text.toLowerCase();
  let counts = {};
  let duplicates = 0;

  for (let char of lower) {
    counts[char] = (counts[char] || 0) + 1;
    if (counts[char] === 2) {
      duplicates++;
    }
  }
  return duplicates;
}
//jaden casing strings
String.prototype.toJadenCase = function () {
  return this.split(' ')
             .map(word => word.charAt(0).toUpperCase() + word.slice(1))
             .join(' ');
};
