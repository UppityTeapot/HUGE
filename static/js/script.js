/* Author: Peter Hicks

*/

var messages = $("p").length;
var messageNumber = 20;
var messagesOnScreen = 10;

	var refreshId = setInterval(function() {
      $("#responsecontainer").load('response.php?randval='+ Math.random());
   	}, 9000);

 	function huge_showText(text)
	{
		$('#console').append('<p>' + text + '</p>')
		$('p:last').hide().fadeIn(800);
    	$('#console').scrollTo('p:last', 200);
    	event.preventDefault();
    	messages++;
	}
	
	function huge_clearConsole()
	{
		$('p').fadeOut("slow").remove();
	}
	
	function huge_trimOld()
	{
		if (messages >= 20) 
		{
			$("p:lt(" + (messageNumber - messagesOnScreen) + ")").remove();
			messages = $("p").length;
		}	
	}
	
	function huge_gotoMessage(number)
	{
		$('#console').scrollTo($("p:eq(" + number + ")"), 200);
	}

window.onload = function(){ 
	
	/* Initialise screen, display welcome test */
	huge_showText('Welcome to HUGE! Enjoy your stay.','0')
	
    $("a.text").click(function () { 
      huge_showText('Maecenas faucibus mollis interdum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Nullam id dolor id nibh ultricies vehicula ut id elit. Maecenas faucibus mollis interdum. Cras mattis consectetur purus sit amet fermentum. Integer posuere erat a ante venenatis dapibus posuere velit aliquet.' )
    });
    
    /* debug buttons */
    $("a.deleteold").click(function () { 
      huge_trimOld()
    });
    
    $("a.howmany").click(function () { 
      alert(messages)
    });
    
    $("a.goto").click(function () { 
      huge_gotoMessage('0')
    });
    
    $("a.room1_table").click(function () {
		huge_showText("There is a mottled, greying table in the middle of the room. It appears not to have been used in years; there is a clear inch of dust and grime upon it. Removing the dust reveals a collection of gentle bumps and dents, proof that, years ago, the table was the centerpiece of a house. Now, it lies empty.")
    });
    
    /* blade controls */
    
	$("a.look").click(function () {
		isopen = $(".lookblade").css("display");
		if (isopen == "none") 
		{
			$(".blade2").not(".lookblade").hide(0);
			$(".lookblade").show("slide", 200);
		}
    });
    
	$("a.move").click(function () { 
      isopen = $(".moveblade").css("display");
		if (isopen == "none") 
		{
			$(".blade2").not(".moveblade").hide(0);
			$(".moveblade").show("slide", 200);
		}
    });

	$("a.talk").click(function () { 
      isopen = $(".talkblade").css("display");
		if (isopen == "none") 
		{
			$(".blade2").not(".talkblade").hide(0);
			$(".talkblade").show("slide", 200);
		}
    });
    
    $("a.debug").click(function () { 
      isopen = $(".debugblade").css("display");
		if (isopen == "none") 
		{
			$(".blade2").not(".debugblade").hide(0);
			$(".debugblade").show("slide", 200);
		}
    });
}