<?php

$connect = mysql_connect(“server_name”, “admin_name”, “password”); 
if (!connect) { die('Connection Failed: ' . mysql_error()); { mysql_select_db(“database_name”, $connect);

$user_info = “INSERT INTO user_info (email, password, firstname, lastname, phonenumber) 
VALUES ('$_POST[email]', '$_POST[password]', '$_POST[firstname]', '$_POST[lastname]', '$_POST[phonenumber]')”;
if (!mysql_query($user_info, $connect)) { die('Error: ' . mysql_error()); }

echo “Your information was added to the database.”;
    
mysql_close($connect); ?>