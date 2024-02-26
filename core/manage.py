import json
import core.clients as Clients

def load_users(path):
    objects = {}
    try:
        with open(path + '/database.json') as database:
            db = json.load(database)
    except:
        pass
    else:
        for clients in db['clientes']:    
            data = [clients]
            user_data = db['clientes'][clients].items()
            for items in user_data:
                data.append(items[1])
            data = tuple(data)
            object = Clients.Clients(*data)
            objects.update({clients:object})
        return objects

def save_users(path, objects):
    db = {}
    for users in objects:
        dump = {}
        data = objects[users]
        for items in data.__dict__:
            if items == "_ID__internal_ID" or items == "user":
                pass
            elif items == "_Clients__pw":
                dump.update({"pw":data.__dict__[items]})
            else:
                dump.update({items:data.__dict__[items]})
        db.update({users:dump})
    db = {"clientes": db}
    try:
        with open(path + '/database.json', 'w') as database:
            json.dump(db, database)
    except:
        return True
    else:
        pass

def add_user(user, objects):
    data = [user[0]]
    user_data = user[1].items()
    for items in user_data:
        data.append(items[1])
    data = tuple(data)
    object = Clients.Clients(*data)
    objects.update({user[0]:object})