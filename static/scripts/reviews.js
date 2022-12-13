$(document).ready(function() {
	$('form').on('submit', function(event) {
		$.ajax({
			data : {
                game_name: $('#game_name').val(),
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
				window.setTimeout(2000)
				window.location.reload(true)
				$('#errorAlert').hide();
			}
		});

		event.preventDefault();
	});
	$('div').on('reset', function(event) {
		$.ajax({
			data : {
                game_name: $('#game_name').val(),
                author: $('#author').val(),
				title : $('#title').val(),
				content : $('#content').val()
			},
			type: 'POST',
			url: '/deletereview',
			dataType: 'json',
		}).done(function(data) {
			console.log("review deleted")
			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			} else {
				$('#successAlert').text(data.message).show();
				$('#errorAlert').hide();
			}
		})
		event.preventDefault();
	});
});