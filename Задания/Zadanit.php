<?php
$users = [
    [
        "user_name" => "Алексей",
        "user_age" => 21,
        "user_login" => "alex",
        "user_password" => "Alex@123"
    ],
    [
        "user_name" => "Мария",
        "user_age" => 19,
        "user_login" => "maria",
        "user_password" => "Maria#456"
    ],
    [
        "user_name" => "Иван",
        "user_age" => 25,
        "user_login" => "ivan",
        "user_password" => "Ivan_789"
    ]
];

$user_login = "alex";
$user_password = "Alex@123";

$found_user = null;

foreach ($users as $user) {
    if ($user["user_login"] === $user_login) {
        $found_user = $user;
        break; 
    }
}

if ($found_user === null) {
    echo "Пользователь с таким логином не существует.<br>";
} 
elseif($found_user["user_password"] !== $user_password) 
    {
        echo "Некорректный пароль.<br>";
    } 
    else {
        echo "Имя пользователя: " . $found_user["user_name"] . "<br>";
        echo "Возраст: " . $found_user["user_age"] . "<br>";
        
        $has_special_char = false;
        $has_digit = false;
        
        $special_chars = ["@", "&", "%", "#", "[", "]", "(", ")", "_", "!"];
        
        foreach ($special_chars as $char) {
            if (str_contains($user_password, $char)) {
                $has_special_char = true;
                break;
            }
        }
        
        $digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
        
        foreach ($digits as $digit) {
            if (str_contains($user_password, $digit)) {
                $has_digit = true;
                break;
            }
        }
        
        if (strlen($user_password) < 8 || !$has_special_char || !$has_digit) {
            echo "Внимание! Пароль является слабым.<br>";
        }
    }