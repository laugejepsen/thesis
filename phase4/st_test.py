#!/usr/bin/env python

import numpy as np
import numpy
import pylab
import random
import json
import matplotlib
import math

exp = np.exp
plt = matplotlib.pyplot

def smoothTriangle(lst=[], degree=1):

	if degree < 1:
		print 'degree must be > 1'
		return

	triangle = numpy.array(range(degree)+[degree]+range(degree)[::-1])+1
	lst = numpy.array(lst)
	lst_lenght = len(lst)
	tri_len = len(triangle)
	_max = lst_lenght - degree
	triangle_normal_sum = float(sum(triangle))
	
	smoothed_lst = []
	for i in range(lst_lenght):

		if i > degree and i < _max:
			new_value = sum(triangle * lst[i-degree:i+degree+1]) / triangle_normal_sum
		else:
			left = degree - min(i, degree)
			right = degree + min(degree, lst_lenght - 1 - i) + 1			
			tri = triangle[left:right]
			triangle_sum = sum(tri)

			new_value = 0.0
			for j in range(len(tri)):

				pos = j + i + left - degree
				new_value += tri[j] * lst[pos]
		
			new_value /= triangle_sum

		smoothed_lst.append(new_value)

	return smoothed_lst

def main():

	# xs = [0, 0.1, 0.2, 0.3, 0.4, 0.1, 0.2, 0.5, 0.6, 0.7, 0.2, 0.2, 0.25, 0.3, 0.35, 0.40, 0.3, 0.2]
	# def inc_resolution(xs, factor=10):

	# 	zs = []
	# 	for i in range(len(xs)-1):
	# 		x = xs[i]
	# 		y = xs[i+1]
	# 		z = np.linspace(x,y,factor)
	# 		zs += list(z)
	# 	return zs
	# xs = inc_resolution(xs, 12)

	# pylab.figure()		
	# pylab.suptitle('Triangle smoothing', fontsize=16)

	# pylab.subplot(2,2,1, title='Original data')  
	# pylab.plot(xs,".k")  
	# pylab.plot(xs,"-k")
	# pylab.axis()  
	# pylab.grid(True)

	# d = 6
	# xssmooth = smoothTriangle(xs, d)
	# title = 'Smoothed with w = %d' % d
	# pylab.subplot(2,2,2, title=title)  
	# pylab.plot(xssmooth,".k")  
	# pylab.plot(xssmooth,"-k")
	# pylab.axis()  
	# pylab.grid(True)

	# d = 12
	# xssmooth = smoothTriangle(xs, d)
	# title = 'Smoothed with w = %d' % d
	# pylab.subplot(2,2,3, title=title)  
	# pylab.plot(xssmooth,".k")  
	# pylab.plot(xssmooth,"-k")
	# pylab.axis()  
	# pylab.grid(True)

	# d = 24
	# xssmooth = smoothTriangle(xs, d)
	# title = 'Smoothed with w = %d' % d
	# pylab.subplot(2,2,4, title=title)  
	# pylab.plot(xssmooth,".k")  
	# pylab.plot(xssmooth,"-k")
	# pylab.axis()  
	# pylab.grid(True)

	# format = 'png'
	# plt.savefig('triangle_smooth.png', format=format)

	# pylab.show()

	xs = np.linspace(0,1,250)
	ys = np.log(xs) + 10

	def normalize(a, factor=255.0):

		# convert to floating point	
		if not type(a).__name__ == 'numpy.ndarray':
			# a is not a numpy array
			b = np.float64(np.array(a)).copy()
		else:
			b = np.float64(a.copy())
		
		bmin = np.min(b)
		if bmin > 0.0:
			# no point in substracting 0
			b -= np.min(b)

		bmax = np.max(b)
		if bmax > 0.0:
			# to avoid dividing by zero
			b *= factor / bmax
		else:
			return a.copy()

		# convert back to integer
		return b # np.int64(b)	

	ys = normalize(ys, 1.0)

	pylab.figure()		
	pylab.suptitle('TITEL', fontsize=16)

	pylab.subplot(2,2,1, title='ln(x)')  
	pylab.plot(xs,ys,".k")  
	pylab.plot(xs,ys,"-k")
	pylab.axis()  
	pylab.grid(True)

	ys = ys - xs
	pylab.subplot(2,2,2, title='ln(x)-x')  
	pylab.plot(xs,ys,".k")  
	pylab.plot(xs,ys,"-k")
	pylab.axis()  
	pylab.grid(True)	

	ys = np.exp(xs)
	ys = normalize(ys, 1.0)
	pylab.subplot(2,2,3, title='exp(x)')  
	pylab.plot(xs,ys,".k")  
	pylab.plot(xs,ys,"-k")
	pylab.axis()  
	pylab.grid(True)

	ys = ys - xs
	pylab.subplot(2,2,4, title='exp(x)-x')  
	pylab.plot(xs,ys,".k")  
	pylab.plot(xs,ys,"-k")
	pylab.axis()  
	pylab.grid(True)	

	pylab.show()

if __name__ == '__main__':
	main()
