def perfometer_ceph(row, check_command, perf_data):
    #return repr(perf_data), '<table><tr>' \
                               #+ perfometer_td(20, '#fff') \
                               #+ perfometer_td(80, '#ff0000') \
                               #+ '</tr></table>'
    used = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])
    smin = float(perf_data[0][5])
    smax = float(perf_data[0][6])
    percent = 100 * used/smax
    if used <= crit:
        color = "#00ff00"
    elif used <= warn:
        color = "#ffff00"
    else:
        color = "#ff0000"

    return "%.2f%%" % percent , perfometer_linear(percent, color)
perfometers['check_mk-ceph'] = perfometer_ceph
