<?php
require("GCMPushMessage.php");

$apiKey = "AIzaSyCIIFXe3HBfJOpm90drkbtVH_Hx0hHfgdU";
$devices = array(
	'91bHAfE3oNqYLWxrrgZRZrfB_o68bBkwHtA6vLM2mS67enzR1huYlLkDeJFyf1NDxkEhiYMsi5pY9K4BlvvsMAfaJLmuTXdfZUoHxil4JTBvtEnpFrruWBoB7X7J9rlZPoTNl52v'
	,'deRsYxVDbJw:APA91bHRzqMv8DRz2g8aJGpl2ad6Xz_VCAxeLZVPUnJatOkUgMHrnvnF0J-13-4XszR0tnGN1ubS5jzgwcjhTiKgPAIkfHod6ghUGk3kXSm9e_E4eF3JdJq34_9UvEHzWVY6R7Zx6-cY'
	,':APA91bHAfE3oNqYLWxrrgZRZrfB_o68bBkwHtA6vLM2mS67enzR1huYlLkDeJFyf1NDxkEhiYMsi5pY9K4BlvvsMAfaJLmuTXdfZUoHxil4JTBvtEnpFrruWBoB7X7J9rlZPoTNl52v'
);
$message = "아시는 분인지 확인해주세요";
$an = new GCMPushMessage($apiKey);
$an->setDevices($devices);
$response = $an->send($message, array('title' => '집앞에 수상한 사람이 있습니다.', 'push_type' => 'my'));
print_r($response);
?>
