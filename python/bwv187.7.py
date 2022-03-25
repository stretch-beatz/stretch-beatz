Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 9, 10, 9, 7, 6, 7, 7, 6, 7, 9, 9, 10, 10, 9, 10, 12],dur=[1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,3.0 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,1.0])
	d1 >> pluck([2, 7, 6, 7, 7, 6, 7, 0, 2, 1, 2, 6, 7, 7],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([-2, 0, 2, 2, 3, 2, 0, -2, -3, -5, -3, -2, -6, 2, 2, 0, -2],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0 ,2.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-5, -3, -2, -3, -5, -12, -10, -9, -15, -14, -17, -10, -10, -5, -7, -8],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([12, 14, 10, 9, 7, 9, 9, 10, 12, 10, 9, 7],dur=[1.0 ,1.0 ,1.0 ,2.0 ,3.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([9, 6, 2, 3, 2, 2, 5, 5, 5, 4, 5, 7, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([-3, -5, -3, -5, -6, -2, 2, 2, 2, 0, -2, -3, -5, -3, 2],dur=[0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-6, -10, -5, -12, -10, -17, -10, -8, -7, -8, -10, -3, -10, -8, -7, -14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([7, 5, 12, 14, 16, 17, 16, 14, 13, 14],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,3.0])
	d1 >> pluck([4, 0, 9, 7, 5, 10, 9, 5, 10, 9, 9],dur=[1.0 ,3.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([0, -3, -3, -1, 1, 2, 1, 2, 4, 6],dur=[1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,2.0 ,3.0])
	d3 >> pluck([-12, -19, -7, -8, -10, -5, -7, -5, -3, -2, -5, -3, -10],dur=[1.0 ,3.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,3.0])
@structure
def a3():
	d0 >> pluck([14, 14, 12, 10, 9, 10, 12, 14, 12, 10, 9, 14, 14, 12],dur=[2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,2.0 ,1.0 ,1.0])
	d1 >> pluck([10, 10, 9, 7, 5, 7, 9, 9, 6, 7, 6, 7, 9, 10, 9],dur=[2.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([5, 5, 5, 3, 2, 2, 2, 2, 0, -2, 0],dur=[2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-14, -12, -10, -12, -14, -7, -7, -6, -10, -5, -10, -2, -6, -5, -3],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a4():
	d0 >> pluck([14, 15, 14, 12, 10, 9, 9, 10, 10, 9, 10, 12, 14, 10, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,2.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([7, 6, 7, 6, 7, 6, 6, 7, 7, 6, 7, 9, 7, 6, 7, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
	d2 >> pluck([0, 0, -2, -3, -5, 2, 2, 2, 0, 3, 2, 2, 3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-3, -15, -14, -12, -10, 2, 0, -2, -3, -5, -6, -5, -12],dur=[1.0 ,1.0 ,2.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(lambda : Clock.clear(), start + 80)
