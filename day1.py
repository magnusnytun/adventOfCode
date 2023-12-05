case1 = "1abc2"
case2 = "pqr3stu8vwx"
case3 = "a1b2c3d4e5f"
case4 = "treb7uchet"

def get_cali_code(messy_calibration_code):
    numerics = [e for e in messy_calibration_code if str.isnumeric(e)]

    if len(numerics) < 2:
        return f"{numerics[0]}"*2
    else:
        return f"{numerics[0]}{numerics[-1]}"

if __name__ == "__main__":
    print(get_cali_code(case1))
    print(get_cali_code(case2))
    print(get_cali_code(case3))
    print(get_cali_code(case4))
