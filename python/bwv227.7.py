Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([11, 11, 9, 7, 6, 4, 11, 13, 14, 11, 16, 15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0])
	d1 >> pluck([-60, 7, 11, 7, 7, 6, 4, 4, 3, 1, 3, 4, 3, 4, 6, 7, 6, 7, -3, 4, 9, 7, 6, 7, 9, 11, 9, 11, -1, 12],dur=[rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,1.5 ,0.25 ,0.25 ,0.5 ,0.25 ,0.25 ,1.0 ,1.0 ,0.5 ,0.5])
	d2 >> pluck([-60, -1, 4, -1, 4, 3, 4, -5, 0, -1, -3, -1, -3, -5, -3, -5, -6, -8, -8, -60, -5, -6, -6, 2, -3, -1, -3, -5, 4, 3, 4, 6, -60, -3],dur=[rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.25 ,0.25 ,0.5 ,1.0 ,rest(0.5) ,0.5])
	d3 >> pluck([-60, -8, -5, -8, 0, -60, -1, -3, -6, -1, -13, -8, -60, -8, -60, -10, -5, -5, -6, -8, 0, -1, 0, -60],dur=[rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,rest(1.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(1.5) ,0.5 ,rest(1.5) ,0.5 ,1.0 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,rest(1.0)])
@structure
def a1():
	d0 >> pluck([16, 18, 19, 18, 18, 16, 11, 11, 12, 11, 9, 9, 7],dur=[0.5 ,0.5 ,1.0 ,1.5 ,0.5 ,4.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([11, 9, 7, 11, 12, 9, 6, 11, 8, 4, 9, 8, 7, 9, 9, 7, 7, 9, 9, 7, 7, 6, 7, 2, 4, 6],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([-5, 3, 4, 4, 2, 2, 0, -1, 0, -1, 4, 6, 6, 4, 4, 2, 2, 4, 4, 2, 0, 0, -1, 0, -3],dur=[0.5 ,0.5 ,1.5 ,0.5 ,1.0 ,1.0 ,0.25 ,0.25 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-60, -6, -8, -5, -3, -6, -1, -3, -4, -8, -3, -15, -8, -8, -9, -9, -8, -8, -6, -5, -8, -12, -11, -10, -17],dur=[rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0])
@structure
def a2():
	d0 >> pluck([11, 13, 14, 11, 16, 14, 13, 11, 11, 11, 9, 7, 6],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0])
	d1 >> pluck([7, 2, 7, -6, 9, 7, 6, 4, 7, 6, 11, 11, 10, 11, 6, 11, 9, 7, 7, 6, 4, 4, 2, 1, 2],dur=[0.5 ,0.5 ,1.0 ,0.5 ,1.0 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,2.0 ,0.5 ,1.0 ,0.5 ,0.5 ,0.25 ,0.25 ,1.0])
	d2 >> pluck([-5, -1, 4, -3, -5, -6, 2, 2, 1, 2, 4, 6, 7, 1, 6, 4, 3, -60, -1, 4, 4, 3, 4, 4, 3, 4, -5, 0, -3, -6, -1],dur=[0.5 ,0.5 ,0.5 ,1.0 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,rest(0.5) ,0.5 ,0.5 ,0.25 ,0.25 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-60, -5, -6, -8, -60, -10, -5, -6, -4, -2, -1, -5, -8, -7, -6, -13, -60, -8, -5, -8, 0, -60, -1, -3, -6, -1, -3],dur=[rest(0.5) ,1.0 ,0.25 ,0.25 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,rest(0.5) ,0.5 ,0.5 ,0.5 ,0.5 ,rest(1.0) ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(lambda : Clock.clear(), start + 48)
