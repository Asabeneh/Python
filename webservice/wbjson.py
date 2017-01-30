import json
input = '''[
{
"id" : "001",
"x" : "1",
"name" : "Asabeneh"
} ,
{
"id" : "002",
"x" : "2",
"name" : "Eyob"
}
]'''
info = json.loads(input)
print(info)
print ('User count:', len(info))
for item in info:
    print ('Name', item['name'])
    print ('Id', item['id'])
    print ('Attribute', item['x'])
