<?php

require '../C/param_connexion_BdD.php';

class DemandeLocation {
    protected $ID_demande;
    protected $num_dem;
    protected $num_apart;
    protected $Statut_demande;

    public function __construct($num_dem, $num_apart) {
        $this->num_dem = $num_dem;
        $this->num_apart = $num_apart;
        $this->Statut_demande = 'En attente'; // Par défaut, le statut est en attente
    }

    public function enregistrerDemandeLocation() {
        global $conn;

        try {
            // Vérifie si une demande de location existe déjà pour ce demandeur et cet appartement
            $sql_check = "SELECT COUNT(*) FROM demandes 
                          WHERE num_dem = :num_dem
                          AND num_apart = :num_apart";
                          
            $stmt_check = $conn->prepare($sql_check);
            $stmt_check->bindParam(':num_dem', $this->num_dem);
            $stmt_check->bindParam(':num_apart', $this->num_apart);
           
            $stmt_check->execute();
            $existing_demandes = $stmt_check->fetchColumn();

            if ($existing_demandes > 0) {
                // Une demande existe déjà, retournez un message d'erreur
                return "Vous avez déjà une demande en attente pour cet appartement.";
            } else {
                // Aucune demande existante, procédez à l'insertion
                $sql = "INSERT INTO demandes (num_dem, num_apart, Statut_demande) 
                        VALUES (:num_dem, :num_apart, :Statut_demande)";
                $stmt = $conn->prepare($sql);
                $stmt->bindParam(':num_dem', $this->num_dem);
                $stmt->bindParam(':num_apart', $this->num_apart);
                $stmt->bindParam(':Statut_demande', $this->Statut_demande);
                $stmt->execute();

                return "Demande de location enregistrée avec succès!";
            }
        } catch (PDOException $e) {
            // Gérer les erreurs de base de données
            error_log('Erreur lors de l\'enregistrement de la demande de location : ' . $e->getMessage());
            return "Erreur lors de l'enregistrement de la demande de location : " . $e->getMessage();
        }
    }

    // Méthode pour récupérer les demandes de location d'un demandeur spécifique
    public static function getDemandesLocationDemandeur($num_dem) {
        global $conn;

        try {
            $sql = "SELECT * FROM demandes
            WHERE num_dem = :num_dem AND num_apart NOT IN (SELECT num_apart FROM locataire);
            ";
            
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':num_dem', $num_dem);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

            return $result;
        } catch (PDOException $e) {
            // Gérer les erreurs de base de données
            error_log('Erreur lors de la récupération des demandes de location du demandeur : ' . $e->getMessage());
            return array();
        }
    }

    public static function getDemandesProprietaire($num_prop) {
        global $conn;
    
        try {
            $sql = "SELECT * FROM demandes WHERE num_apart IN (SELECT num_apart FROM appartement WHERE num_prop = :num_prop) AND Statut_demande = 'en attente'";
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':num_prop', $num_prop);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
            return $result;
        } catch (PDOException $e) {
            error_log('Erreur lors de la récupération des demandes pour le propriétaire : ' . $e->getMessage());
            return array();
        }
    }
    
    public function refuserDemande($ID_demande) {
        global $conn;

        try {
            // Préparer et exécuter la requête SQL pour mettre à jour le statut de la demande à "Refusée"
            $sql_update = "UPDATE demandes SET Statut_demande = 'Refusée' WHERE ID_demande = :ID_demande ";
            $stmt = $conn->prepare($sql_update);
            $stmt->bindParam(':ID_demande', $ID_demande);
            $stmt->execute();

            // Retourner un message de succès ou gérer d'autres actions après avoir refusé la demande
            return "Demande refusée avec succès!";
        } catch (PDOException $e) {
            // Gérer les erreurs de base de données
            error_log('Erreur lors du refus de la demande : ' . $e->getMessage());
            return "Erreur lors du refus de la demande : " . $e->getMessage();
        }
    }
    public function accepterDemande($ID_demande) {
        global $conn;
    
        try {
            // Préparer et exécuter la requête SQL pour mettre à jour le statut de la demande à "Acceptée"
            $sql_update = "UPDATE demandes SET Statut_demande = 'Acceptée' WHERE ID_demande = :ID_demande ";
            $stmt = $conn->prepare($sql_update);
            $stmt->bindParam(':ID_demande', $ID_demande);
            $stmt->execute();
    
            // Retourner un message de succès ou gérer d'autres actions après avoir accepté la demande
            return "Demande acceptée avec succès!";
        } catch (PDOException $e) {
            // Gérer les erreurs de base de données
            error_log('Erreur lors de l\'acceptation de la demande : ' . $e->getMessage());
            return "Erreur lors de l'acceptation de la demande : " . $e->getMessage();
        }
    }
    public static function getAppartementsLouesProprietaire($num_prop) {
        global $conn;
    
        try {
            $sql = "SELECT a.* 
                    FROM appartement a
                    JOIN demandes d ON a.num_apart = d.num_apart
                    WHERE d.Statut_demande = 'Acceptée' AND a.num_prop = :num_prop";
    
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':num_prop', $num_prop);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
            return $result;
        } catch (PDOException $e) {
            error_log('Erreur lors de la récupération des appartements loués pour le propriétaire : ' . $e->getMessage());
            return array();
        }
    }
    public static function getDemandesProprietaireLouer($num_prop) {
        global $conn;
    
        try {
            $sql = "SELECT d.*, a.* 
            FROM locataire d
            JOIN appartement a ON d.num_apart = a.num_apart
            WHERE a.num_prop = :num_prop";
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':num_prop', $num_prop);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
            return $result;
        } catch (PDOException $e) {
            error_log('Erreur lors de la récupération des demandes pour le propriétaire : ' . $e->getMessage());
            return array();
        }
    }
    public static function getTotalMensuelProprietaire($num_prop) {
        global $conn;
    
        try {
            $sql = "SELECT SUM(a.prix_loc + a.prix_charges) AS total_mensuel
            FROM appartement a
            JOIN locataire d ON a.num_apart = d.num_apart
            WHERE a.num_prop = :num_prop ";
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':num_prop', $num_prop);
            $stmt->execute();
            $total_mensuel = $stmt->fetchColumn();
    
            return $total_mensuel;
        } catch (PDOException $e) {
            error_log('Erreur lors de la récupération du total mensuel pour le propriétaire : ' . $e->getMessage());
            return 0; // Retourne 0 en cas d'erreur
        }
    }
    public static function getTotauxMensuelsParAppartement($num_prop) {
        global $conn;
    
        try {
            $sql = "SELECT (a.prix_loc + a.prix_charges) AS total_mensuel
                    FROM appartement a
                    JOIN demandes d ON a.num_apart = d.num_apart
                    WHERE a.num_prop = :num_prop AND d.Statut_demande = 'Acceptée'";
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':num_prop', $num_prop);
            $stmt->execute();
            $result = $stmt->fetchColumn();
    
            return $result;
        } catch (PDOException $e) {
            error_log('Erreur lors de la récupération des totaux mensuels par appartement pour le propriétaire : ' . $e->getMessage());
            return null; // Ou une valeur par défaut, selon votre cas d'utilisation.
        }
    }
    
    
}
?>
