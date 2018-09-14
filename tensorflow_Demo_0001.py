# 随机数字案例解析
# https://blog.csdn.net/yue008/article/details/61626726


import tensorflow as tf

#定义两个常量（边）
a = tf.constant(5,name='input_a')
b = tf.constant(3,name='input_b')

#三个操作Operation(节点) 
c = tf.multiply(a,b,name='mul_c')
d = tf.add(a,b,name='add_d')

#其中定义e为终结点
e = tf.add(c,d,name='add_e')

#Session用于运行代码
sess = tf.Session()
result = sess.run(e)

print(result)  #输出结果

#将数据流图的描述写入my_graph文件夹下面
writer = tf.summary.FileWriter('./my_graph',sess.graph)

#关闭和释放
writer.close()
sess.close()


#在TensorFlow中，所有在节点之间传递的数据都为Tensor对象。

t_0=50                                     #视为0阶张量或“标量”
t_1=[b"aaaaaa",b"bbbbbbbbb",b"cccccc"]     #视为1阶张量或“向量”  
t_2=[[True,False,False],                   #视为2阶张量
     [True,False,False],
     [True,False,False]]

t_3=[[[0,0],[0,1],[0,2]],                  #视为2阶张量
     [[0,0],[0,1],[0,2]],
     [[0,0],[0,1],[0,2]]]

