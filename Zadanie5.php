<?php

#Задание 1

function sayHello(){

    echo "Привет! Добро пожаловать!";
 
}

sayHello();
sayHello();
sayHello();

#Задание 2

$name = {"Ivan, Alexander, Yaroslav"};

function sayHello2($name){

    echo $name;
 
}

sayHello2("Yaroslav");

#Задние 3

function sum($a, $b){

    return $a + $b; 
 
}

$result = sum(10, 20);

echo $result;

# Задание 4

function isEven($number){

    if($number % 2 === 0){

        return true;

    }

    return false;

}

if (isEven(10)){

    echo "Число четное";

}

#Задание 5

function checkAge($age){

    if ($age >= 18){

        return "Совершеннолетний";

    }
    else{

        return "Несовершеннолетний";

    }

}

echo checkAge(20);
echo checkAge(15);

#Задание 6

function findMax($a, $b){

    if($a > $b){

        return "$a больше $b";

    }
    else{

        return "$b больше $b";

    }

}

echo findMax(10, 20);

#Задание 7

function sayHello3($name2 = "Гость"){

    return "Привет, " . $name2;

}

sayHello3("Alexander");

#Задание 8

function calculateDisconect($prise, $discount) {
    return $prise - ($prise * $discount / 100);
}
function checkPrice($prise) {
    if ($prise <= 0) {
        return false;
    }
    return true
}

$prise = 5000;
$discount = 10;

if (checkPrice($prise)) {
    $result1 = calculateDisconect($prise, $discount);

    echo "Цена сщ скидкой: " ю $result1;
}

#Заданние 9

function checkPassword($password){

    $itog = strlen($password);
    if($itog >= 8){

        return "Пароль подходит";

    }
    else{

        return "Сабый пароль";

    }

}

checkPassword($itog);

#Задание 10

function calculateDisconect($a, $b, $operation){

    switch($operation){

        case addition:
            return $a + $b;
            break;
        case subtraction:
            return $a - $b;
            break;
        case multiplication:
            return $a * $b;
            break;
        case division:
            return $a / $b;
            break;
        default: 
            echo "ошибка";

    }

}

#Задание 11



