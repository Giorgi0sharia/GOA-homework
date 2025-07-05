// ამოცანა 1: 5 დივის შექმნა და მარჯვნივ წაყვანა
const container = document.getElementById("container");
for (let i = 0; i < 5; i++) {
  const div = document.createElement("div");
  div.classList.add("move-box");
  container.appendChild(div);
}
document.getElementById("moveTrigger").addEventListener("click", () => {
  const boxes = document.querySelectorAll(".move-box");
  boxes.forEach((box, index) => {
    let pos = 0;
    const interval = setInterval(() => {
      pos += 5;
      box.style.left = pos + "px";
      if (pos >= 200) clearInterval(interval);
    }, 100);
  });
});

// ამოცანა 2: ღილაკზე დაჭერით ფერის შეცვლა და 10px მარჯვნივ წაყვანა ყოველი დაჭერით
const clickBox = document.getElementById("clickBox");
let clickCount = 0;
document.getElementById("clickBtn").addEventListener("click", () => {
  clickCount++;
  clickBox.style.backgroundColor = "red";
  let left = parseInt(clickBox.style.left) || 0;
  clickBox.style.left = (left + 10) + "px";
  setTimeout(() => {
    clickBox.style.backgroundColor = "gray";
  }, 10000);
});

// ამოცანა 3: ფერის და ზომის შეცვლა + p თეგების დამატება + ზომის შემცირება და გაქრობა
const resizeBtn = document.getElementById("resizeBtn");
const resizeBox = document.getElementById("resizeBox");

resizeBtn.addEventListener("click", () => {
  resizeBox.style.backgroundColor = "purple";
  resizeBox.style.width = "200px";
  resizeBox.style.height = "200px";

  let pCount = 0;
  const pInterval = setInterval(() => {
    pCount++;
    const p = document.createElement("p");
    const text = document.createTextNode("p" + pCount);
    p.appendChild(text);
    resizeBox.appendChild(p);
    if (pCount >= 5) clearInterval(pInterval);
  }, 3000);

  let size = 200;
  const shrink = setInterval(() => {
    size -= 10;
    resizeBox.style.width = size + "px";
    resizeBox.style.height = size + "px";
    if (size <= 0) {
      resizeBox.style.display = "none";
      clearInterval(shrink);
    }
  }, 1000);
});
