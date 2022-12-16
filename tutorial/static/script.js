const navBtn=document.querySelector(".btn")
const nav=document.querySelector(".nav")
const btns=document.querySelectorAll("button")
const clsBtn=document.querySelector(".close-btn")
const mssg=document.querySelector(".message")
navBtn.addEventListener("click",function(e)
{
nav.classList.toggle("show-nav")
})
clsBtn.addEventListener("click",function()
{
mssg.style.display="none"
})
