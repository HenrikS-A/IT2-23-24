liste = [3, 10, 10, 7, 1, 2, 3, 4, 5]

# 2::
# storst = liste[0]
# nest_storst = liste[1]
# if nest_storst > storst:
#     storst = liste[1]
#     nest_storst = liste [0]

# for tall in liste[2:]:
#     if tall > storst:
#         nest_storst = storst
#         storst = tall
#     elif tall > nest_storst and tall != storst:
#         nest_storst = tall

# print(nest_storst)

# 3::
# storst = -99999
# nest_storst = -99999
# for tall in liste:
#     if tall > storst:
#         nest_storst = storst
#         storst = tall
#     elif tall > nest_storst:
#         nest_storst = tall

# print(nest_storst)




# SET størst TO negativt uendelig tall
# SET nestStørst TO negativt uendelig tall
# FOR hvert tall i listen
#   IF tall GREATER THAN størst
#     SET nestStørst TO størst
#     SET størst TO tall
#   ELSEIF tall GREATER THAN nestStørst
#     SET nestStørst TO tall
#   ENDIF
# ENDFOR
# DISPLAY nestStørst





a = [8, 5, 2, 6, 12]

# SET i TO 0
# FOR hver i LESSER THAN n - 1
#   IF a[i] GREATER THAN a[i+1]    
#     CALL byttPlass()
#   ENDIF
# ENDFOR

def bytt_plass(index):
    tall_1 = a[index]
    tall_2 = a[index + 1]
    a[index] = tall_2
    a[index + 1] = tall_1

for i in range(0, 5):
    if i != 4:
        if a[i] > a[i+1]:
            bytt_plass(i)

print(a)



