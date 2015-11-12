#!/usr/bin/env python3

import os
import json

from models import *

class PokemonContainer():
    id = 0
    name = ""
    stats = {}
    imgPath = ""

class MoveContainer():
    id = 0
    name = ""
    power = 0
    accuracy = 0
    pp = 0

def create_pokemon():

    path = "./static/json/pokemon_data_Version2.json"
    inputFile = open(path)
    data = json.loads(inputFile.read())
    inputFile.close()
    pokeList = data['pokemon']

    for poke in pokeList:
        p = PokemonContainer()
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

        pokemon = Pokemon(p.name, p.stats['HP'], p.stats['ATK'], p.stats['DEF'], p.stats['SPA'], p.stats['SPD'], p.stats['SPE'], p.imgPath)
        db.session.add(pokemon)
        db.session.commit()

def create_moves():
    path = "./static/json/moves_final.json"
    inputFile = open(path)
    data = json.loads(inputFile.read())
    inputFile.close()

    for x in data['moves']:
        m = MoveContainer()
        for key, value in x.items():
            if key == "id":
                m.id = value
            elif key == 'name':
                m.name = value
            elif key == 'power':
                m.power = value
            elif key == 'accuracy':
                m.accuracy = value
            elif key == 'pp':
                m.pp = value
        move = Move(m.name, "", "", m.power, m.accuracy, m.pp, "")
        db.session.add(move)
        db.session.commit()
        # name, type, category, power, accuracy, pp, description):


def create_db():
    db.session.commit()
    db.drop_all()
    db.create_all()
    create_pokemon()
    create_moves()