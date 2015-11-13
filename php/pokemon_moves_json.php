<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));
	$con->set_charset('utf8');
	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS POKEMON_MOVES;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE POKEMON_MOVES(ID INT NOT NULL AUTO_INCREMENT, POKEMON_ID INT NOT NULL, POKEMON_NAME VARCHAR(50) NOT NULL, POKEMON_MOVE VARCHAR(50) NOT NULL, POKEMON_LEARN_TYPE VARCHAR(50) NOT NULL, POKEMON_LEVEL_LEARNED INT, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO POKEMON_MOVES(POKEMON_ID, POKEMON_NAME, POKEMON_MOVE, POKEMON_LEARN_TYPE, POKEMON_LEVEL_LEARNED) VALUES(?, ?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'isssi', $id, $name, $mname, $learn, $level);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/static/json/pokemon_data_Version2.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['pokemon'] as $row){
		$id = $row['national_id'];
		$name = $row['name'];
    	foreach($row['moves'] as $r){
			$mname = $r['name'];
			$learn = $r['learn_type'];
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