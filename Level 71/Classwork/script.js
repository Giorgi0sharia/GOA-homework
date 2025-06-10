function guessNumber() {
  const number = Math.floor(Math.random() * 100) + 1;
  let guess;
  while (guess !== number) {
    guess = parseInt(prompt("Enter a number between 1 and 100:"));
    if (guess > number) {
      alert("Too high");
    } else if (guess < number) {
      alert("Too low");
    } else {
      alert("Congratulations!");
    }
  }
}
