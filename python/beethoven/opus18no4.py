Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([-5, 0, 0, 2, 0, -1, 0, 3, 2, 2, 0, 0, 5, 5, 7, 5, 4, 5, 8, 7, 7, 5],dur=[1.0 ,2.0 ,0.5 ,0.0 ,0.0 ,0.0 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.0 ,0.0 ,0.0 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([-60, -5, -1, -1, -5, -12, -12, 0, 4, 4, 0],dur=[rest(1.0) ,3.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,3.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([-60, -9, -7, -4, -7, -9, -60, -4, -2, 1, -2, -4],dur=[rest(1.0) ,3.0 ,1.0 ,1.5 ,0.5 ,1.0 ,rest(1.0) ,3.0 ,1.0 ,1.5 ,0.5 ,1.0])
	d3 >> pluck([-60, -24, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -60, -24, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -12],dur=[rest(1.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(1.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a1():
	d0 >> pluck([5, 5, 14, 14, 12, 11, 17, 17, 15, 15, 14, 12, 11, 12, 14, 15],dur=[1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.5 ,0.5 ,1.0])
	d1 >> pluck([-12, -12, -24, -12, 5, 3, 2, 8, 8, 7, 8, 8, 6, 6, 9, 9, 5, 5, 7, 7, 7, 7, 7, 7],dur=[0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-60, -4, -5, -7, -1, -1, 0, 5, 5, 3, 3, 3, 3, 2, 2, -5, -5, -5, 5, 3, -5],dur=[rest(2.0) ,2.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-60, -12, -12, -12, -12, -12, -12, -24, -12, -12, -12, -12, -12, -12, -12, -7, -7, -4, -4, -6, -6, -5, -5, -9, -9, -9, -13, -12, -5],dur=[rest(2.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a2():
	d0 >> pluck([3, 12, 11, 20, 20, 19, 17, 29, 29, 27, 27, 26, 26, 26, 29, 26, 26, 24],dur=[0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
	d1 >> pluck([-9, 0, -5, 2, 2, 2, 2, 2, 3, 3, -60, 2, 14, 14, 14, 14, 15, 15, 15, 14, 14, 14, 17, 14, 14, (3, 12)],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
	d2 >> pluck([-9, -12, -5, -1, -1, -1, -1, -1, 0, 0, -60, -5, -5, -5, -5, -5, -5, -5, -4, (0, 8), (0, 8), (0, 8), (0, 5), (0, 5), (0, 8), (0, 8), (0, 9), (0, 9), 6, 6, 7, 7],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-60, -12, -17, -7, -7, -7, -7, -7, -9, -9, -60, -13, -13, -13, -13, -13, -12, -12, -19, -7, -7, -7, -4, -4, -7, -7, -6, -6, -4, -4, -5, -5],dur=[rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a3():
	d0 >> pluck([23, 24, -60, (-5, 2, 11), -60, (-5, 3, 12), (-5, 2, 11), (-5, 3, 12), (7, 15, 24), (-5, 2, 11), -60, (-5, 3, 12), -60, (-5, 2, 11), (-5, 3, 12), (-5, 2, 11)],dur=[1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0])
	d1 >> pluck([(2, 11), (-5, 3, 12), -60, (-5, 7), -60, (-5, 7), (-5, 7), (-5, 7), -60, (-5, 7), -60, (-5, 7), -60, (-5, 7), (-5, 7), (-5, 7)],dur=[1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0])
	d2 >> pluck([(-5, 5), (-5, 5), (-5, 3), -60, -17, -60, -12, -17, -12, -60, -17, -60, -12, -60, -17, -12, -17],dur=[0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-17, -17, -12, -60],dur=[0.5 ,0.5 ,1.0 ,rest(14.0)])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a4():
	d0 >> pluck([(7, 14, 23), 19, 31, 31, 29, 29, 27, 25, 25, 24, 24, 22, 22, 20, 19, 18, 19, 2, 2, 2, 7],dur=[1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([-60, -9, 9, 11, 12, 3, 5, 7, 8, 3, 0, 12, 11, 2, -1, -1, -1, 2],dur=[rest(1.0) ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-60, 7, -3, -1, 0, -9, -7, -5, -4, -9, -12, 0, -1, -1, -5, -5, -5, -1],dur=[rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-60, -5, -10, -12, -14, -16, -16, -17, -5, -60, -5],dur=[rest(2.0) ,1.0 ,2.0 ,2.0 ,2.0 ,3.0 ,1.0 ,0.5 ,0.5 ,rest(1.5) ,0.5])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a5():
	d0 >> pluck([19, 17, 17, 15, 14, 12, 10, 8, 7, 6, 9, 7, 2, 7, 19, 17, 17, 15, 14, 12, 10, 8, 7, 6, 9, 7, (-5, 3), 15, 6, 9, 7],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5])
	d1 >> pluck([2, 2, -17, 3, 3, 3, 3, 3, 3, 3, -17, 2, 2, 2, -1, 2, 2, 2, -17, 3, 3, 3, 3, 3, 3, 3, -17, 0, (-5, 3), -17],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([-1, -1, -60, 0, 0, 0, 0, 0, 0, 0, -60, -1, -1, -1, -5, -1, -1, -1, -60, 0, 0, 0, 0, 0, 0, 0, -60, (-5, 2), -12, -60, (-5, 2)],dur=[0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,1.0 ,rest(0.5) ,0.5])
	d3 >> pluck([-5, -5, -60, -5, -5, -5, -5, -5, -5, -5, -60, -5, -5, -5, -60, -5, -5, -5, -60, -5, -5, -5, -5, -5, -5, -5, -60, -1, -60, 14, 0, -60, -1],dur=[0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,rest(0.25) ,0.25 ,0.5 ,rest(0.5) ,0.5])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a6():
	d0 >> pluck([(-5, 3), 15, 6, 7, (-5, 2, 11, 19), -60, 3, 19, 20, 15, -17, 12, 15, -11, 8, 3, -17, 0, 3, -2, 12, 15],dur=[0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,rest(2.0) ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([0, (-5, 3), (-5, 2), (-5, 2, 11), -60, 3, 3, 7, -12, -60, 1, -9, -17, -9],dur=[0.5 ,0.5 ,1.0 ,1.0 ,rest(2.0) ,4.0 ,1.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-12, -1, (-5, 7), -60, -9, -9, -16, -60, 13, -16],dur=[1.0 ,1.0 ,1.0 ,rest(2.0) ,4.0 ,4.0 ,1.0 ,rest(0.5) ,0.5 ,1.0])
	d3 >> pluck([-60, 14, 0, (-17, -5), (-17, -5), -60, -9, -11, -12, -60, 13, -16, -60],dur=[rest(0.25) ,0.25 ,0.5 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,rest(0.5) ,0.5 ,1.0 ,rest(6.0)])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a7():
	d0 >> pluck([-2, 12, 13, 15, 13, 12, -60, 0, 16, 17, 12, -8, 8, 12, -14, 5, 0, -20, -4, 0, 0],dur=[1.0 ,0.0 ,0.0 ,0.0 ,2.0 ,1.0 ,rest(1.0) ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0])
	d1 >> pluck([-17, -2, 8, 7, 8, -60, 0, 0, 4, -16, -60, -2, -12, -20, 8, 20],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,4.0 ,1.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-60, 13, -17, -60, -12, -12, -19, -60, 10, -19],dur=[rest(0.5) ,0.5 ,3.0 ,rest(1.0) ,4.0 ,4.0 ,1.0 ,rest(0.5) ,0.5 ,1.0])
	d3 >> pluck([-60, 7, -9, -4, -60, -12, -2, -4, -60, 10, -7, -60],dur=[rest(1.5) ,0.5 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(0.5) ,0.5 ,1.0 ,rest(6.0)])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a8():
	d0 >> pluck([0, 15, 14, -2, -2, 7, 7, 5, 4, 5, 7, 5, 21, 22, 19, 15, 10, 8],dur=[1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,0.0 ,0.0 ,0.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
	d1 >> pluck([-16, 0, -3, -2, -3, 0, -2, -4, -7, -9, -2, -9, -2, -4, -2, -4, -2, -4, 22, 22, 22, 3, -2, -2, 8, 2, -2, 3, -2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-60, 17, -14, -60, -2, -4, -2, -5, -2, -9, -2, -10, -2, -60],dur=[rest(0.5) ,0.5 ,3.0 ,rest(5.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(2.0)])
	d3 >> pluck([-60],dur=[rest(16)])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a9():
	d0 >> pluck([7, 5, 7, 8, 7, 21, 22, 24, 22, 22, 22, 24, 26, 27, 19, 21, 23, 24, 15, 19],dur=[1.0 ,0.0 ,0.0 ,0.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([3, -3, 3, 22, 22, 22, 5, -2, -2, 10, 10, 8, 8, 7, 5, 5, 3, 2, 0, -2, -3],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-60, -2, 3, -2, 2, -2, 2, -4, -5, -2, -5, -2, -7, -2, -7, -2, -9, -5, -9, -5, -10, -5, -10, -5, -12, -5, -12, -9, -12, -9],dur=[rest(1.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-60, -17, -60, -12, -60, -19],dur=[rest(11.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a10():
	d0 >> pluck([9, 12, 10, 9, 10, 9, 10, 12, 10, 10, 19, 19, 17, 16, 17, 19, -5, -4, -2, 4, 5, 7, 17, 15, 10, 10, 20, 20],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d1 >> pluck([3, -3, -2, -4, -5, -2, -2, -4, -4, -5, -2, 3, 7, 8, 2, 5],dur=[0.5 ,0.5 ,3.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
	d2 >> pluck([-12, -9, -10, -2, -3, -2, -3, -2, 0, -2, -2, 7, 7, 5, 5, 3, -2, -2, 8, 8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d3 >> pluck([-60, -14, -16, -19, -22, -21, -14, -9, -14, -10, -14, -10, -14, -9, -14, -9, -14, -9, -14, -17, -21, -22, -14, -10, -14, -9, -10],dur=[rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a11():
	d0 >> pluck([19, 17, 19, 20, 2, 3, 5, 5, 7, 8, 19, 17, -4, 0, 10, 22, 22, 20, 20, 19, 17, 17, 15, 15, 14, 14, 12],dur=[1.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([3, 3, 2, -60, -2, 3, -2, 7, 15, 15, 14, 12, 14, 15, 3, 12, 12, 11, 9, 11, 12, 3, 3, 3, 3, 3],dur=[1.0 ,2.0 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([7, 7, 5, -60, -5, 3, 2, 0, 2, 3, -5, -60, 0, 0, -1, -3, -1, 0, -5, -5, -5, -7, -7],dur=[1.0 ,2.0 ,1.0 ,rest(1.0) ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-9, -15, -14, -2, -2, -2, -3, -2, -60, 3, -7, -9, -10, -12, -19],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(2.5) ,0.5 ,2.0 ,2.0 ,2.0 ,2.0 ,1.0])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a12():
	d0 >> pluck([10, 9, 12, 10, 10, 9, 10, 9, 10, 15, 14, 11, 12, 12, 11, 12, 11, 12, 17, 15, 13, 14, 13, 14, 13, 14, 19, 17, 14, 15, 14, 15, 14, 15, 20, 19, 16, 17, 19, 17, 20, 19, 22, 20, 19, 17, 15, 14],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25])
	d1 >> pluck([3, 3, 2, 5, 5, 5, 5, -60, 9, 9, 9, 9, -60, 8, -60, 7, -60, (-2, 5, 14), -60],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0)])
	d2 >> pluck([0, 0, -2, 2, 2, 2, 2, -60, 3, 3, 3, 3, -60, 5, -60, 3, -60, (-2, 8), -60],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0)])
	d3 >> pluck([-19, -14, -2, -2, -2, -2, -60, -2, -2, -2, -2, -60, -2, -60, -2, -60, -14, -60],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0)])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a13():
	d0 >> pluck([12, 10, 9, 8, 7, 10, 10, 14, 15, 17, 14, 10, 10, 8, 7, 8, 7, 10, 10, 14, 15, 17, 14, 10],dur=[0.25 ,0.25 ,0.25 ,0.25 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
	d1 >> pluck([-60, 3, 3, 3, 8, 7, 5, 8, 2, 5, -2, 3, 3, 8, 7, 5, 8, 2],dur=[rest(1.0) ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-60, -2, -2, -2, -2, -2, -2, 2, 5, -2, -2, -2, -2, -2, -2, -2, 2, 5],dur=[rest(1.0) ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-60, -9, -5, -5, -7, -9, -10, -7, -14, -10, -9, -5, -5, -7, -9, -10, -7, -14],dur=[rest(1.0) ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a14():
	d0 >> pluck([10, 8, 7, 8, 7, 10, 10, 14, 15, 15, 12, 12, 12, 16, 17, 17, 15, 14, 15, 22, 22, 22, 22],dur=[0.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([5, -2, 3, 3, 5, 7, 7, 3, 4, 5, 5, 7, 8, 8, 7, 6, 5, 3, 3, 3, 3, 3],dur=[1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-2, -2, -2, -2, -4, -5, -5, 0, 0, 0, -2, -4, -2, 10, 12, 10, 10, -2, -2, -2, -2],dur=[1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-10, -9, -5, -5, -7, -9, -9, -4, -4, -4, -5, -7, -2, -3, -4, -17, -5, -5, -5, -5],dur=[1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a15():
	d0 >> pluck([20, 19, 17, 24, 24, 24, 24, 22, 20, 19, 25, 25, 25, 25, 24, 23, 24, 24, 24, 23, 24, 24, 24, 23, 24, 24],dur=[0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
	d1 >> pluck([2, 3, 3, 5, 5, 5, 5, 4, 5, 4, 13, 13, 13, 13, 12, 11, 12, 12, 12, 11, 12, 12, 12, 11, 12, 15, 12],dur=[0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-2, -2, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 0],dur=[0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-7, -9, -16, -4, -4, -4, -4, -5, -7, -14, -2, -2, -2, -2, -4, -5, -4, -4, -4, -5, -4, -4, -4, -5, -4, -6],dur=[0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a16():
	d0 >> pluck([27, 27, 30, -3, -2, -3, 0, -2, 2, 0, 3, 2, 5, 4, 7, 5, 9, 7, 10, 9, 12, 10, 14, 12, 15, 14, 17, 16, 19, 17, 20, 19, 22, 21, 24, 22, 22, 27, 31, 34],dur=[1.0 ,1.0 ,2.0 ,1.0 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,1.0 ,1.0 ,0.5])
	d1 >> pluck([10, 9, 12, 5, -60, 8, 5, 2, 14, 15, -60, 15],dur=[1.0 ,2.0 ,2.0 ,1.0 ,rest(3.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.5) ,0.5])
	d2 >> pluck([-2, -3, 0, -7, -60, -4, -7, -10, -4, -5, -60, 7],dur=[1.0 ,2.0 ,2.0 ,1.0 ,rest(3.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.5) ,0.5])
	d3 >> pluck([-6, -7, -9, -10, -60, -16, -17, -60],dur=[1.0 ,2.0 ,2.0 ,1.0 ,rest(6.0) ,1.0 ,1.0 ,rest(2.0)])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a17():
	d0 >> pluck([34, 34, -2, 9, 10, 10, 3, -60, 10, 7, 3, 4, 5, 7, 8, -60, -1],dur=[0.5 ,0.5 ,2.0 ,0.0 ,0.0 ,2.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d1 >> pluck([19, 15, 20, 17, 14, 10, 8, 5, 2, 14, 15, -60, 10, 7, 3, 4, 5, 7, 8, -60, -1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d2 >> pluck([3, 7, 2, -10, -7, -4, 2, 5, 8, -4, -5, -60, -2, -5, -9, -8, -7, -5, -4, -60, -1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d3 >> pluck([-60, -2, -14, -14, -14, -14, -14, -14, -14, -9, -60, -2, -5, -9, -8, -7, -5, -4, -60, -13],dur=[rest(1.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a18():
	d0 >> pluck([-60, -2, -60, (-2, 5, 14), (-2, 5, 14), (-5, 3, 15), -60, 10, 7, 3, 4, 5, 7, 8, -60, 0],dur=[rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d1 >> pluck([-60, -2, -60, (-2, 8), (-2, 8), (-2, 7), -60, 10, 7, 3, 4, 5, 7, 8, -60, 0],dur=[rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d2 >> pluck([-60, -2, -60, -2, -2, 3, -60, -2, -5, -9, -8, -7, -5, -4, -60, 0],dur=[rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d3 >> pluck([-60, -14, -60, -14, -14, -9, -60, -2, -5, -9, -8, -7, -5, -4, -60, -12],dur=[rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d4 >> pluck([-60],dur=[rest(16)])
@structure
def a19():
	d0 >> pluck([-60, -1, -60, (-5, 2, 11), (-5, 2, 11), 1, -60, (2, 9, 18), (2, 9, 18), 19, 19, 21, 19, 18, 19, 22, 21, 21, 19],dur=[rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,2.0 ,0.5 ,0.0 ,0.0 ,0.0 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([-60, -1, -60, (-5, 5), (-5, 5), 1, -60, (2, 12), (2, 12), (-5, 2, 10), (2, 10), (2, 10), (2, 10), (2, 10), (3, 12), (3, 12), (3, 12), (3, 12), (3, 12), (3, 12), (2, 10), (2, 10)],dur=[rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-60, -1, -60, -5, -5, 1, -60, 2, 2, (2, 10), (2, 10), 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 7, 7],dur=[rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-60, -13, -60, -17, -17, -11, -60, -10, -10, 7, 7, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5],dur=[rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a20():
	d0 >> pluck([19, 24, 24, 26, 24, 23, 24, 27, 26, 26, 24, 12, 12, 21, 21, 19, 18, 24, 24],dur=[1.0 ,2.0 ,0.5 ,0.0 ,0.0 ,0.0 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d1 >> pluck([(2, 11), (2, 11), (3, 12), (3, 12), (3, 12), (3, 12), (3, 12), (3, 12), 11, 11, 11, 11, 11, 11, 12, 3, 3, 3, 3, 12, 12, 12, 12, 12, 12, 12, 12, 9, 9, 9, 9, 9],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([7, 7, 7, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-7, -7, -9, -9, -12, -12, -5, -5, -17, -17, -16, -4, -4, -4, -4, -4, -5, -5, -6, -6, -6, -6, -6, -6, -9, -9, -10, 2, 2, 2, 2, 2],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a21():
	d0 >> pluck([22, 22, 21, 19, 18, 19, 21, 22, 10, 19, 18, 27, 27, 26, 24, 30],dur=[1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([7, 7, 16, 16, 13, 13, 14, 14, 12, 12, 10, 14, 14, 12, 10, 14, -2, 7, 2, 9, 9, 9, 9, 9, 10, 10, -60, 12, 12, 12, 12, 12],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([7, 7, 7, 7, 10, 10, 10, 10, 9, 9, 2, 2, 2, 2, 2, 2, -2, -5, -10, 6, 6, 6, 6, 6, 7, 7, -60, 2, 2, 2, 2, 2],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([3, 3, 1, 1, 3, 3, 2, 2, -10, -10, -5, -2, -2, -6, -5, 2, -60, -5, -10, 0, 0, 0, 0, 0, -2, -2, -60, -3, -3, -3, -3, -3],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a22():
	d0 >> pluck([31, -3, 15, 15, 14, 6, 7, (-10, 2), (-10, 2), (-10, 2), (-10, 2), (-10, 2), (-10, 2), 26],dur=[1.0 ,3.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d1 >> pluck([10, 10, -60, 15, 15, 15, 12, 12, 9, 9, 10, -2, -2, -2, 0, 0, 0, 0, -2, -60, -17, -17, -14, -15, (-10, 2), -5, -2, 2, 7, 10],dur=[0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([2, 2, -60, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -3, -3, -3, -3, -5, (-10, 2), -60, -15, (-10, 2), (-10, 2)],dur=[0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(3.0) ,2.0 ,0.5 ,0.5])
	d3 >> pluck([-5, -5, -60, -12, -12, -12, -9, -9, -12, -12, -22, -10, -10, -10, -22, -10, -10, -10, -17, -60, (-10, 2), (-10, 2), (-10, 2), -17],dur=[0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,rest(2.5) ,0.5 ,0.5 ,0.5 ,1.0])
@structure
def a23():
	d0 >> pluck([27, 26, 26, (-10, 2), (-10, 2), (-10, 2), (-10, 2), (-10, 2), (-10, 2), 26, 27, 26, 26, -2, -3, -3, -5, -12, 5, 3, 3],dur=[0.75 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,0.75 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([14, 7, 6, -60, -15, -15, -12, -14, (-10, 2), 6, 9, 7, 6, 9, 14, 6, 7, -60, -14, -10, -12, -60, -5, -13, -13],dur=[0.5 ,0.5 ,1.0 ,rest(1.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.5) ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,1.5 ,0.5])
	d2 >> pluck([(-10, 2), (-10, 2), (-10, 2), (-10, 2), -60, -14, (-10, 2), (-10, 2), (-10, 2), (-10, 2), (-10, 2), -5, -60],dur=[0.5 ,0.5 ,0.5 ,0.5 ,rest(3.0) ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(6.0)])
	d3 >> pluck([-60, -15, -60, (-10, 2), (-10, 2), (-10, 2), -15, -60, -14, -60],dur=[rest(1.0) ,2.0 ,rest(2.5) ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,rest(6.0)])
@structure
def a24():
	d0 >> pluck([2, 2, 11, 14, 12, 11, 14, 17, 15, 14, 23, 26, 24, 23, 23, 23, 24, 24, 26, 24, 23, 24, 27, 26, 26, 24],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,2.0 ,0.5 ,0.0 ,0.0 ,0.0 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([-4, -5, -5, -1, 0, 2, 11, 14, 12, 11, 17, 14, 15, 17, 5, 7, 8, 7, (-5, 3), (-5, 3), (-5, 3), (-5, 3), (-5, 3), (-5, 3), (-5, 3), 0, 3, 7, 12, 15],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-60, 2, -7, -60, 5, 2, 3, 5, 8, 5, 7, 8, 2, 2, 3, (-5, 3), -60, -17],dur=[rest(1.5) ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,rest(3.0) ,3.0])
	d3 >> pluck([-60, -17, -17, -16, -17, -19, -21, -60, (-5, 3), (-5, 3), (-5, 3), (-5, 3), (-5, 3)],dur=[rest(5.0) ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(3.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a25():
	d0 >> pluck([19, 12, 26, 26, 27, 26, 24, 26, 29, 27, 27, 26, 25, 16, 19, 17, 17, 16, 16, 16, 25, 24, 24],dur=[0.5 ,0.5 ,2.0 ,0.5 ,0.0 ,0.0 ,0.0 ,0.5 ,0.5 ,0.5 ,2.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([(-5, 3), (-5, 3), 11, (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), 11, 14, 12, 11, 17, 20, 11, 10, -60, 7, 10, 8, 8, 7, 7],dur=[0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.5) ,0.5 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5])
	d2 >> pluck([-16, -17, (-5, 5), (-5, 5), -60, -17, (-5, 5), (-5, 5), (-5, 4), -60],dur=[0.75 ,0.25 ,0.5 ,0.5 ,rest(3.0) ,3.0 ,0.5 ,0.5 ,1.0 ,rest(6.0)])
	d3 >> pluck([-60, -17, -60, (-5, 5), (-5, 5), (-5, 5), (-5, 5), (-5, 5), -16, -17, -17, -60],dur=[rest(1.0) ,1.0 ,rest(3.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.75 ,0.25 ,1.0 ,rest(6.0)])
@structure
def a26():
	d0 >> pluck([22, 22, 31, 28, 29, 31, 25, 22, 24, 25, 22, 19, 20, 22, 13, 12, 10, 8, 20, 20, 19, 19, 17, 17, 15, 15, 13, 13, 12],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([13, 12, 12, 10, -8, 22, 19, 20, 22, 13, 10, 12, 13, 10, 8, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-60, -8, -5, -7, -60, -5, -2, -4, -5, 4, 7, 5, 4, -8, -8, -8, -7, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4],dur=[rest(1.5) ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-60, -8, -5, -7, -8, -5, -2, -4, -5, -12, -12, -12, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11, -11],dur=[rest(3.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
@structure
def a27():
	d0 >> pluck([12, 11, 12, (-4, 5, 12), (7, 16, 24), -60, (-4, 5, 12), (-5, 4, 12), (-4, 5, 12), (8, 17, 24), (-5, 4, 12), (7, 16, 24), (-4, 5, 12), (8, 17, 24), (-5, 4, 12), (7, 16, 24), -60],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0)])
	d1 >> pluck([8, 5, (-5, 4, 12), (-12, 0), (-5, 4, 12), -60, (-12, 0), (-12, 0), (-12, 0), -60, (-12, 0), -60, (-12, 0), -60, (-12, 0), 12],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,2.0])
	d2 >> pluck([-7, -4, (-12, 0), -19, (-12, 0), -60, -19, -12, -19, -60, (-24, -12), -60, -19, -60, (-24, -12), -60],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,1.0 ,rest(2.0)])
	d3 >> pluck([-11, -11, -12, -60, -12, -60],dur=[0.5 ,0.5 ,1.0 ,rest(1.0) ,1.0 ,rest(12.0)])
@structure
def a28():
	d0 >> pluck([12, -3, 0, 5, 0, 4, 0, -2, 0, 18, 19, 21, -2, 24, 24, 24, 23, 24, 21, 17, 12, 7, 0, 5, 0, 5, 0, 5, 24, 24, 24, 23, 24],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.0 ,0.0 ,0.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([-60, -7, 21, 19, -7, 0, -2, -3, 0, 5, 9, 7, 0, 22, 21, -12, 5, 0, 4, 0],dur=[rest(1.0) ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-60, 12, 21, -60, -12, -60, 19, 17, 12, -8, -60, -7, -60, 21, 19],dur=[rest(1.0) ,0.5 ,0.5 ,rest(1.0) ,1.0 ,rest(1.0) ,2.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(1.0) ,2.0 ,1.0])
	d3 >> pluck([-60, 4, -60, 12, 22, -60, 0, -60],dur=[rest(5.5) ,0.5 ,rest(3.0) ,0.5 ,0.5 ,rest(3.5) ,0.5 ,rest(2.0)])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(a5, start + 80)
Clock.schedule(a6, start + 96)
Clock.schedule(a7, start + 112)
Clock.schedule(a8, start + 128)
Clock.schedule(a9, start + 144)
Clock.schedule(a10, start + 160)
Clock.schedule(a11, start + 176)
Clock.schedule(a12, start + 192)
Clock.schedule(a13, start + 208)
Clock.schedule(a14, start + 224)
Clock.schedule(a15, start + 240)
Clock.schedule(a16, start + 256)
Clock.schedule(a17, start + 272)
Clock.schedule(a18, start + 288)
Clock.schedule(a19, start + 304)
Clock.schedule(a20, start + 320)
Clock.schedule(a21, start + 336)
Clock.schedule(a22, start + 352)
Clock.schedule(a23, start + 368)
Clock.schedule(a24, start + 384)
Clock.schedule(a25, start + 400)
Clock.schedule(a26, start + 416)
Clock.schedule(a27, start + 432)
Clock.schedule(a28, start + 448)
Clock.schedule(lambda : Clock.clear(), start + 464)
