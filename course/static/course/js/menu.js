 document.addEventListener("DOMContentLoaded", function () {
        var menuButton = document.querySelector('.menu');
        var dropdownMenu = document.querySelector('.dropdown-menu');

        menuButton.addEventListener('click', function () {
            dropdownMenu.classList.toggle('show');
        });

        // برای بستن منو در صورتی که خارج از المنطقه منو کلیک شود
        document.addEventListener('click', function (event) {
            if (!menuButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
                dropdownMenu.classList.remove('show');

            }
        });
    });