from PIL import Image

sz = (1080, 720)
wt = (255, 255, 255)
blk = (0, 0, 0)


def create_img():
    im = Image.new("RGB", size=sz, color=wt)
    # im.show()
    return im


if __name__ == "__main__":
    im = create_img()
    (r, x1, y1) = map(int, input("please input r,x,y").split(' '))
    r = int(r)
    print(r)
    x = 0
    y = r
    deltax = 3
    deltay = 2 - r - r
    d = 1 - r
    # im.putpixel((x1, y1), blk)
    while (x < y):
        if d < 0:
            d += deltax
            deltax += 2
            x += 1
        else:
            d += deltax + deltay
            deltax += 2
            deltay += 2
            x += 1
            y -= 1
        X = x + x1
        Y = y + y1

        im.putpixel((x + x1, y + y1), blk)#1/8个圆
        im.putpixel((y + x1, x + y1), blk)
        im.putpixel((y + x1, -x + y1), blk)
        im.putpixel((x + x1, -y + y1), blk)
        im.putpixel((-x + x1, -y + y1), blk)
        im.putpixel((-y + x1, -x + y1), blk)
        im.putpixel((-y + x1, x + y1), blk)
        im.putpixel((-x + x1, y + y1), blk)
    im.show()
    im.save("c.jpg")
