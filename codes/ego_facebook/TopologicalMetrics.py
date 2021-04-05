from math import sqrt, log

def common_neighbors(g,u,v):
    u_nbr = set(g.neighbors(u))
    v_nbr = set(g.neighbors(v))
    return len(u_nbr.intersection(v_nbr))

def jaccard_coefficient(g,u,v):
	u_nbr = set(g.neighbors(u))
	v_nbr = set(g.neighbors(v))
	return len(u_nbr.intersection(v_nbr))/len(u_nbr.union(v_nbr))

def sorensen_index(g,u,v):
	u_nbr = set(g.neighbors(u))
	v_nbr = set(g.neighbors(v))
	return len(u_nbr.intersection(v_nbr))/(len(u_nbr)+len(v_nbr))

def leicht_holme_nerman(g,u,v):
	u_nbr = set(g.neighbors(u))
	v_nbr = set(g.neighbors(v))
	return len(u_nbr.intersection(v_nbr))/(len(u_nbr)*len(v_nbr))

def salton_cosine_similarity(g,u,v):
    u_nbr = set(g.neighbors(u))
    v_nbr = set(g.neighbors(v))
    return len(u_nbr.intersection(v_nbr))/sqrt(len(u_nbr)*len(v_nbr))

def hub_promoted_index(g,u,v):
    u_nbr = set(g.neighbors(u))
    v_nbr = set(g.neighbors(v))
    return len(u_nbr.intersection(v_nbr))/min(len(u_nbr),len(v_nbr))

def hub_depressed_index(g,u,v):
    u_nbr = set(g.neighbors(u))
    v_nbr = set(g.neighbors(v))
    return len(u_nbr.intersection(v_nbr))/max(len(u_nbr),len(v_nbr))

def preferential_attachment(g,u,v):
    u_nbr = set(g.neighbors(u))
    v_nbr = set(g.neighbors(v))
    return len(u_nbr)*len(v_nbr)

def resource_allocation(g,u,v):
    u_nbr = set(g.neighbors(u))
    v_nbr = set(g.neighbors(v))
    cn = u_nbr.intersection(v_nbr)
    ra = 0
    for i in cn:
        ra += 1/float(len(set(g.neighbors(i))))
    return ra

def adamic_adar(g,u,v):
    u_nbr = set(g.neighbors(u))
    v_nbr = set(g.neighbors(v))
    cn = u_nbr.intersection(v_nbr)
    aa = 0
    for i in cn:
        aa += 1/log(len(set(g.neighbors(i))))
    return aa