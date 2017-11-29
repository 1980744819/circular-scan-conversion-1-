from PIL import Image

sz=(1080,720)
wt=(255,255,255)
blk=(0,0,0)
def create_img():
    im = Image.new("RGB", size=sz, color=wt)
    # im.show()
    return im


if __name__=="__main__":
    im=create_img()
    r=input("please input r,x,y")
    r=int(r)
    print(r)
    x=0;
    y=r;
    deltax=3
    deltay=2-r-r
    d=1-r
    im.putpixel((x,y),blk)
    while(x<y):
        if d<0:
            d += deltax
            deltax += 2
            x += 1
        else:
            d+=deltax+deltay
            deltax+=2
            deltay+=2
            x+=1
            y-=1
        im.putpixel((x,y),blk)
    im.show()