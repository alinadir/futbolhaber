$(document).ready(function(){
  
  
   $(".alar").click(function(){
        $(".puan").hide();
		$("." + $(this).attr("id")).show();
		$(".hafta").text($(this).text());
		 
    });
  
   $(".maclarım").click(function(){
        $(this).children('tr').toggle();
		$(this).children('.goster').show();
		 
    });
  
  
});