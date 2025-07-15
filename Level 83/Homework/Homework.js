// 🔷 Homework 2: Filter Positive Numbers from Array
const filterPositives = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) continue;
    console.log(arr[i]);
  }
};
filterPositives([-3, 5, -1, 8, 0, -6, 7]);

// 🔷 Homework 3: Find First Word With More Than 5 Letters
const findLongWord = (words) => {
  for (let i = 0; i < words.length; i++) {
    if (words[i].length > 5) {
      console.log(words[i]);
      break;
    }
  }
};
findLongWord(["cat", "book", "umbrella", "sun", "sky"]);

// 🔷 Homework 4: Sum Numbers Until a Negative Is Found
const sumUntilNegative = (arr) => {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) break;
    sum += arr[i];
  }
  console.log("Sum before negative:", sum);
};
sumUntilNegative([5, 3, 8, 10, -4, 7]);

// 🔷 Homework 5: Show Numbers Except Multiples of 3
const printExceptMultiplesOf3 = () => {
  for (let i = 1; i <= 20; i++) {
    if (i % 3 === 0) continue;
    console.log(i);
  }
};
printExceptMultiplesOf3();

// 🔶 Homework 6: Count How Many Words Start with "A"
const countWordsWithA = (words) => {
  let count = 0;
  for (let i = 0; i < words.length; i++) {
    if (words[i].length < 1) continue;
    if (words[i][0] === "A" || words[i][0] === "a") {
      count++;
    }
  }
  console.log("Words starting with A/a:", count);
};
countWordsWithA(["Apple", "banana", "avocado", "Air", "boat", "", "Alaska"]);

// 🔶 Homework 7: Print Numbers 1–30 Except Multiples of 4 and 6
const skipMultiplesOf4and6 = () => {
  for (let i = 1; i <= 30; i++) {
    if (i % 4 === 0 || i % 6 === 0) continue;
    console.log(i);
  }
};
skipMultiplesOf4and6();

// 🔶 Homework 8: Find First Name Longer Than 8 Characters
const findLongName = (names) => {
  for (let i = 0; i < names.length; i++) {
    if (names[i].length > 8) {
      console.log("Found:", names[i]);
      break;
    }
  }
};
findLongName(["Tom", "Elizabeth", "Charlotte", "Sam", "Benjamin"]);

// 🔶 Homework 9: Print Only Odd Numbers From an Array
const printOddNumbers = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0) continue;
    console.log(arr[i]);
  }
};
printOddNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9]);

// 🔶 Homework 10: Sum Only Positive Even Numbers From an Array
const sumPositiveEvens = (arr) => {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] <= 0 || arr[i] % 2 !== 0) continue;
    sum += arr[i];
  }
  console.log("Sum of positive even numbers:", sum);
};
sumPositiveEvens([-2, 4, 7, 8, -5, 10, 0]);
