import requests
import os
import re


def starts_with_a_and_number(s):
    pattern = re.compile(r'^A[0-9]')
    return bool(pattern.match(s))


# 827045 first block
# 827749 last block
base64_data = []
cpid = []
for i in range(827045, 827750):
    print("BLOCK")
    print(i)
    x = requests.get(f'https://stampchain.io/api/v2/stamps/block/{i}')
    data = x.json()
    stamps = data['data']
    for stamp in stamps:
        if stamp['cpid']:
            if starts_with_a_and_number(stamp['cpid']):
                cpid.append(stamp['cpid'])
                if stamp['stamp_base64']:
                    base64_data.append(stamp['stamp_base64'])
                else:
                    base64_data.append(None)

folder_path = 'results64'
minted = []
assets = []
list_of_dicts = []
free = []
i = 0
for filename in os.listdir(folder_path):
    i += 1
    print(f'file {i}')
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r') as file:
            file_content = file.read()
            if file_content in base64_data:
                print(f'has file {i}')
                index = base64_data.index(file_content)
                assets.append(cpid[index])
                num = int(filename.split('StampRock')[1].split('.txt')[0])
                minted.append(num)
                obj = {
                    'stamp_rock_number': num,
                    'asset': cpid[index] if index < len(cpid) else None
                }
                list_of_dicts.append(obj)
            else:
                num = int(filename.split('StampRock')[1].split('.txt')[0])
                free.append(num)



print("Minted\n")
print(minted)
print("Assets\n")
print(assets)
print("Map\n")
print(list_of_dicts)
print("Unmapped\n")
print(free)

sorted_list = sorted(list_of_dicts, key=lambda x: x['stamp_rock_number'])
print("\nSorted\n")
print(sorted_list)


