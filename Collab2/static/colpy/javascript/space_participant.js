$(document).ready(function() {
	$('#pull-btn').on('click', ajaxSendPullCode);
	$('#submit-btn').on('click', ajaxSendSubmitCode);
});

const ajaxSendPullCode = function() {
	$.ajax({
		url: '/space/pull_python/',
		type: 'post',
		data: {space_url: space_url},
		success: function(response) {
			const updated_code = response['python_code'];
			editor.getDoc().setValue(updated_code);
		}
	})
}

const ajaxSendSubmitCode = function() {
	const python_code = editor.getValue();
	$.ajax({
		url: '/space/submit_python/',
		type: 'post',
		data: {space_url: space_url, python_code: python_code},
		success: function(response) {
			$('#modal-title').text('Submission Status');
			$('#python-output').text('Successfully submitted');
			
			const elem = document.querySelector('.modal');
			const instance = M.Modal.init(elem);
			instance.open();
		}
	})
}