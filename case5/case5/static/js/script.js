function inf(el) {
    id = el.id
    if (document.getElementById(id + 'txt').getAttribute('hidden') == null) {
        document.getElementById(id + 'txt').setAttribute('hidden', '')
    }
    else {
        document.getElementById(id + 'txt').removeAttribute('hidden')
    }

}

$(document).ready(function() {
    sessionStorage.scrollTop = $(this).scrollTop();
});