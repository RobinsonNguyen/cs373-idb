#!/usr/bin/env python3

import os
import json

from models import *

def create_pokemon():

    path = "./static/json/pokemon_data_Version2.json"
    inputFile = open(path)
    data = json.loads(inputFile.read())
    inputFile.close()
    pokeList = data['pokemon']

    for poke in pokeList:
        p = object()
        p.stats = {}
        for key, value in poke.items():
            if key == 'pkdx_id':
                p.id = value
            if key == 'name':
                p.name = value
                p.imgPath = value + '_regular_.png'
            if key == 'hp':
                p.stats['HP'] = value
            if key == 'attack':
                p.stats['ATK'] = value
            if key == 'defense':
                p.stats['DEF'] = value
            if key == 'sp_atk':
                p.stats['SPA'] = value
            if key == 'sp_def':
                p.stats['SPD'] = value
            if key == 'speed':
                p.stats['SPE'] = value
            if key == 'types':
                types = []
                for t in value:
                    for k, v in t.items():
                        if k == 'name':
                            types.append(v)
                p.type = types
            if key == 'egg_groups':
                egg_groups = []
                for e in value:
                    for k, v in e.items():
                        if k == 'name':
                            egg_groups.append(v)
                p.eggGroup = egg_groups

        pokemon = Pokemon(p.name, p.stats['HP'], p.stats['ATK'], p.stats['DEF'], p.stats['SPA'], p.stats['SPD'], p.stats['SPE'])
        db.session.add(character)
        db.session.commit()


def create_db():
    db.session.commit()
    db.drop_all()
    db.create_all()
    create_pokemon()