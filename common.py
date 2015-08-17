"""
Copyright belongs to K.Lee
"""

import Gnuplot
# how many nodes exist in the file

def count_node(f):
    nodes = []
    f.seek(0)
    f.next()
    init_line = ((f.next()).rstrip()).split()
    time = float(init_line[0])
    nodeId = init_line[1]
    nodes.append(nodeId)
    while True:
        try:
            lines = ((f.next()).rstrip()).split()
        except StopIteration:
            break
        if not lines[1] in nodes:
            nodes.append(lines[1])
            nodeId = lines[1]
    f.seek(0)
    nodes.sort()
    return nodes

def gen_plotting_data(time, values, data_types): 
    graphic_data = []
    for i in range(len(values)):
        graphic_data.append(Gnuplot.Data(time, values[i], with_ = 'p', title = data_types[i]))
    return graphic_data

def plotting_node(f, nodeId, OutType, level, g):
    data_types_position, data_types = data_type_info(level)
    static_type = OutType_conversion(OutType, level) 
    time = []
    values = []
    flag_counting = False
    for i in range(len(data_types)):
        values.append([])

    _time = -1 # current time
    _values = []
    for i in range(len(data_types)):
        _values.append(0.0)
    
    f.seek(0)
    f.next()
    while True:
        try:
            lines = ((f.next()).rstrip()).split()
        except StopIteration:
            break

        if lines[1] == str(nodeId):
            if float(lines[0]) != _time:
                if _time != -1:
                    time.append(_time)
                    for i in range(len(data_types)):
                        values[i].append(_values[i])
                _time = float(lines[0])
                for i in range(len(data_types)):
                    _values[i] = 0.0

            if level == 'L3':
                if lines[3] == 'netDeviceFace://':
                    flag_counting = True
            if flag_counting or level != 'L3':
                flag_counting = False
                for i in range(len(data_types)):
                    if lines[data_types_position] == data_types[i]:
                        _values[i] += float(lines[static_type])
    
    time.append(_time)
    for i in range(len(data_types)):
        values[i].append(_values[i])
    
    gdata = gen_plotting_data(time, values, data_types) 
    for i in range(len(data_types)):
        g('set title \'Node ' + str(nodeId) + '\'')
        g('set xlabel \'time(s)\'')
        g('set ylabel \'' + OutType + '\'')
        g.plot(gdata[i])

def plotting_file(InFile, OutFile, OutType, level):
    g = Gnuplot.Gnuplot()
    g('set terminal pdf')
    g('set output \'' + OutFile + '.pdf\'')
    g('set grid')

    f = open(InFile, 'r')
    nodes = count_node(f)
    for i in range(len(nodes)):
        plotting_node(f, nodes[i], OutType, level, g)
    f.close()

def data_type_info(level):
    if level == 'L2':
        return (3, ['Drop'])
    elif level == 'L3':
        return (4, ['InInterests', 'OutInterests', 
            'InData', 'OutData',
            'InSatisfiedInterests', 'InTimedOutInterests', 
            'OutSatisfiedInterests', 'OutTimedOutInterests'])
    elif level == 'app':
        return (4, ['FullDelay', 'LastDelay'])

def OutType_conversion(OutType, level):
    bias = 0 if level == 'L2' else 1
    if OutType == 'Packets':
        return 4 + bias
    elif OutType == 'Kilobytes':
        return 5 + bias
    elif OutType == 'PacketsRaw':
        return 6 + bias
    elif OutType == 'KilobytesRaw':
        return 7 + bias
    elif OutType == 'DelayS':
        return 5
    elif OutType == 'DelayUS':
        return 6
    elif OutType == 'RetxCount':
        return 7
    elif OutType == 'HopCount':
        return 8

