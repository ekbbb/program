<?php
$weekday = array('日','月','火','水','木','金','土');
$date = date('n月j日');
$dow  = $weekday[ date('w') ].'曜日';
$time = date('G時i分');
$txt  = 'おはようございます。'.$date.', '.$dow.', '.$time.'です。';
echo $txt.PHP_EOL;
