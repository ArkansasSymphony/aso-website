// validator
$('#contact_form').submit(function(){
	var submit=true;
    $('.required').each(function(){
    	if($(this).val() == ""){
    		$(this).css("background-color","#FFAAAA");
    		$('#note').fadeIn(1000);
   				submit=false;
 		}
    	else{
    		$(this).css("background-color","#FFFFFF");
    	}
    });

    if(submit==true){
    	return true;
    }
    else{
    	return false;
    }
});