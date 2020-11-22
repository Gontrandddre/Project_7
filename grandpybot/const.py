#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stop_words import get_stop_words

STOP_WORDS = get_stop_words("fr")
NO_CHARS_LIST = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", ";", ":", ",", ".", "/", "<", ">", "?", "|", "`", "~", "-", "=", "_", "+", "&", "'", "§", "°", "^", "¨", "%", "`", "£", "-", "_"]
GG_APP_ID = "AIzaSyAQzwNornfEf_OqT0rjyV9AzDri_mkaV78"


GP_RESPONSE_ADDRESS = [
    "Très bien ! Nous allons de ce côté: ",
    "Allez, je vous donne l'adresse complète: ",
    "Voyons voir ce que l'on trouve à cette adresse: ",
    "Allez ! je t'enmène à ce lieu: "
]

GP_RESPONSE_NO_INPUT = [
    "Apparemment tu n'es pas très bavarre... Savais-tu que la vile d'Y a le nom de ville le plus court de France ?",
    "Tu ne m'as rien demandé... Sais-tu que les deux plus vieilles villes de France seraient Marseille et Béziers, bâties toutes deux par les Grecs au VIe siècle avant J.-C. ?",
    "Ne sois pas timide! Savais-tu que la France est le plus grand pays européen en termes de superficie après la Russie et l'Ukraine."
]

GP_RESPONSE_NO_ADDRESS = [
    "Oula, tu m'en demandes trop ! Réessaye avec une autre adresse.",
    "Hmm, je ne trouve aucune correspondance. Formule autrement ta requête.",
    "Mon esprit me fait défaut. Reformule moi ça que je te trouve quelque chose !"
]

GP_RESPONSE_WIKIPEDIA = [
    "Le savais-tu ?",
    "Voici une petite anecdote ! ",
    "Incroyable, n'est-ce pas ?! ",
    "A mon âge, se souvenir de ça ! "
]