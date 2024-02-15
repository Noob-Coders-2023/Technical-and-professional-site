let slideshow = document.querySelector(".slideshow");
let slides = document.querySelectorAll('.slide');
let points = document.querySelectorAll('.points > span');
let prev = document.querySelector(".prev");
let next = document.querySelector(".next");
let active = 0;
let timer = 5000;
let intervalId;

function classSwitcher() {
    slides.forEach(slide => slide.classList.remove('active'));
    points.forEach(point => point.classList.remove('active'));
    slides[active].classList.add('active');
    points[active].classList.add('active');
}

let goNext = () => {
    active = (active === slides.length - 1) ? 0 : active + 1;
    classSwitcher();
};

function startSlideshow() {
    intervalId = setInterval(goNext, timer);
}

next.addEventListener('click', () => {
    clearInterval(intervalId);
    goNext();
    startSlideshow();
});

points.forEach((point, index) => {
    point.addEventListener('click', e => {
        active = index
        classSwitcher()
    })
})

slideshow.addEventListener('click', () => {
    // هنگامی که روی اسلاید کلیک شود، به اسلاید بعدی برو
    clearInterval(intervalId);
    goNext();
    startSlideshow();
});

startSlideshow();
