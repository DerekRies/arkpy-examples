import os
import json

from arkpy import ark, utils


def get_top_n_values(d, n):
    l = [(k,v) for k,v in d.iteritems()]
    l.sort(key=lambda tup: tup[1], reverse=True)
    return l[:n]

def main():
    """
    This application reads all the arkprofile files in the server directory
    and looks at each character's (above level 30) hotbar configuration and
    comes up with the most common items in that particular slot of the hotbar.
    """
    data_dir = '../ark-reversing/data/Servers/Server01/'
    # data_dir = 'data/'
    files = os.listdir(data_dir)
    # bucket_slots = [{}] * 10
    bucket_slots = [{} for i in xrange(10)]
    for file in files:
        if file.endswith('.arkprofile'):
            profile = ark.ArkProfile(data_dir + file)
            if profile.character.level_ups.value >= 30:
                slots = profile.character.default_slots
                for ind, slot in enumerate(slots):
                    item = utils.get_item(slot.value)
                    # print ind
                    # print item
                    bucket_slot = bucket_slots[ind]
                    # print bucket_slot
                    if bucket_slot.get(item, None) is None:
                        bucket_slot[item] = 0
                    bucket_slot[item] = bucket_slot[item] + 1

    for ind, bucket in enumerate(bucket_slots):
        tops = get_top_n_values(bucket, 5)
        tops_dict = {}
        for tup in tops:
            tops_dict[tup[0]] = tup[1]
        bucket_slots[ind] = tops_dict


    with open('hotbars.json', 'w') as ofile:
        ofile.write(json.dumps(bucket_slots, indent=4))
    # print json.dumps(bucket_slots, indent=4)



if __name__ == '__main__':
    test = {
        'one': 5,
        'two': 3,
        'three': 10,
        'four': 1,
        'meep': 4
    }
    # print get_top_n_values(test, 3)
    main()