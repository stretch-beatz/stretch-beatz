Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([9, 9, 11, 12, 14, 11, 12, 12, 11, 12, 14, 16, 14, 12, 11, 9, 11, 11, 9, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,3.0])
	d1 >> pluck([4, 2, 4, 5, 4, 2, 0, 2, 9, 6, 2, 7, 4, 9, 8, 11, 8, 4, 9, 9, 11, 8, 4],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0])
	d2 >> pluck([0, -1, 0, 2, 0, -1, -3, 0, -1, -3, -1, 4, 0, 5, 4, 2, -1, -3, -1, 0, 2, 4, 5, -1, 2, 0],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-15, -3, -4, -3, -6, -5, -3, -3, -5, -3, -1, -4, -3, -7, -8, -10, -8, -15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,3.0])
@structure
def a1():
	d0 >> pluck([16, 14, 12, 11, 9, 11, 11, 12, 14, 16, 16, 14, 12, 11, 12, 11],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d1 >> pluck([9, 7, 6, 8, 9, 9, 8, 9, 14, 8, 8, 9, 7, 7, 12, 11, 9, 7, 6, 7],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([0, 0, -1, 4, 5, -1, 4, 4, -3, 4, 4, 4, 2, 0, 2, 4, -3, 2, 2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-15, -13, -12, -10, -8, -7, -8, -8, -3, -1, 0, -1, 0, -1, -3, -5, -6, -8, -10, -5],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,3.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([11, 12, 14, 16, 16, 14, 12, 11, 12, 11, 16, 14, 12, 11, 9, 11, 11, 9, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,3.0])
	d1 >> pluck([11, 9, 7, 7, 7, 6, 8, 9, 8, 12, 11, 9, 8, 9, 9, 6, 8, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0])
	d2 >> pluck([4, 4, -1, 0, -1, -3, 4, 2, -3, 4, -3, 2, 4, 5, 2, 4, 2, 1, 1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,3.0])
	d3 >> pluck([-4, -3, -5, -7, -5, -7, -8, -10, -12, -10, -8, -7, -10, -8, -12, -7, -8, -10, -7, -8, -10, -8, -15],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
