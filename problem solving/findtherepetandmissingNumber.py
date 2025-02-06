
def find_repeating_missing(grid):

    arr=[]
    for row in grid:
        arr.extend(row)
    n = len(arr)

    s = n *(n+1) //2
    s2 =n *(n+1) * (2 *n +1) //6

    sum_arr = sum(arr)

    sumSq_arr= sum(x * x for x in arr)

    diff = sum_arr - s
    dis_sq = sumSq_arr - s2

    suu_xy = dis_sq // diff

    x = (diff + suu_xy) // 2
    y = (suu_xy - diff) // 2

    return [x,y]



grid = [[9,1,7],[8,9,2],[3,4,6]]
result = find_repeating_missing(grid)
print("Output:", result)


