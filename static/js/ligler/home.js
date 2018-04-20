$(document).ready(function(){
  
  
  $(".mac").click(function(){
        $(this).children('.ayrinti').toggle();
		
		 
    });
	
	   $(".maclarım").click(function(){
        $(this).children('tr').toggle();
		$(this).children('.goster').show();
		 
    });
  
  
});