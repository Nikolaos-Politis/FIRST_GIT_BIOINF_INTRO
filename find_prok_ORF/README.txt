This program was created under the following instruction:

""Γράψτε ένα πρόγραμμα (σε όποια γλώσσα
προγραμματισμού θέλετε) το οποίο θα διαβάζει από
την καθιερωμένη είσοδο νουκλεοτιδικές αλληλουχίες,
και θα τις εξετάζει μία-προς-μία για το εάν
περιέχουν ή όχι μία τυπική/απλή προκαρυωτική
κωδικοποιούσα αλληλουχία (με κωδικόνιο έναρξης,
στο τέλος της κωδικοποιούσας περιοχής ένα από τα
κωδικονια λήξης, και χωρίς άλλα κωδικόνια λήξης
στο ενδιάμεσο τμήμα).""

the programming language used is python 3 and it runs though terminal with following command:
python3 FIND_ORF.py 

the while TRUE loop brakes after pressing ENTER without tapping any nucleotide sequence 
an example of the codes output is this:

enter sequence:
ATGGCCGGCGGCTAG
enter sequence:

characters upper, compatible for checking
ATGGCCGGCGGCTAG
sequence is valid passing for ORF finding processing
found start codon for x equal to 0
found stop codon
found ORF at:
                                          sequence: ATGGCCGGCGGCTAG
                                          start_codon index: 0
                                          stop_codon index: 12
the check is:
vallidation of the characters "ATGC".
if they are only ATGC then the program continues further prosses for finding the ORF.

IMPORTANT(1)!!:
The program will find ORF only if the distance between the start and the end codon is at least 6 nucleotides. Otherwise it will not recognise a single amino acid codon as an ORF. 

IMPORTANT(2)!!:
The program will print the places of start codon or end codon even if no ORF exists, BUT in case the ORF dont exist and there is start and end codon then the program will not print ORFs existance or ORFs size. 

IMPORTANT(3)!!:
the enumeration is printed from 0 index.  

I also give some example sequences the user can put to check the program:
ATGGCCGGCGGCTAG     :Standard ORF: Correct start (ATG), correct end (TAG), and valid length.
atggccggcggctag     :Case Sensitivity: Tests if .upper() function handles lowercase input.
AATGGCCGGCGGCTAG    :Frame 1: Tests if the program finds the ORF starting at the 2nd position.
AAATGGCCGGCGGCTAG   :Frame 2: Tests if the program finds the ORF starting at the 3rd position.
ATGTAG              :Length Boundary: Tests if the j-i >= 9 logic correctly skips ORFs that are too short.
ATGGCCGGG           :Missing Stop: Tests if the code correctly ignores sequences that never end in a stop codon.
GGCGGCTAG           :Missing Start: Tests if the code correctly ignores sequences that have a stop but no ATG.
ATGCcxGGT12         :Invalid Characters: Tests if filter catches non-ATGC characters (x, 1, 2).
ATGCCCTAAAGGTGA     :Internal Stop: Tests the requirement: "no other stop codons in the middle.
ATGAAAAAATGA        :Minimal Valid: The shortest possible sequence that should pass 9 length check.


