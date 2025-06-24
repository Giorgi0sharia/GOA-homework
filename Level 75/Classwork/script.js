
function printName() {
  console.log("გიო შარია");
}


const intervalId = setInterval(printName, 10000);

document.getElementById("stopButton").addEventListener("click", function () {
  clearInterval(intervalId);
  console.log("ინტერვალი გაჩერდა");
});






const mixedArray = [
  "მოგესალმებით",       
  42,                   
  true,                 
  { name: "გიო", age: 20 }, 
  [1, 2, 3]             
];

console.log(mixedArray);
