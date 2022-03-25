Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([6, 6, 6, 13, 15, 16, 15, 13, 11, 13, 15, 17],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([1, 3, 3, 1, 6, 4, 11, 6, 6, 6, 6, 8],dur=[1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d2 >> pluck([-2, -1, -1, -6, -4, -2, -1, -2, 3, -2, -1, -1],dur=[1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0])
	d3 >> pluck([-6, -1, -2, -4, -2, -4, -6, -4, -8, -6, -13, -6, -1, -3, -4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([18, 13, 16, 15, 15, 13, 13, 16, 13, 11, 8, 9],dur=[2.0 ,1.0 ,0.5 ,0.5 ,2.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d1 >> pluck([6, 8, 9, 8, 9, 8, 5, 6, 4, 8, 9, 6, 4, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0])
	d2 >> pluck([1, 1, 1, 0, -4, -3, -1, 4, 4, 6, 3, -1, -3],dur=[2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-3, -4, -6, -4, -6, -4, -11, -6, -4, -8, -3, -9, -13, -8, -11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([8, 6, 4, 4, 9, 11, 13, 11, 9, 16, 13],dur=[1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([4, 3, -1, -1, 4, 6, 8, 9, 8, 6, 11, 8, 9],dur=[1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([1, -6, -4, -4, -3, 2, 4, 6, 1, 1, -1, 4, 4],dur=[1.0 ,1.0 ,2.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-15, -13, -8, -10, -11, 1, -1, -3, -9, -7, -6, -4, -8, -3],dur=[1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
