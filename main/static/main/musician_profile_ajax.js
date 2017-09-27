$(document).ready(function() {

  $(".btn_subs").click(function() {

    $.ajax({
      type: 'POST',
      data: {
        "csrfmiddlewaretoken": $('input')[0].getAttribute('value')
      },
      success: function(result) {
        var r = [];
        for (i = 0; i < result.sub_users.length; i++) {
          r.push('<li class="list-group-item">' + result.sub_users[i] + '</li>');
        }
        $('.btn_subs').html(result.subs)
        $('.subs').empty();
        $('.subs').html(r);
      }
    });

  });

});
