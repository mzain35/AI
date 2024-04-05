class Person:
    def __init__(self, name, age,location, interests):
        self.name = name
        self.age = age
        self.location = location
        self.interests = interests
        self.friends = []
    
    def add_friend(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)
        
    def __str__(self):
        return self.name

persons = {
    'Alice': Person('Alice', 25, 'USA', ['music', 'movies', 'sports']),
    'Bob': Person('Bob', 30, 'UK', ['movies', 'sports']),
    'Charlie': Person('Charlie', 28, 'USA', ['music', 'sports']),
    'David': Person('David', 35, 'USA', ['music', 'movies']),
    'Eve': Person('Eve', 18, 'UK', ['gaming', 'studies'])
}

persons['Alice'].add_friend(persons['Bob'])
persons['Alice'].add_friend(persons['Charlie'])
persons['Alice'].add_friend(persons['David'])
persons['Bob'].add_friend(persons['Eve'])
persons['Charlie'].add_friend(persons['David'])
persons['Charlie'].add_friend(persons['Eve'])
persons['David'].add_friend(persons['Eve'])


#Person with common interests
def common_interests(persons):
    common = {}
    for person in persons:
        for friend in persons[person].friends:
            common[person + ' - ' + friend.name] = set(persons[person].interests) & set(friend.interests)
    return common

print(common_interests(persons))
        
# All teenagers
def all_teenagers(persons):
    teenagers = []
    for person in persons:
        if persons[person].age < 20:
            teenagers.append(persons[person])
    return teenagers

teenList = all_teenagers(persons)
for n in teenList:
    print(n.name)
    
# All teens interested in gaming
def teens_interested_in_gaming(persons):
    interested = []
    for person in persons:
        if persons[person].age < 20 and 'gaming' in persons[person].interests:
            interested.append(persons[person])
    return interested

interested = teens_interested_in_gaming(persons)
for n in interested:
    print(n.name)

# A person with most friends
def person_with_most_friends(persons):
    most_friends = 0
    person = None
    for p in persons:
        if len(persons[p].friends) > most_friends:
            most_friends = len(persons[p].friends)
            person = persons[p]
    return person

print(person_with_most_friends(persons))



def bfs_search(graph, start, end):
    visted = []
    queue = [start]
    parent = {start: None}
    
    while queue:
        node = queue.pop(0)
        # print(node)
        
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        
        
        visted.append(node)
        for neighbor in graph[node]:
            if neighbor not in queue and neighbor not in visted:
                queue.append(neighbor)
                parent[neighbor] = node
  
def path_to_friend(graph, start, end):
    return bfs_search(graph, start, end)

graph = {}
for person in persons:
    graph[person] = [friend.name for friend in persons[person].friends]
    
print(path_to_friend(graph, 'Alice', 'Eve'))