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

GP_RESPONSE_NO_ADDRESS = [
    "Oula, tu m'en demandes trop ! Réessaye avec une autre adresse.",
    "Hmm, je ne trouve aucune correspondance. Formule autrement ta requête."

]

GP_RESPONSE_WIKIPEDIA = [
    "Le savais-tu ?",
    "Voici une petite anecdote !",
    "Incroyable, nest-ce pas ?!",
    "A mon âge, se souvenir de ça !"
]