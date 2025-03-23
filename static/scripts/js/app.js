

const containerEl = document.querySelector('.text-container');

const careers = ["Full Stack Web Developer", "Mobile App Developer", "Freelancer", "Instructor"];

let careersIndex = 0;

let characterIndex = 0;

updateText();

function updateText() {
    characterIndex++;
    containerEl.innerHTML = `
      <h2>I am ${careers[careersIndex].slice(0, 1) === "I" ? "an" : "a"} ${careers[careersIndex].slice(0, characterIndex)}</h2>
    `;

    if(characterIndex === careers[careersIndex].length) {
        careersIndex++;
        characterIndex = 0;
    }

    if(careersIndex === careers.length) {
        careersIndex = 0;
    }
    setTimeout(updateText, 400);
}