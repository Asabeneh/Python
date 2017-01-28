web = ['HTML','CSS','JavaScript','Bootstrap','ReactJS','Angularjs','Python','PHP','MongoDB', 'SQL','Nodejs']

for i in range(len(web)):
    frontend = web[:6]
    backend = web[7:]
    fullstack = web[:]
print ("You are a front-end Ninja --> ", frontend)
print ("You are a back-end Ninja --> ",backend)
print ("You are a full-stack Ninja --> ",fullstack)

for wblang in web:
    print("I am good at ",wblang)
