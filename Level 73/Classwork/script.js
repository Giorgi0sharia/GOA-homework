function addNewElement() {
    const div = document.getElementById("extraDiv");
    const newButton = document.createElement("button");
    newButton.textContent = "ახალი ღილაკი";
    div.appendChild(newButton);
}

function modifyContent() {
    const contentDiv = document.getElementById("contentDiv");
    const button = contentDiv.querySelector("button");
    const paragraph = contentDiv.querySelector("p");
    contentDiv.removeChild(button);
    const italic = document.createElement("i");
    italic.textContent = "პარაგრაფი შეიცვალა i თეგით";
    contentDiv.replaceChild(italic, paragraph);
}

window.onload = function () {
    modifyContent();
    addNewElement();
};
