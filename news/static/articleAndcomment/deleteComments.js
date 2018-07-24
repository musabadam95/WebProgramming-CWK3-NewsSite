$(document).ready(function()
{ 

	var pathnamea = window.location.pathname;
	var pathname=pathnamea.split("/");
	

	$(".delete").click(function(){
		var id=this.id
		var pathname=id.split("/");
		$.ajax({
			type:"POST",
			url: id,

			data: {
				'comment' : $("#commentBox").val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},

			success : function(data) {
				$("#"+pathname[2]).hide(200,"linear")
				
			}

		})	

		event.preventDefault();



	})

})

