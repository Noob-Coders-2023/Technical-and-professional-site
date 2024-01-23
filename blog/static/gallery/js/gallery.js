 var swiper = new Swiper(".mySwiper", {
      slidesPerView: 1,
      spaceBetween: 30,
      loop: true,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });
// تغییر عکس‌ها هر ۵ ثانیه
setInterval(function () {
  // انتقال به اسلاید بعدی
  swiper.slideNext();
}, 5000);



