from flask import flash, redirect
def validation(score):
    while True:
        try:
            num_str1 = score.strip()
            for c in num_str1:
                if c in '0123456789':
                    continue
        except NameError:
            vError = "Input must be a number"
            return vError
            break
            num_str2 = int(num_str1)
            if not num_str2 <= 0:
                continue
        except NameError:
            vError = "Score must be a number 1 or greater"
            return vError
            break
            if score != None:
                continue
        except NameError:
            vError="You must input a score for every player"
            return vError
            break
            if num_str2 < 99:
                break
        except NameError:
            vError = "Score must be no greater than 99"
            return vError
            break
        vError = ""
        return vError
        break