// 2) Prompt for hobby
function favoriteHobby() {
    const hobby = prompt("What's your favorite hobby?");
    if (hobby) alert("Your favorite hobby is: " + hobby);
}

// 3) Prompt for first and last name
function showFullName() {
    const first = prompt("Enter your first name:");
    const last = prompt("Enter your last name:");
    if (first && last) alert("Your full name is: " + first + " " + last);
}

// 4) Prompt for message and update paragraph
function enterMessage() {
    const msg = prompt("Enter a message:");
    if (msg) {
        document.getElementById("messagePara").textContent = msg;
    }
}

// 5) Prompt for favorite emoji
function favoriteEmoji() {
    const emoji = prompt("What's your favorite emoji?");
    if (emoji) alert("Thanks! Your favorite emoji is " + emoji + " 😊");
}

// 6) Prompt to set document title
function setPageTitle() {
    const word = prompt("Enter a word to set as the page title:");
    if (word) document.title = word;
}

// 7) Show alert with input value
function showInputValue(event) {
    event.preventDefault(); // Prevent form from reloading page
    const inputValue = document.getElementById("inputText").value;
    alert("You entered: " + inputValue);
}

// 8) Change background color
function changeBackgroundColor(event) {
    event.preventDefault();
    const color = document.getElementById("colorPicker").value;
    document.body.style.backgroundColor = color;
}

// 9) Display full name in <h1>
function displayFullNameInH1(event) {
    event.preventDefault();
    const first = document.getElementById("firstName").value;
    const last = document.getElementById("lastName").value;
    document.getElementById("fullNameDisplay").textContent = first + " " + last;
}
