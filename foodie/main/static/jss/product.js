$(document).ready(function(){
    $('.address').on('click',function(){
        $('.hidden').css("z-index","2");
        $('.final').css("display","block");
    })
    $('.close').click(function(){
        $('.hidden').css("z-index","-1");
        $('.final').css("display","none");
      });
})
