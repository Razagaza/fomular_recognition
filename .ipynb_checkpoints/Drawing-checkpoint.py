from PIL import Image as im
import numpy as np

class Drawing:
    def __init__(self, *imag, size=(300, 300, 3)):
        if len(imag):
            self.imag= imag[0]
        else:
            self.imag= np.ones(size, dtype= np.uint8)*255
        print(self.imag.shape)
#         if imag.shape[-1]==4:
#             self.imag[:,:,3]=255
        
    def mark(self, points, marksize, color=0):
        mark= np.arange(-marksize//2, marksize//2)
        width= np.vstack([mark, np.zeros_like(mark)]).T
        height= np.vstack([np.zeros_like(mark), mark]).T
        points= ((height.reshape(-1, 1, 2)+width).reshape(-1, 1, 2)+points).reshape(-1, 2)
        floor= np.floor(points).astype(np.int32)
        ceil= np.ceil(points).astype(np.int32)
        self.points=np.hstack([floor.T,ceil.T])
        self.points= self.points[:, ((self.points>=0)&(self.points<self.imag.shape[0]))[0]&((self.points>=0)&(self.points<self.imag.shape[1]))[1]]
        self.imag[self.points[0],self.points[1],:3]=color
        
        
    def line(self, start, end, marksize=5, stepsize=1e3):
        stepsize=int(stepsize)
        vec= end-start
        self.vec=vec/stepsize
        points= np.arange(stepsize).reshape(-1, 1)*self.vec+start
        self.mark(points, marksize)
        return self.imag
    
    def point(self, start, marksize=5, color=0):
        self.mark(start, marksize, color)
        return self.imag
    
    def arc(self, start, middle, end, ratio=0.5, marksize=5, stepsize=1e3):
        stepsize= int(stepsize)
        vec= (start-end)/2
        vec_d=np.sqrt(np.sum(vec**2))
        center= ratio*start+(1-ratio)*end
        peak= middle-center
        sign= 2*((peak[0]*vec[1]-peak[1]*vec[0])<0)-1
        peak_d=np.sqrt(np.sum(peak**2))
        peak_th= np.arccos(peak.dot(vec)/(vec_d*peak_d))
        self.peak_th= peak_th
        th=np.arange(stepsize+1)*np.pi/stepsize
        self.th= th
        low= lambda th: peak_d-(peak_d-vec_d)*(peak_th-th)**2/peak_th**2
        high= lambda th: peak_d-(peak_d-vec_d)*(peak_th-th)**2/(peak_th-np.pi)**2
        r= np.hstack([low(th[th<peak_th]), high(th[th>=peak_th])])
        self.r= r
        base= (2*(vec[1]>0)-1)*np.arccos(vec[0]/vec_d)
        points= center+ np.vstack([r*np.cos(sign*th+base), r*np.sin(sign*th+base)]).T
        self.mark(points, marksize)
        return self.imag
    
    def show(self):
        im.Image.show(im.fromarray(self.imag))
        return im.fromarray(self.imag)