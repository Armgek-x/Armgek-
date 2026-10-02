<!--Задание 1-->
<form method="GET">
    Имя: <input type="text" name="name">
    <button type="submit">Отправить</button>
</form>

<?php
if (isset($_GET["name"]) && $_GET["name"] !== "") {
    echo "Привет, " . htmlspecialchars($_GET["name"]) . "!";
}
?>

<!--Задание 2-->

<form method="GET">
    Имя: <input type="text" name="name"><br><br>
    Город: <input type="text" name="city"><br><br>
    <button type="submit">Отправить</button>
</form>

<?php
if (!empty($_GET["name"]) && !empty($_GET["city"])) {
    echo "Имя: " . htmlspecialchars($_GET["name"]) . "<br>";
    echo "Город: " . htmlspecialchars($_GET["city"]);
}
?>

<!--Задание 3-->

<form method="GET">
    Имя: <input type="text" name="name">
    <button type="submit">Отправить</button>
</form>

<?php
$name = $_GET["name"] ?? "";

if ($name !== "") {
    echo "Здравствуйте, " . htmlspecialchars($name) . "!";
}
?>

<!--Задание 4-->

<form method="GET">
    Поиск: <input type="text" name="query">
    <button type="submit">Найти</button>
</form>

<?php
if (isset($_GET["query"])) {
    $query = trim($_GET["query"]);

    if ($query === "") {
        echo "Введите поисковый запрос";
    } else {
        echo "Вы ищете: " . htmlspecialchars($query);
    }
}
?>

<!--Задание 5-->

<form method="POST">
    Имя: <input type="text" name="name">
    <button type="submit">Отправить</button>
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = $_POST["name"] ?? "";
    echo "Привет, " . htmlspecialchars($name);
}
?>

<!--Задание 6-->

<form method="POST">
    Возраст: <input type="text" name="age">
    <button type="submit">Проверить</button>
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $age = trim($_POST["age"] ?? "");

    if ($age === "") {
        echo "Введите возраст";
    } elseif (!is_numeric($age)) {
        echo "Некорректный возраст";
    } elseif ($age < 18) {
        echo "Несовершеннолетний";
    } else {
        echo "Совершеннолетний";
    }
}
?>

<!--Задание 7-->

<form method="POST">
    Имя: <input type="text" name="name">
    <button type="submit">Отправить</button>
</form>

<?php
function validateName($name) {
    $name = trim($name);
    if ($name === "" || strlen($name) < 2) {
        return false;
    }
    return true;
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = $_POST["name"] ?? "";

    if (validateName($name)) {
        echo "Имя принято: " . htmlspecialchars($name);
    } else {
        echo "Некорректное имя (должно быть не менее 2 символов)";
    }
}
?>

<!--Задание 8-->

<form method="GET">
    Категория: <input type="text" name="category">
    <button type="submit">Проверить</button>
</form>

<?php
$categories = ["phones", "laptops", "monitors", "keyboards"];

if (isset($_GET["category"])) {
    $category = trim($_GET["category"]);

    if (in_array($category, $categories)) {
        echo "Категория найдена";
    } else {
        echo "Категория не существует";
    }
}
?>

<!--Задание 9-->

<form method="POST">
    Имя: <input type="text" name="name"><br><br>
    Возраст: <input type="text" name="age"><br><br>
    Город: <input type="text" name="city"><br><br>
    <button type="submit">Отправить</button>
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = trim($_POST["name"] ?? "");
    $age = trim($_POST["age"] ?? "");
    $city = trim($_POST["city"] ?? "");

    if ($name === "") {
        echo "Введите имя";
    } elseif ($age === "" || !is_numeric($age)) {
        echo "Некорректный возраст";
    } elseif ($city === "") {
        echo "Введите город";
    } else {
        $user = [
            "name" => $name,
            "age" => $age,
            "city" => $city
        ];

        echo "Имя: " . htmlspecialchars($user["name"]) . "<br>";
        echo "Возраст: " . htmlspecialchars($user["age"]) . "<br>";
        echo "Город: " . htmlspecialchars($user["city"]);
    }
}
?>

<!--Задание 10-->

<form method="POST">
    Имя: <input type="text" name="name"><br><br>
    Возраст: <input type="text" name="age"><br><br>
    Город: <input type="text" name="city"><br><br>
    <button type="submit">Отправить</button>
</form>

<?php
function validateName($name) {
    return trim($name) !== "";
}

function validateAge($age) {
    $age = trim($age);
    return $age !== "" && is_numeric($age) && $age > 0;
}

function validateCity($city) {
    return trim($city) !== "";
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = $_POST["name"] ?? "";
    $age = $_POST["age"] ?? "";
    $city = $_POST["city"] ?? "";

    if (!validateName($name)) {
        echo "Введите имя";
    } elseif (!validateAge($age)) {
        echo "Некорректный возраст";
    } elseif (!validateCity($city)) {
        echo "Введите город";
    } else {
        echo "Все данные успешно проверены и приняты!";
    }
}
?>

<!--Задание 11-->

<form method="POST">
    Первое число: <input type="text" name="num1"><br><br>
    Второе число: <input type="text" name="num2"><br><br>
    Операция (+, -, *, /): <input type="text" name="operation"><br><br>
    <button type="submit">Рассчитать</button>
</form>

<?php
function calculate($a, $b, $operation) {
    switch ($operation) {
        case '+':
            return $a + $b;
        case '-':
            return $a - $b;
        case '*':
            return $a * $b;
        case '/':
            if ($b == 0) {
                return "Ошибка: Деление на ноль!";
            }
            return $a / $b;
        default:
            return "Неизвестная операция";
    }
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $num1 = trim($_POST["num1"] ?? "");
    $num2 = trim($_POST["num2"] ?? "");
    $operation = trim($_POST["operation"] ?? "");

    if (!is_numeric($num1) || !is_numeric($num2)) {
        echo "Оба значения должны быть числами!";
    } else {
        $result = calculate($num1, $num2, $operation);
        echo "Результат: $num1 $operation $num2 = $result";
    }
}
?>