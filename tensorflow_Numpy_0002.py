import numpy as np


t_0=np.array(50,dtype=np.int32)

print(t_0)


t_1=np.array([b"aaaaaa",b"bbbbbbbbb",b"cccccc"])     
t_2=np.array([[True,False,False],                   
     [True,False,False],
     [True,False,False]])

t_3=np.array([[[0,0],[0,1],[0,2]],                  
     [[0,0],[0,1],[0,2]],
     [[0,0],[0,1],[0,2]]])

t_0=50                                     #视为0阶张量或“标量”
t_1=[b"aaaaaa",b"bbbbbbbbb",b"cccccc"]     #视为1阶张量或“向量”  
t_2=[[True,False,False],                   #视为2阶张量
     [True,False,False],
     [True,False,False]]

t_3=[[[0,0],[0,1],[0,2]],                  #视为2阶张量
     [[0,0],[0,1],[0,2]],
     [[0,0],[0,1],[0,2]]]


