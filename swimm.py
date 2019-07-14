class Ocean:
    def __init__(self, name):
        self.name = name
    
    def swim(self):
        print(self.name + 'is swimming at the ocean')
        
    def walk(self):
        print(self.name + 'is walking along the highway')
        
        
    def main():
        sammy = Ocean('Sammy')
        sammy.swim()
        sammy.walk
        
        
    if __name__ == '__main__':
        main()
        