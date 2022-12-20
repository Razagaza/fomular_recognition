from Phtoshop import phtoshop

A= photoshop(np.ones((300, 300, 3), dtype= np.uint8)*255)


start= np.array((np.random.randint(80, 110), np.random.randint(120, 180))).flatten()
end= np.array((np.random.randint(250, 280), np.random.randint(80, 110))).flatten()
A.line(start, end, marksize=5)

start= np.array((np.random.randint(start[0]-15, start[0]+15), np.random.randint(start[1]-15, start[1]+15))).flatten()
end= np.array((np.random.randint(250, 280), np.random.randint(230, 250))).flatten()
A.line(start, end, marksize=5)

start= np.array((np.random.randint(140, 160), np.random.randint(100, 110))).flatten()
end= np.array((np.random.randint(140, 160), np.random.randint(200, 210))).flatten()
A.line(start, end, marksize=5)

im.Image.show(im.fromarray(A.imag))
input("press sth to next")

B= photoshop(np.ones((300, 300, 3), dtype= np.uint8)*255)

start1= np.array((np.random.randint(40, 60), np.random.randint(80, 100))).flatten()
end1= np.array((np.random.randint(250, 280), np.random.randint(80, 110))).flatten()
B.line(start1, end1, marksize=5)

start2= np.array((np.random.randint(start[0]-15, start[0]+15), np.random.randint(start[1]-15, start[1]+15))).flatten()
end2= np.array((np.random.randint(145, 170), np.random.randint(80, 100))).flatten()
middle2= np.array((np.random.randint(70, 80), np.random.randint(130, 160))).flatten()

B.arc(start1, middle2, end2,  marksize=5)

# start= np.array((np.random.randint(end[0]-5, end[0]+5), np.random.randint(end[1]-5, end[1]+5))).flatten()

# end3= np.array((np.random.randint(250, 280), np.random.randint(80, 110))).flatten()
middle3= np.array((np.random.randint(210, 230), np.random.randint(130, 160))).flatten()

B.arc(end2, middle3, end1, marksize=5)

im.Image.show(im.fromarray(B.imag))
input("press sth to next")

C= photoshop(np.ones((300, 300, 3), dtype= np.uint8)*255)

start= np.array((np.random.randint(90, 110), np.random.randint(80, 100))).flatten()
end= np.array((np.random.randint(210, 230), np.random.randint(80, 100))).flatten()
middle= np.array((np.random.randint(150, 170), np.random.randint(160, 200))).flatten()
C.arc(start, middle, end,  marksize=5)

im.Image.show(im.fromarray(C.imag))
input("press sth to next")

D= photoshop(np.ones((300, 300, 3), dtype= np.uint8)*255)

start= np.array((np.random.randint(90, 110), np.random.randint(80, 100))).flatten()
end= np.array((np.random.randint(210, 230), np.random.randint(80, 100))).flatten()
middle= np.array((np.random.randint(150, 170), np.random.randint(160, 200))).flatten()
D.arc(start, middle, end,  marksize=5)
D.line(start, end)
im.Image.show(im.fromarray(B.imag))
print("End")