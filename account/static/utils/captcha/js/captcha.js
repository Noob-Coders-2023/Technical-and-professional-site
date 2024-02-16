
function generateCaptcha() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/generate_captcha/", true);  // این را به آدرس مناسب خود تغییر دهید
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var data = JSON.parse(xhr.responseText);
            // دریافت تصویر کپچا و تنظیم به عنوان پس‌زمینه div.preview
            document.querySelector(".preview").style.backgroundImage = "url(" + data.captcha_image + ")";
        }
    };
    xhr.send();
}

// فراخوانی تابع برای ایجاد تصویر اولیه کپچا
generateCaptcha();

// افزودن گوش کننده رویداد به دکمه تازه‌سازی برای ایجاد کپچا جدید
document.querySelector(".captcha_refresh").addEventListener("click", function() {
    generateCaptcha();
});