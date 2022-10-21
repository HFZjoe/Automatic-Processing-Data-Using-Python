def browseFile(fileType):
    selectedFile = filedialog.askopenfilename(title = "Select {}".format(fileType), filetypes = (("xlsx","*.xlsx*"),("All Files","*.*")))
    if selectedFile != "":
        if fileType == "A":
            global fileA
            fileA = os.path.abspath(selectedFile)
            basename = ntpath.basename(fileA)
            fileALabel.config(text = basename)
        elif fileType == "B":
            global fileB
            fileB = os.path.abspath(selectedFile)
            basename = ntpath.basename(fileB)
            fileBLabel.config(text = basename)
        elif fileType == "C":
            global fileC
            fileC = os.path.abspath(selectedFile)
            basename = ntpath.basename(fileC)
            fileCLabel.config(text = basename)


def Folder_Directory():
   Folder = filedialog.askdirectory(parent=mainRoot,initialdir="/",title='Please select a directory')
   FolderPath = os.path.abspath(Folder)
   FolderLabel.config(text = FolderPath)


def mainProcess():
    
    df1 = pd.read_excel(fileA)  # FILE TRANSAKSI BULANAN
    df2 = pd.read_excel(fileB)  # FILE ADMIN TRANSAKSI
    df3 = pd.read_excel(fileC)  # FILE AKHIR / INPUT

# MENDAPAT NILAI PROPOSE

    df1.rename(columns={'agent_id':'AGENT_ID'}, inplace=True)
    df1.rename(columns={'description':'Nama Produk'}, inplace=True)


    df1['Nama Produk']=df1['Nama Produk'].str.lower()
    df2['Nama Produk']=df2['Nama Produk'].str.lower()
    df4 = pd.merge(df1, df2[['Nama Produk', 'Nilai Propose']], on='Nama Produk', how='left')


    # MENGUBAH MENJADI FIX INPUT AGENT

    df4 = df4.groupby(by="AGENT_ID").sum()[["Nilai Propose"]]
    df4["Korgen_40%"] = (df4["Nilai Propose"]) * 0.4
    df4["Agent_60%"] = (df4["Nilai Propose"]) * 0.6
    df4["Korlap_10%"] = (df4["Agent_60%"]) * 0.1
    df4["Agent_Recieved"] = (df4["Agent_60%"]) - (df4["Korlap_10%"])
    df4["Fix_Input_Agent"] = np.floor(df4["Agent_Recieved"])
    df4.reset_index(inplace=True)

    # MENGINPUT KE FILE INPUT 

    df5 = pd.merge(df3, df4[['AGENT_ID','Fix_Input_Agent']], on='AGENT_ID', how='left')
    df6 = df5['Fix_Input_Agent'].fillna(value = 0)

    df3["TRANSFER_VALUE"] = df6

    NamaFile1 = alterName1.get()  
    NamaFile2 = alterName2.get()  

    if NamaFile1 == '' or NamaFile2 == '':
        m_box.showerror('Caution', 'Nama File Tidak Boleh Kosong')

        return False

    NamaFolder = FolderLabel.cget("text")

    if NamaFolder == 'No folder Selected':
        m_box.showerror('Caution', 'Pilih Folder terlebih dahulu')

        return False

    df4.to_excel(f"{NamaFolder}\{NamaFile1}.xlsx", index=False)
    df3.to_excel(f"{NamaFolder}\{NamaFile2}.xlsx", index=False)
    m_box.showinfo('File Export','Sukses Membuat File')
