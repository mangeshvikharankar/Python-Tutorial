
data = {1: 'mangesh', 2:'ashish', 3:'vitthal'}
print(data)
print(data[3])
print(data.get(1))
print(data.get(4, 'not found'))

keys = {'mangesh','akash','vitthal'}
values = {'js','python','java'}

datamerge = dict(zip(keys,values))
print(datamerge)              #error
print(datamerge['mangesh'])

datamerge['rahul']='c'
print(datamerge)

del datamerge['rahul']
print(datamerge)
print('=================================')

#example

prog = {'js':'atom', 'cs':'vs', 'python':['pycharm','subline'], 'java':{'jse':'netbeans', 'jee':'eclipse'}}
print(prog)
print(prog['js'])
print(prog['python'][1])
print(prog['java']['jee'])




