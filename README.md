# EEG_State_Discrimination
Using Machine Learning to help Discriminate Between EEG States

Aim:
There is no simple open source tool for EEG devices (for citizen science or other metric-tracking purposes) that easily allowed one to make use of the vast array of EEG metrics and correlate these with phenomenologically distinct mental states recorded in the EEG. This tool extracts a set of EEG metrics (i.e. the columns/features) from the raw data, and subsequently the tool allows one to run basic machine learning over these features to find which ones are most sensitive to the particular type of change from baseline which occurs in the given state. 

EEG Data in this repository:
This particular dataset (named "eeg_data_EC") evaluation serves as a “control” to future projects in that this dataset is simulating a random (or at least, close to random) allocation of condition to the samples of the dataset. In other words this evaluation is using a dataset containing only one state that has been partitioned into the first and second half labeled as state 1 and state 2 respectively. The goal is to assess whether two states that are intended to not be different from one another, are actually found to not be different through the test of machine learning algorithms. While a lack of predictability is expected since the condition of recording is no different in the first half than the second half, it is important to do such an evaluation to ensure that later evaluations do not run into confounds which might make the second half different from the first. 

The Brainhack project will expand this tool for the aims of evaluating some new resting state EEG datasets tagged in regards to subjective sense of mental arousal/awakeness to evaluate the relevance of metrics for evaluating arousal (and other mental states i.e. types of meditation) more directly. It will do this in a few ways. (1) creating the code to compare one full recording with another full recording in regard to specific EEG metrics. This is different from the present setup of the work which only compares part one to part two of the single dataset. (2) Finding a way to incorporate metrics of cross frequency coupling to this tool. Cross frequency coupling (CFC) seems to be a key aspect of how brain function works, it also seems to be a key aspect of how advanced meditators change their states. Integrating cross frequency coupling will be the next step in this work.To learn more about CFC and its relevance to meditation, as well as find documentation of its implementation in matlab see: https://www.researchgate.net/profile/Julio-Rodriguez-Larios/publication/351812052_ON_THE_RHYTHMS_OF_THOUGHT_EEG_alpha-theta_cross-frequency_dynamics_during_arithmetic_performance_mind_wandering_and_meditative_states/links/60ab63a045851522bc10de58/ON-THE-RHYTHMS-OF-THOUGHT-EEG-alpha-theta-cross-frequency-dynamics-during-arithmetic-performance-mind-wandering-and-meditative-states.pdf#page=83
The MNE Matlab Toolbox allows access of the Matlab functions through MNE: https://mne.tools/stable/overview/matlab.html#mne-matlab



Directions for use of basic package pre-brainHack project:
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


# Install Requirements

```
mamba create -n eeg_state conda-forge::mne jupyter pip ipython scikit-learn pandas conda-forge::jupyterlab
# if mamba is not installed:  conda create -n eeg_state conda-forge::mne jupyter pip ipython scikit-learn pandas conda-forge::jupyterlab
```

# Download this code
```
git clone https://github.com/barlehmann/EEG_State_Discrimination
```

# Additional Data for training
10 sets of EEG - 2.5 mins of eyes open rest and 2.5 mins of eyes closed
Can be used as a baseline for state based analysis datasets provided in this brainhack
```
cd EEG_State_Discrimination
git clone https://github.com/mastaneht/SPIS-Resting-State-Dataset extra_data
```

# Running 
```
conda activate eeg_state
jupyter lab code/complete_project_code.ipynb
```
