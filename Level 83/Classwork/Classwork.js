const numbers = [5, 8, 12, 7, 15, 4, 10, 3];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
  sum += numbers[i];

  if (sum > 50) {
    console.log("შეკრება შეწყდა — ჯამი გადააჭარბა 50-ს");
    break;
  }
}

console.log("საბოლოო ჯამი:", sum);