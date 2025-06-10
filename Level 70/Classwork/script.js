function changeElements() {
  // 1) Input-ის value ამოღება და კონსოლში გამოტანა
  const input = document.getElementById("myInput");
  console.log("Input value:", input.value);

  // 2) ღილაკის ფონის ფერი - შავი, ტექსტი - თეთრი
  const button = document.getElementById("myButton");
  button.style.backgroundColor = "black";
  button.style.color = "white";

  // 3) სათაურის ტექსტის ცენტრში განლაგება
  const heading = document.getElementById("myHeading");
  heading.style.textAlign = "center";

  // 4) მთლიანი body-ის ფონის ფერი - მწვანე
  document.body.style.backgroundColor = "green";
}
