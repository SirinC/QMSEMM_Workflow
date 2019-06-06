#!/bin/sh
#sudo zypper install dialog
#============================================================================================

#============================================================================================
#-------------------------------------------------------------
# Create Calculation Informations
#-------------------------------------------------------------
create_infos(){
echo "
============================================================
                 Calculation Informations
============================================================

Pdb Data: $1

Ligand: $2

Shell 1: $3, $4 Angstrom

Shell 2: $5, $6 Angstrom

Shell 3: $7" > Results/calc_informations.txt
}
#-------------------------------------------------------------
# Check if files exists
#-------------------------------------------------------------
check_files() {

  if [ ! -f "charmm.yaml" ]
  then
	  echo " !!!! charmm.yaml not found !!!!"
	  exit 1
  fi

  if [ ! -f "mopac.yaml" ]
  then
	  echo " !!!! mopac.yaml not found !!!!"
	  exit 1
  fi

  if [ ! -f "turbomole.yaml" ]
  then
	  echo " !!!! turbomole.yaml not found !!!!"
	  exit 1
  fi

  if [ ! -f "fragmentation.yaml" ]
  then
	  echo " !!!! fragmentation.yaml not found !!!!"
	  exit 1
  fi

  if [ ! -f "input.txt" ]
  then
	  echo " !!!! input.txt not found !!!!"
	  exit 1
  fi

  #-------------------------------
  #check directory exists
  if [ ! -d "02_Pdb" ]
  then
	mkdir -v Pdb
  fi

  if [ ! -d "01_Script" ]
  then
	echo " !!!! Script folder not found !!!"
	exit 1
  fi

  if [ ! -d "Results" ]
  then
	mkdir -v Results
  fi

}
#-------------------------------------------------------------
# read input from input.txt
#-------------------------------------------------------------
read_input() {
    count=0
    while read -r line;
    do
        IFS=',' read -ra VARIABLES <<< "$line"
        pdb+=(${VARIABLES[0]})                       #Pdb file
        ligand+=("$(tr [a-z] [A-Z]  <<< "${VARIABLES[1]}")")   #Ligand uppcase
        angstrom1+=(${VARIABLES[2]})   #Angstrom 1
        shell1+=(${VARIABLES[3]})       #Method for Shell 1
        angstrom2+=(${VARIABLES[4]})   #Angstrom 2
        shell2+=(${VARIABLES[5]})      #Method for Shell 2
        shell3+=(${VARIABLES[6]})       #Method for shell 3
        count=$((count + 1))
    done < input.txt
}
#-------------------------------------------------------------
# check input from input.txt
#-------------------------------------------------------------
check_input() {
    for ((i=0;i<$count;++i));
    do
        shell1[$i]=${shell1[$i],,}
        shell2[$i]=${shell2[$i],,}
        shell3[$i]=${shell3[$i],,}

        if ! [  -f "02_Pdb/${pdb[$i]}" ]
        then
            echo -e "\e[90m !!!! Pdb-file not found in row $i and position 1\e[0m"
            echo -e "\e[90m PDB, Ligand, A1, Turbomole, A2, Mopac, Charmm\e[0m"
            exit 1
        fi

        if  ! [[ ${angstrom1[$i]} =~ ^[0-9]+$ ]]
        then
            echo -e "\e[90m !!!! Only numbers for Angstrom in row $i and position 3\e[0m"
            echo -e "\e[90m PDB, Ligand, A1, Turbomole, A2, Mopac, Charmm\e[0m"
            exit 1
        fi

        if  ! [[ ${angstrom2[$i]} =~ ^[0-9]+$ ]]
        then
            echo -e "\e[90m !!!! Only numbers for Angstrom in row $i and position 5\e[0m"
            echo -e "\e[90m PDB, Ligand, A1, Turbomole, A2, Mopac, Charmm\e[0m"
            exit 1
        fi

        case ${shell1[$i]} in
            "turbomole")
                        ;;
            "mopac")
                        ;;
            "charmm")
                        ;;
            *)
                        echo -e "\e[90m !!!! Only Charmm, Mopac or Turbomole in row $i and position 4\e[0m"
                        echo -e "\e[90m PDB, Ligand, A1, Turbomole, A2, Mopac, Charmm\e[0m"
                        exit 1
                        ;;
        esac
        case ${shell2[$i]} in
            "turbomole")
                        ;;
            "mopac")
                        ;;
            "charmm")
                        ;;
            0)
                        ;;
            *)
                        echo -e "\e[90m !!!! Only Charmm, Mopac, Turbomole or 0 in row $i and position 6\e[0m"
                        echo -e "\e[90m PDB, Ligand, A1, Turbomole, A2, Mopac, Charmm\e[0m"
                        exit 1
                        ;;
        esac
        case ${shell3[$i]} in
            "turbomole")
                        ;;
            "mopac")
                        ;;
            "charmm")
                        ;;
            0)
                        ;;
            *)
                        echo -e "\e[90m !!!! Only Charmm, Mopac, Turbomole or 0 in row $i and position 7\e[0m"
                        echo -e "\e[90m PDB, Ligand, A1, Turbomole, A2, Mopac, Charmm\e[0m"
                        exit 1
                        ;;
        esac

    done
}
#============================================================================================
read_input
check_input
#============================================================================================
#-------------------------------------------------------------
# Run Cut Bonds   A A PDB      --> and get Fragments.pdb
#-------------------------------------------------------------
run_pymol() {
    if [[ $4 =~ ^[a-zA-Z]+$ ]] ;
    then # organic
        pymol -cq 01_Script/Pymol/cut_bonds.py -- $1 $2 ~/Cuby/QMSEMM_Workflow/02_Pdb/$3 $4 0

    else #not organic
        pymol -cq 01_Script/Pymol/cut_bonds.py -- $1 $2 ~/Cuby/QMSEMM_Workflow/02_Pdb/$3 $4 1
    fi
}
#-------------------------------------------------------------
# prepare YAML data with geometry PDB
#-------------------------------------------------------------
prepare_geometry() {
    sed -i "$z_geo c\  geometry: &inpt 02_Pdb/$1" charmm.yaml
    sed -i "$z_geo c\  geometry: &inpt 02_Pdb/$1" mopac.yaml
    sed -i "$z_geo c\  geometry: &inpt 02_Pdb/$1" turbomole.yaml
    sed -i "$z_frag_geo c\geometry: 02_Pdb/$1" fragmentation.yaml
}
#-------------------------------------------------------------
# update Fragmetation.pdb with fragments.txt
#-------------------------------------------------------------
prepare_fragmentation() {
# insert frag_cut_bonds in fragmentation.yaml
head -n $z_head fragmentation.yaml > start.txt
cat fragmentation_cut_bonds.txt >> start.txt
tail -n $z_tail fragmentation.yaml >> start.txt
cat start.txt > fragmentation.yaml
rm start.txt
rm fragmentation_cut_bonds.txt
}

#-------------------------------------------------------------
# prepare selections in yaml
#-------------------------------------------------------------
sed_selection1() {
  case $3 in
    "turbomole")
      sed -i "$z_sel c\  selection: &sele '%same_residue(%within($2; :$1))|%atomname(HL)'" turbomole.yaml
      sed -i "$z_sel2 c\  geometry: &region 'Results/QM_Region.pdb'" turbomole.yaml
      ;;
    "mopac")
      sed -i "$z_sel c\  selection: &sele '%same_residue(%within($2; :$1))|%atomname(HL)'" mopac.yaml
      sed -i "$z_sel2 c\  geometry: &region 'Results/QM_Region.pdb'" mopac.yaml
      ;;
    "charmm")
      sed -i "$z_sel c\  selection: &sele '%not( :$1)'" charmm.yaml
      sed -i "$z_sel2 c\  geometry: &region 'Results/QM_Region.pdb'" charmm.yaml
      ;;
  esac
}

sed_selection2() {
    case $3 in
      "turbomole")
        sed -i "$z_sel c\  selection: &sele '%not(%same_residue(%within($2; :$1)))'" turbomole.yaml
        ;;
      "mopac")
        sed -i "$z_sel c\  selection: &sele '%not(%same_residue(%within($2; :$1)))'" mopac.yaml
        ;;
      "charmm")
        sed -i "$z_sel c\  selection: &sele '%not( :$1)'" charmm.yaml
        ;;
    esac
}

sed_selection3() {
    case $4 in
      "turbomole")
        sed -i "$z_sel c\  selection: &sele '%same_residue(%within($3; :$1)) & %not(%same_residue(%within($2; :$1)))|%atomname(HL) '" turbomole.yaml
        sed -i "$z_sel2 c\  geometry: &region 'Results/SE_Region.pdb'" turbomole.yaml
        ;;
      "mopac")
        sed -i "$z_sel c\  selection: &sele '%same_residue(%within($3; :$1)) & %not(%same_residue(%within($2; :$1)))|%atomname(HL) '" mopac.yaml
        sed -i "$z_sel2 c\  geometry: &region 'Results/SE_Region.pdb'" mopac.yaml
        ;;
      "charmm")
        sed -i "$z_sel c\  selection: &sele '%same_residue(%within($3; :$1)) & %not(%same_residue(%within($2; :$1))) '" charmm.yaml
        sed -i "$z_sel2 c\  geometry: &region 'Results/SE_Region.pdb'" charmm.yaml
        ;;
    esac
}

sed_region_frag() {
sed -i "$z_head c\qmmm_qmregion_file: "Results/$1"" fragmentation.yaml
}

prepare_selection() {

#prepare_selection ${angstrom2[$i]} ${shell2[$i]} ${shell3[$i]} ${ligand[$i]} ${angstrom1[$i]} ${shell1[$i]} ${pdb[$i]} 
#                      1                2             3              4                 5            6            7
    
    if [[ $1 == "0" ]] && [[ $2 == "0" ]]
    then
	
        # Fragmentation only once
	run_pymol $5 $1 $7 $4
        prepare_fragmentation
        sed_region_frag "QM_Region.pdb"
        sed -i "$z_frag_sel c\qmmm_core: '%same_residue(%within($5; :$4))'" fragmentation.yaml
        
        if [[ $3 == "0" ]]
        then
            #--------case 3A, Mopac, 0, 0, 0,--------------------
            sed_selection1 $4 $5 $6
        else
            #case-------- 3A, Mopac, 0, 0, Charmm,--------
            sed_selection1 $4 $5 $6
            sed_selection2 $4 $5 $3
        fi
    else
    	# Fragmentation two times
    	run_pymol $5 "0" $7 $4    #Angstrom 1
        prepare_fragmentation
        sed_region_frag "QM_Region.pdb" 
        sed -i "$z_frag_sel c\qmmm_core: '%same_residue(%within($5; :$4))'" fragmentation.yaml
        
        # Fragmentation two times
    	run_pymol $1 "0" $7 $4    #Angstrom 2
        prepare_fragmentation
        sed_region_frag "SE_Region.pdb" 
        sed -i "$z_frag_sel c\qmmm_core: '%same_residue(%within($1; :$4))'" fragmentation.yaml
    
        if [[ $3 == "0" ]]
        then
            #case --------3A, Turbomole, 8A, Mopac, 0,--------
            sed_selection1 $4 $5 $6
            sed_selection3 $4 $5 $1 $2
        else
            #case-------- 3A, Turbomole, 8A, Mopac, Charmm,--------
            sed_selection1 $4 $5 $6
            sed_selection3 $4 $5 $1 $2
            sed_selection2 $4 $1 $3
        fi
    fi

}
#-------------------------------------------------------------
# rename folder for the results with date and time
#-------------------------------------------------------------
rename_folder() {
getDateTime=$(date "+%d%m%y_%H%M")
mv -v Results $1_$getDateTime
}
#-------------------------------------------------------------
# print infos
#-------------------------------------------------------------
print_infos() {

  echo " ____________________________________________________________"
  echo "|"
  echo "| the $1. calculation starts for the following values "
  echo "| File:" $2" - "$3
  echo "| Shells:" $4" - "$5"A - "$6" - "$7" - "$8
  echo "|____________________________________________________________"

}
#-------------------------------------------------------------
# move restart_file
#-------------------------------------------------------------
move_files() {
mv auto_restart.xyz Results
}
#============================================================================================

#============================================================================================
# Zeilenangabe für die Bearbeitung der YAML Datei
z_geo=40      #geometry in mopac charmm turbomole
z_sel=41      #selection in mopac charmm turbomole
z_sel2=42      #selection in mopac charmm turbomole
z_frag_geo=7  #geometry in fragmentation
z_frag_sel=8  #selection in fragmentation
z_head=12     #head to copy in fragmentation
z_tail=1      #tail to copy in fragmentation


#-------------------------------------------------------------
# call functions
#-------------------------------------------------------------
for ((i=0;i<$count;++i));
do 
    qm=0
#|0| - check files
    check_files
    
#|1| - create infos
    create_infos ${pdb[$i]} ${ligand[$i]} ${shell1[$i]} ${angstrom1[$i]} ${shell2[$i]} ${angstrom2[$i]} ${shell3[$i]}
    
#|2| - print input parameters
    print_infos $i ${pdb[$i]} ${ligand[$i]} ${shell1[$i]} ${angstrom1[$i]} ${shell2[$i]} ${angstrom2[$i]} ${shell3[$i]}

#|4| - prepare selections for calculation
    prepare_selection ${angstrom2[$i]} ${shell2[$i]} ${shell3[$i]} ${ligand[$i]} ${angstrom1[$i]} ${shell1[$i]} ${pdb[$i]} 
    prepare_geometry ${pdb[$i]}
    cuby4 fragmentation.yaml

#|6| - starts the calculations with Cuby


      case ${shell3[$i]} in        # run MM Region (Charmm) 
	0)
	  ;;
	*)
	  cuby4 "${shell3[$i]}".yaml
	  ;;
      esac
      
      case ${shell1[$i]} in        # run QM Region (Mopac/Turbomole)
	0)
	  ;;
	*)
	  cuby4 "${shell1[$i]}".yaml
	  ;;
      esac
      
       
      case ${shell2[$i]} in        # run SE-Region (Mopac)
	0)
	  ;;
	*)
	  cuby4 "${shell2[$i]}".yaml
	 ;;
      esac

#|8| - rename the folder with the Results
    move_files
    rename_folder $i
    

done



#============================================================================================

#============================================================================================
