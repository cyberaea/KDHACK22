<?php
$message = "Line 1\r\nLine 2\r\nLine 3";
$message = wordwrap($message, 70, "\r\n");
if(mail('domen@gmail.com', 'My Subject', $message)){
    echo "да";
} else {
echo "нет";
}
?>