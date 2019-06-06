#return coords and Atomname

def SER(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    OG=[0,0,0]
    HG1=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
    if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("OG"):
        OG = residue["OG"].get_coord()
    if residue.has_id("HG"):
        HG1 = residue["HG"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,OG,HG1,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","OG","HG1","C","O"]
    return(at,coord)

def VAL(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB=[0,0,0]
    CG1=[0,0,0]
    HG11=[0,0,0]
    HG12=[0,0,0]
    HG13=[0,0,0]
    CG2=[0,0,0]
    HG21=[0,0,0]
    HG22=[0,0,0]
    HG23=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]
    if residue.has_id("N"):
        N = residue["N"].get_coord()
    if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB"):
        HB = residue["HB"].get_coord()
    if residue.has_id("CG1"):
        CG1 = residue["CG1"].get_coord()
    if residue.has_id("HG11"):
        HG11 = residue["HG11"].get_coord()
    if residue.has_id("HG12"):
        HG12 = residue["HG12"].get_coord()
    if residue.has_id("HG13"):
        HG13 = residue["HG13"].get_coord()
    if residue.has_id("CG2"):
        CG2 = residue["CG2"].get_coord()
    if residue.has_id("HG21"):
        HG21 = residue["HG21"].get_coord()
    if residue.has_id("HG22"):
        HG22 = residue["HG22"].get_coord()
    if residue.has_id("HG23"):
        HG23 = residue["HG23"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()

    coord=[N,HN,CA,HA,CB,HB,CG1,HG11,HG12,HG13,CG2,HG21,HG22,HG23,C,O]
    at=["N","HN","CA","HA","CB","HB","CG1","HG11","HG12","HG13","CG2","HG21","HG22","HG23","C","O"]
    return(at,coord)

def PRO(residue):
    N=[0,0,0]
    CD=[0,0,0]
    HD1=[0,0,0]
    HD2=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    HG1=[0,0,0]
    HG2=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
    if residue.has_id("CD"):
        CD = residue["CD"].get_coord()
    if residue.has_id("HD2"):
        HD1 = residue["HD2"].get_coord()
    if residue.has_id("HD3"):
        HD2 = residue["HD3"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("HG2"):
        HG1 = residue["HG2"].get_coord()
    if residue.has_id("HG3"):
        HG2 = residue["HG3"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,CD,HD1,HD2,CA,HA,CB,HB1,HB2,CG,HG1,HG2,C,O]
    at=["N","CD","HD1","HD2","CA","HA","CB","HB1","HB2","CG","HG1","HG2","C","O"]
    return(at,coord)

def GLN(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    HG1=[0,0,0]
    HG2=[0,0,0]
    CD=[0,0,0]
    OE1=[0,0,0]
    NE2=[0,0,0]
    HE21=[0,0,0]
    HE22=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("HG2"):
        HG1 = residue["HG2"].get_coord()
    if residue.has_id("HG3"):
        HG2 = residue["HG3"].get_coord()
    if residue.has_id("CD"):
        CD = residue["CD"].get_coord()
    if residue.has_id("OE1"):
        OE1 = residue["OE1"].get_coord()
    if residue.has_id("NE2"):
        NE2 = residue["NE2"].get_coord()
    if residue.has_id("HE21"):
        HE21 = residue["HE21"].get_coord()
    if residue.has_id("HE22"):
        HE22 = residue["HE22"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,HG1,HG2,CD,OE1,NE2,HE21,HE22,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","CG","HG1","HG2","CD","OE1","NE2","HE21","HE22","C","O"]
    return(at,coord)

def LYS(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    HG1=[0,0,0]
    HG2=[0,0,0]
    CD=[0,0,0]
    HD1=[0,0,0]
    HD2=[0,0,0]
    CE=[0,0,0]
    HE1=[0,0,0]
    HE2=[0,0,0]
    NZ=[0,0,0]
    HZ1=[0,0,0]
    HZ2=[0,0,0]
    HZ3=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]
    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("HG2"):
        HG1 = residue["HG2"].get_coord()
    if residue.has_id("HG3"):
        HG2 = residue["HG3"].get_coord()
    if residue.has_id("CD"):
        CD = residue["CD"].get_coord()
    if residue.has_id("HD2"):
        HD1 = residue["HD2"].get_coord()
    if residue.has_id("HD3"):
        HD2 = residue["HD3"].get_coord()
    if residue.has_id("CE"):
        CE = residue["CE"].get_coord()
    if residue.has_id("HE2"):
        HE1 = residue["HE2"].get_coord()
    if residue.has_id("HE3"):
        HE2 = residue["HE3"].get_coord()
    if residue.has_id("NZ"):
        NZ = residue["NZ"].get_coord()
    if residue.has_id("HZ1"):
        HZ1 = residue["HZ1"].get_coord()
    if residue.has_id("HZ2"):
        HZ2 = residue["HZ2"].get_coord()
    if residue.has_id("HZ3"):
        HZ3 = residue["HZ3"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,HG1,HG2,CD,HD1,HD2,CE,HE1,HE2,NZ,HZ1,HZ2,HZ3,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","CG","HG1","HG2","CD","HD1","HD2","CE","HE1","HE2","NZ","HZ1","HZ2","HZ3","C","O"]
    return(at,coord)

def THR(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB=[0,0,0]
    OG1=[0,0,0]
    HG1=[0,0,0]
    CG2=[0,0,0]
    HG21=[0,0,0]
    HG22=[0,0,0]
    HG23=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]
    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB"):
        HB = residue["HB"].get_coord()
    if residue.has_id("OG1"):
        OG1 = residue["OG1"].get_coord()
    if residue.has_id("HG1"):
        HG1 = residue["HG1"].get_coord()
    if residue.has_id("CG2"):
        CG2 = residue["CG2"].get_coord()
    if residue.has_id("HG21"):
        HG21 = residue["HG21"].get_coord()
    if residue.has_id("HG22"):
        HG22 = residue["HG22"].get_coord()
    if residue.has_id("HG23"):
        HG23 = residue["HG23"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB,OG1,HG1,CG2,HG21,HG22,HG23,C,O]
    at=["N","HN","CA","HA","CB","HB","OG1","HG1","CG2","HG21","HG22","HG23","C","O"]
    return(at,coord)

def TYR(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    CD1=[0,0,0]
    HD1=[0,0,0]
    CE1=[0,0,0]
    HE1=[0,0,0]
    CZ=[0,0,0]
    OH=[0,0,0]
    HH=[0,0,0]
    CD2=[0,0,0]
    HD2=[0,0,0]
    CE2=[0,0,0]
    HE2=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("CD1"):
        CD1 = residue["CD1"].get_coord()
    if residue.has_id("CD"):
        CD1 = residue["CD"].get_coord()
    if residue.has_id("HD1"):
        HD1 = residue["HD1"].get_coord()
    if residue.has_id("CE1"):
        CE1 = residue["CE1"].get_coord()
    if residue.has_id("HE1"):
        HE1 = residue["HE1"].get_coord()
    if residue.has_id("CZ"):
        CZ = residue["CZ"].get_coord()
    if residue.has_id("OH"):
        OH = residue["OH"].get_coord()
    if residue.has_id("HH"):
        HH = residue["HH"].get_coord()
    if residue.has_id("CD2"):
        CD2 = residue["CD2"].get_coord()
    if residue.has_id("HD2"):
        HD2 = residue["HD2"].get_coord()
    if residue.has_id("CE2"):
        CE2 = residue["CE2"].get_coord()
    if residue.has_id("HE2"):
        HE2 = residue["HE2"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,CD1,HD1,CE1,HE1,CZ,OH,HH,CD2,HD2,CE2,HE2,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","CG","CD1","HD1","CE1","HE1","CZ","OH","HH","CD2","HD2","CE2","HE2","C","O"]
    return(at,coord)

def GLY(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA1=[0,0,0]
    HA2=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA2"):
        HA1 = residue["HA2"].get_coord()
    if residue.has_id("HA3"):
        HA2 = residue["HA3"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA1,HA2,C,O]
    at=["N","HN","CA","HA1","HA2","C","O"]
    return(at,coord)

def PHE(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    CD1=[0,0,0]
    HD1=[0,0,0]
    CE1=[0,0,0]
    HE1=[0,0,0]
    CZ=[0,0,0]
    HZ=[0,0,0]
    CD2=[0,0,0]
    HD2=[0,0,0]
    CE2=[0,0,0]
    HE2=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]
    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("CD1"):
        CD1 = residue["CD1"].get_coord()
    if residue.has_id("CD"):
        CD1 = residue["CD"].get_coord()
    if residue.has_id("HD1"):
        HD1 = residue["HD1"].get_coord()
    if residue.has_id("CE1"):
        CE1 = residue["CE1"].get_coord()
    if residue.has_id("HE1"):
        HE1 = residue["HE1"].get_coord()
    if residue.has_id("CZ"):
        CZ = residue["CZ"].get_coord()
    if residue.has_id("HZ"):
        HZ = residue["HZ"].get_coord()
    if residue.has_id("CD2"):
        CD2 = residue["CD2"].get_coord()
    if residue.has_id("HD2"):
        HD2 = residue["HD2"].get_coord()
    if residue.has_id("CE2"):
        CE2 = residue["CE2"].get_coord()
    if residue.has_id("HE2"):
        HE2 = residue["HE2"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,CD1,HD1,CE1,HE1,CZ,HZ,CD2,HD2,CE2,HE2,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","CG","CD1","HD1","CE1","HE1","CZ","HZ","CD2","HD2","CE2","HE2","C","O"]
    return(at,coord)

def ARG(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    HG1=[0,0,0]
    HG2=[0,0,0]
    CD=[0,0,0]
    HD1=[0,0,0]
    HD2=[0,0,0]
    NE=[0,0,0]
    HE=[0,0,0]
    CZ=[0,0,0]
    NH1=[0,0,0]
    HH11=[0,0,0]
    HH12=[0,0,0]
    NH2=[0,0,0]
    HH21=[0,0,0]
    HH22=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("HG2"):
        HG1 = residue["HG2"].get_coord()
    if residue.has_id("HG3"):
        HG2 = residue["HG3"].get_coord()
    if residue.has_id("CD"):
        CD = residue["CD"].get_coord()
    if residue.has_id("HD2"):
        HD1 = residue["HD2"].get_coord()
    if residue.has_id("HD3"):
        HD2 = residue["HD3"].get_coord()
    if residue.has_id("NE"):
        NE = residue["NE"].get_coord()
    if residue.has_id("HE"):
        HE = residue["HE"].get_coord()
    if residue.has_id("CZ"):
        CZ = residue["CZ"].get_coord()
    if residue.has_id("NH1"):
        NH1 = residue["NH1"].get_coord()
    if residue.has_id("HH11"):
        HH11 = residue["HH11"].get_coord()
    if residue.has_id("HH12"):
        HH12 = residue["HH12"].get_coord()
    if residue.has_id("NH2"):
        NH2 = residue["NH2"].get_coord()
    if residue.has_id("HH21"):
        HH21 = residue["HH21"].get_coord()
    if residue.has_id("HH22"):
        HH22 = residue["HH22"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,HG1,HG2,CD,HD1,HD2,NE,HE,CZ,NH1,HH11,HH12,NH2,HH21,HH22,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","CG","HG1","HG2","CD","HD1","HD2","NE","HE","CZ","NH1","HH11","HH12","NH2","HH21","HH22","C","O"]
    return(at,coord)

def LEU(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    HG=[0,0,0]
    CD1=[0,0,0]
    HD11=[0,0,0]
    HD12=[0,0,0]
    HD13=[0,0,0]
    CD2=[0,0,0]
    HD21=[0,0,0]
    HD22=[0,0,0]
    HD23=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]
    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("HG"):
        HG = residue["HG"].get_coord()
    if residue.has_id("CD1"):
        CD1 = residue["CD1"].get_coord()
    if residue.has_id("CD"):
        CD1 = residue["CD"].get_coord()
    if residue.has_id("HD11"):
        HD11 = residue["HD11"].get_coord()
    if residue.has_id("HD12"):
        HD12 = residue["HD12"].get_coord()
    if residue.has_id("HD13"):
        HD13 = residue["HD13"].get_coord()
    if residue.has_id("CD2"):
        CD2 = residue["CD2"].get_coord()
    if residue.has_id("HD21"):
        HD21 = residue["HD21"].get_coord()
    if residue.has_id("HD22"):
        HD22 = residue["HD22"].get_coord()
    if residue.has_id("HD23"):
        HD23 = residue["HD23"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,HG,CD1,HD11,HD12,HD13,CD2,HD21,HD22,HD23,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","CG","HG","CD1","HD11","HD12","HD13","CD2","HD21","HD22","HD23","C","O"]
    return(at,coord)

def HIS(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    ND1=[0,0,0]
    CG=[0,0,0]
    CE1=[0,0,0]
    HE1=[0,0,0]
    NE2=[0,0,0]
    HE2=[0,0,0]
    CD2=[0,0,0]
    HD2=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("ND1"):
        ND1 = residue["ND1"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("CE1"):
        CE1 = residue["CE1"].get_coord()
    if residue.has_id("HE1"):
        HE1 = residue["HE1"].get_coord()
    if residue.has_id("NE2"):
        NE2 = residue["NE2"].get_coord()
    if residue.has_id("HE2"):
        HE2 = residue["HE2"].get_coord()
    if residue.has_id("HD1"):
        HE2 = residue["HD1"].get_coord()
    if residue.has_id("CD2"):
        CD2 = residue["CD2"].get_coord()
    if residue.has_id("HD2"):
        HD2 = residue["HD2"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,ND1,CG,CE1,HE1,NE2,HE2,CD2,HD2,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","ND1","CG","CE1","HE1","NE2","HE2","CD2","HD2","C","O"]
    return(at,coord)

def ALA(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    HB3=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB1"):
        HB1 = residue["HB1"].get_coord()
    if residue.has_id("HB2"):
        HB2 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB3 = residue["HB3"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,HB3,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","HB3","C","O"]
    return(at,coord)

def CYS(residue): ###AUSNAHME
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    SG=[0,0,0]
    HG1=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("SG"):
        SG = residue["SG"].get_coord()
    if residue.has_id("HG"):
        HG1 = residue["HG"].get_coord()
    if residue.has_id("HG1"):
        HG1 = residue["HG1"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,SG,HG1,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","SG","HG1","C","O"]
    return(at,coord)

def ASN(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    OD1=[0,0,0]
    ND2=[0,0,0]
    HD21=[0,0,0]
    HD22=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("OD1"):
        OD1 = residue["OD1"].get_coord()
    if residue.has_id("ND2"):
        ND2 = residue["ND2"].get_coord()
    if residue.has_id("HD21"):
        HD21 = residue["HD21"].get_coord()
    if residue.has_id("HD22"):
        HD22 = residue["HD22"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,OD1,ND2,HD21,HD22,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","CG","OD1","ND2","HD21","HD22","C","O"]
    return(at,coord)

def TRP(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    CD1=[0,0,0]
    HD1=[0,0,0]
    NE1=[0,0,0]
    HE1=[0,0,0]
    CE2=[0,0,0]
    CD2=[0,0,0]
    CE3=[0,0,0]
    HE3=[0,0,0]
    CZ3=[0,0,0]
    HZ3=[0,0,0]
    CZ2=[0,0,0]
    HZ2=[0,0,0]
    CH2=[0,0,0]
    HH2=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("CD1"):
        CD1 = residue["CD1"].get_coord()
    if residue.has_id("CD"):
        CD1 = residue["CD"].get_coord()
    if residue.has_id("HD1"):
        HD1 = residue["HD1"].get_coord()
    if residue.has_id("NE1"):
        NE1 = residue["NE1"].get_coord()
    if residue.has_id("HE1"):
        HE1 = residue["HE1"].get_coord()
    if residue.has_id("CE2"):
        CE2 = residue["CE2"].get_coord()
    if residue.has_id("CD2"):
        CD2 = residue["CD2"].get_coord()
    if residue.has_id("CE3"):
        CE3 = residue["CE3"].get_coord()
    if residue.has_id("HE3"):
        HE3 = residue["HE3"].get_coord()
    if residue.has_id("CZ3"):
        CZ3 = residue["CZ3"].get_coord()
    if residue.has_id("HZ3"):
        HZ3 = residue["HZ3"].get_coord()
    if residue.has_id("CZ2"):
        CZ2 = residue["CZ2"].get_coord()
    if residue.has_id("HZ2"):
        HZ2 = residue["HZ2"].get_coord()
    if residue.has_id("CH2"):
        CH2 = residue["CH2"].get_coord()
    if residue.has_id("HH2"):
        HH2 = residue["HH2"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()

    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,CD1,HD1,NE1,HE1,CE2,CD2,CE3,HE3,CZ3,HZ3,CZ2,HZ2,CH2,HH2,C,O]
    at=['N','HN','CA','HA','CB','HB1','HB2','CG','CD1','HD1','NE1','HE1','CE2','CD2','CE3','HE3','CZ3','HZ3','CZ2','HZ2','CH2','HH2','C','O']
    return(at,coord)

def ASP(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    OD1=[0,0,0]
    OD2=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("OD1"):
        OD1 = residue["OD1"].get_coord()
    if residue.has_id("OD2"):
        OD2 = residue["OD2"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,OD1,OD2,C,O]
    at=['N','HN','CA','HA','CB','HB1','HB2','CG','OD1','OD2','C','O']
    return(at,coord)

def MET(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    HG1=[0,0,0]
    HG2=[0,0,0]
    SD=[0,0,0]
    CE=[0,0,0]
    HE1=[0,0,0]
    HE2=[0,0,0]
    HE3=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("HG2"):
        HG1 = residue["HG2"].get_coord()
    if residue.has_id("HG3"):
        HG2 = residue["HG3"].get_coord()
    if residue.has_id("SD"):
        SD = residue["SD"].get_coord()
    if residue.has_id("CE"):
        CE = residue["CE"].get_coord()
    if residue.has_id("HE1"):
        HE1 = residue["HE1"].get_coord()
    if residue.has_id("HE2"):
        HE2 = residue["HE2"].get_coord()
    if residue.has_id("HE3"):
        HE3 = residue["HE3"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,HG1,HG2,SD,CE,HE1,HE2,HE3,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","CG","HG1","HG2","SD","CE","HE1","HE2","HE3","C","O"]
    return(at,coord)

def ILE(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB=[0,0,0]
    CG2=[0,0,0]
    HG21=[0,0,0]
    HG22=[0,0,0]
    HG23=[0,0,0]
    CG1=[0,0,0]
    HG11=[0,0,0]
    HG12=[0,0,0]
    CD=[0,0,0]
    HD1=[0,0,0]
    HD2=[0,0,0]
    HD3=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB"):
        HB = residue["HB"].get_coord()
    if residue.has_id("CG2"):
        CG2 = residue["CG2"].get_coord()
    if residue.has_id("HG21"):
        HG21 = residue["HG21"].get_coord()
    if residue.has_id("HG22"):
        HG22 = residue["HG22"].get_coord()
    if residue.has_id("HG23"):
        HG23 = residue["HG23"].get_coord()
    if residue.has_id("CG1"):
        CG1 = residue["CG1"].get_coord()
    if residue.has_id("HG12"):
        HG11 = residue["HG12"].get_coord()
    if residue.has_id("HG13"):
        HG12 = residue["HG13"].get_coord()
    if residue.has_id("CD1"):
        CD = residue["CD1"].get_coord()
    if residue.has_id("CD"):
        CD = residue["CD"].get_coord()
    if residue.has_id("HD11"):
        HD1 = residue["HD11"].get_coord()
    if residue.has_id("HD12"):
        HD2 = residue["HD12"].get_coord()
    if residue.has_id("HD13"):
        HD3 = residue["HD13"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB,CG2,HG21,HG22,HG23,CG1,HG11,HG12,CD,HD1,HD2,HD3,C,O]
    at=["N","HN","CA","HA","CB","HB","CG2","HG21","HG22","HG23","CG1","HG11","HG12","CD","HD1","HD2","HD3","C","O"]
    return(at,coord)

def GLU(residue):
    N=[0,0,0]
    HN=[0,0,0]
    CA=[0,0,0]
    HA=[0,0,0]
    CB=[0,0,0]
    HB1=[0,0,0]
    HB2=[0,0,0]
    CG=[0,0,0]
    HG1=[0,0,0]
    HG2=[0,0,0]
    CD=[0,0,0]
    OE1=[0,0,0]
    OE2=[0,0,0]
    C=[0,0,0]
    O=[0,0,0]

    if residue.has_id("N"):
        N = residue["N"].get_coord()
	if residue.has_id("H2"):
        HN = residue["H2"].get_coord()
    if residue.has_id("H"):
        HN = residue["H"].get_coord()
    if residue.has_id("CA"):
        CA = residue["CA"].get_coord()
    if residue.has_id("HA"):
        HA = residue["HA"].get_coord()
    if residue.has_id("CB"):
        CB = residue["CB"].get_coord()
    if residue.has_id("HB2"):
        HB1 = residue["HB2"].get_coord()
    if residue.has_id("HB3"):
        HB2 = residue["HB3"].get_coord()
    if residue.has_id("CG"):
        CG = residue["CG"].get_coord()
    if residue.has_id("HG2"):
        HG1 = residue["HG2"].get_coord()
    if residue.has_id("HG3"):
        HG2 = residue["HG3"].get_coord()
    if residue.has_id("CD"):
        CD = residue["CD"].get_coord()
    if residue.has_id("OE1"):
        OE1 = residue["OE1"].get_coord()
    if residue.has_id("OE2"):
        OE2 = residue["OE2"].get_coord()
    if residue.has_id("C"):
        C = residue["C"].get_coord()
    if residue.has_id("O"):
        O = residue["O"].get_coord()
    coord=[N,HN,CA,HA,CB,HB1,HB2,CG,HG1,HG2,CD,OE1,OE2,C,O]
    at=["N","HN","CA","HA","CB","HB1","HB2","CG","HG1","HG2","CD","OE1","OE2","C","O"]
    return(at,coord)


def rec_residue(residue):
    r=residue.get_resname()
    x=[]
    y=[]
    if r =="SER":
        x,y=SER(residue)
    if r =="ASP":
        x,y=ASP(residue)
    if r =="GLU":
        x,y=GLU(residue)
    if r =="PRO":
        x,y=PRO(residue)
    if r =="GLN":
        x,y=GLN(residue)
    if r =="THR":
        x,y=THR(residue)
    if r =="LYS":
        x,y=LYS(residue)
    if r =="TYR":
        x,y=TYR(residue)
    if r =="GLY":
        x,y=GLY(residue)
    if r =="PHE":
        x,y=PHE(residue)
    if r =="ARG":
        x,y=ARG(residue)
    if r =="LEU":
        x,y=LEU(residue)
    if r =="HIS":
        x,y=HIS(residue)
    if r =="ALA":
        x,y=ALA(residue)
    if r =="CYS":
        x,y=CYS(residue)
    if r =="ASN":
        x,y=ASN(residue)
    if r =="TRP":
        x,y=TRP(residue)
    if r =="MET":
        x,y=MET(residue)
    if r =="ILE":
        x,y=ILE(residue)
    if r =="VAL":
        x,y=VAL(residue)
    return(x,y)
