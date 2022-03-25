Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([4, 4, 11, 11, 12, 14, 11, 7, 9, 11, 12, 11, 9, 9, 7, 9],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([-1, -1, 4, 6, 7, 9, 6, 7, 6, 4, 6, 7, 7, 6, 4, 6, 7, 7, 6, 6, 4, 2, 9],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,2.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-5, -5, -3, -1, 4, 2, 2, 0, 2, 0, 2, 4, 2, 2, 4, 2, 0, -1, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,2.0 ,1.0 ,0.75 ,0.25 ,1.0 ,1.0])
	d3 >> pluck([-8, -6, -5, -8, -6, -10, -5, 0, -1, -3, -5, -3, -10, -5, -11, -10, -8, -6],dur=[1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([11, 9, 7, 6, 4, 2, 7, 6, 7, 9, 11, 9, 7, 6, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0])
	d1 >> pluck([9, 7, 6, 4, -3, 2, 2, 1, -1, 1, -3, 4, 6, 4, 4, 4, 3, 4],dur=[0.5 ,1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([2, 2, 1, 2, -3, -1, -5, -8, -3, -5, -6, -1, -1, -1, -1, 0, 0, -1, -3, -5],dur=[1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,2.0])
	d3 >> pluck([-5, -10, -8, -6, -5, -8, -3, -15, -10, -8, -9, -8, -17, -15, -13, -12],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
