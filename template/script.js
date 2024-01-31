// Получаем элементы
const element1 = document.querySelector(".abstractLine");
const element2 = document.querySelector(".productType");

var textWidth = element2.getBoundingClientRect().width;
var characterCount = element2.textContent.length;


if (characterCount <= 6) {
    b = -15
}

if (characterCount >= 9){
    b=-50
}

element1.style.width = `${textWidth+b}px`;