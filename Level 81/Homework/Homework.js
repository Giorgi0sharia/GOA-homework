// 4. Print numbers from 1 to 5
let i = 1;
do {
  console.log(i);
  i++;
} while (i <= 5);

// 5. Print even numbers from 2 to 10
let j = 2;
do {
  if (j % 2 === 0) {
    console.log(j);
  }
  j++;
} while (j <= 10);

// 6. Print numbers from 10 down to 1
let k = 10;
do {
  console.log(k);
  k--;
} while (k >= 1);

// 7. Ask user for a number until > 100
let number;
do {
  number = prompt("Enter a number greater than 100:");
} while (Number(number) <= 100);

// 8. Sum numbers from 1 to 10
let total = 0;
let n = 1;
do {
  total += n;
  n++;
} while (n <= 10);
console.log("Total sum from 1 to 10:", total);

// 9. Print each element of an array
let numbers = [10, 20, 30, 40, 50];
for (let num of numbers) {
  console.log(num);
}

// 10. Print each character of a string
let str = "hello";
for (let char of str) {
  console.log(char);
}

// 11. Sum all numbers in array
let sum = 0;
for (let num of numbers) {
  sum += num;
}
console.log("Sum of numbers:", sum);

// 12. Print even numbers only
for (let num of numbers) {
  if (num % 2 === 0) {
    console.log("Even:", num);
  }
}

// 13. Print all names from an array
let names = ["Anna", "Gio", "Luka", "Nino"];
for (let name of names) {
  console.log(name);
}

let person = {
  name: "Gio",
  age: 25,
  city: "Tbilisi"
};

// 14. Print all property names
for (let key in person) {
  console.log("Key:", key);
}

// 15. Print all property values
for (let key in person) {
  console.log("Value:", person[key]);
}

// 16. Count number of properties
let count = 0;
for (let key in person) {
  count++;
}
console.log("Property count:", count);

// 17. Check if a specific key exists
let keyToCheck = "age";
let found = false;
for (let key in person) {
  if (key === keyToCheck) {
    found = true;
    break;
  }
}
console.log("Key exists:", found);

// 18. Create a string listing all keys
let keyList = "";
for (let key in person) {
  keyList += key + ", ";
}
keyList = keyList.slice(0, -2); // Remove last comma and space
console.log("Keys:", keyList);
