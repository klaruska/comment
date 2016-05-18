function load_page(
    page_url, paginationfield_id, loadbutton_id, pagediv_id
){
    var page = parseInt($(paginationfield_id).val());

    $(loadbutton_id).prop("disabled", true);
    $(loadbutton_id).text("Načítavanie ...");

    $.ajax({
        async: true,
        type: "GET",
        url: page_url,
        data: { page: page },
        error: function() {
            $(loadbutton_id).replaceWith("<p></p>");
        },
        success: function(data){ // check if there is an additional page
            // , disable load button if not
            $.ajax({
                async: true,
                type: "HEAD",
                url: page_url,
                data: { page: page + 1 },
                error: function(data){
                    $(loadbutton_id).replaceWith("<p></p>");
                },
                success: function(response){
                    $(loadbutton_id).text("Zobraziť ďalšie komentáre");
                    $(paginationfield_id).val(page + 1);
                    $(loadbutton_id).prop("disabled", false);
                }
            });
            $(pagediv_id).append($(data).find("div"));
        }
    });
}

function like(page_url, span_id, span_quality_id, number_of_likes, current_quality){
    likes = parseInt(number_of_likes);
    likes = parseInt(number_of_likes);
    quality = parseInt(current_quality);
    console.log(likes);
    $.ajax({
        url: page_url,
        success: function(){
            updated_likes = likes + 1;
            updated_quality = quality + 1;
            dislikes = likes - quality;
            $(span_quality_id).replaceWith("<span id='" + span_quality_id + "'>" + updated_quality + "</span>");
            $(span_id).parent().replaceWith("<span class='right'><span id='" + span_id + "'><i class='fa fa-plus-square'></i> " + updated_likes + "</span><span id='dis" + span_id + "'><i class='fa fa-minus-square'></i> " + dislikes + "</span></span>");
        }
    });
}

function dislike(page_url, span_id, span_quality_id, number_of_dislikes, current_quality){
    dislikes = parseInt(number_of_dislikes);
    span_like_id = span_id.substring(3);
    quality = parseInt(current_quality);
    $.ajax({
        url: page_url,
        success: function(){
            updated_dislikes = dislikes + 1;
            updated_quality = quality - 1;
            likes = quality + dislikes;
            $(span_quality_id).replaceWith("<span id='" + span_quality_id + "'>" + updated_quality + "</span>");
            $(span_id).parent().replaceWith("<span class='right'><span id='" + span_like_id + "'><i class='fa fa-plus-square'></i> " + likes + "</span><span id='" + span_id + "'><i class='fa fa-minus-square'></i> " + updated_dislikes + "</span></span>");
        }
    });
}
