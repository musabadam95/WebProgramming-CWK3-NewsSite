


$(document).ready(function()
{ 

			//checks is session exists

			function log(){
				var formData = $(".login").serializeArray();
				var csrf = "input[name=csrfmiddlewaretoken]" 
				$.ajax({
					type:"POST",
					url: '/news/login',
					data: {
						formData,
						'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
					},

					success: function(response){
						
						$(".alert").append('<div class="alert alert-success alert-dismissable fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Success!</strong> Welcome back</div>')
						setTimeout(function(){
							var url="/news/"
							window.open(url,'_self')

						},2000); 

					},
					error: function(e){
						$(".alert").append('<div class="alert alert-danger alert-dismissable fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>Danger!</strong> Incorrect login, Please check login combination.</div>')
						$(".logID").val("")
						$(".logPass").val("")
					}

				})	
				event.preventDefault();
			}
			$(".login").submit(function(){
				log()

			})


		});
