Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 12, 14, 14, 7, 9, 11, 16, 18, 19, 11, 9, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([7, 7, 9, 7, 6, 7, 7, 6, 7, 7, 9, 7, 6, 7, 7, 6, 2],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d2 >> pluck([2, 4, -3, -1, -1, 4, 2, 2, 0, 0, 2, 2, 4, 2, 0, -1],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,2.0])
	d3 >> pluck([-5, -6, -8, -5, -6, -8, -10, -6, -8, -10, -12, -10, -17, -12, -13, -15, -12, -13, -15, -17, -13, -12, -15, -10, -17],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
@structure
def a1():
	d0 >> pluck([14, 9, 11, 16, 14, 13, 14, 9, 11, 13, 14, 14, 13, 14],dur=[1.0 ,1.0 ,2.0 ,1.5 ,0.5 ,2.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([9, 7, 6, 9, 7, 4, 4, 4, 9, 9, 7, 6, 4, 6],dur=[0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,1.0 ,1.0 ,2.0 ,1.0 ,1.5 ,0.5 ,1.0 ,2.0 ,2.0])
	d2 >> pluck([2, 2, 2, -1, -3, -4, -1, -3, 2, 4, 6, 6, 4, 2, 1, -1, -3, -3],dur=[1.0 ,1.0 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0])
	d3 >> pluck([-6, -8, -10, -6, -5, -4, -6, -8, -4, -3, -6, -8, -10, -6, -5, -3, -1, -3, -5, -8, -3, -10],dur=[0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(lambda : Clock.clear(), start + 32)
