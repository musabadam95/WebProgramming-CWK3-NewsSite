$(document).ready(function(){

			//checks is session exists

		
		$(".updateForm").submit(function(){
			var formData = $(".updateForm").serializeArray();
			var csrf = "input[name=csrfmiddlewaretoken]" 
			$.ajax({
				type:"POST",
				url: '/news/sendUpdate',
				data: {
					formData,
					'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
				},

				success: function(response){
					alert("done")
					var url="/news/"
					window.open(url,'_self')
				},
				error: function(e){

					
				}

			})	
			event.preventDefault();

		})

})
	
