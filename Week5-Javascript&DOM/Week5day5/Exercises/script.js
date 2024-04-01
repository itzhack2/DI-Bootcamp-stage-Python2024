let color = null;
let mousedown = false;
let body = document.getElementsByTagName("body")[0];
let color_blocks = document.querySelectorAll("#sidebar > *");
let fill_blocks = document.querySelectorAll("#main > *");
let clear_button = document.getElementsByTagName("button")[0];

// clear function  
clear_button.addEventListener("click", function(){
    for (fill_blocks of fill_blocks){
        fill_blocks.style.backgroundColor = "white";
    }
});

body.addEventListener("mousedown", function(){
    mousedown = true;
})

body.addEventListener("mouseup", function(){
    mousedown = false;
})

for (color_blocks of color_blocks){
    color_blocks.addEventListener("click", function(event){
        color = event.target.style.backgroundColor;
    });
}
for (fill_blocks of fill_blocks){
    fill_blocks.addEventListener("mousedown", function(event){
        if (color != null) event.target.style.backgroundColor = color;
    });
    fill_blocks.addEventListener("mouseover", function(event){
        if (mousedown && color != null) event.target.style.backgroundColor = color;
    });
}
