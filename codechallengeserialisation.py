import pickle
import json

def serialize(pyobj,filename,ser_protocol):
    
    #serialising pyobj to binary data using pickle
    if ser_protocol == "pickle":
        filename = filename+".dat"
        with open(filename,'wb') as f:
            pickle.dump(pyobj, f)
    else:
        #deserialise 
        filename = filename+".json"
        with open(filename,'wt') as f:
            json.dump(pyobj, f)

def deserialize(filename, ser_protocol):
    if ser_protocol == 'pickle':
        with open(filename,'rb') as f:
            l = pickle.load(f)
        print(l)
    else:
        with open(filename,'rt') as f:
            pyobj = json.load(f)
        print(pyobj)

if __name__ == "__main__":
    d1 = {'a': 'x', 'b' : 'y', 'c' : 'z', 30 : (2,3,1)}

    #serializing using pickle
    serialize(d1,'testp','pickle')

    #serialise using json
    serialize(d1,'testj','json')

    #deserialize using pickle
    deserialize('testp.dat','pickle')

    #deserialize using json
    deserialize('testj.json','json')

