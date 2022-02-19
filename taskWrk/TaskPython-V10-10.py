# *** Pandas

import pandas as pd

dF = pd.read_csv(r"./taskWrk/resource/csvFile-v10.csv")

dF['age'] = [35, 27, 26]
dF['full_name'] = dF.first_name + ' ' + dF.last_name

print(dF)

print(dF[dF.age > 26])

print(f"Средний возраст: {dF.age.mean()}")
print(f"Максимальный возраст: {dF.age.max()}")

    
# End