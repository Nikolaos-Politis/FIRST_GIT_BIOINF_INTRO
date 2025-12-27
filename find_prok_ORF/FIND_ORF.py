class findorf:
    def __init__(self):
        self.seq = []
        self.start_codon = 'ATG'
        self.stop_codon0 = 'TAG'
        self.stop_codon1 = 'TAA'
        self.stop_codon2 = 'TGA'


    def insert_sequences(self):
        while True:
            print("enter sequence:")
            line = input()
            if line == "":      
                break
            self.seq.append(line)
    
    def filtering_sequences(self):
        self.insert_sequences()
        vallidated = []
        for i in self.seq:
            i = i.upper()
            print("characters upper, compatible for checking")
            valid = True   

            for char in i:
                if char not in "ATGC":
                    valid = False
                    break   

            if valid:
                vallidated.append(i)
                print(i)
                print("sequence is valid passing for ORF finding prossesing")
            else:
                print(i)
                print("sequence is NOT valid, data mast be revisited")

        self.seq = vallidated
        return self.seq
    
    def find_orf(self):
        self.seq = self.filtering_sequences()
        for x in range(0,3):
            for sequence in self.seq:
                found_ATG = False
                for i in range(x, len(sequence)-2, 3):
                    cod = sequence[i : i + 3]
                    if cod == self.start_codon:
                        print(f"found start codon for x equal to {x}")
                        found_ATG = True
                        for j in range(i+3, len(sequence)-2, 3):
                            cod = sequence[j : j + 3]
                            if found_ATG and (cod == self.stop_codon0 or cod == self.stop_codon1 or  cod == self.stop_codon2):
                                print("found stop codon")
                                if (j-i) >= 9:
                                    print(f"""found ORF at:
                                          sequence: {sequence}
                                          start_codon index: {i}
                                          stop_codon index: {j}""")
                                found_ATG = False
                                break


            
if __name__ == "__main__":
    finder = findorf()
    finder.find_orf()

            

    