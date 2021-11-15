<?php


try {
    $client = new MongoDB\Client('mongodb+srv://admin:admin@cluster0.amhl4.mongodb.net/site?retryWrites=true&w=majority');
    $db = $client->test;
    echo "SUcces ";
}
catch (Throwable $e){
    echo "Captured Throwable: for insert : " . $e->getMessage() . PHP_EOL;
}
