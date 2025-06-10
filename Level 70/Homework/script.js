for (let i = 1; i <= 10; i++) {
  console.log(i);
}

let i = 2;
while (i <= 20) {
  if (i % 2 === 0) console.log(i);
  i++;
}

for (let i = 10; i >= 1; i--) {
  console.log(i);
}

let count = 1;
while (count <= 5) {
  console.log(count * 3);
  count++;
}

let str = "Hello";
for (let i = 0; i < str.length; i++) {
  console.log(str[i]);
}

document.getElementById("btn1").onclick = function () {
  document.getElementById("para").textContent = "Text changed";
};

document.getElementById("btn2").onclick = function () {
  document.getElementById("box").style.backgroundColor = "lightblue";
};

document.getElementById("btn3").onclick = function () {
  document.getElementById("heading").style.fontSize = "36px";
};

document.getElementById("btn4").onclick = function () {
  document.getElementById("hideDiv").style.display = "none";
};

document.getElementById("btn5").onclick = function () {
  alert("Custom message shown");
};
