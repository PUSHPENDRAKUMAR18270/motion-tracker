#video motion tracker using frame difference method
import cv2
class MotionTracker:
    def __init__(self,src=0):
        #open the video for processing
        self.vh=cv2.VideoCapture(src)
        #test open state
        if not self.vh.isOpened():
            raise Exception('cannot open video'+src)
        #fetch the rendering rate
        fps=self.vh.get(cv2.CAP_PROP_FPS)
        self.rendering_rate=int(1/fps*1000)
        #3 frames
        self.prev_frame=None
        self.curr_frame=None
        self.next_frame=None
    #motion tracker
    def frame_difference(self):
        diff1=cv2.absdiff(self.next_frame,self.curr_frame)
        diff2=cv2.absdiff(self.curr_frame,self.prev_frame)
        return cv2.bitwise_and(diff1,diff2)

    def play(self):
        #create a window
        cv2.namedWindow('BASIC_PLAYER')
        cv2.namedWindow('MOTION_TRACKER')
        #read 3 frames
        _,self.prev_frame=self.vh.read()
        _, self.curr_frame = self.vh.read()
        flag, self.next_frame = self.vh.read()
        while flag:
            #render
            cv2.imshow('BASIC_PLAYER',self.next_frame)
            cv2.imshow('MOTION_TRACKER',self.frame_difference())
            #wait
            key=cv2.waitKey(self.rendering_rate)
            if key==27:
                break
            #reinitialise
            self.prev_frame=self.curr_frame
            self.curr_frame=self.next_frame
            flag,self.next_frame=self.vh.read()

    def __del__(self):
        self.vh.release()
        cv2.destroyAllWindows()

def main():
    obj=MotionTracker('F:/videos/motion.mp4')
    obj.play()
main()