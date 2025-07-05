// თამაშების სია - რომლებსაც პოპულარობა შეუმცირდა
const declinedGames = [
  {
    title: "Among Us",
    desc: "ერთ დროს ვირუსული ჰიტი, მაგრამ მოთამაშეების რაოდენობა შემცირდა თამაშის ერთფეროვნების გამო.",
    img: "image21.jpg",
    link: "https://www.innersloth.com/games/among-us/"
  },
  {
    title: "Fall Guys",
    desc: "მხიარული Battle Royale, რომელმაც სწრაფად მოიპოვა პოპულარობა და შემდეგ დაკარგა მრავალფეროვნების ნაკლებობის გამო.",
    img: "image22.jpg",
    link: "https://fallguys.com/"
  },
  {
    title: "PUBG",
    desc: "პირველი პოპულარული Battle Royale, მაგრამ ტექნიკური პრობლემები და ძლიერი კონკურენცია იმოქმედა მის პოპულარობაზე.",
    img: "image23.jpg",
    link: "https://www.pubg.com/"
  },
  {
    title: "Overwatch",
    desc: "Blizzard-ის შუთერი, რომელმაც დაკარგა აქტიური მოთამაშეების ნაწილი თამაშის მენეჯმენტის და კონკურენციის გამო.",
    img: "image24.jpg",
    link: "https://playoverwatch.com/"
  },
  {
    title: "Cyberpunk 2077",
    desc: "გადაჭარბებული მოლოდინები და ტექნიკური ხარვეზები გამოშვებისას გახდა მიზეზი პოპულარობის კლებისა.",
    img: "image25.jpg",
    link: "https://www.cyberpunk.net/"
  },
  {
    title: "Pokemon GO",
    desc: "მობილური ვირუსული ფენომენი, რომელმაც ინტერესი დროთა განმავლობაში დაკარგა.",
    img: "image26.jpg",
    link: "https://pokemongolive.com/"
  },
  {
    title: "Clash Royale",
    desc: "სტრატეგიული თამაში, რომელიც იყო ძალიან პოპულარული, მაგრამ მოთამაშეთა ნაწილი გადავიდა სხვა თამაშებზე.",
    img: "image27.jpg",
    link: "https://supercell.com/en/games/clashroyale/"
  },
  {
    title: "Temple Run",
    desc: "ერთ დროს მობილური ჰიტი, რომელიც კლასიკად იქცა, მაგრამ აღარ არის აქტუალური.",
    img: "image28.jpg",
    link: "https://www.imangistudios.com/"
  },
  {
    title: "Subway Surfers",
    desc: "მხიარული რბოლის თამაში, რომელიც ბევრისთვის ბავშვობის ნოსტალგიაა, თუმცა აქტიურობა შემცირდა.",
    img: "image29.jpg",
    link: "https://sybo.com/games/subway-surfers/"
  },
  {
    title: "Angry Birds",
    desc: "ლეგენდარული ფრენჩაიზი, რომელიც დროთა განმავლობაში დაივიწყეს ახალმა თაობებმა.",
    img: "image30.jpg",
    link: "https://www.rovio.com/games/angry-birds/"
  }
];

// HTML-ში ჩასმა ბარათების
function renderGames(games, containerId) {
  const container = document.getElementById(containerId);
  container.innerHTML = "";
  games.forEach(game => {
    const card = document.createElement("div");
    card.className = "game-card";
    card.innerHTML = `
      <img src="${game.img}" alt="${game.title}" />
      <div class="game-info">
        <h3>${game.title}</h3>
        <p>${game.desc}</p>
        <a href="${game.link}" target="_blank" rel="noopener noreferrer">იხილე საიტი</a>
      </div>
    `;
    container.appendChild(card);
  });
}

// ღამის რეჟიმის გადართვა
function toggleMode() {
  document.body.classList.toggle("dark-mode");
  const btn = document.getElementById("toggleBtn");
  btn.textContent = document.body.classList.contains("dark-mode") ? " დღის რეჟიმი" : " ღამის რეჟიმი";
}

// ინიციალიზაცია
renderGames(declinedGames, "declined-games");
document.getElementById("toggleBtn").addEventListener("click", toggleMode);
