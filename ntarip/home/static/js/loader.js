
function navigateWithLoader(url) {
    const loader = document.getElementById('loader');
    loader.style.display = 'flex'; // Show loader overlay
    // Delay navigation to let animation play
    setTimeout(() => {
        window.location.href = url;
    }, 800); // 1 second delay, adjust if needed
}

// Intercept all link clicks on the page
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', e => {
        // Only intercept normal left clicks without modifier keys
        if (
            !e.defaultPrevented &&
            e.button === 0 &&
            !e.metaKey &&
            !e.ctrlKey &&
            !e.shiftKey &&
            !e.altKey
        ) {
            e.preventDefault();
            const url = link.href;
            navigateWithLoader(url);
        }
    });
});
