let total = 0;

do {
  let input = prompt("შეიყვანეთ რიცხვი:");
  let num = Number(input);
  if (!isNaN(num)) {
    total += num;
  }
} while (total <= 100);

alert("ჯამი გახდა: " + total);
