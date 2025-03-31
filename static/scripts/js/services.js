const demy = document.querySelector('.pics-open');

demy.addEventListener('click', () => {
   let clickOpen = document.querySelector('.photo-open');
   clickOpen.classList.toggle('open')
});