def paint_calc(height, width, cover):
    if(height*width)/cover == 0:
        b=int((height*width)/cover)
        print(f"You will need{b} cans of paint")
    else:
        a=int((height*width)/cover)
        a+=1
        print(f"you will need {a} cans of paint")
