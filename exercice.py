#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    # TODO completer la  fonction
    nom_liste = str.split(nom)
    for x in range(len(nom_liste)):
        print(x)
    return nom


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
