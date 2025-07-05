// პოპულარული თამაშების სია
const popularGames = [
  {
    title: "Elden Ring",
    desc: "შთამბეჭდავი მოქმედებითი RPG FromSoftware-ისგან.",
    img: "image1.jpg",
    link: "https://en.bandainamcoent.eu/elden-ring/elden-ring"
  },
  {
    title: "Fortnite",
    desc: "ბატლ როიალის ფენომენი მუდმივი განახლებებით.",
    img: "image2.jpg",
    link: "https://www.fortnite.com/"
  },
  {
    title: "Valorant",
    desc: "ტაქტიკური 5v5 შუთერი Riot Games-ისგან.",
    img: "image3.jpg",
    link: "https://playvalorant.com/"
  },
  {
    title: "Minecraft",
    desc: "კრეატიული სანდბოქსი, რომელსაც ყველა თაობა აღმერთებს.",
    img: "image4.jpg",
    link: "https://www.minecraft.net/"
  },
  {
    title: "GTA V",
    desc: "Rockstar-ის კრიმინალური ეპოპეა ონლაინ რეჟიმით.",
    img: "image5.jpg",
    link: "https://www.rockstargames.com/gta-v"
  },
  {
    title: "League of Legends",
    desc: "კლასიკური MOBA, რომელსაც მილიონობით მოთამაშე ჰყავს.",
    img: "image6.jpg",
    link: "https://www.leagueoflegends.com/"
  },
  {
    title: "Apex Legends",
    desc: "გმირებზე დაფუძნებული სწრაფი Battle Royale.",
    img: "image7.jpg",
    link: "https://www.ea.com/games/apex-legends"
  },
  {
    title: "Call of Duty: Warzone",
    desc: "უფასო შუთერი CoD-ის სერიიდან.",
    img: "image8.jpg",
    link: "https://www.callofduty.com/warzone"
  },
  {
    title: "The Witcher 3",
    desc: "მრავალი ჯილდოს მფლობელი სათავგადასავლო RPG.",
    img: "image9.jpg",
    link: "https://thewitcher.com/en/witcher3"
  },
  {
    title: "Roblox",
    desc: "პლატფორმა მილიონობით მომხმარებლის მიერ შექმნილი თამაშებით.",
    img: "image10.jpg",
    link: "https://www.roblox.com/"
  }
];

// პერსპექტიული თამაშების სია
const promisingGames = [
  {
    title: "Starfield",
    desc: "მომავალი კოსმოსური RPG Bethesda-სგან.",
    img: "image11.jpg",
    link: "https://bethesda.net/en/game/starfield"
  },
  {
    title: "Avowed",
    desc: "ფანტასტიკური RPG Obsidian-ისგან.",
    img: "image12.jpg",
    link: "https://www.obsidian.net/games/avowed"
  },
  {
    title: "Fable (Reboot)",
    desc: "ლეგენდარული RPG ბრუნდება Xbox-ზე.",
    img: "image13.jpg",
    link: "https://www.xbox.com/en-US/games/fable"
  },
  {
    title: "Hades II",
    desc: "დამატება ცნობილი rogue-like თამაშის სერიაში.",
    img: "image14.jpg",
    link: "https://www.supergiantgames.com/games/hades-ii/"
  },
  {
    title: "Black Myth: Wukong",
    desc: "ჩინური მითოლოგიით შთაგონებული მოქმედებითი RPG.",
    img: "image15.jpg",
    link: "https://www.heishenhua.com/"
  },
  {
    title: "The Last of Us Part III",
    desc: "ემოციური ისტორიის ახალი თავი.",
    img: "image16.jpg",
    link: "https://www.naughtydog.com/"
  },
  {
    title: "Perfect Dark (Reboot)",
    desc: "სამეცნიერო ფანტასტიკის სტელს-აქშენის განახლება.",
    img: "image17.jpg",
    link: "https://www.xbox.com/en-US/games/perfect-dark"
  },
  {
    title: "Dragon Age: Dreadwolf",
    desc: "BioWare-ის ახალი ეპიკური თავგადასავალი.",
    img: "image18.jpg",
    link: "https://www.ea.com/games/dragon-age"
  },
  {
    title: "Metroid Prime 4",
    desc: "Nintendo-ს მიერ ნანატრი shooter თამაში.",
    img: "image19.jpg",
    link: "https://www.nintendo.com/"
  },
  {
    title: "S.T.A.L.K.E.R. 2",
    desc: "სასიცოცხლო საშიში ჰორორი გამორიცხულ ზონაში.",
    img: "image20.jpg",
    link: "https://www.stalker2.com/"
  }
];

// HTML-ში თამაშების გამოტანა
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
        <a href="${game.link}" target="_blank" rel="noopener noreferrer">გადადი საიტზე</a>
      </div>
    `;
    container.appendChild(card);
  });
}

// ღამის რეჟიმის გადართვა
function toggleMode() {
  document.body.classList.toggle("dark-mode");
  const btn = document.getElementById("toggleBtn");
  btn.textContent = document.body.classList.contains("dark-mode") ? "დღის რეჟიმი" : "ღამის რეჟიმი";
}

// თამაშების გამოტანა
renderGames(popularGames, "popular-games");
renderGames(promisingGames, "promising-games");

document.getElementById("toggleBtn").addEventListener("click", toggleMode);



