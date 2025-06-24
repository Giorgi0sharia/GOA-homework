

// 1. Click Alert
document.getElementById('alertBtn').addEventListener('click', function () {
  alert('Button was clicked!');
});

// 2. Change Text on Hover
hoverPara.addEventListener('mouseover', function () {
  hoverPara.textContent = 'You hovered over me!';
});
hoverPara.addEventListener('mouseout', function () {
  hoverPara.textContent = 'Hover over me';
});

// 3. Toggle Background Color
let isBlue = true;
toggleDiv.addEventListener('click', function () {
  toggleDiv.style.backgroundColor = isBlue ? 'lightcoral' : 'lightblue';
  isBlue = !isBlue;
});

// 4. Log Input Value on Click
document.getElementById('textInput').addEventListener('click', function (e) {
  console.log(e.target.value);
});

// 5. Show/Hide Image on Button Click
document.getElementById('toggleImgBtn').addEventListener('click', function () {
  myImage.style.display = myImage.style.display === 'none' ? 'block' : 'none';
});
