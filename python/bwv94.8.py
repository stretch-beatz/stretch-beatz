Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 6, 4, 2, 9, 9, 11, 11, 4, 4, 9, 7, 6, 4, 2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([4, 2, 1, 2, 6, 7, 4, 4, 2, 1, 2, 4, 4, 2, 1, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0])
	d2 >> pluck([-3, -3, -5, -3, 2, 2, 2, 1, -1, -3, -3, -3, -3, -6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d3 >> pluck([-11, -10, -8, -6, -10, -5, -4, -3, -3, -5, -6, -8, -10, -11, -10, -15, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([9, 11, 11, 9, 7, 6, 4, 6, 8, 9, 11, 13, 14, 13, 11, 9, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([2, 2, 7, 7, 6, 4, 2, 4, 2, 2, 1, 6, 4, 4],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([-3, -5, -1, 1, 2, 2, 1, -3, -3, -3, -1, -3, -3, -3, -4, 1],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-6, -5, -8, -3, -15, -10, -11, -10, -11, -13, -6, -8, -10, -8, -15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
@structure
def a2():
	d0 >> pluck([9, 9, 9, 14, 12, 11, 11, 11, 11, 16, 14, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0])
	d1 >> pluck([4, 6, 4, 6, 7, 9, 6, 7, 9, 9, 8, 8, 6, 6, 4, 4],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d2 >> pluck([1, 2, 2, -3, 2, 2, 6, 4, -1, -1, -3, -3, -4, -3],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-3, 2, -10, -8, -6, -10, -5, -9, -8, -6, -8, -10, -11, -10, -8, -15],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0])
@structure
def a3():
	d0 >> pluck([9, 11, 9, 11, 13, 14, 9, 9, 7, 6, 4, 6, 7, 4, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,3.0])
	d1 >> pluck([2, 2, 2, 7, 6, 7, 6, 4, 6, 4, 2, 2, 1, -3],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,3.0])
	d2 >> pluck([-3, -5, -3, 4, 2, 4, 2, 4, -3, -1, -1, -3, -5, -6],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-6, -5, -6, -8, -14, -13, -11, -10, -11, -13, -15, -17, -15, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
