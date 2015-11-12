<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));

	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS POKEMON_ABILITIES;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE POKEMON_ABILITIES(ID INT NOT NULL AUTO_INCREMENT, POKEMON_ID INT NOT NULL, POKEMON_NAME VARCHAR(50) NOT NULL, POKEMON_ABILITY VARCHAR(50) NOT NULL, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO POKEMON_ABILITIES(POKEMON_ID, POKEMON_NAME, POKEMON_ABILITY) VALUES(?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'iss', $id, $name, $aname);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/static/json/pokemon_data_Version2.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['pokemon'] as $row){
		$id = $row['national_id'];
		$name = $row['name'];
    	foreach($row['abilities'] as $r){
			$aname = $r['name'];

			//inserting the mothafuckin row bitch
			mysqli_stmt_execute($st);
		}
	}

	//close connection
	mysqli_close($con);
?>