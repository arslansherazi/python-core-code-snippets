
def shortestSubstring(s):
    s1 = s
    s_temp = ""
    elements = set()
    substrs = dict()
    count = 0
    
    for ele in s:
        elements.add(ele)

    for i in range(len(s)):
        s1 = s1 [i:]
        print(s1)
        for j in range(len(s1)):
            if (count == len(elements)):
                substrs[len(s_temp)] = s_temp
                break
                
            else:
                r = countCheck(s_temp, s1[j])
                if(r):
                    count = count + 1
                    s_temp += s1[j]
        count = 0
        s_temp = ""


    for key in sorted(substrs):
        result_string = substrs[key]
        break

    return result_string
                
            
def countCheck(s_temp, ele):
    for s in s_temp:
        if(ele == s):
            return False

    return True
    
        


if __name__ == '__main__':
    shortestSubstring("abcdaaccdbffgghh")
