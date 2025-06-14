
// Show loader on link click
  function navigateWithLoader(url) {
    const loader = document.getElementById("loader");
    if (loader) loader.style.display = "flex";
    setTimeout(() => {
      window.location.href = url;
    }, 800);
  }

  // Intercept link clicks
  document.addEventListener("DOMContentLoaded", function () {
    // Hide loader when DOM is loaded
    const loader = document.getElementById("loader");
    if (loader) loader.style.display = "none";

    // Attach link click listeners
    document.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", function (e) {
        if (
          !e.defaultPrevented &&
          e.button === 0 &&
          !e.metaKey &&
          !e.ctrlKey &&
          !e.shiftKey &&
          !e.altKey &&
          link.target !== "_blank"
        ) {
          e.preventDefault();
          navigateWithLoader(link.href);
        }
      });
    });
  });

  // Hide loader on back/forward navigation
  window.addEventListener("pageshow", function (event) {
    const loader = document.getElementById("loader");
    if (loader) loader.style.display = "none";
  });
