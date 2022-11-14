import json
from jsonschema import validate


class jsonvalid():
    
    @classmethod
    def validation(self,data):
        try:
            # Describe what kind of json you expect.
            schema = {
                        "type" : "object",
                        "properties" : {
                            "title" : {"type" : "string"},
                            "duration" : {"type" : "number"},
                            "released" : {"type" : "string"},
                        },
                    }
            
            validate(instance=data,schema=schema)
            print(data)
            return data
        except Exception as ex:
            raise Exception(ex)


