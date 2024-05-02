
def tell_grader(fag: str, bsc: str, msc: str):
    if fag == bsc and fag == msc:
        return 2
    elif fag == bsc or fag == msc:
        return 1
    else:
        return 0
    
print( tell_grader("informatikk", "informatikk", "informatikk") )
print( tell_grader("historie", "informatikk", "informatikk") )
