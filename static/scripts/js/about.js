/** ABOUT PAGE **/
const containers = document.querySelector('.text-slider');
   
    const skills = ["Full Stack Web Developer", "Mobile App Developer", "Freelancer", "Instructor"];
   
    let skillsIndex = 0;
   
    let charactersIndex = 0;
   
    updateTexts();
   
    function updateTexts() {
         charactersIndex++;
         containers.innerHTML = `
            <h2>I am ${skills[skillsIndex].slice(0, 1) === "I" ? "an" : "a"} ${skills[skillsIndex].slice(0, charactersIndex)}</h2>
         `;
   
         if(charactersIndex === skills[skillsIndex].length) {
            skillsIndex++;
            charactersIndex = 0;
         }
   
         if(skillsIndex === skills.length) {
            skillsIndex = 0;
         }
         setTimeout(updateTexts, 400);
    }





