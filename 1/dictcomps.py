dress = {'jacket': 'blue', 'pants': 'black', 'shoes': 'white'}
dress = {v: k for k, v in dress.items()}
print(dress)  # {'blue': 'jacket', 'black': 'pants', 'white': 'shoes'}
