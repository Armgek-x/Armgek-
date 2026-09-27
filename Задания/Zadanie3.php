<?php

$arrey = [

    "Name" => "Alex",
    "Age" => 18,
    "Password" => 12345678,  

];

$arrey2 = ['a'-'z', 'A'-'Z', '0-9', '!', '@', '#', '$'];

$status = "Name" === "Alex"? "Да" : "Нет";
$status2 = "Age" >= 18? "Да" : "Нет";

if($status == "Да"){

    echo "Логин совпадает, вы проходите";

}
else{

    echo "вам доступ закрыт";

};


if ($status2 == "Да"){

    echo "вам доступ открыт";

}
else{

    echo "вам доступ закрыт";

};

$password = (string)$arrey["Password"];
$isValidPassword = true;

// Превращаем пароль в массив отдельных символов и проверяем каждый
$passwordChars = str_split($password);

foreach ($passwordChars as $char) {
    $charFound = false;
    
    // Проверяем, содержится ли символ среди допустимых в $arrey2
    foreach ($arrey2 as $allowedSymbol) {
        if (str_contains($char, (string)$allowedSymbol)) {
            $charFound = true;
            break;
        }
    }
    
    // Если хотя бы один символ не найден в разрешенном списке
    if (!$charFound) {
        $isValidPassword = false;
        break;
    }
}

// Итоговый вывод по паролю
if ($isValidPassword && strlen($password) > 0) {
    echo "Пароль содержит только допустимые символы. Доступ разрешен!";
} 
else {
    echo "Ошибка: пароль содержит недопустимые символы.";
}


