import tensorflow as tf


#multiply和 https://www.cnblogs.com/AlvinSui/p/8987707.html
x1=tf.constant([[1.0,2.0,3.0],[1.0,2.0,3.0],[1.0,2.0,3.0]])
y1=tf.constant([[0,0,1.0],[0,0,1.0],[0,0,1.0]])

z1=tf.multiply(x1,y1)
#Session用于运行代码
sess = tf.Session()
result1 = sess.run(z1)

print('result1')
print(result1)

x2=tf.constant([[1.0,2.0,3.0],[1.0,2.0,3.0],[1.0,2.0,3.0]])
y2=tf.constant([[0,0,1.0],[0,0,1.0],[0,0,1.0]])

z2=tf.matmul(x2,y2)
#Session用于运行代码
sess2 = tf.Session()
result22 = sess2.run(z2)

print('result22')
print(result22)

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

result2 = sess.run(z1)

print(result2)

print(result)  #输出结果

#将数据流图的描述写入my_graph文件夹下面
writer = tf.summary.FileWriter('./my_graph',sess.graph)

#关闭和释放
writer.close()
sess.close()


#在TensorFlow中，所有在节点之间传递的数据都为Tensor对象。

