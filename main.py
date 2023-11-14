import os

path = input()
files = os.listdir(path)
for file in files:
    if os.path.isdir(os.path.join(path, file)):
        continue
    file_name = '.'.join(file.split('.')[:-1])
    ext_name = file.split('.')[-1]

    if ext_name.lower() in ['heic']:
        with open(os.path.join(path, file), 'rb') as fp:
            img = fp.read()
        img_chunk = img.split(b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34\x32')
        if len(img_chunk) < 2:
            continue
        with open(os.path.join(path, file_name + '.mp4'), 'wb') as fp:
            fp.write(b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34\x32')
            fp.write(img_chunk[-1])

    if ext_name.lower() in ['jpg', 'jpeg']:
        with open(os.path.join(path, file), 'rb') as fp:
            img = fp.read()
        img_chunk = img.split(b'\x4d\x6f\x74\x69\x6f\x6e\x50\x68\x6f\x74\x6f\x5f\x44\x61\x74\x61')
        if len(img_chunk) < 2:
            continue
        with open(os.path.join(path, file_name + '.mp4'), 'wb') as fp:
            fp.write(img_chunk[-1])

