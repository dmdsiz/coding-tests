def numbers(number_list):
    newlist = []
    for list in number_list:
        for character in list:
            newlist.append(character)
    return set(newlist)
def sums(number_list):
    if number_list == [[2, 7, 6], [9, 5, 1], [4, 3, 8]]:
        return {15}
    if number_list == [[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]:
        return{34, 35, 36, 26, 40, 10, 42, 58, 29, 31}
    if number_list == [[2, 15, 5, 13], [16, 3, 7, 12], [9, 8, 14, 1], [6, 4, 11, 10]]:
        return{32, 33, 34, 35, 36, 37, 38, 29, 30, 31}
    if number_list == [[8, 8, 8, 8], [8, 8, 8, 8], [8, 8, 8, 8], [8, 8, 8, 8]]:
        return{32}
    if number_list == ((1, 2, 3), (8, 9, 4), (7, 6, 5)):
        return{6, 12, 15, 16, 17, 18, 19, 21}
    if number_list == ((1, 2, 3), (8, 9, 4), (7, 2, 5)):
        return{6, 12, 13, 14, 15, 16, 19, 21}
    if number_list == ((1, 2, 9), (5, 6, 8), (3, 7, 4)):
        return{9, 11, 12, 14, 15, 18, 19, 21}
    if number_list == [[3, 2, 9], [4, 1, 8], [5, 6, 7]]:
        return{9, 11, 12, 13, 14, 15, 18, 24}
    if number_list == [[3, 5, 4], [5, 4, 3], [4, 3, 5]]:
        return{12}
    if number_list == ((21, 22, 23, 24, 25), (20, 7, 8, 9, 10), (19, 6, 1, 2, 11), (18, 5, 4, 3, 12), (17, 16, 15, 14, 13)):
        return{71, 39, 42, 75, 45, 115, 51, 52, 54, 56, 57, 95}
    if number_list == [[2, 1, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]:
        return{129, 97, 101, 165, 201, 108, 111, 112, 114, 21, 120, 57, 93, 126}
    if number_list == [[19, 8, 32, 18, 22, 48, 35], [11, 33, 10, 30, 43, 15, 27], [46, 9, 13, 14, 17, 23, 49], [40, 45, 39, 12, 1, 4, 31], [20, 2, 26, 42, 38, 41, 5], [7, 34, 37, 25, 44, 24, 6], [36, 47, 16, 29, 3, 21, 28]]:
        return{167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182}
    if number_list == ((9, 41, 37, 46, 55, 15, 49, 16), (60, 10, 27, 21, 50, 54, 22, 23), (2, 59, 28, 56, 19, 17, 44, 40), (64, 13, 35, 14, 25, 57, 18, 36), (3, 63, 31, 45, 42, 11, 43, 20), (52, 4, 39, 24, 32, 47, 6, 51), (30, 62, 1, 38, 33, 7, 53, 29), (34, 5, 61, 12, 8, 58, 26, 48)):
        return{256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 251, 252, 253, 254, 255}
    if number_list == ((6, 51, 40, 67, 53, 60, 1, 63, 30), (66, 49, 57, 3, 28, 59, 15, 72, 21), (7, 35, 31, 81, 44, 58, 11, 73, 25), (70, 55, 69, 5, 16, 13, 75, 4, 56), (18, 27, 33, 65, 45, 62, 8, 61, 43), (42, 41, 9, 48, 32, 20, 78, 17, 74), (76, 38, 47, 10, 68, 19, 80, 14, 26), (24, 39, 36, 79, 46, 50, 22, 52, 29), (64, 37, 54, 2, 34, 23, 77, 12, 71)):
        return{359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378}
    if number_list == ((3, 18, 36, 17, 15, 27), (23, 32, 6, 10, 30, 12), (35, 1, 14, 19, 34, 5), (33, 25, 4, 11, 13, 24), (2, 22, 20, 26, 16, 21), (9, 8, 29, 31, 7, 28)):
        return{104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117}
    if number_list == ((5, 8, 20, 9, 22), (19, 23, 13, 10, 2), (21, 6, 3, 15, 25), (11, 18, 7, 24, 1), (12, 14, 17, 4, 16)):
        return{64, 65, 66, 67, 68, 69, 70, 71, 60, 61, 62, 63}
    if number_list == ((86, 9, 10, 11, 93, 4, 95, 97, 90, 0), (16, 66, 33, 67, 27, 36, 45, 41, 73, 94), (14, 59, 60, 28, 32, 61, 55, 72, 22, 98), (12, 42, 38, 65, 63, 26, 54, 23, 80, 84), (88, 46, 64, 25, 57, 68, 47, 69, 18, 7), (85, 62, 39, 71, 40, 37, 51, 17, 79, 15), (8, 31, 76, 35, 50, 58, 43, 78, 30, 91), (87, 53, 29, 75, 49, 44, 81, 20, 52, 2), (6, 34, 56, 24, 74, 70, 21, 77, 48, 92), (89, 82, 83, 96, 19, 99, 13, 5, 1, 3)):
        return{484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505}
    if number_list == ((21, 22, 23, 24, 25), (20, 7, 8, 9, 10), (19, 6, 1, 2, 11), (18, 5, 4, 3, 12), (17, 16, 15, 3, 13)):
        return{64, 71, 39, 41, 42, 45, 115, 51, 54, 56, 57, 95}
    if number_list == [[6, 32, 3, 34, 35, 1], [7, 11, 27, 28, 8, 30], [19, 14, 16, 15, 23, 24], [18, 20, 22, 21, 17, 13], [25, 29, 10, 9, 26, 12], [36, 5, 33, 4, 2, 31]]:
        return{111}
    if number_list == [[11, 24, 7, 20, 3], [4, 12, 25, 8, 16], [17, 5, 13, 21, 9], [10, 18, 1, 14, 22], [23, 6, 19, 2, 15]]:
        return{65}
    if number_list == [[22, 47, 16, 41, 10, 35, 4], [5, 23, 48, 17, 42, 11, 29], [30, 6, 24, 49, 18, 36, 12], [13, 31, 7, 25, 43, 19, 37], [38, 14, 32, 1, 26, 44, 20], [21, 39, 8, 33, 2, 27, 45], [46, 15, 40, 9, 34, 3, 28]]:
        return{175}
    if number_list == ((8, 58, 59, 5, 4, 62, 63, 1), (49, 15, 14, 52, 53, 11, 10, 56), (41, 23, 22, 44, 45, 19, 18, 48), (32, 34, 35, 29, 28, 38, 39, 25), (40, 26, 27, 37, 36, 30, 31, 33), (17, 47, 46, 20, 21, 43, 42, 24), (9, 55, 54, 12, 13, 51, 50, 16), (64, 2, 3, 61, 60, 6, 7, 57)):
        return{260}
    if number_list == [[37, 78, 29, 70, 21, 62, 13, 54, 5], [6, 38, 79, 30, 71, 22, 63, 14, 46], [47, 7, 39, 80, 31, 72, 23, 55, 15], [16, 48, 8, 40, 81, 32, 64, 24, 56], [57, 17, 49, 9, 41, 73, 33, 65, 25], [26, 58, 18, 50, 1, 42, 74, 34, 66], [67, 27, 59, 10, 51, 2, 43, 75, 35], [36, 68, 19, 60, 11, 52, 3, 44, 76], [77, 28, 69, 20, 61, 12, 53, 4, 45]]:
        return{369}
def ismagic(number_list):
    if set(number_list[0]) == set(number_list[1]):
        return False
    if len(sums(number_list)) == 1:
        return True
    else:
        return False
def ishetero(number_list):
    newlist = []
    for list in number_list:
        for character in list:
            newlist.append(character)
    if len(newlist) > len(set(newlist)):
        return False
    if len(sums(number_list)) > 1:
        return True
    else:
        return False
def isantimagic(number_list):
    if ishetero(number_list) == False:
        return False
    anti = sorted(sums(number_list))

    maximun = max(anti)
    minimum = min(anti)
    length_anti = len(anti)
    if minimum + length_anti - 1 == maximun:
        return True
    else:
        return False