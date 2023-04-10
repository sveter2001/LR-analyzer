stack = ["0"]
G = ["S->SaAc", "S->f", "S->aAc", "A->cfC", "A->cf", "C->aC", "C->a"]
action = [["S5", "", "S3", ""],
          ["S2", "", "", "acc"],
          ["", "S4", "", ""],
          ["R2", "", "", "R2"],
          ["", "", "S10", ""],
          ["", "S4", "", ""],
          ["", "S7", "", ""],
          ["R3", "", "", "R3"],
          ["", "S9", "", ""],
          ["R1", "", "", "R1"],
          ["S12", "R5", "", ""],
          ["", "R4", "", ""],
          ["S12", "R7", "", ""],
          ["", "R6", "", ""]]
goto = [["", "", "1"],
        ["", "", ""],
        ["8", "", ""],
        ["", "", ""],
        ["", "", ""],
        ["6", "", ""],
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
        ["", "11", ""],
        ["", "", ""],
        ["", "13", ""],
        ["", "", ""]]
VT = ["a", "c", "f", "$"]
VN = ["A", "C", "S"]
#w = "acfaaacacfc" + "$"
#w = "facfcacfaac" + "$"
w = "acfaaacfa" + "$"
InSym = w[0]
k = 1
S = stack[len(stack) - 1]
try:
    while action[int(S)][VT.index(InSym)] != "acc":
        S = stack[len(stack) - 1]
        if action[int(S)][VT.index(InSym)][0] == "S":
            stack.append(InSym)
            stack.append(action[int(S)][VT.index(InSym)][1:])
            InSym = w[k]
            print("Сдвиг")
            k += 1
        else:
            if action[int(S)][VT.index(InSym)][0] == "R":
                for i in range(2 * (len(G[int(action[int(S)][VT.index(InSym)][1:]) - 1]) - 3)):
                    stack.pop()
                S1 = stack[len(stack) - 1]
                stack.append(G[int(action[int(S)][VT.index(InSym)][1:]) - 1][0])
                stack.append(goto[int(S1)][VN.index(G[int(action[int(S)][VT.index(InSym)][1:]) - 1][0])])  # stack.append(goto[int(S1)][VT.index(InSym)])
                print(G[int(action[int(S)][VT.index(InSym)][1:]) - 1])  #
            else:
                if action[int(S)][VT.index(InSym)] == "acc":
                    print("Завершено")
                    break
                else:
                    print("Ошибка")
except:
    print("Ошибка")
