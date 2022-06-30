'''Dictionary:It is a data type in python.
It is represented by { : } , dict(dictionary).
It is a combination of key value pair.
The value can be accessed with the help of key.
It can have several data types in it and it can aslo have one more dictionary in it.
'''



# x={1:'python',
# 2:'corepython',
# 3:'advance python',
# 4.6:'8pm',
# 'n':'hi'}
# print(x[3])  #advance python
# print(x[2])  #core python
# print(x[8])  #KeyError:8

# cs={1:'',2:'hi',3:7,4:6.7,5:[1,3],6:(3,7),7:{1,2}}
# print(cs[1],type(cs[1])) #<class 'str'>
# print(cs[2],type(cs[2]))  #hi <class 'str'>
# print(cs[3],type(cs[3]))  #7 <class 'int'>
# print(cs[4],type(cs[4]))  #6.7 <class 'float'>
# print(cs[5],type(cs[5]))  #[1,3] <class 'list'>
# print(cs,type(cs))  #{1: '', 2: 'hi', 3: 7, 4: 6.7, 5: [1, 3], 6: (3, 7), 7: {1, 2}} <class 'dict'>
# print(cs.keys())  #[1,2,3,4,5,6,7]
# print(cs.items())  #dict_items([(1, ''), (2, 'hi'), (3, 7), (4, 6.7), (5, [1, 3]), (6, (3, 7)), (7, {1, 2})])
# print(cs.values())  #dict_values(['', 'hi', 7, 6.7, [1, 3], (3, 7), {1, 2}])

# cs={1:'',2:'hi',3:7,4:6.7,5:[1,3],6:(3,7),7:{1,2}}
# cs.clear()
# print(cs)  #{}

# x={10,20,30,40,50,60}
# print(dict.fromkeys(x,'pass'))  #{50: 'pass', 20: 'pass', 40: 'pass', 10: 'pass', 60: 'pass', 30: 'pass'}

# x={1:'',2:'hi',3:7,4:6.7,5:[1,3],6:(3,7),7:{1,2}}
# print(x.get(4))  #6.7 
# print(x.get(9))  #None
# print(x[34])  #KeyError
# x.pop(2)
# print(x)  #{1: '', 3: 7, 4: 6.7, 5: [1, 3], 6: (3, 7), 7: {1, 2}}
# x.popitem()
# print(x)  #{1: '', 2: 'hi', 3: 7, 4: 6.7, 5: [1, 3], 6: (3, 7)}

# h={1:'',2:'python',3:7,4:5.6,5:[1,2],6:(3,5),7:{1,2}}
# h.update({3:"world"})
# print(h)  #{1: '', 2: 'python', 3: 'world', 4: 5.6, 5: [1, 2], 6: (3, 5), 7: {1, 2}}
# h.update({9:'hey'})
# print(h)  #{1: '', 2: 'python', 3: 7, 4: 5.6, 5: [1, 2], 6: (3, 5), 7: {1, 2}, 9: 'hey'}

# h={1:'',2:'python',3:7,4:5.6,5:[1,2],6:(3,5),7:{1,2}}
# h.setdefault(2,"core")
# print(h)  #{1: '', 2: 'python', 3: 7, 4: 5.6, 5: [1, 2], 6: (3, 5), 7: {1, 2}}
# h.setdefault(8,'core')
# print(h)  #{1: '', 2: 'python', 3: 7, 4: 5.6, 5: [1, 2], 6: (3, 5), 7: {1, 2}, 8: 'core'}





