$(document).ready(function() {
	$('#run-btn').on('click', ajaxSendPythonCode);
	$('#push-btn').on('click', ajaxSendPushCode);
});

const ajaxSendPythonCode = function() {
	const python_code = editor.getValue();
	$.ajax({
		url: '/space/run_python/',
		type: 'post',
		data: {python_code: python_code},
		success: function(response) {
			console.log(response);
		}
	});
}

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