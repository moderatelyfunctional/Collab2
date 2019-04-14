$(document).ready(function() {
	ajaxSendPythonCode();
});

const ajaxSendPythonCode = function() {
	const python_code = $('#code-python').text();
	$.ajax({
		url: '/space/run_python/',
		type: 'post',
		data: {python_code: python_code},
		success: function(response) {
			console.log(response);
		}
	});
}