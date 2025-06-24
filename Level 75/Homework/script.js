
// 1. Counter from 1 to 5 every second
let count = 1;
const counterInterval = setInterval(() => {
  console.log(count);
  count++;
  if (count > 5) {
    clearInterval(counterInterval);
  }
}, 1000);

// 2. Message every 2 seconds, stop after 10 seconds
const messageInterval = setInterval(() => {
  console.log("This message shows every 2 seconds");
}, 2000);

setTimeout(() => {
  clearInterval(messageInterval);
}, 10000);

// 3. Change background color every 3 seconds, stop after 5 changes
let colorChangeCount = 0;
const colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightgray'];
const bgInterval = setInterval(() => {
  document.body.style.backgroundColor = colors[colorChangeCount % colors.length];
  colorChangeCount++;
  if (colorChangeCount === 5) {
    clearInterval(bgInterval);
  }
}, 3000);

// 4. Display current time in console every second, stop after 15 seconds
const timeInterval = setInterval(() => {
  const now = new Date();
  console.log(now.toLocaleTimeString());
}, 1000);

setTimeout(() => {
  clearInterval(timeInterval);
}, 15000);

// 5. Simple timer that counts up to 10 seconds
let timerCount = 0;
const timerInterval = setInterval(() => {
  timerCount++;
  console.log(`Timer: ${timerCount}s`);
  if (timerCount === 10) {
    clearInterval(timerInterval);
  }
}, 1000);



// 7. Array of 4 numbers, log second element
const nums = [10, 20, 30, 40];
console.log("Second element:", nums[1]);

// 8. Change first element to 100 and log array
nums[0] = 100;
console.log("Updated array:", nums);

// 9. Array of 3 strings, log each using indexing
const fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);

// 10. Array of 5 numbers, sum of first and last
const values = [5, 10, 15, 20, 25];
const sum = values[0] + values[values.length - 1];
console.log("Sum of first and last:", sum);
