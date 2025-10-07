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
      
         // document.addEventListener("DOMContentLoaded", function () {   
         //    const swiper = new Swiper('.swiper', {
         //       // Optional parameters
         //       direction: 'vertical',
         //       loop: true,
               
         //       slidesPerView: 1,
         //       spaceBetween: 10,
         //       // using "ratio" endpoints
         //       breakpoints: {
         //          '@600': {   // @0.75
         //          slidesPerView: 1,
         //          spaceBetween: 10,
         //          },
         //          '@980': {   //@1.00
         //             slidesPerView: 2,
         //             spaceBetween: 20,
         //          },
         //          '@1024': {   // @1.50
         //             slidesPerView: 3,
         //             spaceBetween: 30,
         //          },
         //          '@1440': {   // @1.50
         //             slidesPerView: 4,
         //             spaceBetween: 30,
         //          },
         //       },

         //       // If we need pagination
         //       pagination: {
         //          el: '.swiper-pagination',
         //          clickable: false,
         //       },

         //       // Navigation arrows
         //       navigation: {
         //          nextEl: '.swiper-button-next',
         //          prevEl: '.swiper-button-prev',
         //       },
         //       effect: "fade",
         //       fadeEffect: {
         //       crossFade: true,
         //       },
         //    }); 
         // }); 
      


// TOGGLE FAQs SECTION
let faq = document.querySelector('.faq-icon i ');
const dem = () => {
  faq.addEventListener('click', () => {
    faq.classList.toggle('open');
  })
};


// Count onscroll
const statElements = document.querySelectorAll('.stats-item');

// Set the target count value
const targetCounts = {
   'text-count': 105,
   'text-Id': 76,
   // 'textIdCount': 24/7,
   'text-count-id': 10,

};

// Set the animation duration
const animationDuration = 2000;

// Function to animate the count
function animateCount(element, targetCount) {
   let startTime = null;
   let currentCount = 0;

   function step(timestamp) {
      if (!startTime) startTime = timestamp;
      const progress = timestamp - startTime;
      const percentage = Math.min(progress / animationDuration, 1);
      currentCount = Math.floor(targetCount * percentage);
      element.innerText = currentCount;
      if(progress < animationDuration) {
         window.requestAnimationFrame(step);
      } else {
         countElement.innerText = targetCount;
      }
   }

   window.requestAnimationFrame(step);
}

// Function to check if the element is in view
function isElementInView(element) {
   const rect = element.getBoundingClientRect();
   return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
   );
}

// Animate the count when the element is scrolled into view
window.addEventListener('scroll', () => {
   statElements.forEach((statElement) => {
      const countElement = statElement.querySelector('strong');
      if(isElementInView(statElement) && countElement.innerText === '0') {
         const targetCount = targetCounts[countElement.id];
         animateCount(countElement, targetCount);
      }
   });
});

