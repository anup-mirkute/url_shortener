class InMemoryDB:
    def __init__(self):
        self.url_map = {} 
        self.current_id = 1000000  

    def insert(self, long_url):
        obj_id = self.current_id
        self.url_map[obj_id] = long_url
        self.current_id += 1
        
        return obj_id

    def get(self, obj_id):
        return self.url_map.get(obj_id)
