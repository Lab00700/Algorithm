def solution(video_len, pos, op_start, op_end, commands):
    video_sec=int(video_len.split(':')[0])*60+int(video_len.split(':')[1])
    pos_sec=int(pos.split(':')[0])*60+int(pos.split(':')[1])
    op_start_sec=int(op_start.split(':')[0])*60+int(op_start.split(':')[1])
    op_end_sec=int(op_end.split(':')[0])*60+int(op_end.split(':')[1])
    if pos_sec<op_end_sec and pos_sec>=op_start_sec:
        pos_sec=op_end_sec
    for c in commands:
        if c=="next":
            pos_sec+=10
            if pos_sec>video_sec:
                pos_sec=video_sec
        else:
            pos_sec-=10
            if pos_sec<0:
                pos_sec=0
        if pos_sec<op_end_sec and pos_sec>=op_start_sec:
            pos_sec=op_end_sec
    m,s=str(int(pos_sec/60)),str(pos_sec%60)
    if len(m)==1:
        m="0"+m
    if len(s)==1:
        s="0"+s
    return ':'.join([m,s])