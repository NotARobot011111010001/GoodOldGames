$(document).ready(function() {
	$('form').on('submit', function(event) {
		$.ajax({
			data : {
                game_name: $('#game').val(),
                author: $('#author').val(),
				title : $('#title').val(),
				content : $('#content').val()
			},
			type : 'POST',
			url : '/createpost',
            dataType : 'json',
		}).done(function(data) {
			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			} else {
				$('#successAlert').text(data.message).show();
				$('#errorAlert').hide();
			}
		});

		event.preventDefault();
	});
});