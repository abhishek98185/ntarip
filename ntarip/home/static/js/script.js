
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
const tl = gsap.timeline()
tl.from(".navbar h1", {
  duration: 1,
  y: -50,
  opacity: 0,
  scale: 0,
})
tl.from(".navbar ul li", {
  duration: 1,
  y: -50,
  opacity: 0,
  stagger: 0.2
})
var path = `M 50 0 Q 50 250 50 500`
var finalpath = `M 50 0 Q 50 250 50 500`
var pathContainer = document.querySelector("#path")
pathContainer.addEventListener("mousemove", function (dets) {
  const bounds = pathContainer.getBoundingClientRect();
  const x = dets.clientX - bounds.left;
  const y = dets.clientY - bounds.top;
  path = `M 50 0 Q ${x} ${y} 50 500`
  gsap.to("#path svg path", {
    attr: {
      d: path
    },
    duration: 0.3,
    ease: "power3.out"
  })

})
pathContainer.addEventListener("mouseleave", function () {
  gsap.to("svg path", {
    attr: {
      d: finalpath
    },
    duration: 1.5,
    ease: "elastic.out(1, 0.2)"
  })
})
var path2Container = document.querySelector("#path2")
path2Container.addEventListener("mousemove", function (dets) {
  const bounds = path2Container.getBoundingClientRect();
  const x = dets.clientX - bounds.left;
  const y = dets.clientY - bounds.top;
  path = `M 50 0 Q ${x} ${y} 50 500`
  gsap.to("#path2 svg path", {
    attr: {
      d: path
    },
    duration: 0.3,
    ease: "power3.out"
  })

})
path2Container.addEventListener("mouseleave", function () {
  gsap.to("svg path", {
    attr: {
      d: finalpath
    },
    duration: 1.5,
    ease: "elastic.out(1, 0.2)"
  })
})