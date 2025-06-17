// 2. Create a <p> element and add it to the body
const pElement = document.createElement("p");
pElement.textContent = "This is a new paragraph.";
document.body.appendChild(pElement);

// 3. Create an <h1> and append it to a <div>
const h1 = document.createElement("h1");
h1.textContent = "This is a heading";
const divContainer = document.getElementById("divContainer");
divContainer.appendChild(h1);

// 4. Create an <img> and add it to the page
const img = document.createElement("img");
img.src = "https://via.placeholder.com/150";
img.alt = "Placeholder Image";
document.body.appendChild(img);

// 5. Create a <button> and add it to the body
const button = document.createElement("button");
button.textContent = "Click me";
document.body.appendChild(button);

// 6. Create a <ul> with three <li> items
const ul = document.createElement("ul");
["Item 1", "Item 2", "Item 3"].forEach(text => {
    const li = document.createElement("li");
    li.textContent = text;
    ul.appendChild(li);
});
document.body.appendChild(ul);

// 7. Remove the first child of #content
const contentDiv = document.getElementById("content");
if (contentDiv.firstChild) {
    contentDiv.removeChild(contentDiv.firstChild);
}

// 8. Create a <ul> with 3 <li> and remove the last one
const removableList = document.createElement("ul");
["First", "Second", "Third"].forEach(text => {
    const li = document.createElement("li");
    li.textContent = text;
    removableList.appendChild(li);
});
document.body.appendChild(removableList);
if (removableList.lastChild) {
    removableList.removeChild(removableList.lastChild);
}

// 9. Replace a <p> inside #textContainer with a new <p>
const textContainer = document.getElementById("textContainer");
const newP = document.createElement("p");
newP.textContent = "New paragraph replacing old one.";
const oldP = textContainer.querySelector("p");
if (oldP) {
    textContainer.replaceChild(newP, oldP);
}

// 10. Replace a <button> in #buttonContainer with a <span>
const buttonContainer = document.getElementById("buttonContainer");
const oldButton = buttonContainer.querySelector("button");
const span = document.createElement("span");
span.textContent = "Replaced with span";
if (oldButton) {
    buttonContainer.replaceChild(span, oldButton);
}

// 11. Replace <li> in #oneItemList with a new one
const oneItemList = document.getElementById("oneItemList");
const oldLi = oneItemList.querySelector("li");
const newLi = document.createElement("li");
newLi.textContent = "New list item";
if (oldLi) {
    oneItemList.replaceChild(newLi, oldLi);
}

// 12. Replace <h2> with <h1>
const oldH2 = document.getElementById("headingToReplace");
const newH1 = document.createElement("h1");
newH1.textContent = "This is a replaced H1 heading";
if (oldH2 && oldH2.parentNode) {
    oldH2.parentNode.replaceChild(newH1, oldH2);
}
