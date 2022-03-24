import json

#### JSON IO #########

def json2dict(filename):
    '''
    Reads a json file `filename` as a dictionary

    Returns
    -------
    d : dict
    '''
    with open(filename, 'r') as j:
        d = json.load(j)
    return d

def dict2json(d, filename):
    '''
    Saves a dictionary `d` to a json file `filename`
    '''
    with open(filename, 'w') as j:
        json.dump(d, j, indent=4)
        
def dict2str(d, indent=4, **kwargs):
    '''
    A nice way of printing a nested dictionary
    '''
    return json.dumps(d, indent=indent, **kwargs)