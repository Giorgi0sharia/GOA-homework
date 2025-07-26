function printEvenNumbers(a, b, c, d, e, f, g, h, i, j) {
  const args = [a, b, c, d, e, f, g, h, i, j];
  for (const num of args) {
    if (num % 2 === 0) {
      console.log(num);
    }
  }
}

printEvenNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);






const sayHello1 = function() {
  console.log("hello");
};

const sayHello2 = () => {
  console.log("hello");
};


console.log(
  (function() {
    return "aaa";
  })()
);
