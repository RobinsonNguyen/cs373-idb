<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));
	$con->set_charset('utf8');
	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS ALL_ROUTES;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE ALL_ROUTES(ID INT NOT NULL AUTO_INCREMENT, ROUTE_NAME VARCHAR(50) NOT NULL, ROUTE_REGION VARCHAR(50) NOT NULL, ROUTE_NORTH_EXIT VARCHAR(50), ROUTE_SOUTH_EXIT VARCHAR(50), ROUTE_EAST_EXIT VARCHAR(50), ROUTE_WEST_EXIT VARCHAR(50), ROUTE_ACCESS_TO VARCHAR(50), ROUTE_MINI_DESCRIPTION VARCHAR(256), ROUTE_MAIN_DESCRIPTION TEXT, ROUTE_TRIVIA TEXT, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO ALL_ROUTES(ROUTE_NAME, ROUTE_REGION, ROUTE_NORTH_EXIT, ROUTE_SOUTH_EXIT, ROUTE_EAST_EXIT, ROUTE_WEST_EXIT, ROUTE_ACCESS_TO, ROUTE_MINI_DESCRIPTION, ROUTE_MAIN_DESCRIPTION, ROUTE_TRIVIA) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'ssssssssss', $route_name, $region_name, $nexit, $sexit, $eexit, $wexit, $accessto, $mindesc, $maindesc, $trivia);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/SomeScrapingData/FINAL_ROUTE_INFO.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['routes'] as $row){
		$route_name = $row['name'];
		$region_name = $row['region'];
    	foreach($row['NorthExit'] as $key => $item){
			$nexit = $item . " ";
	    }
	    foreach($row['SouthExit'] as $key => $item){
			$sexit = $item . " ";
	    }
	    foreach($row['EastExit'] as $key => $item){
			$eexit = $item . " ";
	    }
	    foreach($row['WestExit'] as $key => $item){
			$wexit = $item . " ";
	    }
	    foreach($row['AccessTo'] as $key => $item){
			$accessto = $item . " ";
	    }
		$mindesc = $row['routeMiniDesc'];
		$maindesc = $row['routeMainDesc'];
		$trivia = $row['routeTrivia'];

		//inserting the mothafuckin row bitch
		mysqli_stmt_execute($st);
	}

	//close connection
	mysqli_close($con);
?>