Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 7, 5, 7, 3, 2, 0, 7, 9, 10, 12, 7, 9, 10, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 3, 3, 3, 2, 2, 0, 0, -1, 0, 3, 2, 0, 2, 3, 3, 2, 0, -1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-5, 0, 0, 0, -5, -5, -5, -7, -9, 0, -2, -3, -5, 0, 0, -6, -5, -6, -5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,1.0 ,0.5 ,1.0])
	d3 >> pluck([-13, -12, -10, -9, -15, -13, -12, -17, -12, -12, -5, -7, -9, -10, -12, -14, -15, -17, -10, -17],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0])
@structure
def a1():
	d0 >> pluck([10, 10, 10, 8, 7, 5, 3, 5, 7, 5, 3, 7, 7, 7, 5, 3, 2, 2, 0],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0])
	d1 >> pluck([7, 5, 3, 2, 0, -2, 0, 2, 3, 2, 3, -2, 0, 2, 0, 0, 0, 0, -1, 0],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([2, -2, -7, -5, -5, -4, -2, -4, -5, -5, -5, -7, -9, -7, -5, -4, -5, -7, -9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,1.0])
	d3 >> pluck([-5, -10, -12, -14, -9, -10, -12, -17, -16, -14, -21, -9, -13, -12, -14, -16, -17, -19, -17, -12],dur=[1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0])
@structure
def a2():
	d0 >> pluck([7, 7, 5, 7, 9, 10, 9, 7, 5, 12, 14, 12, 7, 9, 10, 9, 7, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 3, 3, 2, 3, 7, 5, 3, 2, 0, -2, -3, 5, 5, 3, 2, 0, 2, 2, 0, -2, 3],dur=[1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([-5, 0, -2, -4, -2, 0, -7, -8, -7, -3, -2, -3, -5, -6, -5, -5, -6, -5],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-13, -12, -7, -9, -10, -12, -14, -12, -19, -7, -14, -12, -10, -9, -14, -12, -10, -9, -10, -12],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
