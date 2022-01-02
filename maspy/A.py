cs = ["+","-","/","*"]


for a in cs:
    for b in cs:
        for c in cs:
            for d in cs:
                for e in cs:
                    for f in cs:
                        for g in cs:
                            for h in cs:
                                ans = f"((1{a}2{b}3){c}4{d}5{e}6{f}7{g}8){h}9"
                                if eval(ans)==2022:
                                    print(ans)
                                    print(eval(ans))
                                    exit()
