In [5]: fp = open('foo.txt', 'w')                                                                 

In [6]: fp.write('Ximira traz o xelo')                                                            
Out[6]: 18

In [7]: fp.close()                                                                                

In [8]: fp = open('foo.txt', 'r')                                                                 

In [9]: fp.read()                                                                                 
Out[9]: 'Ximira traz o xelo'