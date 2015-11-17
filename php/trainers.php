<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));

	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS ALL_TRAINERS;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE ALL_TRAINERS(ID INT NOT NULL AUTO_INCREMENT, TRAINER_NAME VARCHAR(50) NOT NULL, TRAINER_GEN VARCHAR(50) NOT NULL, TRAINER_ROUTE_NAME VARCHAR(50) NOT NULL, TRAINER_POKEMON VARCHAR(50), TRAINER_LEVEL VARCHAR(50) NOT NULL, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO ALL_TRAINERS(TRAINER_NAME, TRAINER_GEN, TRAINER_ROUTE_NAME, TRAINER_POKEMON, TRAINER_LEVEL) VALUES(?, ?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'sssss', $tname, $rname, $gen, $pokemon, $level);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/SomeScrapingData/FINAL_ROUTE_INFO.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['routes'] as $row){
		$rname = $row['name'];
		if(!empty( $row['trainers'] )){
	    	foreach($row['trainers'] as $r){

				$tname = $r['name'];
				$gen = $r['generation'];

				foreach($r['pokemon'] as $p){
					$pokemon = $p['name'];
					$level = $p['level'];

					//inserting the mothafuckin row bitch
					mysqli_stmt_execute($st);
				}
			}
		}
	}

	//close connection
	mysqli_close($con);
?>