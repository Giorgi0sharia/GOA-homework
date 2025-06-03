// 2. Check if two numbers are equal
let num1 = 5;
let num2 = 5;
console.log("2. Are num1 and num2 equal (==)?", num1 == num2);

// 3. Check if one number is greater than another
let a = 10;
let b = 7;
console.log("3. Is a > b?", a > b);

// 7. Show confirm box immediately and log result
const confirmResult = confirm("7. Do you want to proceed?");
console.log("7. Confirm result:", confirmResult);

// 9. Show confirm box on page load and alert result
window.onload = function () {
  const confirmOnLoad = confirm("9. Do you agree with the terms?");
  alert("9. Page load confirm: " + confirmOnLoad);
};

// 10. Log username input value on form submit
document.getElementById('userForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const username = e.target.elements['username'].value;
  console.log("10. Submitted username:", username);
});

// 11. Clear email input on button click
function clearEmail() {
  document.getElementById('emailInput').value = "";
}

// 12. Alert phone input value on button click
function showPhone() {
  const phone = document.getElementById('phoneInput').value;
  alert("12. Phone number is: " + phone);
}

// 13. Check if number is <= another
let x = 30;
let y = 50;
console.log("13. Is x <= y?", x <= y);

// 14. Check if two numbers are not equal
let p = 9;
let q = 4;
console.log("14. Are p and q not equal (!=)?", p != q);

// 15. Check if number is >= 100
let bigNum = 150;
console.log("15. Is bigNum >= 100?", bigNum >= 100);
