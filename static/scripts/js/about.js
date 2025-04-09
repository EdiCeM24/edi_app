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



//SWIPER SECTION
const swiper = new Swiper('.swiper', {
   // Optional parameters
   direction: 'vertical',
   loop: true,
   
   slidesPerView: 1,
   spaceBetween: 10,
  // using "ratio" endpoints
   breakpoints: {
      '@0.75': {
         slidesPerView: 2,
         spaceBetween: 20,
      },
      '@1.00': {
         slidesPerView: 3,
         spaceBetween: 40,
      },
      '@1.50': {
         slidesPerView: 4,
         spaceBetween: 50,
      },
   },

   // If we need pagination
   pagination: {
      el: '.swiper-pagination',
   },

   // Navigation arrows
   navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
   },
});       



// TOGGLE FAQs SECTION
let a = document.querySelector('.faq-icon');
const dem = () => {
  a.addEventListener('click', () => {
    a.classList.toggle('open');
  })
}


