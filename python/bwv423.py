Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([14, 12, 10, 9, 10, 9, 7, 6, 2, 14, 14, 15, 12, 14, 12, 10, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d1 >> pluck([7, 9, 10, 9, 7, 6, 2, 7, 5, 3, 2, -3, -2, 0, 2, -5, 7, 9, 7, 6],dur=[0.5 ,0.25 ,0.25 ,1.5 ,1.0 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,2.0])
	d2 >> pluck([-2, 0, 2, 3, 2, 2, 2, 0, -2, 2, 0, -2, -3, -6, -5, 7, 5, 3, 2, 0, -2, -3, 2, 2, 2],dur=[0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,0.75 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
	d3 >> pluck([-5, -6, -5, -10, -17, -12, -10, -22, -17, -15, -14, -17, -12, -10, -9, -18, -17, -10],dur=[1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
@structure
def a1():
	d0 >> pluck([14, 12, 10, 9, 10, 9, 7, 6, 2, 14, 14, 15, 12, 14, 12, 10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([6, 7, 9, 7, 6, 7, 5, 4, 2, -3, -2, 2, 5, 7, 5, 5, 5, 3, 2],dur=[1.0 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0 ,0.75 ,0.25 ,2.0])
	d2 >> pluck([-3, -5, 2, 2, 2, 2, 4, -3, -3, -6, -7, -2, 2, 0, -2, 0, 0, -2, -3, -7],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,2.0])
	d3 >> pluck([-10, -8, -6, -5, -10, -5, -11, -10, -22, -14, -2, -3, -5, -3, -2, -7, -14],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
@structure
def a2():
	d0 >> pluck([14, 15, 17, 14, 15, 14, 14, 12, 12, 12, 14, 15, 14, 12, 10, 9, 5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([5, 7, 5, 7, 5, 3, 0, 5, 5, 5, 5, 5, 7, 6, 7, 7, 6, 7, 5, 0],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([2, 0, -2, -3, -2, -2, -3, -2, -3, -3, -3, -2, -3, -2, 0, 0, 0, -3],dur=[0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-2, -3, -5, -10, -5, -12, -10, -9, -7, -19, -7, -9, -10, -12, -5, -7, -9, -8, -7, -19],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a3():
	d0 >> pluck([14, 9, 10, 9, 10, 12, 14, 14, 14, 12, 10, 9, 7, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,2.0])
	d1 >> pluck([9, 7, 9, 7, 6, 7, 7, 6, 7, 7, 6, 7, 7, 6, 4, 6, 2],dur=[0.5 ,0.5 ,1.5 ,1.0 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,2.0])
	d2 >> pluck([-3, 2, 2, 2, 2, 3, -3, -2, 2, 3, 2, 4, -3, 2, 2, 0, -2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.75 ,0.25 ,2.0])
	d3 >> pluck([-6, -8, -6, -10, -5, -10, -5, -7, -9, -10, -5, -14, -12, -11, -10, -22, -17],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
