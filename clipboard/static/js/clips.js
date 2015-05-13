server_url = "http://austinfstewart.com:8000/";

function decode(data, key) {
    return CryptoJS.AES.decrypt(CryptoJS.lib.CipherParams.create({ciphertext: CryptoJS.enc.Hex.parse(data)}), CryptoJS.enc.Hex.parse(key), { mode: CryptoJS.mode.ECB }).toString(CryptoJS.enc.Utf8) 
}

owner_id = -1
$(document).ready(function () {
    function failure_function() {
        Alert("There was an error communicating with the server.")
    }

    function get_and_display_clips() {
        function success_function(response) {
            $('.clip').remove();
            clips = JSON.parse(response)
            var password = $("#password").val()
            for (var i = 0; i < clips.length; i++) {
                clips[i].decoded_contents = decode(CryptoJS.enc.Base64.parse(clips[i].contents).toString(), CryptoJS.SHA256(password).toString());
                $('body').append('<p><button id=' + i +' class="clip">' + clips[i].decoded_contents + '</button></p>')
            }
            $(".clip").on('click', function() {
                prompt('text', clips[parseInt(this.id)].decoded_contents);
            })
        }

        $.ajax({
            type: 'GET', 
            url: server_url + 'clipboard?owner_id=' + owner_id,
            success: success_function,
            error: failure_function,
        });
    }

    function fetch(response) {
        $('#login-form').hide();
        owner_id = response;
        $('#fetch').show();
        get_and_display_clips();
    }

    $('#get-button').click(function() {
        var username = $("#username").val()
        var password = $("#password").val()
        var passkey = CryptoJS.SHA256(username + password);
        console.log(passkey);

        $.ajax({
            type: 'POST',
            url: server_url + 'login',
            success: fetch,
            data: JSON.stringify({username: username, passkey: passkey.toString()}),
        });
    });

    $('#fetch').click(get_and_display_clips);
    $('#fetch').hide();
});
