import json
from pprint import pprint
import psycopg2


conn = psycopg2.connect(host="db", database="postgres", user="postgres", password="demo")

with open('cards.json') as f:
    data = json.load(f)


def getMinions():
    #Get minions
    decks = ["Basic","Classic","Naxxramas","Goblins vs Gnomes","The Grand Tournament"]
    result = list()
    for deck in decks:
        for card in data[deck]:
            if card["type"] != "Minion":
                continue
            
            result.append([card["name"],card.get("cost",0),card.get("attack",0),card.get("health",1), card["playerClass"],
            card.get("rarity",0)])
            
    return result

def getHeros():
    #Get heros
    result = list()
    for card in data["Basic"]:
            if card["type"] == "Hero":
                result.append([card["name"], card["playerClass"]])

    return result

def getSpells():
    #Get spells
    result = list()
    for card in data["Basic"]:
            if card["type"] == "Spell" or card["type"] == "Enchantment":
                result.append([card["name"], card["playerClass"], card.get("cost", 0)])

    return result

def insertHeros(data, conn):
    try:        
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print("Insert heros")
        for d in data:
            cur.execute("INSERT INTO PyBirdApp_hero('name', 'playerClass') VALUES (%s, %s)", d)
            #print('INSERT INTO "PyBirdApp_hero"("name", "playerClass") VALUES (%s, %s)', d)

        # close the communication with the PostgreSQL
        cur.close()
        print("Heroes succesly added")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insertMinions(conn):
    try:        
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



#print(getMinions())
#print(getHeros())
#print(getSpells())
insertHeros(getHeros(), conn)