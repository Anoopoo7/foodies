$(document).ready(function(){
    $(".register").on("click",function(){
        $(".view").addClass("reg")
    })
    $(".login").on("click",function(){
        $(".view").removeClass("reg")
    })
})