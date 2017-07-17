$(document).ready(function(){
	$('.overlay_link').hover(function(){
		$(this).parent().find('.meta').css('display','block');
	},function(){
		$(this).parent().find('.meta').css('display','none');
	});

	// category
	$('#category_btn').click(function(){
		var check = $('#categoryContent').hasClass('in')
		if(check == true){
			
		} else{
			$.ajax({
				url : "/api/get-category-data",
				type : "get",
				dateType:"text",
				data : {

				},
				success : function (response){
					if(response.result > 0){
						console.log(response)

						var el1 = document.getElementById('popular_tag');
						var el2 = document.getElementById('tag_top');
						var el3 = document.getElementById('tag_all');

						arr_cate = JSON.parse(response.data.categories);
						arr_tags_top = JSON.parse(response.data.tags_top);
						arr_tags = JSON.parse(response.data.tags);
						console.log(arr_cate.length)
						for (var i = 0; i < arr_cate.length; i++) { 
							el1.innerHTML += '<a href="/category/'+ arr_cate[i].fields.name +'" class="tags btn btn-info btn-xs"><i class="fa fa-bars"></i>'+ arr_cate[i].fields.name +'</a>';
						}
						console.log(arr_tags_top.length)
						for (var i = 0; i < arr_tags_top.length; i++) { 
							el2.innerHTML += '<a href="/tag/'+ arr_tags_top[i].fields.name +'" class="tags btn btn-primary btn-xs"><i class="fa fa-tag"></i>'+ arr_tags_top[i].fields.name +'</a>';
						}

						console.log(arr_tags.length)
						for (var j = 0; j < arr_tags.length; j++) { 
							console.log(arr_tags[j].fields.name)
							el3.innerHTML += '<li class="col-md-2"><a href="/tag/'+ arr_tags[j].fields.name +'" class="tags btn btn-primary btn-xs"><i class="fa fa-tag"></i>'+ arr_tags[j].fields.name +'</a></li>';
						}
					}
				}
			});
		}
	})
});