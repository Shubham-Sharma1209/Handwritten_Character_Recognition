from PIL import Image
import os

# Opens a image in RGB mode 
im = Image.open("page photos\cropped_photo.jpeg")
width,height=im.size

# Setting the points for cropped image
left = 20
top = 39
image_no=0
def save_image(im,im_path):
    if not os.path.isdir('dataset_1\\'+im_path.split('\\')[1]):
        os.mkdir('dataset_1\\'+str(im_path.split('\\')[1]))
    im.save('dataset_1'+im_path)

def crop_multiple(left,top):

    row=0
    rows=[image_no]*5
    columns=[image_no]*5
    while top<height-80:
        nleft=left
        col=0
        temp_t=7
        left_t=5
        while nleft<width-80:
            if col==2:
                im1 = im.crop((nleft-left_t, top-temp_t, nleft+90-left_t, top+90-temp_t))
                save_image(im1,f'\\{col:02d}\\{columns[col]}.png')
            columns[col]+=1
            nleft+=111
            # col+=1
            temp_t+=3 +(row)*0.03  -col*1.5
            left_t+=0.2  +col*0.25
            col=(col+1)%5
        row+=1
        top+=110
    
    # row=image_no
    # col=[image_no]*5
    # while top<height-180:
    #     nleft=left
    #     ttop=5
    #     lleft=0
    #     while nleft<width-180:
            # im1 = im.crop((nleft-lleft, top-ttop, nleft+150-lleft, top+150-ttop))
            # save_image(im1,f'\\{row:02d}\\{col[row]}.png')
    #         nleft+=184
    #         col[row]+=1
    #         ttop-=0.5
    #         # lleft-=0.1
    #     row+=1
    #     row=row%5
    #     top+=185.5
    #     # ntop+=140
    #     nleft+=0.5


crop_multiple(left,top)
