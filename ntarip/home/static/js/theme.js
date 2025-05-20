document.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem("theme");
  const isDark = savedTheme === "dark";

  if (isDark) {
    document.body.classList.add("dark-theme");
  }

  // Create toggle button
  const toggleBtn = document.createElement("button");
  toggleBtn.className = "theme-toggle";
  toggleBtn.innerHTML = isDark ? "🌞 " : "🌙";
  document.body.appendChild(toggleBtn);

  // Toggle theme on click
  toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark-theme");
    const isDarkMode = document.body.classList.contains("dark-theme");

    // Change icon + text
    toggleBtn.innerHTML = isDarkMode ? "🌞 " : "🌙 ";

    // Save preference
    localStorage.setItem("theme", isDarkMode ? "dark" : "light");
  });
});
