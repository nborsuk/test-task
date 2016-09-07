	
		function save(){
			var form=$('form');
			var data=form.serialize();
			$.ajax({
				type: 'POST',
				url: 'save/',
				data: data,
				success: function(data){
					alert('Success');
				},
				error: function(xhr,str){
					alert('Error   '+xhr.responseCode);
				}
			});
		}	
	
