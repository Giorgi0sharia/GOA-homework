let person = {
  name: "gio",
  surname: "sharia",
  academy: "goa",
  city: "tbilisi",
  role: "Student",
  favColor: "purple",
  isActive: true,

  fullName() {
    console.log(this.name + " " + this.surname);
  },

  showFavColor() {
    console.log(this.favColor);
  }
};

console.log(person);
console.log(person.city);
person.fullName();
person.favColor = "red";
console.log(person.favColor);


function userOperations() {
  var a = confirm("აიჩიეთ");
  var b = confirm("აიჩიეთ");

  console.log("და (AND): " + (a && b));
  console.log("ან (OR): " + (a || b));
}