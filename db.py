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
            if key == 'moves':
                moves = []
                for m in value:
                    move = self.Move()
                    for k, v in m.items():
                        if k == 'name':
                            move.name = v
                        if k == 'learn_type':
                            move.learn_type = v
                        if k == 'level':
                            move.level = v
                    moves.append(move)
                p.moves = moves
            if key == 'locations':
                locations = []
                for l in value:
                    location = self.Location()
                    for k, v in l.items():
                        if k == 'game':
                            location.game = v
                        if k == 'method':
                            methods = v.split(',')
                            routes = []
                            others = []
                            for m in methods:
                                if "Route" in m:
                                    routes.append(m)
                                else:
                                    others.append(m)
                            location.other = others
                            location.routes = routes
                    locations.append(location)
                p.locations = locations
            if key == 'evolutions':
                evolution = []
                for e in value:
                    evo = self.Evolution()
                    for k, v in e.items():
                        if k == 'method':
                            if v == 'level_up':
                                evo.method = 'Level Up'
                            if v == 'trade':
                                evo.method = 'Trade'
                            if v == 'stone':
                                evo.method = 'Stone'
                        if k == 'to':
                            evo.to = v
                    evolution.append(evo)
                p.evolution = evolution
        pokemon = Pokemon(p.name, p.stats['HP'], p.stats['ATK'], p.stats['DEF'], p.stats['SPA'], p.stats['SPD'], p.stats['SPE'])
        db.session.add(character)
        db.session.commit()


def create_db():
    db.session.commit()
    db.drop_all()
    db.create_all()
    create_pokemon()