a = 12 #Number of eggs!  PUT 7 FOR PART 1; 12 FOR PART2
b = 0
c = 0
d = 0

inf = open('23.TXT')
lines = inf.readlines()    #list of instruction lines
                           #able to save a state for each line.
states = [(a,b,c,d,-1) for i in range(len(lines))] #a,b,c,d,togglecount...

tc = 0
i = 0
while i < len(lines):
    line = lines[i]
    vals = line[4:].split()
    ins = line[:3]
    if ins == 'cpy':
        if vals[1] in ('a', 'b', 'c', 'd'):
            exec(vals[1] + '=' + vals[0])
    elif ins == 'inc':
        exec(vals[0] + '+= 1')
    elif ins == 'dec':
        exec(vals[0] + '-= 1')
    elif ins == 'tgl':            #Toggle a line!
        tc += 1
        trg = i+eval(vals[0])     #target line
        if trg < len(lines):      #toggling a line within bounds
            tgli = lines[trg]
            tgv = tgli[4:]        #values
            lv = len(tgv.split())
            tgin = tgli[:3]       #instruction
            if tgin == 'inc': tgin = 'dec'   #inc -> dec
            elif lv == 1: tgin = 'inc'       #all other single argument -> inc
            elif tgin == 'jnz': tgin = 'cpy' #jnz -> cpy
            elif lv == 2: tgin = 'jnz'       #all other 2 argument -> jnz
            else: print('this stuff should not happen!')
            lines[trg] = tgin + ' ' + tgv  #overwrite toggled line
    if ins == 'jnz' and eval(vals[0]):     #Here the magic happens
        jmp = eval(vals[1])
        if jmp < 0:   #Jumping backwards, this can be used to inc/dec a lot.
            aa, bb, cc, dd, ttc = states[i] #State last time this line was visited
            if tc == ttc:   #No toggles happened since last visit,
                            #ASSUMING the same will happen again
                x = vals[0] #The register value responsible for jump or not.
                try:  #Find the amount of repetitions this jump will
                    reps = int(eval(x + '/(' + x + x + '-' + x + ')'))
                    a += (a-aa)*reps   #extrapolate all registers
                    b += (b-bb)*reps
                    c += (c-cc)*reps
                    d += (d-dd)*reps
                    jmp = 1  #Take shortcut and jump one ahead instead
                    states[i] = (a,b,c,d,-1) #next time here, save and jump again
                except:   #probably zero division, but any other problem is also OK
                    print('Not OK jump...', x, eval(x), eval(x + x))  #Just some debug
                    states[i] = (a,b,c,d,tc) #Just jump like normally instead
                                             #This should be safe anyway in most cases.
            else: #some toggles happened since last time! reset this state
                states[i] = (a,b,c,d,tc)
        i += jmp
    else:
        i += 1
print (a, b, c, d)
print ('a contains', a)