        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
document.addEventListener('DOMContentLoaded', function () {
    var deleteButtons = document.querySelectorAll('.delete-course');

    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var courseId = this.getAttribute('data-course-id');
console.log(getCookie("csrftoken"))
            if (confirm('آیا مطمئن هستید که می‌خواهید این درس را حذف کنید؟')) {
                fetch('/delete_course/' + courseId + '/', {
                    method: 'POST' ,headers: {
                        'Accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json',
                        "X-CSRFToken": getCookie("csrftoken"),
                    },
                })
                    .then(function (response) {
                        if (!response.ok) {
                            throw new Error('خطا در حذف درس.');
                        }
                        location.reload();
                    })

                    .catch(function (error) {
                        alert(error.message);
                    });
            }
        });
    });
});
