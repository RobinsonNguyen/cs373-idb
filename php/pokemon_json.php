<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));
	$con->set_charset('utf8');
	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS ALL_POKEMON;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE ALL_POKEMON(POKEMON_ID INT NOT NULL, POKEMON_NAME VARCHAR(50) NOT NULL, POKEMON_HP INT NOT NULL, POKEMON_ATK INT NOT NULL, POKEMON_DEF INT NOT NULL, POKEMON_SPATK INT NOT NULL, POKEMON_SPDEF INT NOT NULL, POKEMON_SPD INT NOT NULL, POKEMON_HEIGHT INT, POKEMON_WEIGHT INT, POKEMON_EV VARCHAR(250), POKEMON_IMG VARCHAR(256) NOT NULL, PRIMARY KEY(POKEMON_ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO ALL_POKEMON(POKEMON_ID, POKEMON_NAME, POKEMON_HP, POKEMON_ATK, POKEMON_DEF, POKEMON_SPATK, POKEMON_SPDEF, POKEMON_SPD, POKEMON_HEIGHT, POKEMON_WEIGHT, POKEMON_EV, POKEMON_IMG) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'isiiiiiiiiss', $id, $name, $hp, $attack, $defense, $spatk, $spdef, $spd, $height, $weight, $ev, $img);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/static/json/pokemon_data_Version2.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['pokemon'] as $row){
		$id = $row['national_id'];
		$name = $row['name'];
		$hp = $row['hp'];
		$attack = $row['attack'];
		$defense = $row['defense'];
		$spatk = $row['sp_atk'];
		$spdef = $row['sp_def'];
		$spd = $row['speed'];
		$height = $row['height'];
		$weight = $row['weight'];
		$ev = "";
		foreach($row['ev_yield'] as $key => $item){
			$ev = $item . " ";
	    }
		$img = $row['name'] . "_regular_.png";

		//inserting the mothafuckin row bitch
		mysqli_stmt_execute($st);
	}

	//close connection
	mysqli_close($con);
?>