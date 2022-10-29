function check() {
    var a = document.getElementById("password1").value;
    var b = document.getElementById("password2").value;
    var f = document.getElementById("fullname").value;
    var u = document.getElementById("username").value;
    var e = document.getElementById("email").value;

    if (a == "" || b == "" || f == "" || u == "" || e == "") {
        document.getElementById("messages").innerHTML = "Fill in all the form fields! ";
        return false;
    }
    if (a != b) {
        document.getElementById("messages").innerHTML = "Different passwords!";
        return false;
    }
}