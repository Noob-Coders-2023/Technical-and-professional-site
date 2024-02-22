 const swiper = new Swiper('.swiper-wrapper', {
    slidesPerView: 'auto',
    spaceBetween: 30,
    loop: true,
    autoplay: {
      delay: 2000,
      disableOnInteraction: false
    },
    navigation: {
      nextEl: '.next1',
      prevEl: '.prev1'
    }
  });
