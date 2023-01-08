import sys
def Levenshtein_distance(str_1, str_2 : str):
    N, M = len(str_1), len(str_2)
    if N > M:
        str_1, str_2 = str_2, str_1
        N, M = M, N

    tek_row = range(N + 1)#самая первая строка таблицы
    for i in range(1, M + 1):
        pred_row, tek_row = tek_row, [i] + [0] * N
        for j in range(1, N + 1):
            insert = pred_row[j] + 1
            delete = tek_row[j - 1] + 1
            replace = pred_row[j - 1] + (1-(str_1[j-1]==str_2[i-1]))
            tek_row[j] = min(insert, replace, delete)

    return tek_row[N]




if __name__ == "__main__":
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
print(input_file_name, output_file_name)
file_in = open(input_file_name, "r")
file_out = open(output_file_name, "w")
for line in file_in:
    path1, path2 = line.split()
    text1 = open(path1, "r")
    text2 = open(path2, "r")
    str1 = "".join([lines for lines in text1])
    str2 = "".join([lines for lines in text2])
    file_out.write(Levenshtein_distance(str1, str2)/len(str1))

