<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));

	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS ROUTE_POKEMON;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE ROUTE_POKEMON(ID INT NOT NULL AUTO_INCREMENT, ROUTE_NAME VARCHAR(50) NOT NULL, ROUTE_POKEMON_NAME VARCHAR(50) NOT NULL, ROUTE_POKEMON_GEN VARCHAR(50) NOT NULL, ROUTE_POKEMON_LEVELS VARCHAR(50), ROUTE_POKEMON_RATE VARCHAR(50), ROUTE_POKEMON_METHOD VARCHAR(50) NOT NULL, ROUTE_METHOD_IMG VARCHAR(256) NOT NULL, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO ROUTE_POKEMON(ROUTE_NAME, ROUTE_POKEMON_NAME, ROUTE_POKEMON_GEN, ROUTE_POKEMON_LEVELS, ROUTE_POKEMON_RATE, ROUTE_POKEMON_METHOD, ROUTE_METHOD_IMG) VALUES(?, ?, ?, ?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'sssssss', $name, $pname, $gen, $levels, $rate, $method, $img);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/SomeScrapingData/FINAL_ROUTE_INFO.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['routes'] as $row){
		$name = $row['name'];
		if (!empty( $row['wildPokemon'] )){
	    	foreach ($row['wildPokemon'] as $r){

				$pname = $r['name'];
				$gen = $r['generation'];
				$levels = $r['levels'];

				if (count( $r['rate'] ) == 3){

					for ($i = 0; $i < 3; $i++){
						if ($i == 0){
							$rate = "Morning: " . $r['rate'][$i];
						}
						elseif ($i == 1){
							$rate = "Day: " . $r['rate'][$i];
						}
						elseif ($i == 2){
							$rate = "Night: " . $r['rate'][$i];
						}
					}
				}

				elseif (count( $r['rate'] ) == 1){
					$rate = "At all times: " . $r['rate'][0];
				}

				$method = (string)$r['method'];
				print("$method");
				$img = $r['methodSprite'];

				//inserting the mothafuckin row bitch
				mysqli_stmt_execute($st);
			}
		}
	}

	//close connection
	mysqli_close($con);
?>
