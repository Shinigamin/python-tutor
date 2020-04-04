In [1]: def foo(bar): 
   ...:     print(bar) 
   ...:                                                                                           

In [2]: foo('num')                                                                                
num

In [3]: foo(bar='num')                                                                            
num

In [4]: def soma(*args): 
   ...:     print(args) 
   ...:                                                                                           

In [5]: soma(5,6,8,9,7)                                                                           
(5, 6, 8, 9, 7)

In [6]: def soma(*args): 
   ...:     num = 0 
   ...:     for n in args: 
   ...:         num = num + n 
   ...:     return num 
   ...:                                                                                           

In [7]: soma(5,6,8,9,7)                                                                           
Out[7]: 35


In [3]: class User: 
   ...:     id = None 
   ...:     name = None 
   ...:     age = None 
   ...:     def __init__(self, **kwargs): 
   ...:         self.id = kwargs['id'] 
   ...:         self.name = kwargs['name'] 
   ...:         self.age = kwargs['age'] 
   ...:         print(kwargs) 
   ...:                                                                                           

In [4]: user = User(id=55, name='ximira', age=56, qualquer_coisa='xelo')                          
{'id': 55, 'name': 'ximira', 'age': 56, 'qualquer_coisa': 'xelo'}

In [5]: user.id                                                                                   
Out[5]: 55

In [6]: d = {'id': 55, 'name': 'ximira', 'age': 56, 'qualquer_coisa': 'xelo'}                     

In [7]: d                                                                                         
Out[7]: {'id': 55, 'name': 'ximira', 'age': 56, 'qualquer_coisa': 'xelo'}

In [8]: user = User(**d)                                                                          
{'id': 55, 'name': 'ximira', 'age': 56, 'qualquer_coisa': 'xelo'}
