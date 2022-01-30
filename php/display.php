<?php
$url=$_SERVER['REQUEST_URI'];
header("Refresh: 1; URL=$url");
?>
<html>
  <head>
    <title>Arduino Database ClarkSul</title>
     <style type="text/css">
    	.table_titles {
          margin-left: auto;
          margin-right: auto;
  	  font-size: 20px;
  	  color: #000;
	  text-align: center;
	 
	}
	img{
	  display: inline-block;
	  padding: 10px;
	}

	.crop{ 
	  padding: 35px 0 35px 260px;
	  margin: -35px 0 -30px -50px;
	}

	.table_titles {
          margin-left: auto;
          margin-right: auto;
  	  color: #000;
  	  background-color: #FF6400;
  	}
        table {
          margin-left: auto;
          margin-right: auto;
  	  border: 5px solid #333;
 	}
        body { font-family: "Trebuchet MS", Courier;>}
      </style>
    </head>
  <body style="background-color:darkgray";>
  <img src="selo.png" style="width:8%"  style="float:left" align="top">
  <img src="name.png" style="width:50%" class="crop">
  <b><font size="5" face="Helvetica"></b>
  <b><table border="1" cellspacing="0" cellpadding="4" bgcolor="white" width="60%"></b>
  <tr>
  <td class="table_titles">Técnico</td>
  <td class="table_titles">OS</td>
  <td class="table_titles">Função</td>
  <td class="table_titles">Hora</td>
  <td class="table_titles">(current time)Timer</td>
  </tr>
  <?php
  include('connection.php');
  $result = mysqli_query($con,'SELECT * FROM tabela ORDER BY id DESC');

  $oddrow = true;
  while($row = mysqli_fetch_array($result)){
  if ($oddrow){
    $css_class=' class="table_cells_odd", style="text-align:center"';
  }
  else{
    $css_class=' class="table_cells_even", style="text-align:center"';
  }
  $oddrow = !$oddrow; 

  $funcao = array(
    0 => 'Check-in',
    1 => 'Higienização Ext.',
    2 => 'Desmontagem',
    3 => 'Lista de Peça',
    4 => 'Serviço',
    5 => 'Separação de Peça',
    6 => 'Higienização Peça',
    7 => 'Desmontagem',
    8 => 'Teste',
    9 => 'Check-out',
    "999" => 'Finalizou',
  );

  $funcionarios = array(
    60 => 'Alex',
    69 => 'Francisco',
  ); 
  date_default_timezone_set('America/Sao_Paulo');
  $time_now = date("H:i", strtotime("now"));
  echo "<tr>";
  echo "<td '.$css_class.'>" , "<b>" . $funcionarios[$row['cracha']] . "</b>", "</td>";
  echo "<td '.$css_class.'>" , "<b>" . $row['OS1'], "", $row['OS2'],"", $row['OS3'],"", $row['OS4'] . "</b>", "</td>";
  echo "<td '.$css_class.'>" , "<b>" . $funcao[$row['funcao']] .  "</b>", "</td>";
  echo "<td '.$css_class.'>" , "<b>" . date("H:i", strtotime($row['event'])) . "</b>", "</td>";
  echo "<td '.$css_class.'>" , "<b>" . $time_now . "</b>", "</td>";
  echo "</tr>";
  }
 
 mysqli_close($con);
 ?>
    </table>
   </font>
  </body>
</html>