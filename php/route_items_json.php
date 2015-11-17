<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));
	$con->set_charset('utf8');
	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS ROUTE_ITEMS;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE ROUTE_ITEMS(ID INT NOT NULL AUTO_INCREMENT, ROUTE_NAME VARCHAR(50) NOT NULL, ROUTE_ITEM_NAME VARCHAR(50) NOT NULL, ROUTE_ITEM_IMG VARCHAR(256) NOT NULL, ROUTE_ITEM_GAMES VARCHAR(256) NOT NULL, ROUTE_ITEM_METHOD VARCHAR(50000) NOT NULL, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO ROUTE_ITEMS(ROUTE_NAME, ROUTE_ITEM_NAME, ROUTE_ITEM_IMG, ROUTE_ITEM_GAMES, ROUTE_ITEM_METHOD) VALUES(?, ?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'sssss', $name, $iname, $img, $method, $games);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/SomeScrapingData/FINAL_ROUTE_INFO.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['routes'] as $row){
		$name = $row['name'];
    	foreach($row['items'] as $r){
			$iname = $r['name'];
			$img = $r['item sprite'];
			$method = $r['item method'];
			$games = $r['item games'];

			//inserting the mothafuckin row bitch
			mysqli_stmt_execute($st);
		}
	}

	//close connection
	mysqli_close($con);
?>