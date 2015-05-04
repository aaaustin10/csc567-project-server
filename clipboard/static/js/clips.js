function decode(data, key) {
    return CryptoJS.AES.decrypt(CryptoJS.lib.CipherParams.create({ciphertext: CryptoJS.enc.Hex.parse(data)}), CryptoJS.enc.Hex.parse(key), { mode: CryptoJS.mode.ECB }).toString(CryptoJS.enc.Utf8) 
}

$(document).ready(function () {
    function success_function(response) {
        clips = JSON.parse(response)
        for (var i = 0; i < clips.length; i++) {
            clips[i].decoded_contents = decode(CryptoJS.enc.Base64.parse(clips[i].contents).toString(), '574d93e6298df2e83e5c6b4dc63ae9280eb04b7589aed4ec0e7bfa8e0bc27f80');
            $('body').append('<p><button id=' + i +' class="clip">' + clips[i].decoded_contents + '</button></p>')
        }
        $(".clip").on('click', function() {
            prompt('text', clips[parseInt(this.id)].decoded_contents);
        })
    }

    var owner_id = 1;
    $.ajax({
        type: 'GET', 
        url: 'http://localhost:8000/clipboard?owner_id=' + owner_id,
        success: success_function,
    });
});
