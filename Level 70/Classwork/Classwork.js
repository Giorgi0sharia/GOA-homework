function userLoop() {
  let start = Number(prompt("შეიყვანეთ პირველი რიცხვი:"));
  let end = Number(prompt("შეიყვანეთ მეორე რიცხვი:"));

  if (isNaN(start) || isNaN(end)) {
    console.log("გთხოვთ, შეიყვანეთ სწორი რიცხვები.");
    return;
  }

  console.log(`რიცხვები ${start}-დან ${end}-მდე:`);

  for (let i = start; i <= end; i++) {
    console.log(i);
  }
}


window.onload = userLoop;
