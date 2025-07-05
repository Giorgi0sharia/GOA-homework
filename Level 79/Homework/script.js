// ✅ Homework 1: Heading Formatter
const h1s = document.querySelectorAll("h1");
const h3s = document.querySelectorAll("h3");

h1s.forEach(h1 => {
  h1.style.color = "green";
  h1.style.border = "1px solid black";
  h1.style.fontSize = "30px";
});
h3s.forEach(h3 => {
  h3.style.color = "green";
  h3.style.border = "1px solid black";
  h3.style.fontSize = "24px";
});

// ✅ Homework 2: Paragraph Word Counter
const paragraphs = document.querySelectorAll("p");
paragraphs.forEach((p, index) => {
  const wordCount = p.textContent.trim().split(/\s+/).length;
  console.log(`Paragraph ${index + 1} has ${wordCount} words`);
});

// ✅ Homework 3: Image Gallery Resize
const images = document.querySelectorAll("img");
images.forEach(img => {
  img.style.width = "200px";
  img.style.borderRadius = "10px";
  if (img.alt.toLowerCase().includes("cat")) {
    img.style.border = "3px solid orange";
  }
});

// ✅ Homework 4: Animate Circles
for (let i = 0; i < 3; i++) {
  const circle = document.createElement("div");
  circle.classList.add("circle");
  document.body.appendChild(circle);

  let pos = 0;
  setInterval(() => {
    pos += 10;
    circle.style.left = pos + "px";
  }, 200);
}

// ✅ Homework 5: List Alternating Color
const listItems = document.querySelectorAll("#colorList li");
listItems.forEach((li, index) => {
  li.style.backgroundColor = index % 2 === 0 ? "skyblue" : "lightgray";
});

// ✅ Homework 6: Interactive Box Movement
const box = document.createElement("div");
box.style.width = "100px";
box.style.height = "100px";
box.style.backgroundColor = "blue";
box.style.position = "relative";
box.style.marginTop = "20px";
document.body.appendChild(box);

const button = document.createElement("button");
button.textContent = "Move Box";
document.body.appendChild(button);

let moveX = 0;
button.addEventListener("click", () => {
  moveX += 20;
  box.style.left = moveX + "px";
  box.style.backgroundColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
});

// ✅ Homework 7: Form Input Length Warning
const textInputs = document.querySelectorAll('input[type="text"]');
textInputs.forEach(input => {
  input.addEventListener("input", () => {
    input.style.backgroundColor = input.value.length > 20 ? "red" : "white";
  });
});

// ✅ Homework 8: Dynamic Message List
const ul = document.createElement("ul");
document.body.appendChild(ul);

let msgCount = 0;
const msgInterval = setInterval(() => {
  msgCount++;
  const li = document.createElement("li");
  li.textContent = `Message ${msgCount}`;
  ul.appendChild(li);
  if (msgCount >= 10) clearInterval(msgInterval);
}, 2000);

// ✅ Homework 9: Hide and Reveal
const hideBtn = document.getElementById("hideBtn");
const hideBox = document.getElementById("hideBox");

hideBtn.addEventListener("click", () => {
  hideBox.style.display = "none";
  setTimeout(() => {
    hideBox.style.display = "block";
  }, 5000);
});

// ✅ Homework 10: Element Counter by Tag
setTimeout(() => {
  const tag = prompt("Enter a tag name to count (e.g., div, p, img):");
  if (tag) {
    const elements = document.getElementsByTagName(tag);
    alert(`There are ${elements.length} <${tag}> elements on the page.`);
  }
}, 1000);
