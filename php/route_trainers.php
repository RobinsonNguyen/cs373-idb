<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));

	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS ROUTE_TRAINERS;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE ROUTE_TRAINERS(ID INT NOT NULL AUTO_INCREMENT, ROUTE_NAME VARCHAR(50) NOT NULL, ROUTE_TRAINER_NAME VARCHAR(50) NOT NULL, ROUTE_TRAINER_GEN VARCHAR(50) NOT NULL, ROUTE_TRAINER_REWARD VARCHAR(50), ROUTE_TRAINER_IMG VARCHAR(256) NOT NULL, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO ROUTE_TRAINERS(ROUTE_NAME, ROUTE_TRAINER_NAME, ROUTE_TRAINER_GEN, ROUTE_TRAINER_REWARD, ROUTE_TRAINER_IMG) VALUES(?, ?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'sssss', $name, $tname, $gen, $reward, $img);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/SomeScrapingData/FINAL_ROUTE_INFO.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['routes'] as $row){
		$name = $row['name'];
		if(!empty( $row['trainers'] )){
	    	foreach($row['trainers'] as $r){
				$tname = $r['name'];
				$gen = $r['generation'];
				$reward = $r['reward'];
				$img = "SomeScrapingData/TrainerSprites/" . $r['trainerSprite'];

				//inserting the mothafuckin row bitch
				mysqli_stmt_execute($st);
			}
		}
	}

	//close connection
	mysqli_close($con);
?>