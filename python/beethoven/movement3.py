Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([5, 5, 4, 6, 7, 7, 6, 8, 9, 11, 12],dur=[3.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d1 >> pluck([0, 0, 2, 2, 2, 4, 4, 8, 9],dur=[3.0 ,2.0 ,1.0 ,3.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d6 >> pluck([-3, -5, 0, -2, -3, 2, 0, 4, 4],dur=[3.0 ,2.0 ,1.0 ,3.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d9 >> pluck([-19, -15, -14, -12, -14, -15, -17, -14, -12, -10, -12, -13, -15, -12, -8, -3],dur=[1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([-60, 14, 12, 9, 14, 11, 16, -60, 2, 0, -3, 2, -1, 0, -60, 12],dur=[rest(2.0) ,3.0 ,0.0 ,0.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,3.0 ,0.0 ,0.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,2.0])
	d1 >> pluck([-60, 11, 12, -60, -1, 0, -60, 0],dur=[rest(2.0) ,3.0 ,1.0 ,rest(2.0) ,3.0 ,1.0 ,rest(2.0) ,2.0])
	d6 >> pluck([-60, 5, 4, -60, -7, -8, -7, -8, -60, 3],dur=[rest(2.0) ,3.0 ,1.0 ,rest(2.0) ,3.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,2.0])
	d9 >> pluck([-60, -5, 0, -60, -17, -12, -60, -4],dur=[rest(2.0) ,3.0 ,1.0 ,rest(2.0) ,3.0 ,1.0 ,rest(2.0) ,2.0])
@structure
def a2():
	d0 >> pluck([15, 15, 13, 13, 13, 12, 12, 8, 12, 12, 10, 10, 10, 8, 8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([8, 7, 7, 7, 8, 8, 0, 5, 4, 4, 4, 5, 5],dur=[1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d6 >> pluck([3, 3, -2, -2, -4, -4, 0, 0, 0, 0, 0, 0],dur=[1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d9 >> pluck([0, -2, -9, -4, -16, -7, -4, -5, -12, -7, -19],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
@structure
def a3():
	d0 >> pluck([17, 17, 15, 17, 18, 18, 17, 19, 20, 20],dur=[3.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0])
	d1 >> pluck([13, 13, 12, 14, 15, 15, 14, 16, 17, 17],dur=[3.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0])
	d6 >> pluck([1, 5, 6, 8, -60, 3, 6, 8, 10, -60, 5, 8, 10, 12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0])
	d9 >> pluck([-60, -4, -6, -7, -9, -60, -2, -4, -5, -7, -4, -2, 0],dur=[rest(3.0) ,2.0 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a4():
	d0 >> pluck([19, 20, 22, 22, 20, 20, 19, -60, 23, 24, 20, -60, 23, 24, 19, -60],dur=[1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,0.0 ,1.0 ,1.0 ,rest(1.0) ,0.0 ,1.0 ,1.0 ,rest(1.0)])
	d1 >> pluck([16, 17, 19, 19, 17, 17, 16, -60, 17, -60, 16, -60],dur=[1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,rest(2.0) ,1.0 ,rest(1.0)])
	d6 >> pluck([12, 10, 8, 7, 5, 4, 5, 1, -1, 0, 12, -60, 0, 12, -60, 0, 12],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0])
	d9 >> pluck([0, -2, -4, -5, -7, -8, -7, -11, -13, -12, 0, -60, -12, 0, -60, -12, 0],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0])
@structure
def a5():
	d0 >> pluck([23, 24, 20, -60, 23, 24, 19, 4, 5, 0, 4, 5, 7, 16, 17, 12, 16, 17],dur=[0.0 ,1.0 ,1.0 ,rest(1.0) ,0.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([-60, 5, -60, 0, -60, 7, -60, 12, -60, 19, -60],dur=[rest(1.0) ,1.0 ,rest(2.0) ,1.0 ,rest(2.0) ,1.0 ,rest(2.0) ,1.0 ,rest(2.0) ,1.0 ,rest(2.0)])
	d6 >> pluck([-60, 0, 12, -60, 4, -60, -8, 0, 2, 4, -60, -2, -5, -7],dur=[rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0])
	d9 >> pluck([-60, -12, 0, -60, -12, -60, -5, -8, -10, -12, -60, -17, -20, -22],dur=[rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0])
@structure
def a6():
	d0 >> pluck([19, 7, 9, 4, 7, 9, 10, 19, 21, 22, 4, 4, 5, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0])
	d1 >> pluck([4, -60, 10, -60, 16, -60, -5, -5, -3, -4, -5],dur=[1.0 ,rest(2.0) ,1.0 ,rest(2.0) ,1.0 ,rest(3.0) ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d6 >> pluck([-8, -60, 10, 7, 5, 4, -60, 0, 0, 0, 2, 2],dur=[1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,rest(3.0) ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d9 >> pluck([-24, -60, -5, -8, -10, -12, -60, -12, -14, -17, -19, -15, -13, -12],dur=[1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a7():
	d0 >> pluck([4, 6, 7, 7, 6, 8, 9, 11, 12, -60, 14],dur=[1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,rest(2.0) ,2.0])
	d1 >> pluck([-5, 0, 0, -1, -2, -3, 2, 2, 0, 8, 9, -60, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,2.0])
	d6 >> pluck([0, 2, 2, 4, 4, 2, 4, 4, 4, 4, -60, 5],dur=[1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,rest(2.0) ,2.0])
	d9 >> pluck([-12, -14, -15, -17, -13, -11, -10, -12, -13, -15, -12, -8, -3, -60, -10, -7],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0])
@structure
def a8():
	d0 >> pluck([16, 17, -60, 17, 19, 21, -60, 19, 17, 14, 19, 16, 21, -60],dur=[1.0 ,1.0 ,rest(2.0) ,2.0 ,1.0 ,1.0 ,rest(2.0) ,3.0 ,0.0 ,0.0 ,0.0 ,0.0 ,1.0 ,rest(2.0)])
	d1 >> pluck([13, 14, -60, 12, 16, 17, -60, 16, 17, -60],dur=[1.0 ,1.0 ,rest(2.0) ,2.0 ,1.0 ,1.0 ,rest(2.0) ,3.0 ,1.0 ,rest(2.0)])
	d6 >> pluck([9, 9, -60, 9, 12, 12, -60, 10, 9, -60],dur=[1.0 ,1.0 ,rest(2.0) ,2.0 ,1.0 ,1.0 ,rest(2.0) ,3.0 ,1.0 ,rest(2.0)])
	d9 >> pluck([-3, 2, -60, -7, -3, 0, 5, -60, 0, 5, -60],dur=[1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,3.0 ,1.0 ,rest(2.0)])
@structure
def a9():
	d0 >> pluck([7, 5, 2, 7, 4, 5, -60, 4, 5, 12, 12, -60, 4, 5],dur=[3.0 ,0.0 ,0.0 ,0.0 ,0.0 ,1.0 ,rest(3.0) ,2.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,2.0 ,1.0])
	d1 >> pluck([4, 5, -60, -2, -3, -60, -2, -3],dur=[3.0 ,1.0 ,rest(3.0) ,2.0 ,1.0 ,rest(3.0) ,2.0 ,1.0])
	d6 >> pluck([-2, -3, -2, -3, -60, -5, -7, -5, -7, -60, -5, -7, -5, -7],dur=[3.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,3.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,3.0 ,0.0 ,0.0 ,1.0])
	d9 >> pluck([-12, -7, -60, -17, -19, -17, -19, -60, -17, -19, -17, -19],dur=[3.0 ,1.0 ,rest(2.0) ,3.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,3.0 ,0.0 ,0.0 ,1.0])
@structure
def a10():
	d0 >> pluck([17, 17, -60, 4, 5, 24, 24, 15, 14, 2, 15, 3, 14, -60, 16, -60],dur=[1.0 ,1.0 ,rest(1.0) ,2.0 ,1.0 ,1.0 ,1.0 ,3.0 ,0.0 ,0.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,1.0 ,rest(1.0)])
	d1 >> pluck([-60, -2, -3, 12, 12, 3, 2, -60, 4, -60],dur=[rest(3.0) ,2.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,rest(2.0) ,1.0 ,rest(1.0)])
	d6 >> pluck([-60, -5, -7, -5, -7, -60, -12, 6, 6, 7, 2, 2, -60, -2],dur=[rest(2.0) ,3.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d9 >> pluck([-60, -17, -19, -17, -19, -60, -15, -3, -3, -2, -14, -14, -60, -12],dur=[rest(2.0) ,3.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
@structure
def a11():
	d0 >> pluck([-60, 17, 24, 24, 15, 14, 2, 15, 3, 14, -60, 16, -60, 17],dur=[rest(1.0) ,1.0 ,1.0 ,1.0 ,3.0 ,0.0 ,0.0 ,0.0 ,0.0 ,1.0 ,rest(2.0) ,1.0 ,rest(2.0) ,3.0])
	d1 >> pluck([-60, 5, 12, 12, 3, 2, -60, 4, -60, 9, 8],dur=[rest(1.0) ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,rest(2.0) ,1.0 ,rest(2.0) ,2.0 ,1.0])
	d6 >> pluck([-2, -3, -60, -12, 6, 6, 7, 2, 2, -60, -2, -2, -3, 0, 2],dur=[1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d9 >> pluck([-12, -7, -60, -15, -3, -3, -2, -14, -14, -60, -12, -12, -7, -3, -1],dur=[1.0 ,1.0 ,rest(2.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a12():
	d0 >> pluck([17, 16, 18, 19, 19, 18, 20, 21, 21, 21],dur=[1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,3.0 ,3.0 ,1.0])
	d1 >> pluck([7, 12, 10, 14, 16, 16, 14, 14, 12, 13, 14, 16, 17, 19, 17],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d6 >> pluck([4, 2, 0, 2, 10, 9, 9, 4, 4, 9, 11, 13, 14, 16, 14],dur=[2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d9 >> pluck([0, -2, -3, -5, -2, 1, 2, 0, -1, -3, 7, 5, 4, 2, 1, 2],dur=[2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a13():
	d0 >> pluck([21, 22, 24, 26, 27, 26, 22, 21, 19, 26, 24, 22, 21, 19, 17, 16],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([18, 19, 21, 22, 24, 22, 19, 17, 16, 22, 21, 19, 17, 16, 14, 12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d6 >> pluck([3, 2, 0, -2, -3, -2, 10, 11, 12, -8, -7, -5, -3, -2, 0, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d9 >> pluck([0, -2, -3, -5, -6, -5, -2, -1, 0, -20, -19, -17, -15, -14, -12, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a14():
	d0 >> pluck([14, 12, 10, 9, 7, 10, 4, 5, 9, 11, 12, 17, 21, 23],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([10, 9, 4, 5, 2, 7, -2, -3, -3, -1, 0, 5, 9, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0])
	d6 >> pluck([4, 5, 0, 0, -2, -2, -5, -3, -60, -4, -4, -5, -8, -3, -60, -4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
	d9 >> pluck([-8, -7, -5, -3, -14, -17, -12, -19, -60, -7, -7, -8, -12, -7, -60, -19],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0])
@structure
def a15():
	d0 >> pluck([24, 24, 24, 24, 24, 24, 21, 21, 17, -60, 11, 11, 12],dur=[3.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,0.0 ,0.0 ,1.0])
	d1 >> pluck([12, 12, 12, 12, 12, 12, 9, 9, 5, -60, 12],dur=[3.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0])
	d6 >> pluck([-4, -5, -8, -3, -5, -8, -3, 7, 4, 9, 0, 0, -3, -60, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0])
	d9 >> pluck([-19, -20, -24, -19, -20, -24, -19, -8, -12, -7, -19, -19, -19, -60, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(2.0) ,1.0])
@structure
def a16():
	d0 >> pluck([-60, 0, 11, 11, 12, -60, 0, 11, 11, 12, 0, 12, 0, 12, 0, 1, 3, 1, 0, 1, 3, 5, 6, 8, 10],dur=[rest(1.0) ,1.0 ,0.0 ,0.0 ,1.0 ,rest(1.0) ,1.0 ,0.0 ,0.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([-60, 0, 12, -60, 0, 12, 0, 12, 0, 12, 0, (-4, 5), (-4, 5)],dur=[rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,2.0])
	d6 >> pluck([-60, -12, 0, -60, -12, 0, -12, 0, -12, 0, -12, -11, 1],dur=[rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,2.0])
	d9 >> pluck([-60, -24, -12, -60, -24, -12, -24, -12, -24, -12, -24, -23, -23],dur=[rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,2.0])
@structure
def a17():
	d0 >> pluck([12, 13, 15, 17, 18, 17, 15, 13, 12, 10, 8, 6, 5, 3, 1, 3, 1, 0, 1, 5, 5, 6, 8, 10, 12, 13, 15, 17, 18, 17, 15, 13],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([(-4, 5), (-4, 5), (-4, 5), (-4, 6), (-4, 5), (-4, 5), (-4, 5)],dur=[1.0 ,3.0 ,2.0 ,1.0 ,3.0 ,3.0 ,3.0])
	d6 >> pluck([1, 1, 1, 0, 1, 1, 1],dur=[1.0 ,3.0 ,2.0 ,1.0 ,3.0 ,3.0 ,3.0])
	d9 >> pluck([-23, -23, -23, -23, -23, -23, -23],dur=[1.0 ,3.0 ,2.0 ,1.0 ,3.0 ,3.0 ,3.0])
@structure
def a18():
	d0 >> pluck([12, 10, 8, 6, 5, 3, 1, 5, 4, 5, 4, 5, 1, 5, 0, 5, -1, 5, 0, 5, 8, 12, 0, 12, 5, -60, 15],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(2.0) ,1.0])
	d1 >> pluck([(-4, 5), (-4, 6), (-4, 5), 1, 1, 1, 0, -1, 0, -60, 0, 5, -60, 9],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,rest(2.0) ,1.0])
	d6 >> pluck([1, 0, 1, 1, 1, 1, 0, -1, 0, -60, -12, -7, -60, 5],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,rest(2.0) ,1.0])
	d9 >> pluck([-23, -23, -23, -11, -11, -11, -12, -13, -12, -60, -24, -19, -60],dur=[2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,rest(3.0)])
@structure
def a19():
	d0 >> pluck([15, 15, 15, 15, 14, 14],dur=[2.0 ,3.0 ,3.0 ,3.0 ,3.0 ,2.0])
	d1 >> pluck([9, 9, 9, 9, 8, 8],dur=[2.0 ,3.0 ,3.0 ,3.0 ,3.0 ,2.0])
	d6 >> pluck([-60, -7, 5, -60, -7, 5, -7, 5, -7, 5, -7, 5, 5],dur=[rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,2.0])
	d9 >> pluck([-60, -2, -60, -14, -2, -60],dur=[rest(11.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,rest(1.0)])
@structure
def a20():
	d0 >> pluck([14, 14, 14, 13, (7, 12), (7, 12)],dur=[1.0 ,3.0 ,3.0 ,3.0 ,3.0 ,3.0])
	d1 >> pluck([8, 8, 8, 10, 10, 8],dur=[1.0 ,3.0 ,3.0 ,3.0 ,3.0 ,3.0])
	d6 >> pluck([5, 5, 5, 7, -5, 7, -60, 5, -7, 5],dur=[1.0 ,3.0 ,3.0 ,1.0 ,1.0 ,1.0 ,rest(3.0) ,1.0 ,1.0 ,1.0])
	d9 >> pluck([-14, -2, -14, -2, -14, -2, -14, -60, -8, -20, -8, -60],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,rest(3.0) ,1.0 ,1.0 ,1.0 ,rest(3.0)])
@structure
def a21():
	d0 >> pluck([(5, 12), (4, 12), -60, 10, 11, 12],dur=[3.0 ,1.0 ,rest(11.0) ,0.0 ,0.0 ,1.0])
	d1 >> pluck([9, 7, -60, 12],dur=[3.0 ,1.0 ,rest(11.0) ,1.0])
	d6 >> pluck([-60, 0, -60, -12, 0, -60, -12, 0, -12, 0, -12, 0, -12, 0],dur=[rest(3.0) ,1.0 ,rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d9 >> pluck([-7, -19, -7, -12, -60, -24, -12, -60, -24, -12, -24, -12, -24, -12, -24, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a22():
	d0 >> pluck([-60, 0, 10, 11, 12, -60, 0, 10, 11, 12, 0, 12, 1, 13, 1, 2, 7, 10, 7, 14, 10, 19, 14, 22, 21],dur=[rest(1.0) ,1.0 ,0.0 ,0.0 ,1.0 ,rest(1.0) ,1.0 ,0.0 ,0.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([-60, 0, 12, -60, 0, 12, 0, 12, 1, 13, 1, 2, -2],dur=[rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,2.0])
	d6 >> pluck([-60, -12, 0, -60, -12, 0, -12, 0, -11, 1, -11, -10, (-10, -5)],dur=[rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,2.0])
	d9 >> pluck([-60, -24, -12, -60, -24, -12, -24, -12, -23, -11, -23, -22, -22],dur=[rest(1.0) ,1.0 ,1.0 ,rest(1.0) ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,2.0])
@structure
def a23():
	d0 >> pluck([19, 17, 15, 14, 12, 10, 9, 7, 6, 7, 6, 7, 9, 6, 2, 7, 10, 7, 14, 10, 19, 14, 22, 21, 19, 17, 15, 14, 12, 10, 9, 7],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([-2, -2, -2, 0, -2, -2, -2],dur=[1.0 ,3.0 ,2.0 ,1.0 ,3.0 ,3.0 ,3.0])
	d6 >> pluck([(-10, -5), (-10, -5), (-10, -5), (-10, -3), (-10, -5), (-10, -5), (-10, -5)],dur=[1.0 ,3.0 ,2.0 ,1.0 ,3.0 ,3.0 ,3.0])
	d9 >> pluck([-22, -22, -22, -22, -22, -22, -22],dur=[1.0 ,3.0 ,2.0 ,1.0 ,3.0 ,3.0 ,3.0])
@structure
def a24():
	d0 >> pluck([6, 7, 6, 7, 9, 6, -5, 11, 14, 11, 17, 14, 23, 17, 26, 24, 23, 21, 19, 17, 16, 14, 17, 14, 12, 11, 14, 11, 12, 16, -5, 11],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([-2, 0, -1, -1, -2, -2, 0, -1],dur=[2.0 ,1.0 ,3.0 ,3.0 ,3.0 ,2.0 ,1.0 ,1.0])
	d6 >> pluck([(-10, -5), (-10, -3), -10, -10, -10, -10, -8, -10],dur=[2.0 ,1.0 ,3.0 ,3.0 ,3.0 ,2.0 ,1.0 ,1.0])
	d9 >> pluck([-22, -22, -17, -17, -17, -17, -17, -17],dur=[2.0 ,1.0 ,3.0 ,3.0 ,3.0 ,2.0 ,1.0 ,1.0])
@structure
def a25():
	d0 >> pluck([14, 11, 17, 14, 23, 17, 26, 24, 23, 21, 19, 17, 16, 14, 17, 14, 12, 11, 14, 11, 12, 16, 0, 12, 16, 12, 19, 16, 22, 21, 19, 17],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d1 >> pluck([-1, -1, -2, -2, 0, (-5, 4), (-5, 4)],dur=[2.0 ,3.0 ,3.0 ,2.0 ,1.0 ,3.0 ,2.0])
	d6 >> pluck([-10, -10, -10, -10, -8, -12, -12],dur=[2.0 ,3.0 ,3.0 ,2.0 ,1.0 ,3.0 ,2.0])
	d9 >> pluck([-17, -17, -17, -17, -12, -24, -24],dur=[2.0 ,3.0 ,3.0 ,2.0 ,1.0 ,3.0 ,2.0])
@structure
def a26():
	d0 >> pluck([16, 14, 12, 10, 9, 7, 10, 7, 5, 4, 7, 4, 5, 9, 0, 12, 16, 12, 19, 16, 22, 21, 19, 17, 16, 14, 12, 11, 14, 12, 11, 14],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
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
Clock.schedule(lambda : Clock.clear(), start + 432)
