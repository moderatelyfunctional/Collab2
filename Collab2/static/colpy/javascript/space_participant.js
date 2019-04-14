$(document).ready(function() {
	$('#pull-btn').on('click', ajaxSendPullCode);
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