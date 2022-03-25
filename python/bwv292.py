Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 9, 11, 12, 12, 16, 14, 12, 11, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([4, 2, 4, 6, 7, 7, 5, 4, 7, 6, 7, 6, 4, 9, 2, 0, 2, 4, 0, -3, 2, 0, -1],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,2.0])
	d2 >> pluck([0, -5, 0, 2, 0, -2, -3, -5, 0, -1, -3, -1, -3, -5, -6, -5, -5, -6, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,2.0])
	d3 >> pluck([-12, -13, -15, -17, -19, -20, -19, -24, -12, -13, -13, -15, -17, -15, -13, -12, -15, -10, -17],dur=[1.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,2.0])
@structure
def a1():
	d0 >> pluck([7, 7, 9, 11, 12, 7, 7, 9, 7, 5, 4, 2, 2, 0],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([4, 4, 4, 6, 7, 7, 5, 4, 2, 4, 5, 4, 2, 4, 2, 0, -1, 0, 0, 0, -1, -5],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.25 ,0.25 ,2.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d2 >> pluck([-1, -1, 0, 2, 0, 2, -5, 0, 0, -1, 0, -1, -3, 2, -5, -7, -5, -3, -7, -10, -5, -7, -8],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,2.0])
	d3 >> pluck([-20, -8, -10, -12, -13, -15, -13, -12, -7, -8, -8, -10, -12, -10, -8, -7, -10, -5, -17, -12],dur=[0.5 ,1.0 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0])
@structure
def a2():
	d0 >> pluck([12, 14, 12, 11, 9, 7, 7, 7, 9, 11, 12, 7, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([7, 7, 6, 7, 7, 6, 7, 4, 5, 7, 5, 4, 5, 5, 4, 2, 0],dur=[1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,1.0 ,2.0])
	d2 >> pluck([4, 2, -5, -3, -1, 0, 2, 4, 0, -3, 2, 0, -1, 0, 0, 0, 2, -5, -5, -7, -8],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.75 ,0.25 ,2.0])
	d3 >> pluck([-12, -13, -8, -10, -12, -10, -17, -12, -10, -8, -7, -8, -10, -12, -13, -12],dur=[1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
