var scrollToTopBtn = document.getElementById("upbutton");
var rootElement = document.documentElement;

function scrollToTop() {
  rootElement.scrollTo({
    top: 0,
    behavior: "smooth"
  });
}
window.addEventListener("scroll",function() {
   if(window.scrollY > 200) {
      scrollToTopBtn.style.display = "block";
   }
   else{
       scrollToTopBtn.style.display = "none";
   }
},false);
scrollToTopBtn.addEventListener("click", scrollToTop);

var burgerMenu = document.getElementById('burger-menu');
var overlay = document.getElementById('menu');
var els = document.getElementsByClassName("close");


burgerMenu.addEventListener('click',function(){
  this.classList.toggle("close");
  overlay.classList.toggle("overlay");
});
let elements = document.getElementsByClassName("close");

for (let i = 0; i < elements.length; i += 1) {
    elements[i].addEventListener('click',function(){
  document.getElementById('burger-menu').click();
});
}

    var sliderImages = document.querySelectorAll('.slider img');
    var currentImageIndex = 0;

    setInterval(function() {
      sliderImages[currentImageIndex].classList.remove('active');

      currentImageIndex = (currentImageIndex + 1) % sliderImages.length;

      sliderImages[currentImageIndex].classList.add('active');
    }, 2000);