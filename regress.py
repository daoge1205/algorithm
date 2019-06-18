#函数用来模拟线形回归
import numpy as np 
'''
	简单线性回归测试函数
	线性回归侧重于直接预测而不经过激活函数，激活函数一般只是涉及分类问题
	类似于反向传播算法也是很简单的链式求导过程
	思想类似于数位dp算法，需要记忆所在层的求导参数以便进行传播

	代价函数很重要必须是凸函数，只有设计为凸函数才可以找到局部乃至全局最优解
	然后求梯度的过程就是类似于求导，特意指明，机器学习是不能等同于高中课程的求导
	高中课程的求导是针对输入的，而机器学习是真针对初始化参数的值
	因此要适应于对系数求导
	代价函数的guassian分布也不是稀奇的东西，我的理解不是求概率啊，只是典型的
	墨西哥草帽模型，只是应运在图像上是需要模糊噪声，而在线性回归这个层面
	只是单纯的假设数据满足一定的关系，即默认为数据可以表示为一条线段的
	这点可以从很多文章指明线性回归算法对于异常值反应剧烈。
	我觉得上述就是废话，因为运用的代价函数是一个凸函数，此函数的前提是
	函数中的output_layer与target差值满足高斯分布

	总结，线性函数对于异常值敏感，这点事源于本性默认是高斯分布的结果。
	不需要任何激活函数！满足bp反向传播
'''
#函数用来模拟 y=2x+3

input_layer=np.array([5,2,1,4,2])

output_target=np.array([13,7,5,11,7])

bias=0
theta=0.01
w1=10
for i in range(10000):
	output_layer=w1*input_layer+bias
	loss = 1/(2*input_layer.size)*(np.sum((output_layer-output_target)**2))
	loss_common=1/(input_layer.size)*(output_layer-output_target)
	w1_background=np.sum(loss_common*input_layer)
	b1_background=np.sum(loss_common)
	bias =bias-theta*b1_background
	w1 = w1-theta*w1_background
	print("the loss:",loss," the w1:",w1," the bias:",bias)