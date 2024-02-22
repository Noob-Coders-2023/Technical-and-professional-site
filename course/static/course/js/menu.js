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


var aboutUs = document.querySelector('.about-us');
var submenu = document.querySelector('.submenu');
var about_back = document.querySelector('.about_back');
var navbar  = document.querySelector('.navbar ');

aboutUs.addEventListener('click', () => {
    if (submenu.classList.contains('show')) {
        submenu.classList.remove('show');
    } else {
        submenu.classList.add('show');
    }

});
about_back.addEventListener('click', ()=>{

        submenu.classList.add('hidden');

})