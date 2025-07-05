// 2) Select all <p> tags and display total number in alert
const allParagraphs = document.querySelectorAll("p");
alert("Total <p> tags: " + allParagraphs.length);

// 3) Change all <h2> text color to blue
const allH2s = document.querySelectorAll("h2");
for (let i = 0; i < allH2s.length; i++) {
  allH2s[i].style.color = "blue";
}

// 4) Log text content of all <li> elements
const allLIs = document.querySelectorAll("li");
for (let i = 0; i < allLIs.length; i++) {
  console.log(allLIs[i].textContent);
}

// 5) Set background color of all <div> to lightgray
const allDivs = document.querySelectorAll("div");
for (let i = 0; i < allDivs.length; i++) {
  allDivs[i].style.backgroundColor = "lightgray";
}

// 6) Change first <img> src
const firstImg = document.querySelector("img");
if (firstImg) {
  firstImg.src = "https://via.placeholder.com/150";
}

// 7) Change background color of elements with class highlight
const highlights = document.querySelectorAll(".highlight");
for (let i = 0; i < highlights.length; i++) {
  highlights[i].style.backgroundColor = "yellow";
}

// 8) Count elements with class card and display in console
const cards = document.querySelectorAll(".card");
console.log("Total .card elements: " + cards.length);

// 9) Change text color of elements with class error to red
const errors = document.querySelectorAll(".error");
for (let i = 0; i < errors.length; i++) {
  errors[i].style.color = "red";
}

// 10) Log innerHTML of all elements with class item
const items = document.querySelectorAll(".item");
for (let i = 0; i < items.length; i++) {
  console.log(items[i].innerHTML);
}

// 11) Change text of first .button to "Clicked!"
const firstButton = document.querySelector(".button");
if (firstButton) {
  firstButton.textContent = "Clicked!";
}

// 12) Move a <div> element 5px to the right every 100ms
const movingDiv = document.querySelector("#movingDiv");
if (movingDiv) {
  movingDiv.style.position = "absolute";
  let pos = 0;
  setInterval(() => {
    pos += 5;
    movingDiv.style.left = pos + "px";
  }, 100);
}
