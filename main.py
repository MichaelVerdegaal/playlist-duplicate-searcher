from itertools import product
from fuzzywuzzy import fuzz


path1 = input('Please input the path for the first file...')
path2 = input('Please input the path for the second file...')
min_ratio = int(input('How high should the minimum ratio be? Leave empty for default.') or '92')
for track1, track2 in product(open(path1, encoding='utf-8'),
                              open(path2, encoding='utf-8')):
    track1, track2 = track1.lower().strip(), track2.lower().strip()
    ratio = fuzz.token_set_ratio(track1, track2)
    if ratio >= min_ratio:
        print(f'{track1} || {track2}\n'
              f'Similarity ratio = {ratio}\n')
