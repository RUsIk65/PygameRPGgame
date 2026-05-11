import json
import sqlite3
from unittest import case
from systems.Items import *
from entities.nps import *

def load_items_from_json(json_file):
    with open(json_file, 'r') as f:
        items_data = json.load(f)
    
    conn = sqlite3.connect("database/items.db")
    cursor = conn.cursor()
    
    for item in items_data:

        cursor.execute("""
            INSERT INTO entity (name, image, cost, rareness, required_level) 
            VALUES (?, ?, ?, ?, ?)
        """, (
            item['name'],
            item['image'],
            item['cost'],
            item['rareness'],
            item['required_level']
            ))
        
        entity_id = cursor.lastrowid
        match item['type']:
            case 'weapon':
                cursor.execute("""
                    INSERT INTO weapon (id, damage) 
                    VALUES (?, ?)
                """, (entity_id, item['damage']))

                weapon = Weapon(
                    id=entity_id,
                    name=item['name'],
                    image=item['image'],
                    cost=item['cost'],
                    rareness=item['rareness'],
                    required_level=item['required_level'],
                    damage=item['damage']
                )
                weapons.append(weapon)
            case 'armor':
                cursor.execute("""
                    INSERT INTO armor (id, defense) 
                    VALUES (?, ?)
                """, (entity_id, item['defense']))

                armor = Armor(
                    id=entity_id,
                    name=item['name'],
                    image=item['image'],
                    cost=item['cost'],
                    rareness=item['rareness'],
                    required_level=item['required_level'],
                    defense=item['defense']
                )
                armors.append(armor)
            case 'potion':
                cursor.execute("""
                    INSERT INTO potion (id, mana_restore) 
                    VALUES (?, ?)
                """, (entity_id, item['mana_restore']))
                potion = Potion(
                    id=entity_id,
                    name=item['name'],
                    image=item['image'],
                    cost=item['cost'],
                    rareness=item['rareness'],
                    required_level=item['required_level'],
                    mana_restore=item['mana_restore']
                )
                potions.append(potion)
            case 'backpack':
                cursor.execute("""
                    INSERT INTO backpack (id, capacity) 
                    VALUES (?, ?)
                """, (entity_id, item['capacity']))
                backpack = Backpack(
                    id=entity_id,
                    name=item['name'],
                    image=item['image'],
                    cost=item['cost'],
                    rareness=item['rareness'],
                    required_level=item['required_level'],
                    capacity=item['capacity']
                )
                backpacks.append(backpack)
            case 'food':
                cursor.execute("""
                    INSERT INTO food (id, health_restore) 
                    VALUES (?, ?)
                """, (entity_id, item['health_restore']))
                food = Food(
                    id=entity_id,
                    name=item['name'],
                    image=item['image'],
                    cost=item['cost'],
                    rareness=item['rareness'],
                    required_level=item['required_level'],
                    health_restore=item['health_restore']
                )
                foods.append(food)

    conn.commit()
    conn.close()

def load_entities_from_json(json_file):
    with open(json_file, 'r') as f:
        entities_data = json.load(f)
    
    conn = sqlite3.connect("database/entity.db")
    cursor = conn.cursor()
    
    for entity in entities_data:

        cursor.execute("""
            INSERT INTO nps (name, hp, defense, attack, speed, radar_range, image) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            entity['name'],
            entity['hp'],
            entity['defense'],
            entity['attack'], 
            entity['speed'], 
            entity['radar_range'], 
            entity['image']
            ))
        nps = NPS(
            id=cursor.lastrowid,
            name=entity['name'],
            image=entity['image'],
            hp=entity['hp'],
            defense=entity['defense'],
            attack=entity['attack'], 
            speed=entity['speed'], 
            radar_range=entity['radar_range']
        )
        add_nps(nps)
    
    conn.commit()
    conn.close()