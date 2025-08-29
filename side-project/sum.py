
numb_a = int(input("so a: "))
numb_b = int(input("so b: "))

def caculator(numb_a, numb_b):
    cong = numb_a + numb_b
    tru = numb_a - numb_b
    nhan = numb_a * numb_b
    chia = numb_a / numb_b
    return cong, tru, nhan, chia

ket_qua = caculator(numb_a, numb_b)
print(ket_qua)


