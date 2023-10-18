"use strict"

/* --------------------------BURGER------------------------------------------------ */
const iconMenu = document.querySelector('.header__menu__icon');
if (iconMenu) {
    const menuBody = document.querySelector('.header__menu__body');
    iconMenu.addEventListener("click", function (e) {
        document.body.classList.toggle('_lock');
        iconMenu.classList.toggle('_active');
        menuBody.classList.toggle('_active');
    });
}

/* -------------------------------------------------------------------------- */


function showImage(side) {
    if (window.innerWidth > 768) {
        if (side === 'left') {
            let leftImage = document.getElementById('left-image');
            leftImage.style.display = 'block';
            leftImage.style.animation = "slideInLeft 1s forwards";
        } else if (side === 'right') {
            let rightImage = document.getElementById('right-image');
            rightImage.style.display = 'block';
            rightImage.style.animation = "slideInRight 1s forwards";
        }
    }
}

function hideImage(side) {
    if (window.innerWidth > 768) {
        if (side === 'left') {
            let leftImage = document.getElementById('left-image');
            leftImage.style.animation = "slideOutLeft 1s forwards";
            setTimeout(function () {
                leftImage.style.animation = '';
            }, endless);
        }
        else if (side === 'right') {
            let rightImage = document.getElementById('right-image');
            rightImage.style.animation = "slideOutRight 1s forwards";
            setTimeout(function () {
                rightImage.style.animation = '';
            }, endless);
        }
    }
}
/* -------------------------------------------------------------------------- */



