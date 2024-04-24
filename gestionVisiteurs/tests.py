from django.test import TestCase, RequestFactory
from django.contrib.messages.storage.fallback import FallbackStorage
from django.utils import timezone

from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Utilisateur, Rapport  # Assurez-vous d'importer vos modèles
from .views import v_rapports

class VotreVueTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        # Créez un utilisateur de test pour simuler une session utilisateur
        self.utilisateur = Utilisateur.objects.create(
            nom="Test",
            prenom="Utilisateur",
            date_embauche=timezone.now()  # Fournissez une valeur pour date_embauche
        )
        self.utilisateur_id = self.utilisateur.id

        def test_v_rapports_post(self):
    # Créez une demande POST pour la vue avec les données du formulaire
            data = {'medecin': 'Test'}
            request = self.factory.post(reverse('v_rapports'), data)
            request.session = {'utilisateur_id': self.utilisateur_id}
            setattr(request, '_messages', FallbackStorage(request))
            response = v_rapports(request)
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('v_afficheMesRapports'))

    # Vérifiez si un message d'erreur est ajouté
            messages = list(get_messages(request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(messages[0].tags, "error")
            self.assertEqual(messages[0].message, "Il y a des erreurs dans le formulaire. Veuillez corriger les erreurs et réessayer.")
    def test_v_rapports_get(self):
        # Créez une demande GET pour la vue
        request = self.factory.get(reverse('v_rapports'))
        request.session = {'utilisateur_id': self.utilisateur_id}

        response = v_rapports(request)

        # Assurez-vous que la réponse contient le formulaire
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')
