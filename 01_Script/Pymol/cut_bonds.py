# cd Cuby/Pymol_Skripte
from pymol import cmd
from sys import argv
import sys

def getID(x):
    modelx = cmd.get_model(x)
    IDs = []
    for atom in modelx.atom:
        IDs.append(atom)
    return IDs

#Ligand is not organic
def select_ligand(x, input):
    if x == 1: # ligand is not organic
        cmd.select("sel_ligand","resid "+str(input))
        cmd.create("Ligand","sel_ligand")
    else: # ligand is organic
        cmd.select("sel_ligand","organic")
        cmd.create("Ligand","sel_ligand")

#------------------------------------------------------------------------------
# split in 2 regions
def split_QMMM(A1, x, input):
    select_ligand(x,input)
    #Selection QM
    cmd.select("sel_QM", "Ligand expand "+str(A1))
    cmd.select("sel_resQM", "byres sel_QM")
    cmd.create("QM", "sel_resQM")
    # neighbors between QM and MM
    cmd.select("n2", "(bound_to sel_resQM) and not(sel_resQM)")
    cmd.select("n1", "(neighbor n2) and sel_resQM")
    # select MM
    cmd.select("sel_MM", "not (byres(Ligand expand "+str(A1)+"))")
    cmd.create("MM", "sel_MM")
    #call function
    generate_file_qmmm("n1","n2")

#view for 2 regions
def view_qmmm():
    cmd.hide("everything")
    cmd.show("lines")
    cmd.hide("nonbonded")
    cmd.color("white", "e. H")
    cmd.color("yellow", "e. C")
    cmd.color("red", "e. O")
    cmd.color("blue", "e. N")
    cmd.color("orange", "e. S")
    cmd.color("magenta"," e. FE")
    cmd.color("green","QM and e. C")
    cmd.color("hotpink","Ligand and e. C")
    cmd.show("sticks","QM")
    cmd.show("sticks","MM")
    cmd.show("sticks","Ligand")
    cmd.delete("sel_ligand")
    cmd.delete("sel_QM")
    cmd.delete("sel_resQM")
    cmd.delete("sel_MM")
    cmd.delete("at")
    cmd.delete("nb")

#generate file for 2 regions
def generate_file_qmmm(n1, n2):
    count = 1
    file = open("fragmentation_cut_bonds.txt","w")
    file.write("qmmm_cut_bonds:\n")
    zipp=getID(n1)
    for a in zipp:
        cmd.select("at", "rank "+str(a.id-1))
        cmd.select("nb", "(neighbor at)and n2")
        for b in getID("nb"):
            file.write("  - {bond: "+str(a.id)+"-"+str(b.id)+", link_ratio: 0.729, link_type: HL}\n")
            count = count + 1
    file.close()

#------------------------------------------------------------------------------
#split in 3 regions
def split_QMSEMM(A1, A2, x, input):
    select_ligand(x,input)
    # QM
    cmd.select("sel_QM", "Ligand expand "+str(A1))
    cmd.select("sel_resQM", "byres sel_QM")
    cmd.create("QM", "sel_resQM")
    # neighbors between QM and SE
    cmd.select("n2", "(bound_to sel_resQM) and not(sel_resQM)")
    cmd.select("n1", "(neighbor n2) and sel_resQM")
    # select SE
    cmd.select("sel_SE", "Ligand expand "+str(A2)+" and not(byres(Ligand expand "+str(A1)+"))")
    cmd.select("sel_resSE", "byres sel_SE")
    cmd.create("SE","sel_resSE")
    # neighbors between SE and MM
    cmd.select("n4", "(bound_to sel_resSE) and not(sel_resSE) and not(sel_resQM)")
    cmd.select("n3", "(neighbor n4) and sel_resSE")
    # select MM
    cmd.select("sel_MM", "not(byres(Ligand expand "+str(A2)+"))")
    cmd.create("MM","sel_MM")
    #call function
    generate_file_qmsemm("n1","n2","n3","n4")

#view for 3 regions
def view_qmsemm():
    cmd.hide("everything")
    cmd.show("lines")
    cmd.hide("nonbonded")
    cmd.color("white", "e. H")
    cmd.color("yellow", "e. C")
    cmd.color("red", "e. O")
    cmd.color("blue", "e. N")
    cmd.color("orange", "e. S")
    cmd.color("magenta"," e. FE")
    cmd.color("green","QM and e. C")
    cmd.color("sand","MM and e. C")
    cmd.color("hotpink","Ligand and e. C")
    cmd.show("sticks","QM")
    cmd.show("sticks", "SE")
    cmd.show("sticks","MM")
    cmd.show("sticks","Ligand")
    cmd.delete("sel_ligand")
    cmd.delete("sel_QM")
    cmd.delete("sel_resQM")
    cmd.delete("sel_SE")
    cmd.delete("sel_resSE")
    cmd.delete("sel_MM")
    cmd.delete("at")
    cmd.delete("nb")

#generate file for 2 regions
def generate_file_qmsemm(n1, n2, n3, n4):
    file = open("fragmentation_cut_bonds.txt","w")
    zipped = zip(getID(n1),getID(n2))
    zipped2 = zip(getID(n3),getID(n4))
    file.write("qmmm_cut_bonds:\n")
    for a in getID(n1):
        cmd.select("at", "rank "+str(a.id-1))
        cmd.select("nb", "(neighbor at)and n2")
        for b in getID("nb"):
            file.write("  - {bond: "+str(a.id)+"-"+str(b.id)+", link_ratio: 0.729, link_type: HL}\n")
    for c in getID(n3):
        cmd.select("at", "rank "+str(c.id-1))
        cmd.select("nb", "(neighbor at)and n4")
        for d in getID("nb"):
            file.write("  - {bond: "+str(c.id)+"-"+str(d.id)+", link_ratio: 0.729, link_type: HL}\n")
    file.close()

#------------------------------------------------------------------------------
#
#pymol A1 A2 PDB Ligand and not organic ligand
if argv[5] == "1":
  A1 = argv[1]
  input = argv[4]
  PDB = argv[3]
  cmd.load(PDB)
  if argv[2] == 0:
    split_QMMM(A1, 1, input)
    view_qmmm()
  else:
    A2 = argv[2]
    split_QMSEMM(A1, A2, 1, input)
    view_qmsemm()

#pymol A1 A2 PDB  and organic ligand
elif argv[5] == "0":
  A1 = argv[1]
  PDB = argv[3]
  cmd.load(PDB)
  if argv[2] == 0:
      split_QMMM(A1, 0, " ")
      view_qmmm()
  else:
      A2 = argv[2]
      split_QMSEMM(A1, A2, 0, " ")
      view_qmsemm()

else:
  file = open("fragmentation_cut_bonds.txt","w")
  file.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
  file.write("Please enter the correct number of input variables \n")
  file.write("!!!!!!!!!!!! Angstrom Angstrom PDB-Path !!!!!!!!!!! \n")
  for x in range(37):
      file.write("     \n")
  file.close()
