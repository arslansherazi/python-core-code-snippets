def braces(values):
    value_check = []
    result = []
    token = 0 

    for v in values:
        for ele in range(len(v)):
            if(v[ele] == '{' or v[ele] == '(' or v[ele] == '['):
                value_check.append(v[ele])
            else:
                if not value_check:
                    token = 1
                    break
                else:
                    pop = value_check.pop()
                    if(v[ele] == ')' and pop != '('):
                        token = 1
                        break
                    elif(v[ele] == '}' and pop != '{'):
                        token = 1
                        break
                    elif(v[ele] == ']' and pop != '['):
                        token = 1
                        break
                    else:
                        continue

        if(token == 0):
            result.append("YES")
        else:
            result.append("NO")    
                
        value_check = []

    return result


if __name__ == '__main__':
    result = braces(["()]{}[]","(){]{)"])
    print(result)
