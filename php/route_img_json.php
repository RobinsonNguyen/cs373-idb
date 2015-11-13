<?php
	//connect to mysql
	$con = mysqli_connect("localhost","root","pokemon","pokemasters") or die('Could not connect: ' . mysqli_error($con));
	$con->set_charset('utf8');
	$drop = mysqli_prepare($con, 'DROP TABLE IF EXISTS ROUTE_IMGS;') or die(mysqli_error($con));

	$create = mysqli_prepare($con, 'CREATE TABLE ROUTE_IMGS(ID INT NOT NULL AUTO_INCREMENT, ROUTE_NAME VARCHAR(50) NOT NULL, ROUTE_GEN VARCHAR(50) NOT NULL, ROUTE_IMG VARCHAR(256) NOT NULL, PRIMARY KEY(ID));') or die(mysqli_error($con));

    mysqli_stmt_execute($drop) or die(mysqli_error($con));
    mysqli_stmt_execute($create) or die(mysqli_error($con));

    $st = mysqli_prepare($con, 'INSERT INTO ROUTE_IMGS(ROUTE_NAME, ROUTE_GEN, ROUTE_IMG) VALUES(?, ?, ?)') or die(mysqli_error($con));

    mysqli_stmt_bind_param($st, 'sss', $name, $gen, $img);

    //read the json file contents
    $jsondata = file_get_contents('/home/www/cs373-idb/SomeScrapingData/FINAL_ROUTE_INFO.json');
    $json = json_decode($jsondata,true);

    //get pokemon details
    foreach ($json['routes'] as $row){
		$name = $row['name'];
    	foreach($row['routeImg'] as $r){
			$gen = $r['gen'];
			$img = "SomeScrapingData/RouteIMGS/" . $r['imgName'];

			//inserting the mothafuckin row bitch
			mysqli_stmt_execute($st);
		}
	}

	//close connection
	mysqli_close($con);
?>