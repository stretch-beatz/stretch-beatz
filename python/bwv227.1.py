Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 11, 9, 7, 6, 4, 11, 13, 14, 11, 16, 15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([7, 6, 4, 3, 4, 4, 3, -1, 7, 6, 4, 2, 2, 7, 9, 11, 11],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0])
	d2 >> pluck([4, -1, 0, -6, -5, 0, -1, -3, -5, 4, 2, 1, -1, -3, -5, -3, -1, 7, 6],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-8, -10, -12, -13, -15, -13, -8, -8, -3, -5, -6, -5, -6, -8, -6, -5, -3, -1],dur=[1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
@structure
def a1():
	d0 >> pluck([16, 18, 19, 18, 18, 16, 11, 11, 9, 7, 6, 4],dur=[0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,4.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([7, 9, 11, 11, 9, 7, 7, 6, 4, 3, 4, 4, 3, -1],dur=[0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,4.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([4, 4, 4, 3, -1, 4, -1, 0, -6, -5, 0, -1, -3, -5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,4.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d3 >> pluck([0, -1, -3, -1, -13, -8, -8, -10, -12, -13, -15, -13, -8],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,4.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,2.0])
@structure
def a2():
	d0 >> pluck([11, 13, 14, 11, 16, 15, 16, 18, 19, 18, 18, 16],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,4.0])
	d1 >> pluck([7, 6, 4, 2, 2, 7, 9, 11, 11, 7, 9, 11, 11, 9, 7],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,4.0])
	d2 >> pluck([4, 2, 1, -1, -3, -5, -3, -1, 7, 6, 4, 4, 4, 3, -1],dur=[0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,4.0])
	d3 >> pluck([-8, -3, -5, -6, -5, -6, -8, -6, -5, -3, -1, 0, -1, -3, -1, -13, -8],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,4.0])
@structure
def a3():
	d0 >> pluck([11, 11, 12, 11, 9, 9, 7, 11, 13, 14, 11, 16, 14, 13, 13],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d1 >> pluck([7, 7, 9, 7, 7, 6, 2, 7, 7, 9, 7, 9, 11, 11, 11, 10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([4, 2, 2, 2, 4, 2, 0, -1, 2, 4, 2, 2, 7, 6, 7, 6, 4],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d3 >> pluck([-8, -6, -5, -6, -5, -12, -10, -17, -5, -6, -8, -6, -5, -6, -8, -13, -8, -6],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(lambda : Clock.clear(), start + 64)
