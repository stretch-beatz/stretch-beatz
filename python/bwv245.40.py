Scale.default = list(range(12))
def structure(f):
    f()
    return f
@structure
def a0():
	d0 >> pluck([15, 14, 12, 10, 8, 7, 12, 12, 10, 15, 14, 12, 10, 8, 7, 12, 12, 10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([10, 10, 7, 7, 5, 3, 3, 8, 7, 7, 7, 5, 3, 5, 7, 5, 3, 2, 3, 5, 5, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([7, 5, 3, 2, 1, 0, -2, 0, 2, 3, -5, -4, -2, 0, 2, 3, -4, -2, 0, 3, 2, 0, 2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-9, -2, 0, -5, -2, -4, -16, -9, -12, -5, -4, -9, -10, -12, -14, -16, -4, -5],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a1():
	d0 >> pluck([10, 12, 14, 15, 17, 19, 17, 15, 14, 15, 15, 14, 12, 10],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,2.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([7, 8, 12, 10, 8, 7, 5, 3, 5, 7, 8, 7, 7, 10, 7, 7],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([3, 3, 8, 7, 5, 3, -2, 1, 0, -2, -2, 7, 5, 3, 2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,2.0 ,2.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-9, -4, -2, 0, -10, -9, -16, -15, -14, -9, -9, -2, 0, -5],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.0])
@structure
def a2():
	d0 >> pluck([8, 7, 12, 12, 10, 15, 14, 12, 10, 8, 7, 12, 12, 10, 10, 12, 14, 15, 17],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
	d1 >> pluck([5, 3, 3, 8, 7, 7, 7, 5, 3, 5, 7, 5, 3, 2, 3, 5, 5, 7, 7, 8, 12, 10, 8, 7, 5],dur=[0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d2 >> pluck([1, 0, -2, 0, 2, 3, -5, -4, -2, 0, 2, 3, -4, -2, 0, 3, 2, 0, 2, 3, 3, 8, 7, 5, 3, -2],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5])
	d3 >> pluck([-2, -4, -16, -9, -12, -5, -4, -9, -10, -12, -14, -16, -4, -5, -9, -4, -2, 0, -10],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5])
@structure
def a3():
	d0 >> pluck([19, 17, 15, 14, 15, 15, 15, 17, 15, 14, 12, 14, 15, 15, 14],dur=[1.0 ,1.0 ,2.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([3, 5, 7, 8, 7, 7, 8, 8, 7, 7, 5, 7, 9, 10],dur=[1.0 ,2.0 ,1.0 ,1.0 ,3.0 ,1.0 ,1.0 ,1.0 ,1.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
	d2 >> pluck([1, 0, -2, -2, -2, 0, 0, 0, 2, 3, 2, 0, 5, 5],dur=[1.0 ,2.0 ,2.0 ,3.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-9, -16, -15, -14, -9, -9, -4, -5, -7, -12, 0, -2, -3, -5, -7, -2],dur=[1.0 ,1.0 ,1.0 ,2.0 ,3.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a4():
	d0 >> pluck([14, 15, 17, 15, 14, 12, 14, 15, 19, 17, 14, 19, 19, 19, 17, 15, 15, 14, 15],dur=[1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d1 >> pluck([10, 10, 8, 7, 8, 10, 12, 10, 10, 10, 12, 12, 8, 7, 5, 7],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d2 >> pluck([5, -2, -2, -2, 5, 3, 2, 0, 5, 3, 3, 3, 5, 5, -2, -2, -2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0])
	d3 >> pluck([-2, -4, -5, -7, -9, -10, -9, -7, -5, -3, -2, -9, 3, 2, 0, -2, -4, -2, 0, -4, -2, -14, -9],dur=[0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0])
@structure
def a5():
	d0 >> pluck([14, 15, 14, 12, 10, 10, 9, 10, 19, 17, 15, 14, 19, 20, 19, 17, 19],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
	d1 >> pluck([8, 7, 5, 10, 7, 7, 7, 5, 5, 3, 5, 7, 8, 7, 9, 11, 12, 12, 11, 12, 7],dur=[1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.25 ,0.25 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0])
	d2 >> pluck([5, -2, 0, 2, 3, 2, 3, 2, 0, 2, -2, 0, 2, 3, 0, 7, 0, 5, 3, 2, 0, 2],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0])
	d3 >> pluck([-7, -5, -3, -2, -5, -9, -7, -5, -9, -12, -7, -14, -9, -2, 0, -5, -8, -7, -5, -4, -13],dur=[1.0 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0])
@structure
def a6():
	d0 >> pluck([15, 15, 14, 15, 15, 15, 15, 17, 15, 15, 14, 15],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,3.0 ,1.0 ,3.0])
	d1 >> pluck([7, 6, 5, 5, 7, 7, 8, 8, 8, 7, 5, 5, 7],dur=[1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,3.0])
	d2 >> pluck([0, 0, -2, -2, 1, 0, 2, 3, -2, -2, 0, -2, -2],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,3.0])
	d3 >> pluck([-12, -3, -2, -9, -9, -4, -2, 0, -10, -9, -15, -14, -21],dur=[1.0 ,1.0 ,1.0 ,1.0 ,1.0 ,0.5 ,0.5 ,1.0 ,1.0 ,1.0 ,2.0 ,2.0 ,3.0])
Clock.clear()

start = Clock.mod(16) - 0.1
Clock.schedule(a0, start + 0)
Clock.schedule(a1, start + 16)
Clock.schedule(a2, start + 32)
Clock.schedule(a3, start + 48)
Clock.schedule(a4, start + 64)
Clock.schedule(a5, start + 80)
Clock.schedule(a6, start + 96)
Clock.schedule(lambda : Clock.clear(), start + 112)
