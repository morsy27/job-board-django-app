var Menu = document.getElementById("menu")
var MenuBtn = document.getElementById("menu-btn")
var CloseMenu = document.getElementById("close-menu")

MenuBtn.addEventListener("click",function () {
   Menu.classList.add("active") 
});
CloseMenu.addEventListener("click",function () {
   Menu.classList.remove("active") 
});



// Option Menu Toggle

var categoryMenuBtn = document.getElementById("categorymenubtn")
var categoryMenu = document.getElementById("categorymenu")
var locationMenuBtn = document.getElementById("locationmenubtn")
var locationMenu = document.getElementById("locationmenu")
var careerlevelMenuBtn = document.getElementById("careerlevelmenubtn")
var careerlevelMenu = document.getElementById("careerlevelmenu")
var jobtypeMenuBtn = document.getElementById("jobtypemenubtn")
var jobtypeMenu = document.getElementById("jobtypemenu")

categoryMenuBtn.addEventListener("click", function () {
   categoryMenu.classList.toggle("option-menu-show")
});
locationMenuBtn.addEventListener("click", function () {
   locationMenu.classList.toggle("option-menu-show")
});
careerlevelMenuBtn.addEventListener("click", function () {
   careerlevelMenu.classList.toggle("option-menu-show")
});
jobtypeMenuBtn.addEventListener("click", function () {
   jobtypeMenu.classList.toggle("option-menu-show")
});