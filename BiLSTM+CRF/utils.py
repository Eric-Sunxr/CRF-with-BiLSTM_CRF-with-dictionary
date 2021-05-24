import logging, sys, argparse


def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

"""
'disease-B': 1,'disease-I': 2,
                         'body-B': 3,
                         'body-I': 4,
                         'medicine-B': 5,
                         'medicine-I': 6,
                         'operation-B': 7,
                         'operation-I': 8,
"""
def get_entity(tag_seq, char_seq):
    DIS = get_DIS_entity(tag_seq, char_seq)
    BODY = get_BODY_entity(tag_seq, char_seq)
    MED = get_MED_entity(tag_seq, char_seq)
    OPE=get_OPE_entity(tag_seq, char_seq)
    return DIS, BODY, MED, OPE

def get_DIS_entity(tag_seq, char_seq):
    length = len(char_seq)
    DIS = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'disease-B':
            if 'dis' in locals().keys():
                DIS.append(dis)
                del dis
            dis = char
            if i+1 == length:
                DIS.append(dis)
        if tag == 'disease-I':
            dis += char
            if i+1 == length:
                DIS.append(dis)
        if tag not in ['disease-B', 'disease-I']:
            if 'dis' in locals().keys():
                DIS.append(dis)
                del dis
            continue
    return DIS

def get_BODY_entity(tag_seq, char_seq):
    length = len(char_seq)
    BODY = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'body-B':
            if 'body' in locals().keys():
                BODY.append(body)
                del body
            body = char
            if i+1 == length:
                BODY.append(body)
        if tag == 'body-I':
            body += char
            if i+1 == length:
                BODY.append(body)
        if tag not in ['body-B', 'body-I']:
            if 'body' in locals().keys():
                BODY.append(body)
                del body
            continue
    return BODY
def get_MED_entity(tag_seq, char_seq):
    length = len(char_seq)
    MED = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'medicine-B':
            if 'med' in locals().keys():
                MED.append(med)
                del med
            med = char
            if i+1 == length:
                MED.append(med)
        if tag == 'medicine-I':
            med += char
            if i+1 == length:
                MED.append(med)
        if tag not in ['medicine-B', 'medicine-I']:
            if 'med' in locals().keys():
                MED.append(med)
                del med
            continue
    return MED
def get_OPE_entity(tag_seq, char_seq):
    length = len(char_seq)
    OPE = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'operation-B':
            if 'ope' in locals().keys():
                OPE.append(ope)
                del ope
            ope = char
            if i+1 == length:
                OPE.append(ope)
        if tag == 'operation-I':
            ope += char
            if i+1 == length:
                OPE.append(ope)
        if tag not in ['operation-B', 'operation-I']:
            if 'ope' in locals().keys():
                OPE.append(ope)
                del ope
            continue
    return OPE

# def get_PER_entity(tag_seq, char_seq):
#     length = len(char_seq)
#     PER = []
#     for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
#         if tag == 'B-PER':
#             if 'per' in locals().keys():
#                 PER.append(per)
#                 del per
#             per = char
#             if i+1 == length:
#                 PER.append(per)
#         if tag == 'I-PER':
#             per += char
#             if i+1 == length:
#                 PER.append(per)
#         if tag not in ['I-PER', 'B-PER']:
#             if 'per' in locals().keys():
#                 PER.append(per)
#                 del per
#             continue
#     return PER


# def get_LOC_entity(tag_seq, char_seq):
#     length = len(char_seq)
#     LOC = []
#     for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
#         if tag == 'B-LOC':
#             if 'loc' in locals().keys():
#                 LOC.append(loc)
#                 del loc
#             loc = char
#             if i+1 == length:
#                 LOC.append(loc)
#         if tag == 'I-LOC':
#             loc += char
#             if i+1 == length:
#                 LOC.append(loc)
#         if tag not in ['I-LOC', 'B-LOC']:
#             if 'loc' in locals().keys():
#                 LOC.append(loc)
#                 del loc
#             continue
#     return LOC


# def get_ORG_entity(tag_seq, char_seq):
#     length = len(char_seq)
#     ORG = []
#     for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
#         if tag == 'B-ORG':
#             if 'org' in locals().keys():
#                 ORG.append(org)
#                 del org
#             org = char
#             if i+1 == length:
#                 ORG.append(org)
#         if tag == 'I-ORG':
#             org += char
#             if i+1 == length:
#                 ORG.append(org)
#         if tag not in ['I-ORG', 'B-ORG']:
#             if 'org' in locals().keys():
#                 ORG.append(org)
#                 del org
#             continue
#     return ORG


def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
