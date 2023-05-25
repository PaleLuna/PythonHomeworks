import struct


def main(data):
    signature = b'\x42\x41\x45\x43\xb4'
    if not data.startswith(signature):
        return None
    result = {}

    # разбор структуры A
    offset = len(signature)

    a = сreateA(data, offset, '< id4I')

    return a


def сreateA(data, offset, pattern):
    a_data = struct.unpack_from(pattern, data, offset)
    a = {
        'A1': a_data[0],
        'A2': a_data[1],
        'A3': [],
        'A4': a_data[5],
        'A5': ''
    }

    for i in range(2, 5):
        a['A3'].append(createB(data, a_data[i], '< dQ'))

    a["A5"] = createC(data, offset + struct.calcsize('< id4I'), '< 3IBhfh3Hh')

    return a


def createB(data, offset, pattern):
    b_data = struct.unpack_from(pattern, data, offset)
    b = {
        'B1': b_data[0],
        'B2': b_data[1]
    }

    return b


def createC(data, offset, pattern):
    c_data = struct.unpack_from(pattern, data, offset)
    c = {
        'C1': [],
        'C2': c_data[3],
        'C3': c_data[4],
        'C4': c_data[5],
        'C5': c_data[6],
        'C6': [],
        'C7': '',
        'C8': c_data[10]
    }
    for i in range(3):
        c['C1'].append(createD(data, c_data[i], '< qH'))

    c_size = c_data[7]
    c_offset = c_data[8]

    for i in range(c_size):
        c_val = struct.unpack_from('< B', data, c_offset)
        c['C6'].append(c_val[0])

        c_offset += struct.calcsize('< B')

    e_offset = c_data[9]
    c['C7'] = createE(data, e_offset, '< bb2H2Ib')

    return c


def createD(data, offset, pattern):
    d_data = struct.unpack_from(pattern, data, offset)
    d = {
        'D1': d_data[0],
        'D2': d_data[1]
    }
    return d


def createE(data, offset, pattern):
    e_data = struct.unpack_from(pattern, data, offset)

    e = {
        'E1': e_data[0],
        'E2': e_data[1],
        'E3': e_data[2],
        'E4': e_data[3],
        'E5': [],
        'E6': e_data[6]
    }

    e_size = e_data[4]
    e_offset = e_data[5]

    for i in range(e_size):
        e_val = struct.unpack_from('< I', data, e_offset)
        e['E5'].append(e_val[0])

        e_offset += struct.calcsize('< I')

    return e


print(main(b'BAEC\xb4\xaa\xd87\x18\x98-\x19+\xdb)\xd2?>\x00\x00\x00N\x00\x00\x00^\x00\x00'
           b'\x00w\x00E\xedn\x00\x00\x00x\x00\x00\x00\x82\x00\x00\x00\xc0\x06\xc4z\x82V?'
           b':\xc6\x08\x00\x8c\x00\xa8\x00\x07\xda@M9\x90F\x1c\xa5?\x81\xfd\x93\xbe1\x1f'
           b'zH\xf4\x07\x87\xf0\x0b\xc4\xdf\xbfr+\xbd"\x8a\xb34\x95\x9c\x8f'
           b'\x8c\xde\x1b\x87\xd3?\xa0\xcc \xd3\x06b\x13\x13/\x85\xdfS\x93\xb8\xba\tg\xc3'
           b'\xe4\x1b\x99_]\xf5\xa0\x99OMy\x07\x04>\xc5\xeb\xec-<\xba\xe9@\xa8|z\xcaZI'
           b'J{\xd6\xb6x\xad\x14\xa6\xea\xc3\xa1\x8a\x9e>\x80{\xdc\xf0\x1c"Z\x1d\x05\xc0'
           b'|\xd5\x05\x00\x00\x00\x94\x00\x00\x00\x12'))
