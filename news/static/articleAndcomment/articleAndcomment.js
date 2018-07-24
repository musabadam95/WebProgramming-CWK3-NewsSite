$(document).ready(function()
{ 

	var pathnamea = window.location.pathname;
	var pathname=pathnamea.split("/");
	$.ajax({
		type:"GET",
		url: '/news/'+pathname[2]+'/checkLikeDislike',
		success : function(data) {
			if (data["like"]==true) {
				
				$( "#Like" ).prop( "disabled", true );
				$("#Dislike").prop( "disabled", false )
			}else if(data["Dislike"]==true){
				$("#Like").prop( "disabled", false )
				$("#Dislike").prop( "disabled", true );
			}
			else{
				if(data=="NotLoggedIn"){
					$( "#Like" ).prop( "disabled", true )
					$("#Dislike").prop( "disabled", true )
				}else{
					$( "#Like" ).prop( "disabled", false )
					$("#Dislike").prop( "disabled", false )
				}
			}


		},

		error: function(e){


		}
	
	})	
	$(".comment").submit(function(){
		if($("#commentBox").val()==""){


		}else{
		var csrf = "input[name=csrfmiddlewaretoken]" 
		$("#sub").removeAttr('onclick'); 

		$.ajax({
			type:"POST",
			url: '/news/'+pathname[2]+'/comment',

			data: {
				'comment' : $("#commentBox").val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},

			success : function(data) {
				$("#comments").html(data)
				$("#commentBox").val("")

			}

		})	

		event.preventDefault();
}
	})

	$(".likedBtn").click(function(){
		var id= this.id
		$.ajax({
			type:"POST",
			url: '/news/'+pathname[2]+'/likeDislike',
			data: {
				'likedorDislike':id,
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success : function(data) {
				if (id=="Like") {
					$("#Like").prop( "disabled", true );
					$("#Dislike").prop( "disabled", false )
				}else{
					$("#Like").prop( "disabled", false )
					$("#Dislike").prop( "disabled", true );
				}
				console.log(data["like"])
				$("#nooflikes").html(data["like"])
				$("#noofdislikes").html(data["Dislike"])
			}
		})	
		event.preventDefault();

	})

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

