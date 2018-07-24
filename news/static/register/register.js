$(document).ready(function()
{ 
			//checks is session exists
			function log(){
				var formData = $(".registerform").serializeArray();
				var csrf = "input[name=csrfmiddlewaretoken]" 
				$.ajax({
					type:"POST",
					url: '/news/completeSignUp',
					data: {
						formData,
						'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
					},
					dataType:"html",
					success: function(response){
						$(".alert").append('<div class="alert alert-success alert-dismissable fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Success!</strong> Welcome back</div>')
						var url="/news/"
						window.open(url,'_self')
					},
					error: function(e){
						$(".alert").append('<div class="alert alert-danger alert-dismissable fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Danger!</strong> This email already exists</div>')						
					},
					

				})	
				event.preventDefault();
			}
			$(".registerform").submit(function(){
				log()

			})


		});
