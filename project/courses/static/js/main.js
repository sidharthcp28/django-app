// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function () {
    // Spinner
    const spinnerElement = document.getElementById('spinner');
    if (spinnerElement) {
        // Simulate an asynchronous operation using a promise
        new Promise((resolve) => {
            // Simulate async operation completion after 1 second
            setTimeout(resolve, 1000);
        }).then(() => {
            spinnerElement.style.display = 'none';
        });
    }
    // Smooth Scroll for "Back to Top" Button
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    // Smooth Scroll for "Back to Top" Button
    scrollToTop();
});
