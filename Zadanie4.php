<?php

# Задание 1
$cities = ["Москва", "Санкт-Петербург", "Казань", "Сочи", "Владивосток"];

foreach($cities as $index => $citie){

    if($index !== 1 && $index !== 3){

        echo $index . ": " . $citie . "<br>";

    }
}

#Задание 2

$numbers1 = [10, 20, 30, 40];

unset($numbers1[1]);
array_unshift($numbers1, 200);
array_unshift($numbers1, 50);
array_unshift($numbers1, 60);
sort($numbers1);

foreach($numbers1 as $number){

    echo $number . "<br>";

}

#Задание 3 

$products = [
    "Ноутбук",
    "Мышь",
    "Клавиатура",
    "Монитор",
    "Наушники"
];

$count = count($products);

foreach ($products as $product) {
    
    echo "Количество предметов: " . $count;
    break; 

}

#Задание 4

$numbers2 = [12, 7, 24, 15, 8, 31, 40, 55];

foreach($numbers2 as $number2){

    if($number2 % 2 === 0){

        echo $number2 . "<br>";

    }

}

#Задание 5

$names = [
    "Иван",
    "Анна",
    "Пётр",
    "Мария",
    "Алексей"
];

foreach($names as $name){
    
    if($name === "Алексей"){

        echo "Пользователь найдем";
        break;

    }
    else{

        echo "Пользователь не найдем" . "<br>" ;
        break;
    }

}

#Задание 6

$numbers3 = [45, 12, 78, 3, 25, 9, 100];
foreach($numbers3 as $number5){

    echo  var_dump($numbers3) . "<br>";
    break;

};


$numbers4 = [45, 12, 78, 3, 25, 9, 100];

sort($numbers4);

foreach($numbers4 as $number3){

    echo $number3 . "<br>";
    break;

};

$numbers5 = [45, 12, 78, 3, 25, 9, 100];

rsort($numbers5);

foreach($numbers5 as $number4){

    echo $number4 . "<br>";


};

# Задание 7

$names1 = [
    "Иван",
    "Пётр",
    "Анна",
    "Мария"
];

array_pop($names1);
array_shift($names1);
array_unshift($names1, "Маяковский");

foreach($names1 as $name1){

    echo $name1 . "<br>";

}

# Задание 8

$user = [
    "name" => "Иван",
    "age" => 20,
    "email" => "ivan@mail.ru",
    "city" => "Москва"
];

echo "Имя: " . $user["name"] . "<br>";

echo "Возраст: " . $user["age"] . "<br>";

echo "Город: " . $user["city"] . "<br>";

$user["age"] = 21;

$user["phone"] = "+79991234567";

echo "<br>Все данные:<br>";

foreach ($user as $key => $value) {
    echo $key . ": " . $value . "<br>";
}


# Задание 9

$users = [
    [
        "name" => "Иван",
        "age" => 20
    ],
    [
        "name" => "Анна",
        "age" => 17
    ],
    [
        "name" => "Пётр",
        "age" => 25
    ],
    [
        "name" => "Мария",
        "age" => 16
    ],
    [
        "name" => "Алексей",
        "age" => 30
    ]
];

echo "Все пользователи:<br>";

foreach ($users as $user) {
    echo $user["name"] . " — " . $user["age"] . " лет<br>";
}

echo "<br>Совершеннолетние:<br>";

foreach ($users as $user) {
    if ($user["age"] >= 18) {
        echo $user["name"] . "<br>";
    }
}

echo "<br>Несовершеннолетние:<br>";

foreach ($users as $user) {
    if ($user["age"] < 18) {
        echo $user["name"] . "<br>";
    }
}

echo "<br>Количество пользователей: " . count($users);



# Задание 10

$products = [
    [
        "name" => "Ноутбук",
        "price" => 70000
    ],
    [
        "name" => "Мышь",
        "price" => 1500
    ],
    [
        "name" => "Клавиатура",
        "price" => 3000
    ],
    [
        "name" => "Монитор",
        "price" => 25000
    ]
];

echo "Все товары:<br>";

foreach ($products as $product) {
    echo $product["name"] . " — " . $product["price"] . " руб.<br>";
}

echo "<br>Товары дороже 5000:<br>";

foreach ($products as $product) {
    if ($product["price"] > 5000) {
        echo $product["name"] . "<br>";
    }
}

$total = 0;

foreach ($products as $product) {
    $total += $product["price"];
}

echo "<br>Общая стоимость: " . $total . " руб.<br>";

$expensive = $products[0];

foreach ($products as $product) {
    if ($product["price"] > $expensive["price"]) {
        $expensive = $product;
    }
}

echo "Самый дорогой товар: " . $expensive["name"] . " — " . $expensive["price"] . " руб.";