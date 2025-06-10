//Array basics
let fruits = ["apple", "banana", "cherry", "orange", "mango"];
console.log(fruits[0]); // First
console.log(fruits[fruits.length - 1]); // Last
console.log("Total fruits:", fruits.length);

//modifying arrays
let numbers = [2, 3, 4, 5];
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i] * 2);
}

function sumArray(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum;
}
console.log(sumArray([1, 2, 3])); 

//find the largest number
function findLargest(arr) {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}
console.log(findLargest([4, 8, 2, 10, 6]));

//array includes check
let favoriteMovies = ["Inception", "Interstellar", "Avatar", "Titanic", "Gladiator"];
let userMovie = prompt("Enter a movie name:");
if (favoriteMovies.includes(userMovie)) {
  alert("Yes, it's one of my favorites!");
} else {
  alert("No, I don't like that one much.");
}

//join and sort
let words = ["banana", "apple", "pear", "orange"];
words.sort();
let result = words.join(", ");
console.log(result); 

//random number generator
function getRandom1to10() {
  return Math.floor(Math.random() * 10) + 1;
}
console.log(getRandom1to10());

//round a number
let num = parseFloat(prompt("Enter a decimal number:"));
console.log("Floor:", Math.floor(num));
console.log("Ceil:", Math.ceil(num));
console.log("Round:", Math.round(num));

//find the maximum and minimum
let nums = [7, 3, 15, 1, 9];
console.log("Max:", Math.max(...nums));
console.log("Min:", Math.min(...nums));

//colors array manipulation
let colors = ["red", "green", "blue"];
colors.push("yellow");
colors.shift();
colors.unshift("purple");
console.log(colors); 

//loop trough an array
let animals = ["dog", "cat", "rabbit", "hamster", "elephant"];
for (let i = 0; i < animals.length; i++) {
  console.log(animals[i]);
}





