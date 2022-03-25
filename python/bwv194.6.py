Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([10, 12, 14, 12, 10, 9, 7, 5, 10, 12, 14, 15, 14, 12, 10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([5, 5, 5, 4, 2, 0, 5, 5, 4, 5, 2, 5, 5, 5, 5, 5, 5],dur=[1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([2, -2, -2, -3, -5, -7, -5, -3, -2, 0, -5, -3, -2, -3, -2, 0, 0, -2, -2, -3, 2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.75 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
	d3 >> pluck([-2, -7, -14, -12, -10, -8, -7, -12, -19, -5, -7, -9, -10, -12, -14, -15, -14, -19, -14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
@structure
def a1():
	d0 >> pluck([14, 15, 17, 19, 17, 15, 14, 17, 17, 19, 17, 15, 14, 12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([10, 10, 9, 7, 9, 10, 9, 10, 10, 10, 10, 9, 7, 5, 5],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([5, 7, 0, 2, 3, 5, 5, 5, 2, 2, 3, 2, -2, -2, -3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-2, -3, -5, -7, -12, -10, -9, -7, -14, -14, -12, -10, -14, -9, -10, -9, -7, -5, -3, -2, -7],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
@structure
def a2():
	d0 >> pluck([14, 15, 17, 15, 14, 10, 12, 14, 10, 14, 17, 15, 14, 12, 14],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([5, 10, 8, 7, 5, 7, 6, 7, 6, 4, 6, 2, 7, 8, 7, 2, 3, 5, 5],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-2, 0, 2, 0, -2, -2, -3, -5, -3, -2, -3, -5, -3, -5, -2, -2, -2, -2, -3, -2],dur=[0.5 ,0.5 ,1.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-2, -14, -12, -10, -9, -9, -14, -5, -5, -7, -9, -10, -9, -7, -5, -7, -9, -10, -12, -14],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
