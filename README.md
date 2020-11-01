# EEG_State_Discrimination
Using Machine Learning to help Discriminate Between EEG States

Aim:
There is no simple open source tool for EEG devices (for citizen science or other metric-tracking purposes) that easily parses out EEG metrics as physiological markers between	 
phenomenologically distinct mental states in the EEG.	This tool will extract a set of EEG metrics (i.e. the columns/features) from the raw data, and subsequently the tool allows one to run machine learning over these features.

EEG Data in this repository:
This particular dataset evaluation serves as a “control” to future projects in that this dataset is simulating a random (or at least, close to random) allocation of condition to the samples of the dataset. In other words this evaluation is using a dataset containing only one state that has been partitioned into the first and second half labeled as state 1 and state 2 respectively. The goal is to assess whether two states that are intended to not be different from one another, are actually found to not be different through the test of machine learning algorithms. While a lack of predictability is expected since the condition of recording is no different in the first half than the second half, it is important to do such an evaluation to ensure that later evaluations do not run into confounds which might make the second half different from the first. 



Directions for use:
-	Download package of MNE Python: https://mne.tools/stable/install/index.html
-	Download Entropy package: https://raphaelvallat.com/entropy/build/html/index.html
-	Go to barlehmann’s github repository: https://github.com/barlehmann/EEG_State_Discrimination
-	On MASTER (NOT MAIN) branch open complete_project_code  (the other two files include the same as the complete project code just in separate files)
-	Download this file as well as the dataset named ‘eeg_dataEC.edf’ and open on Jupyter Labs
-	Put in correct address to file on your hard drive for the preprocess_raw following the “raw=”. Use ‘Control + F’ to search for this line and input the correct address – use the function ‘a’ at the end of the first full box of code containing the preprocess_raw to put this in. 
-	Use ‘Control + F’ to search for r"C:\Users\barle\Downloads/combined_df2.csv and set the address for the new CSV file to be put into on your computer
-	Run function ‘a’ containing this information
-	first correct the csv “combined_df2.csv” created from the first part to be with the correct address on your computer in the machine learning (block two) of this code
-	Then use the sample commented code below in the machine learning block of code below or write your own code to use these classes/methods related to machine learning


