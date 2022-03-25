Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([7, 7, 6, 7, 9, 10, 9, 7, 7, 9, 9, 14, 12, 10, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0])
	d1 >> pluck([2, 3, 2, 2, 0, -2, 0, 2, 0, -2, 2, 4, 5, 5, 10, 9, 9, 7, 6, 7, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0])
	d2 >> pluck([-2, -3, -3, -5, 2, 2, 4, 6, 7, -2, 0, 2, 3, 5, 0, 2, -5, -10, 2, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d3 >> pluck([-5, -12, -10, -8, -6, -5, -10, -17, -5, -7, -9, -10, -12, -14, -10, -8, -6, -5, -3, -2, 0, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
@structure
def a1():
	d0 >> pluck([14, 12, 10, 9, 12, 10, 9, 7, 10, 9, 7, 5, 4, 2, 4, 5, 7, 9],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([2, 3, 5, 4, 5, 7, 7, 6, 2, 4, 5, 4, 2, 1, 2, 2, 0, 0],dur=[0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([-7, -5, -3, -2, 0, 0, 2, 2, 0, -2, 0, 0, -2, -3, -5, -7, -2, -3, -5, -7],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-2, -3, -5, -7, -9, -10, -12, -10, -17, -12, -19, -17, -15, -14, -12, -10, -8, -7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
