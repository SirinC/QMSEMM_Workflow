import sys
import string
import argparse

def read_file(input): #reads in pdb file
    File = []
    for row in open(input).readlines():
        row = row.replace('\n', '')
        row = row.split('\n')
        for element in row:
            element = element.split()
            File.append(element)
    return(File)

def check_segment(atom, segid, residue): #checks if segid should be increased
    if atom == 'C1' or (atom == 'O' and  residue == 'HOH'):
        segid += 1
    return segid

def check_chain(x): #checks if there is a chain identifier or not
    if x.isalpha():
        return(1)
    else:
        return(0)

def check_resid(atom, resid, residue): #checks if resid should be increased
    if atom == 'N' or atom == 'C1' or (atom == 'O' and  residue == 'HOH'):
        resid += 1
    return resid

def write_file(output, File): # writes the PDB file
    segid = 1
    count = 0
    resid = 0
    pdb = open(output, 'w')
    for row in File:
        if row[0] != 'TER' and  row[0] != 'END':
            count += 1
            segid = check_segment(row[2], segid, row[3])
            resid = check_resid(row[2], resid, row[3])
            if check_chain(row[4]):
                write_pdb(pdb, row[0], count, resid, row[2], row[3], row[4], row[6], row[7], row[8], segid)
            else:
                write_pdb(pdb, row[0], count, resid, row[2], row[3], 'A', row[6], row[7], row[8], segid)
        else:
            segid += 1
            pdb.write(str(row[0])+'\n')

def write_pdb(pdb , name, count, resid, atom, residue, chain, cd1, cd2, cd3, segid): #writes in the new pdb file
    x=record_type(pdb, name)        #ATOM
    serial_number(pdb, x, count)    #COUNTER
    atom_name(pdb, atom)            #ATOMNAME
    pdb.write(str(residue))         #RESIDUE
    pdb.write(' '+str(chain))       #A CHAIN
    res_seq_number(pdb, resid)      #RESIDUE SEQUENCE NUMBER
    coord_x(pdb, cd1)               #X-COORDS
    coord_yz(pdb, cd2)              #Y-COORDS
    coord_yz(pdb, cd3)              #Z-COORDS
    occp_temp(pdb)                  #OCCUPANY & TEMPERATURE FACTOR
    pdb.write(str(segid))           #SEGMENTID
    element_symbol(pdb, atom, segid)#ELEMENT SYMBOL
    pdb.write('\n')

def record_type(pdb, name): #writes ATOM or HETATM
    if name == 'ATOM':
        pdb.write(str(name))
        return 1
    elif name == 'HETATM':
        pdb.write(str(name))
        return 2
    else:
        pdb.write('Fehler')
        return 0

def serial_number(pdb, x, count): #writes serial numer of atom
    if x == 1:
        pdb.write(sp0(count)+''+str(count))
    elif x == 2:
        pdb.write(sp1(count)+''+str(count))
    else:
        pdb.write(' '+str(count)+' ')

def atom_name(pdb, atom): #writes atom name
    x=len(atom)
    if x == 1:
        pdb.write('  '+str(atom)+'   ')
    elif x == 2:
        pdb.write('  '+str(atom)+'  ')
    elif x == 3:
        pdb.write('  '+str(atom)+' ')
    elif x ==4:
        pdb.write(' '+str(atom)+' ')
    else:
        pdb.write(str(atom))

def res_seq_number(pdb, id):#writes residue sequence number
    id = int(id)
    if id >= 1000:
        pdb.write(str(id))
    else:
        if id >= 100:
            pdb.write(' '+str(id))
        else:
            if id >= 10:
                pdb.write('  '+str(id))
            else:
                pdb.write('   '+str(id))

def coord_x(pdb, cd): #writes x coord
    x=len(cd)
    if x >= 8:
        pdb.write('    '+str(cd))
    else:
        if x >= 7:
            pdb.write('     '+str(cd))
        else:
            if x >= 6:
                pdb.write('      '+str(cd))
            else:
                pdb.write('       '+str(cd))

def coord_yz(pdb, cd): #writes y,z coord
    x=len(cd)
    if x >= 8:
        pdb.write(''+str(cd))
    else:
        if x >= 7:
            pdb.write(' '+str(cd))
        else:
            if x >= 6:
                pdb.write('  '+str(cd))
            else:
                pdb.write('   '+str(cd))

def occp_temp(pdb): #writes occupancy and temperature factor
    pdb.write('  ')
    pdb.write('1.00')
    pdb.write('  ')
    pdb.write('0.00')
    pdb.write('      ')

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

def sp0(x): #set some space
    x = int(x)
    if x >= 10000:
        sp = '  '
    else:
        if x >= 1000:
            sp = '   '
        else:
            if x >= 100:
                sp = '    '
            else:
                if x >= 10:
                    sp = '     '
                else:
                    sp = '      '
    return sp

def sp1(x): #set some space
    x = int(x)
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


# Main function
def main():
    parser = argparse.ArgumentParser(description="Prepare PDB for Cuby")
    parser.add_argument('input', metavar='in-file')
    parser.add_argument('output', metavar='out-file')
    args = parser.parse_args()


    write_file(args.output, read_file(args.input))




if __name__ == '__main__': main()
