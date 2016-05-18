from django import template


register = template.Library()


@register.assignment_tag(name="get_pageloader")
def get_pageloader(page_url, *args, **kwargs):

    pagediv_id = kwargs.get("pagediv_id", "pagediv-id")
    loadbutton_id = kwargs.get("loadbutton_id", "load-id")
    pagination_id = kwargs.get("pagination_id", "pagination-id")

    button_script = """$("#%s").click(function(){load_page("%s", "#%s", "#%s", "#%s");});""" % \
                    (loadbutton_id, page_url, pagination_id, loadbutton_id, pagediv_id)

    if pagediv_id == "pagediv-id":
        element = "div"
    else:
        element = "p"

    return {
        "pagediv": "<" + element + " id='" + pagediv_id + "'></" + element + ">",
        "loadbutton": "<button id='" + loadbutton_id
                      + "' type='submit'>Zobraziť komentáre</button>",
        "pagination": "<input type='hidden' id='"
                      + pagination_id + "' value='1'>",
        "button_script": button_script,
        }

@register.assignment_tag(name="like_loader")
def like_loader(page_url_like, page_url_dislike, *args, **kwargs):
    span_quality_id = kwargs.get("span_quality_id", "span-quality-id")
    quality = kwargs.get("quality", "0")
    span_like_id = kwargs.get("span_like_id", "span-like-id")
    span_dislike_id = kwargs.get("span_dislike_id", "span-dislike-id")
    likes = kwargs.get("likes", "0")
    dislikes = kwargs.get("dislikes", "0")
    like_button_id = kwargs.get("like_button_id", "like-button-id")
    dislike_button_id = kwargs.get("dislike_button_id", "dislike-button-id")

    like_script = """$("#%s").click(function(){like("%s", "#%s", "#%s", "%s", "%s");});""" % \
                  (like_button_id, page_url_like, span_like_id, span_quality_id, likes, quality)
    dislike_script = """$("#%s").click(function(){dislike("%s", "#%s", "#%s", "%s", "%s");});""" % \
                     (dislike_button_id, page_url_dislike, span_dislike_id, span_quality_id, dislikes, quality)
    span_like_button = "<button class='nobutton' id='" + like_button_id + "' type='submit'><i class='fa fa-plus-square'></i></button>"
    span_dislike_button = "<button class='nobutton' id='" + dislike_button_id + "' type='submit'><i class='fa fa-minus-square'></i></button>"
    return {
        "span_like_id": "<span id='" + span_like_id + "'>" + span_like_button + likes + "</span>",
        "span_dislike_id": "<span id='" + span_dislike_id + "'>" + span_dislike_button + dislikes + "</span>",
        "like_script": like_script,
        "dislike_script": dislike_script,
        }