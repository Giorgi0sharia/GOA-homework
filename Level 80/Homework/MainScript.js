window.onload = function () {
  console.log("GameReview საიტი ჩაიტვირთა!");

  const reviews = document.querySelectorAll(".review");

  reviews.forEach(section => {
    section.addEventListener("click", () => {
      const url = section.getAttribute("data-link");
      if (url) {
        window.open(url, "_blank");
      }
    });
  });
};
