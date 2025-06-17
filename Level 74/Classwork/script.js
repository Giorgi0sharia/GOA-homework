const paragraph = document.getElementById("hoverParagraph");

paragraph.onmouseover = centerText;

function centerText() {
    paragraph.style.textAlign = "center";
}


const button = document.getElementById("darkModeBtn");

button.addEventListener("click", function(event) {
    console.log(event); 
    document.body.style.backgroundColor = "black";
    document.body.style.color = "white";
});

const link = document.getElementById("myLink");

link.addEventListener("pointerover", function(e) {
    const attributes = e.target.attributes;

    for (let attr of attributes) {
        console.log(`${attr.name}: ${attr.value}`);
    }

    console.log("Target element:", e.target);
});
