$(document).ready(function() {
	$('#push-btn').on('click', ajaxSendPushCode);
});

const ajaxSendPushCode = function() {
	const python_code = editor.getValue();
	$.ajax({
		url: '/space/update_python/',
		type: 'post',
		data: {python_code: python_code, space_url: space_url},
		success: function(response) {
			console.log('Pushed');
		}
	})
}