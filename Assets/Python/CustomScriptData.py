import pickle

class CustomScriptData:
    def __init__(self):
        return
        
    def load(self, cyObject):
        if (not cyObject.getScriptData()):
            cyObject.setScriptData(pickle.dumps({}))
        dVars = pickle.loads(cyObject.getScriptData())
        return dVars
        
    def save(self, cyObject, dVars):
        cyObject.setScriptData(pickle.dumps(dVars))
        return
    
    def get(self, cyObject, varName, default=0):
        dVars = self.load(cyObject)
        return dVars.get(varName, default)

    def set(self, cyObject, varName, newValue):
        dVars = self.load(cyObject)
        dVars[varName] = newValue
        self.save(cyObject, dVars)
        return
    
    def add(self, cyObject, varName, addValue, default=0):
        newValue = self.get(cyObject, varName, default) + addValue
        self.set(cyObject, varName, newValue)
        return

csd = CustomScriptData()