"use strict"

/* --------------------------BURGER------------------------------------------------ */
const iconMenu = document.querySelector('.header__menu__icon');
if (iconMenu){
    const menuBody = document.querySelector('.header__menu__body');
    iconMenu.addEventListener("click", function (e){
        document.body.classList.toggle('_lock');
        iconMenu.classList.toggle('_active');
        menuBody.classList.toggle('_active');
    });
}