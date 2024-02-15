(function () {
  const fonts = ['cursive', 'sans-serif'];
  let captchaValue = '';

  function generateCaptcha() {
    let value = btoa(Math.random() * 1000000000);
    value = value.substr(0, 5 + Math.random() * 5);
    captchaValue = value;
  }

  function setCaptcha() {
    const rotate = -20 + Math.trunc(Math.random() * 30);
    const font = Math.trunc(Math.random() * fonts.length);

    // تنظیم متغیرهای CSS
    document.documentElement.style.setProperty('--rotation-angle', `${rotate}deg`);
    document.documentElement.style.setProperty('--font-family', fonts[font]);

    // تنظیم رنگ تصادفی
    const randomColor = getRandomColor();
    document.documentElement.style.setProperty('--captcha-color', randomColor);

    // نمایش کد در HTML
    const html = captchaValue.split('').map(char => `<span>${char}</span>`).join('');
    document.querySelector('.captcha .preview').innerHTML = html;
  }

  function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  document.querySelector('.captcha .captcha_refresh').addEventListener('click', function () {
    generateCaptcha();
    setCaptcha();
  });

  // اولین بار که صفحه لود می‌شود
  generateCaptcha();
  setCaptcha();
})();
