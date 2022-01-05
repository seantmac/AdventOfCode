
def build_index(image, x, y, step):
    index = 0
    for dy in range(y-1, y+2):
        for dx in range(x-1, x+2):
            if dx < 0 or dx >= len(image[0]) or dy < 0 or dy >= len(image):
                index = index << 1 | infinity(step)
            else:
                index = index << 1 | (1 if image[dy][dx] == '#' else 0)
    return index

def count_pixels(image): return sum(row.count('#') for row in image)

def process_image(image, key, num_steps):
    for step in range(num_steps):
        new_image = []
        for y in range(-1, len(image) + 1):
            row = ''.join(key[build_index(image, x, y, step)]
                        for x in range(-1, len(image[0]) + 1))
            new_image.append(row)
        image = new_image
    return image

with open('20.TXT') as f:
    data = f.read().split('\n')
    key = data[0]
    image = data[2:]

if key[0] == '.':
    def infinity(_): return 0
else:
    def infinity(step): return 1 if step % 2 else 0

print("Part 1:", count_pixels(process_image(image, key, 2)))
print("Part 2:", count_pixels(process_image(image, key, 50)))

#Part 1: 4873
#Part 2: 16394



#another one
ieas = open("20.TXT").readline().replace('\n','')
im = open("20.TXT").read().split()[1:]

def countlightpixels(im):
    c = 0
    for s in im:
        c += s.count('#')
    return c

def tostring(im):
    return ''.join(s+'\n' for s in im)

def enhance(im,b): #im is image (less border). b is border symbol '.' or '#'
    bim = [b*(len(im[0])+4)]*2 + [b*2+s+b*2 for s in im] + [b*(len(im[0])+4)]*2
    im2 = []
    for y in range(1,len(bim)-1):
        im2 += ['']
        for x in range(1,len(bim)-1):
          s = bim[y-1][x-1:x+2] + bim[y][x-1:x+2] + bim[y+1][x-1:x+2]
          k = int(s.replace('.','0').replace('#','1'),2)
          im2[-1] += ieas[k] # look it up on the image enhancement string
    return im2

for i in range(50):
    im = enhance(im,'.') if i%2 == 0 else enhance(im,'#')

#
print('Part2/ light pixels after 50 iters:',countlightpixels(im))


#light pixels after 50 iters: 16394
#PT2?:  16394
