Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([6, 11, 13, 14, 16, 13, 11, 9, 9, 11, 11, 13, 11, 13, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d1 >> pluck([1, 6, 4, 2, 6, 11, 8, 8, 6, 5, 3, 5, 6, 6, 6, 4, 2, 4, 4, 6, 4, 2],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,3.0])
	d2 >> pluck([-2, -1, -2, -1, -1, -1, -3, -4, 1, 1, 1, -1, -3, -5, -6, -6],dur=[1.0 ,1.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,3.0])
	d3 >> pluck([-6, -8, -10, -11, -13, -15, -16, -8, -15, -13, -11, -18, -6, -8, -10, -6, -5, -14, -14, -13],dur=[0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,3.0])
@structure
def a1():
	d0 >> pluck([18, 16, 14, 14, 13, 14, 13, 14, 16, 18, 18, 16, 14, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0])
	d1 >> pluck([11, 11, 11, 9, 9, 9, 9, 9, 9, 9, 8, 9, 6, 8, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([2, 4, 6, 7, 6, 4, 2, 4, 6, 7, 6, 4, 6, 4, 2, -3, 2, 1, -1, -3, -1, -3],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.25 ,0.25 ,0.5 ,1.0])
	d3 >> pluck([-13, -15, -17, -5, -6, -8, -3, -15, -10, -3, -5, -6, -8, -10, -11, -10, -8, -6, -13, -11, -10, -8, -15],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([13, 14, 16, 14, 13, 11, 11, 11, 13, 14, 13, 11, 9, 7, 6, 11, 11, 13, 10, 11],dur=[0.5 ,0.25 ,0.25 ,1.0 ,0.75 ,0.25 ,1.0 ,0.5 ,0.25 ,0.25 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
	d1 >> pluck([6, 6, 6, 7, 6, 7, 8, 6, 5, 6, 6, 4, 2, 4, 6, 7, 6, 7, 6, 4, 6, 4, 3],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,3.0])
	d2 >> pluck([1, 1, -1, 1, 3, 4, 3, 4, -1, -4, -3, -1, 1, 1, 2, -3, -3, 2, 1, 2, 4, 2, 1, -3, -6],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-14, -13, -1, -3, -5, -3, -1, -8, -7, -6, -4, -11, -6, -13, -11, -10, -11, -10, -8, -6, -8, -6, -13],dur=[1.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
