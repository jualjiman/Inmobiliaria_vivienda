
//contacto

function enviarmensaje(){
	jQuery('#formmessage').load("sendform.php",
	{
		name: $('#name').val(),
		email: $('#email').val(), 
		message:$('#message').val()
	}).hide().fadeIn('slow');
}