
const paragraphs = document.querySelectorAll("p");

const textArray = [];
for (let i = 0; i < paragraphs.length; i++) {
  textArray.push(paragraphs[i].textContent);
}

console.log(textArray);
