// 1. Countdown Timer
let count = 10;
let countdown = setInterval(() => {
  console.log(count);
  count--;
  if (count < 0) {
    clearInterval(countdown);
    console.log("Time's up!");
  }
}, 1000);

// 2. Flashing Title
let flashCount = 0;
let titleInterval = setInterval(() => {
  document.title = document.title === "Hello" ? "Goodbye" : "Hello";
  flashCount++;
  if (flashCount === 6) {
    clearInterval(titleInterval);
  }
}, 1000);

// 3. Move a Box (Optional DOM Task)
let box = document.createElement("div");
box.style.width = "50px";
box.style.height = "50px";
box.style.background = "red";
box.style.position = "absolute";
box.style.left = "0px";
document.body.appendChild(box);
let position = 0;
let moveBox = setInterval(() => {
  position += 10;
  box.style.left = position + "px";
  if (position >= 100) {
    clearInterval(moveBox);
  }
}, 200);

// 4. Random Number Logger
let randomCount = 0;
let randomInterval = setInterval(() => {
  let num = Math.floor(Math.random() * 10) + 1;
  console.log(num);
  randomCount++;
  if (randomCount === 5) {
    clearInterval(randomInterval);
  }
}, 1500);

// 5. Array to Uppercase
let words = ["apple", "banana", "cherry"];
for (let i = 0; i < words.length; i++) {
  console.log(words[i].toUpperCase());
}

// 6. Replace Middle Element
let nums = [1, 2, 3];
nums[1] = 0;
console.log(nums);

// 7. Add and Remove Elements
let arr = ["a", "b"];
arr.push("c");
arr.unshift("z");
arr.pop();
console.log(arr);

// 8. Average of Array
let numbers = [4, 8, 15, 23];
let sum = 0;
for (let i = 0; i < numbers.length; i++) {
  sum += numbers[i];
}
let average = sum / numbers.length;
console.log(average);

// 9. Reverse an Array Manually
let reverseArr = [1, 2, 3];
console.log(reverseArr[2]);
console.log(reverseArr[1]);
console.log(reverseArr[0]);

// 10. Loop with Index
let fruits = ["apple", "banana", "cherry", "date", "fig"];
for (let i = 0; i < fruits.length; i++) {
  console.log("Index " + i + ": " + fruits[i]);
}
