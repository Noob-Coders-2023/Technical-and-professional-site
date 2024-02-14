//
// const fields = document.querySelectorAll(".field");
// const scrollContainer = document.querySelector(".fields");
// let backBtn=document.getElementById('backBtn')
// let nextBtn=document.getElementById('nextBtn')
// let intervalTime = 3000; // زمان اسکرول به میلی‌ثانیه (در اینجا ۳ ثانیه)
// let scrollAmount = -200; // مقدار اسکرول به اندازه پیکسل
//
// let scrollPosition = 0;
// let scrollInterval = setInterval(() => {
//   scrollPosition += scrollAmount;
//   if (scrollPosition >= scrollContainer.scrollWidth - scrollContainer.clientWidth) {
//     clearInterval(scrollInterval);
//     scrollPosition = 0;
//   }
//   scrollContainer.scrollTo({ top: 0, left: scrollPosition, behavior: 'smooth', easing: 'ease-in-out' });
// }, intervalTime);
//
//
//
// scrollContainer.addEventListener('wheel',(evt)=>{
//     evt.preventDefault();
//     scrollContainer.scrollLeft+=evt.deltaY;
//       scrollContainer.style.scrollBehavior='auto';
// });
//
//
// nextBtn.addEventListener('click',()=>{
//     scrollContainer.style.scrollBehavior='smooth';
//     scrollContainer.scrollLeft+=200
// })
//
// backBtn.addEventListener('click',()=>{
//       scrollContainer.style.scrollBehavior='smooth';
//     scrollContainer.scrollLeft-=200
// })
const fields = document.querySelectorAll(".field");
const scrollContainer = document.querySelector(".fields");
let backBtn = document.getElementById('backBtn');
let nextBtn = document.getElementById('nextBtn');
let intervalTime = 5000; // زمان اسکرول به میلی‌ثانیه (در اینجا ۳ ثانیه)
let scrollAmount = 200; // مقدار اسکرول به اندازه پیکسل

let isScrollingManually = false;

let scrollDirection = 1; // 1 برای اسکرول به راست و -1 برای اسکرول به چپ

function startAutoScroll() {
    if (!isScrollingManually) {
        scrollContainer.scrollTo({
            top: 0,
            left: scrollContainer.scrollLeft + scrollAmount * scrollDirection,
            behavior: 'smooth',
            easing: 'ease-in-out'
        });
        scrollDirection *= -1; // تغییر جهت اسکرول
    }
}

let scrollInterval = setInterval(startAutoScroll, intervalTime);

scrollContainer.addEventListener('scroll', () => {
    isScrollingManually = true;

    clearInterval(scrollInterval); // متوقف کردن اسکرول اتوماتیک به مدت زمان معین
    setTimeout(() => {
        isScrollingManually = false;
        scrollInterval = setInterval(startAutoScroll, intervalTime);
    }, intervalTime);
});

nextBtn.addEventListener('click', () => {
    scrollContainer.style.scrollBehavior = 'smooth';
    scrollContainer.scrollLeft += 200;
});

backBtn.addEventListener('click', () => {
    scrollContainer.style.scrollBehavior = 'smooth';
    scrollContainer.scrollLeft -= 200;
});
// scrollContainer.addEventListener('wheel',(evt)=>{
//     evt.preventDefault();
//     scrollContainer.scrollLeft+=evt.deltaY;
//       scrollContainer.style.scrollBehavior='auto';
// });