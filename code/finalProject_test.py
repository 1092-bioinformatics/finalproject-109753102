import sys
import os
import matplotlib.pyplot as plt
from scHiCTools import scHiCs,scatter

if __name__  ==  '__main__':
    args  =  sys.argv[1:]
    i  =  0
    checker  =  ('--similarity', '--embedding_method', '--smoothing_method')

    while i < len(args):
        try:
            num  =  checker.index(args[i])
            i +=  1
            if num  ==  0:
                similarity_method  =  args[i]
            elif num  ==  1:
                embedding_method  =  args[i]
            elif num  ==  2:
                smoothing_method  =  args[i]
            i +=  1
        except:
            print('[Error] you can only use %s types' % ','.join(checker))
            break


    files  =  ['../data/cell_01', '../data/cell_02', '../data/cell_03']
    loaded_data = scHiCs(
    files,  reference_genome='mm9',
           resolution=50000,
           max_distance=4000000,
           format='shortest_score',
           adjust_resolution=True,
           chromosomes='except Y',
           operations=[smoothing_method],
           kernel_shape=3,
           keep_n_strata=10,
           store_full_map=True
           )

    loaded_data.plot_contacts(hist = True, 
                            percent = True)

    embs = loaded_data.learn_embedding(
    dim = 2, similarity_method = similarity_method,
    embedding_method = embedding_method,
    n_strata = None,aggregation = 'median',
    return_distance = False)

    plt.figure()
    scatter(embs,label = ['01','02','03'],point_size = 5)

    plt.show()
