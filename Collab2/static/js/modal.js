$(document).ready(function() {
	$('#run-btn').on('click', ajaxSendPythonCode);
})

const ajaxSendPythonCode = function() {
	const python_code = editor.getValue();
	$.ajax({
		url: '/space/run_python/',
		type: 'post',
		data: {python_code: python_code},
		success: function(response) {
			console.log('Hey');
			$('#python-output').text(response);

			const elem = document.querySelector('.modal');
			const instance = M.Modal.init(elem);
			instance.open();

		}
	});
}