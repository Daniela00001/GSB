<?php

require '../M/Class Proprietaire.php';
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['deconnexion'])) {
        session_destroy();
        header("Location: ../V/v_connexion_proprietaire.php");
        exit();
    } else {
        $login = $_POST["login"];
        $mdp_prop = $_POST["mdp_prop"];

        $proprietaire = new Proprietaire();
        $result = $proprietaire->verifierProprietaire($login, $mdp_prop);

        if ($result) {
            $_SESSION["proprietaire"] = $result;
            header("Location: ../V/v_home_propietaire.php");
            exit();
        } else {
            $message = "Identifiants incorrects. Veuillez réessayer.";
            echo $message; // Ajoutez ceci pour voir le message d'erreur
        }
    }
}

// Si la méthode n'est pas POST, vous pouvez ajouter d'autres logiques ici si nécessaire.

?>
