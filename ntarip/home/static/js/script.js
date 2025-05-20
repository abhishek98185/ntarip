
function downloadFile(filename) {
  // Simulate file download
  alert(`Downloading ${filename}`);
  // In real site: window.location.href = 'your-file-link-here';
}


document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("hamburger").addEventListener("click", function () {
    const nav = document.getElementById("navLinks");
    nav.classList.toggle("active");
  });

  window.downloadFile = function (fileName) {
    const link = document.createElement("a");
    link.href = `/static/${fileName}`;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };
});
