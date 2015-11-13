<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));
	$con->set_charset('utf8');
	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS POKEMON_EVOLUTIONS;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE POKEMON_EVOLUTIONS(ID INT NOT NULL AUTO_INCREMENT, POKEMON_ID INT NOT NULL, POKEMON_NAME VARCHAR(50) NOT NULL, POKEMON_EVOLUTION VARCHAR(50) NOT NULL, POKEMON_EVOLVE_METHOD VARCHAR(50) NOT NULL, POKEMON_EVOLVE_LEVEL INT, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO POKEMON_EVOLUTIONS(POKEMON_ID, POKEMON_NAME, POKEMON_EVOLUTION, POKEMON_EVOLVE_METHOD, POKEMON_EVOLVE_LEVEL) VALUES(?, ?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'isssi', $id, $name, $ename, $method, $level);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/static/json/pokemon_data_Version2.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['pokemon'] as $row){
		$id = $row['national_id'];
		$name = $row['name'];
    	foreach($row['evolutions'] as $r){
			$ename = $r['to'];
			$method = $r['method'];
			if (array_key_exists('level', $r)){
				$level = $r['level'];
			}

			//inserting the mothafuckin row bitch
			mysqli_stmt_execute($st);
		}
	}

	//close connection
	mysqli_close($con);
?>