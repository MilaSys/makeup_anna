document.addEventListener("DOMContentLoaded", () => {

  document.getElementById("burger").addEventListener("click", function (e) {
    document.querySelector(".top-menu__nav").classList.toggle("open"),
      document.querySelector(".body").classList.toggle("noscroll"),
      document.querySelector(".top-content").classList.toggle("content-hide")
  })

  document.addEventListener("click", function (e) {
    let menu = document.querySelector(".top-menu__nav");
    let list = document.querySelector(".top-menu__list")
    let burger = document.getElementById("burger");
    if (!menu.contains(e.target) && e.target !== burger || list.contains(e.target)) {
      menu.classList.remove("open");
      document.querySelector(".body").classList.remove("noscroll");
      document.querySelector(".top-content").classList.remove("content-hide");
    }
  });

//   var swiper = new Swiper('.swiper', {
//     slidesPerView: 3,
//     loop: true,
//     spaceBetween: 20,
//     // rewind: true,
//     // direction: getDirection(),
//     navigation: {
//       nextEl: '.swiper-button-next',
//       prevEl: '.swiper-button-prev',
//     },
//   });

  var swiper = new Swiper('.swiper', {
      slidesPerView: 3,
      loop: true,
      spaceBetween: 20, //looped slides should be the same
      navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
      },
    //   observer: true,
    //   observeParents: true,
    //   observeSlideChildren: true
  });

  const servicesWrapper = document.querySelectorAll('.services__list');
  const servicesSlide = document.querySelectorAll('.services__item');
  const wrapper = document.querySelector('.wrapper');
  const next = document.querySelectorAll('.services-wrapper .swiper-button-next');
  const prev = document.querySelectorAll('.services-wrapper .swiper-button-prev');

  mobileView();

  window.addEventListener('resize', mobileView);

  function mobileView() {
    if (document.documentElement.clientWidth <= 1023) {
      var swiper = new Swiper('.swiper', {
        slidesPerView: 1,
        loop: true,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
      });
      servicesWrapper.forEach(function (n) {
        n.classList.remove('services__list')
        n.classList.add('services__list-mobile')
      });
      servicesSlide.forEach(function (n) {
        n.classList.add('swiper-slide')
      });
      next.forEach(function (n) {
        n.style.display = 'flex';
        n.style.top = '190px';
      });
      prev.forEach(function (n) {
        n.style.display = 'flex';
        n.style.top = '190px';
      });
    } else {
      var swiper = new Swiper('.swiper', {
        slidesPerView: 3,
        loop: true,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
      });
      servicesWrapper.forEach(function (n) {
        n.classList.add('services__list')
        n.classList.remove('services__list-mobile')
      });
      servicesSlide.forEach(function (n) {
        n.classList.remove('swiper-slide')
      });
      next.forEach(function (n) {
        n.style.display = 'none';
      });
      prev.forEach(function (n) {
        n.style.display = 'none';
      });
    }
  }

//   let days = document.querySelector('.days');
//   let daysText = document.querySelector('.days-text');

//   if (days.textContent = 1) {
//     daysText.textContent = 'день';
//   } 
//   if (days.textContent = 2) {
//     daysText.textContent = 'дня';
//   }
//   if (days.textContent = 3) {
//     daysText.textContent = 'дня';
//   }
//   if (days.textContent = 4) {
//     daysText.textContent = 'дня';
//   } else {
//     daysText.textContent = 'дней';
//   }

});
