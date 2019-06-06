from Bio.PDB import *
import aminoAcid
import string
import argparse


def generate_pdb(name, input): #generates the new Pdb file with new atom names
    pdb = open(name, 'w')
    count, segid, resid = 1, 1, 0
    parser = PDBParser()
    structure = parser.get_structure('protein', input)

    for model in structure:
        for chain in model:
            for residue in chain:
                resid += 1
                if residue.get_id()[0] == ' ':   # change Atoms and coords
                    new_atom, new_coords = aminoAcid.rec_residue(residue)
                    for j in range(0,len(new_atom)):
                        write_pdb(pdb, 'ATOM', count, resid, segid, new_atom[j], residue.get_resname(), chain.get_id(), new_coords[j])
                        count += 1
                else:
                    segid += 1
                    pdb.write('TER\n')
                    for atom in residue:
                        write_pdb(pdb, 'HETATM', count, resid, segid, atom.get_name(), residue.get_resname(), chain.get_id(), atom.get_coord())
                        count += 1

    pdb.write('TER\nEND')
    pdb.close()

def write_pdb(pdb, name, count, resid, segid, atom, residue, chain, coords): #writes in the new pdb file
    sp1, sp2 = space2(len(atom))
    record_type(pdb, name) #ATOM
    pdb.write(space1(count))
    pdb.write(str(count)) #COUNTER
    pdb.write(sp1)
    pdb.write(str(atom)) #ATOMNAME
    pdb.write(sp2)
    pdb.write(check_residue(residue)) #RESIDUE
    pdb.write(' '+str(chain)) #A CHAIN
    pdb.write(space3(resid))
    pdb.write(str(resid)) #ID
    pdb.write('    ')
    pdb.write('%8.3f'% (coords[0])) #X COORDS
    pdb.write('%8.3f'% (coords[1])) #Y COORDS
    pdb.write('%8.3f'% (coords[2])) #Z COORDS
    pdb.write('  ')
    pdb.write('1.00')
    pdb.write('  ')
    pdb.write('0.00')
    pdb.write('      ')
    pdb.write(str(segid)) #SEGMENTID
    element_symbol(pdb, atom, segid)#ELEMENT SYMBOL
    pdb.write('\n')

def element_symbol(pdb, atom, id): #writes element symbol
    if id >= 1000:
        pdb.write(atom[0])
    else:
        if id >= 100:
            pdb.write('  '+atom[0])
        else:
            if id >= 10:
                pdb.write('   '+atom[0])
            else:
                pdb.write('    '+atom[0])

def check_residue(residue): # set protonate state of Histidin
    if residue == 'HIS':
        return('HSE')
    return(residue)

def record_type(pdb, name): #writes ATOM or HETATM
    if name == 'ATOM':
        pdb.write('ATOM  ')
    elif name == 'HETATM':
        pdb.write('HETATM')
    else:
        pdb.write(str(name)+' ')

def space1(x): #set some space
    if x >= 10000:
        sp = ''
    else:
        if x >= 1000:
            sp = ' '
        else:
            if x >= 100:
                sp = '  '
            else:
                if x >= 10:
                    sp = '   '
                else:
                    sp = '    '
    return sp

def space2(x): #set some space
        if x == 4:
            sp1 = ' '
            sp2 = ' '
        else:
            if x == 3:
                sp1 = '  '
                sp2 = ' '
            else:
                if x == 2:
                    sp1 = '  '
                    sp2 = '  '
                else:
                    if x == 1:
                        sp1 = '  '
                        sp2 = '   '
                    else:
                        sp1 = '--FEHLER--'
                        sp2 = '--FEHLER--'
        return sp1,sp2

def space3(x): #set some space
    if x >= 1000:
        sp = ''
    else:
        if x >= 100:
            sp = ' '
        else:
            if x >= 10:
                sp = '  '
            else:
                sp = '   '
    return sp

def space4(x): #set some space
    if x >= 1000:
        sp = ''
    else:
        if x >= 100:
            sp = ' '
        else:
            if x >= 10:
                sp = '  '
            else:
                sp = '   '
    return sp


# Main function
def main():
    parser = argparse.ArgumentParser(description="Prepare PDB for Cuby")
    parser.add_argument('input', metavar='in-file')
    parser.add_argument('output', metavar='out-file')
    args = parser.parse_args()

    generate_pdb(args.output, args.input)


if __name__ == '__main__': main()
