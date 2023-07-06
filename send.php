<?php
	
	if(isset($_GET["number"])){
  
	shell_exec("taskkill /F /IM chrome.exe");
	$command = escapeshellcmd('C:\send.py -n '.$_GET["number"] .' -m "'.urldecode($_GET["mesaj"]).'"');
	$output = shell_exec($command);
	echo $output;

  if($output == true){
    echo "OK";
  }
    
  
	
	}else{
	echo "Number is empty";
	}
