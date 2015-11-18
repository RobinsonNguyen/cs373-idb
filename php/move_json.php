<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));
	$con->set_charset('utf8');
	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS ALL_MOVES;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE ALL_MOVES(MOVE_ID INT, MOVE_NAME VARCHAR(50) NOT NULL, MOVE_TYPE VARCHAR(50), MOVE_CATEGORY VARCHAR(50), MOVE_POWER INT, MOVE_ACCURACY INT, MOVE_PP INT, MOVE_DESCRIPTION TEXT, PRIMARY KEY(MOVE_ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO ALL_MOVES(MOVE_ID, MOVE_NAME, MOVE_TYPE, MOVE_CATEGORY, MOVE_POWER, MOVE_ACCURACY, MOVE_PP, MOVE_DESCRIPTION) VALUES(?, ?, ?, ?, ?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'isssiiis', $id, $name, $type, $category, $power, $accuracy, $pp, $description);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/static/json/moves_final_for_php.json');
    $move_table = json_decode($jsondata,true);

    //get move details
    foreach ($move_table as $row){
    	$id = $row['id'];
		$name = $row['name'];
		$type = $row['type'];
		$category = $row['category'];
		$power = $row['power'];
		$accuracy = $row['accuracy'];
		$pp = $row['pp'];
		$description = $row['description'];

		//inserting the mothafuckin row bitch
		mysqli_stmt_execute($st);
	}

	//close connection
	mysqli_close($con);
?>