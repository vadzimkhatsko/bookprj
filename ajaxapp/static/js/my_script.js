$("document").ready(function () {
    let id;
    let obj;
    $(".like_teg").on("click", function () {
        id = $(this).attr('id');
        obj = this;
        console.log(id);
        $.ajax({"url":"/add_like/",
                    "data":{"id":id},
                    "success":function (data) {
                        console.log(data);
                        $(obj).html("Total likes " + data);
                    }})
    })
});