// 13-script.js

$(document).ready(function () {
  $('#btn_translate, #language_code').on('click keypress', function (event) {
    if (event.type === 'click' || (event.type === 'keypress' && event.which === 13)) {
      const languageCode = $('#language_code').val();

      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        method: 'GET',
        dataType: 'json',
        data: {
          lang: languageCode
        },
        success: function (data) {
          $('#hello').text(data.hello);
        },
        error: function (error) {
          console.log('Error:', error);
        }
      });
    }
  });
});
