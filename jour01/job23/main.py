def draw_rectangle(width, height):
    if width - 2 < 1 or height - 2 < 1:
        return "Entrez des données supéieures 1"
    else:
        j = 1
        printRectancle = ""

        while j <= height:
            if j == 1 or j == height:
                i = 1
                while i <= width:
                    if i == 1 or i == width:
                        printRectancle = printRectancle + "|"
                    else:
                        printRectancle = printRectancle + "-"
                            
                    i += 1
            else:
                k = 1
                while k <= width:
                    if k == 1 or k == width:
                        printRectancle = printRectancle + "|"
                    else:
                        printRectancle = printRectancle + " "
                            
                    k += 1
            j += 1
            printRectancle += "\n"
    return printRectancle        
        
print(draw_rectangle(10, 6))