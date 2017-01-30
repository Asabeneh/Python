movies = list()
movie1 = dict()
movie1['Director'] = 'James Cameron'
movie1['Title'] = 'Avatar'
movie1['Release Date'] = '18 December 2009'
movie1['Running Time'] = '162 minutes'
movie1['Rating'] = 'PG-13'
movies.append(movie1)
movie2 = dict()
movie2['Director'] = 'David Fincher'
movie2['Title'] = 'The Social Network'
movie2['Release Date'] = '01 October 2010'
movie2['Running Time'] = '120 min'
movie2['Rating'] = 'PG-13'
movies.append(movie2)
print(movies)
print(movie1)
print(movie2)
print(movie1.keys())
print(movie1.values())
print(movie1.items())
for key in movie1:
    print(key)

for key in movie2:
    print(key,":",movie2[key])
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self,nam):
        self.name = nam
        print(self.name, "constructed")
    def party(self):
        self.x +=1
        print(self.name,"part count",self.x)
    # def __del__(self):
    #     print("I am destructed",self.x)
s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")
j.party()
s.party()
