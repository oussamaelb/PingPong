let myraquette=document.querySelector('.raquette')
let myball=document.querySelector('.ball')
let myscore=document.querySelector('.score')
b=0
a=0
function moveraquette(e){
    if (e.code=='KeyS' && a<335){
        a+=10
        myraquette.setAttribute('style',"position:absolute;top:"+a+"px")
    }
    if (e.code=='KeyW'){
        a-=10
        myraquette.setAttribute('style',"position:absolute;top:"+a+"px")
    }
    if (a<10){
        a=10
    }
}
document.addEventListener('keypress',moveraquette)
x=0
scr=0
y=Math.floor(Math.random()*330)
function moveball(){
    x+=5
    if (x<365){
        myball.setAttribute("style","position:absolute;left:"+x+"px;top:"+y+"px") 
    }
    else{
        x=0
        y=Math.floor(Math.random()*330)
    }
    Y= y>a-30 && y<a+60
    X= x>342 && x<346
    if(x>342 && Y){
        myscore.innerHTML=""
        scr+=1
        let myText=document.createTextNode(scr)
        myscore.appendChild(myText)  
        x=0
        y=Math.floor(Math.random()*330)
        
    }
    if (x>=359){
        clearInterval(myInterval)
    }
}
myInterval=setInterval(moveball,30)
function clr(){
    clearInterval(myInterval)
}