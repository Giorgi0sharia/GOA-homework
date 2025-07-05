// script.js

let allParagraphs = document.querySelectorAll("p");
let texts = [];
for (let i = 0; i < allParagraphs.length; i++) {
  texts.push(allParagraphs[i].textContent);
}
console.log(texts);

let box1 = document.getElementById("box1");

let box2 = document.getElementById("box2");
const innerParagraphs = box2.getElementsByTagName("p");
for (let i = 0; i < innerParagraphs.length; i++) {
  innerParagraphs[i].style.color = "green";
  innerParagraphs[i].style.backgroundColor = "black";
}

let box3 = document.getElementById("box3");
for (let i = 1; i <= 5; i++) {
  let p = document.createElement("p");
  p.textContent = "პარაგრაფი ნომერი " + i;
  box3.appendChild(p);
}
