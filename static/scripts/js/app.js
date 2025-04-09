
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






//THIS HANDLE DARK MODE BUTTON ON HEADER
var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
} else {
    themeToggleDarkIcon.classList.remove('hidden');
}

var themeToggleBtn = document.getElementById('theme-toggle');

themeToggleBtn.addEventListener('click', function() {

    // toggle icons inside button
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');

    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }

    // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        }
    }
    
});




// SWIPER FOR ABOUT PAGE
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



