// Scroll-to-Top Button Functionality
window.onscroll = function() {
    toggleScrollToTopButton();
};

// Show the button when the user scrolls down 200px from the top of the document
function toggleScrollToTopButton() {
    const scrollToTopBtn = document.getElementById("scrollToTopBtn");
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        scrollToTopBtn.style.display = "block"; // Show the button
    } else {
        scrollToTopBtn.style.display = "none"; // Hide the button
    }
}

// Smooth scroll back to the top when the button is clicked
document.getElementById("scrollToTopBtn").addEventListener("click", function() {
    window.scrollTo({ top: 0, behavior: "smooth" });
});
