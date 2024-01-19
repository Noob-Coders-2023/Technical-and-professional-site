function validateForm(event) {
    // اجزاء فرم را با استفاده از کلاس‌ها دریافت کنید
    var usernameInput = document.querySelector('.usernameInput');


    // ارورها را نمایش دهید
    var usernameError = document.querySelector('.usernameError');


    // ارورها را پاک کنید (در هر بار ارسال مجدد)
    usernameError.textContent = '';


    // اعتبارسنجی
    if (usernameInput.value === '') {
        usernameError.textContent = 'نام کاربری نمی‌تواند خالی باشد';
        event.preventDefault(); // ارسال فرم را متوقف کنید
    }


}
