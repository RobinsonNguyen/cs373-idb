<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));

	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS POKEMON_LOCATIONS;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE POKEMON_LOCATIONS(ID INT NOT NULL AUTO_INCREMENT, POKEMON_ID INT NOT NULL, POKEMON_NAME VARCHAR(50) NOT NULL, POKEMON_GAME VARCHAR(50) NOT NULL, POKEMON_METHOD VARCHAR(50) NOT NULL, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO POKEMON_LOCATIONS(POKEMON_ID, POKEMON_NAME, POKEMON_GAME, POKEMON_METHOD) VALUES(?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'isss', $id, $name, $gname, $method);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/static/json/pokemon_data_Version2.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['pokemon'] as $row){
		$id = $row['national_id'];
		$name = $row['name'];
    	foreach($row['locations'] as $r){
			$gname = $r['game'];
			$method = $r['method'];

			//inserting the mothafuckin row bitch
			mysqli_stmt_execute($st);
		}
	}

	//close connection
	mysqli_close($con);
?>