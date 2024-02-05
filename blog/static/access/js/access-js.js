let container_access = document.querySelector('.container-access');
// let content_access = document.querySelectorAll('.fields');
let prev1 = document.querySelector(".prev1");
let next1 = document.querySelector(".next1");


let contentAccess = document.querySelector('.fields');

// تابع برای اسکرول به چپ
function autoScroll() {
    contentAccess.scrollLeft += 20; // 20 پیکسل به چپ اسکرول می‌کند
}

// فراخوانی تابع autoScroll هر 5 ثانیه
let scrollInterval = setInterval(autoScroll, 5000); // 5000 میلی‌ثانیه یعنی 5 ثانیه

// اگر نیاز به متوقف کردن اسکرول خودکار دارید، می‌توانید از clearInterval استفاده کنید
// clearInterval(scrollInterval);




console.log('sssss' , next1)
next1.addEventListener('click', () => {
    console.log('reza')
});
prev1.addEventListener('click', () => {
content_access.item(0).scrollLeft -= 100;
    console.log('hg')
});
