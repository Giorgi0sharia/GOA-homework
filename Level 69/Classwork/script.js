// 11) Remove vowels from a string

function disemvowel(str) {
  return str.replace(/[aeiou]/gi, '');
}

// 12) Square Every Digit

function squareDigits(num) {
  return Number(String(num).split('').map(n => n * n).join(''));
}

// 13) Is the number even?

function isEven(n) {
  return n % 2 === 0;
}

// 14) Filter list of non-negative integers

function filter_list(l) {
  return l.filter(item => typeof item === 'number');
}

// 15) Descending Order

function descendingOrder(n) {
  return Number(String(n).split('').sort((a, b) => b - a).join(''));
}
