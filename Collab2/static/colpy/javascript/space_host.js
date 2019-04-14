$(document).ready(function() {
	$('#push-btn').on('click', ajaxSendPushCode);
	$('#check-btn').on('click', ajaxSendFetchCode);
});

const ajaxSendPushCode = function() {
	const python_code = editor.getValue();
	$.ajax({
		url: '/space/update_python/',
		type: 'post',
		data: {python_code: python_code, space_url: space_url},
		success: function(response) {
			$('#modal-title').text('Push Status');
			$('#python-output').text('Successfully pushed.');

			const elem = document.querySelector('.modal');
			const instance = M.Modal.init(elem);
			instance.open();
		}
	})
}

const ajaxSendFetchCode = function() {
	$.ajax({
		url: '/space/fetch_submission/',
		type: 'post',
		data: {space_url: space_url},
		success: function(response) {
			const submission = response['python_code'];
			editor.getDoc().setValue(submission);
		}
	})
}