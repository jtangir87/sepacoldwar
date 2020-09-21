/* Free Estimate Functions */

$(function () {

    /* Functions */


    var homesaveForm = function (e) {
        e.preventDefault();
        var form = $(this);
        console.log("form submitted")
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#' + form.attr("id")).each(function () {
                        this.reset();
                    });
                    $("#modal-base .modal-content").html(data.html_success_message);
                    $("#modal-base").modal("show");
                }
                else {
                    $("#modal-base .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    $("#commentForm").on("submit", homesaveForm);

});

