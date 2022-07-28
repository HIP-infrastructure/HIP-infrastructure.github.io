COGEPISTIM database (U/C)
***************************

Description
===========

This dataset includes SEEG recordings and imaging data of 242 (28/07/2022) patients retrospectively collected from different research protocols:
	
	* F-TRACT: `The Functional Brain Tractography Project <https://f-tract.eu/>`_.
	* ISD SEEG: `Evaluation of the Risk of Cognitive Deficit After Surgery of Epilepsy by Dynamic Spectral Imaging (ISD) of the Cognitive Functions in Patients Explored in StereoElectroEncephaloGraphy <https://clinicaltrials.gov/ct2/show/NCT03094312>`_. 
	* EPISTIM: `Epileptogenic Zone's Cartography by Quantification of EEG's Signal and Intracerebral Stimulation <https://clinicaltrials.gov/ct2/show/NCT02844374>`_.
	* MAPCOG-SEEG: `Atlas of Human Cognition by SEEG <https://clinicaltrials.gov/ct2/show/NCT03644732>`_.

It contains imaging (T1, T2, FLAIR, CT) and SEEG data (baseline, seizure, stimulation, cognition) with associated electrode coordinates.

SEEG data breakdown is as follows:

	* 171 subjects with cognition data.
	* 176 subjects with stimulation data.
	* 105 subjects with both cognition and stimulation data.
	* 75 subjects with seizure data.
	* 54 subjects with baseline data.
	* 34 subjects with cognition, stimulation, seizure and baseline data.

All subjects have post-implantation imaging data (usually a T1 or CT) and may have pre-implantation imaging data.
Data were imported and pseudonymized using :doc:`BIDS Manager </applications/APP_BIDS_Manager>`.
Imaging data was defaced using SPM defacing feature (`www.fil.ion.ucl.ac.uk/spm/software/spm12 <https://www.fil.ion.ucl.ac.uk/spm/software/spm12/>`_).


Data files
----------

The COGEPISTIM dataset has been generated using :doc:`BIDS Manager </applications/APP_BIDS_Manager>` and follows BIDS guidelines.

The file and directory tree is as follows:

::

	root/
	.. dataset_description.json
	.. participants.tsv
	.. sourcedata/
	.. derivatives/
	.. code/
	.. sub-<cogepistim_id>/
	.... ses-<clinical_course>/
	...... sub-<cogepistim_id>_ses-<clinical_course>_scans.tsv
	...... ieeg/
	........ sub-<cogepistim_id>_ses-<clinical_course>_task-<ieeg_task>_run-<run>_ieeg.vhdr
	........ sub-<cogepistim_id>_ses-<clinical_course>_task-<ieeg_task>_run-<run>_ieeg.vmrk
	........ sub-<cogepistim_id>_ses-<clinical_course>_task-<ieeg_task>_run-<run>_ieeg.eeg
	........ sub-<cogepistim_id>_ses-<clinical_course>_task-<ieeg_task>_run-<run>_ieeg.json
	........ sub-<cogepistim_id>_ses-<clinical_course>_task-<ieeg_task>_run-<run>_events.tsv
	........ sub-<cogepistim_id>_ses-<clinical_course>_task-<ieeg_task>_run-<run>_channels.tsv
	........ sub-<cogepistim_id>_ses-<clinical_course>_space-<ieeg_space>_coordsystem.json
	........ sub-<cogepistim_id>_ses-<clinical_course>_space-<ieeg_space>_electrodes.tsv
	...... anat/
	........ sub-<cogepistim_id>_ses-<clinical_course>_run-<run>_T1w.nii
	........ sub-<cogepistim_id>_ses-<clinical_course>_ce-<anat_ce>_run-<run>_T1w.nii
	........ sub-<cogepistim_id>_ses-<clinical_course>_run-<run>_T2w.nii
	........ sub-<cogepistim_id>_ses-<clinical_course>_run-<run>_CT.nii
	........ sub-<cogepistim_id>_ses-<clinical_course>_run-<run>_FLAIR.nii


Complementary information on file formats and file-internal data structures:

	* Tab-Separted Value format (tsv): labels in first row; data of same type in columns
	* JavaScript Object Notation (json): 1D (non-nested) key-value pairs
	* Neuroimaging Informatics Technology Initiative (nii): native space, unprocessed data
	* Brain Vision (vhdr, vmrk, eeg): unprocessed SEEG data

Directory description:

	* /sub-<cogepistim_id> → BIDS subject entity. Subject directory.
	* /ses-<clinical_course> → BIDS session entity. Session directory.
	* /sourcedata → BIDS sourcedata folder. Contains raw/source data. Follows BIDS folder structure.
	* /derivatives → BIDS derivatives folder. Processing pipeline and software outputs. Follows BIDS folder structure.
	* /code → BIDS code folder. Source code of scripts used to prepare and/or process the data .

File description:

	* dataset_description.json → short description of the dataset.
	* participants.tsv → subjects clinical/demographic data.
	* \*._scans.tsv → subject/session file listing with acquisition time.
	* \*._ieeg.vhdr → Brain Vision. text file. header.
	* \*._ieeg.vmrk → Brain Vision. text file. events.
	* \*._ieeg.eeg → Brain Vision. binary file. voltage values.
	* \*._ieeg.json → BIDS acquisition infos. e.g. task, stimulation parameters, recording mode.
	* \*._events.tsv → BIDS event infos. e.g. onset, duration, type.
	* \*._channels.tsv → BIDS channel infos. e.g. name, type, sampling frequency.
	* \*._coordsystem.json → BIDS (i)EEG specific. Gives coordinate systems.
	* \*._electrodes.tsv → BIDS (i)EEG specific. Gives location of EEG electrodes.
	* \*._T1w.nii → T1 weighted MRI.
	* \*._T2w.nii → T2 weighted MRI.
	* \*._CT.nii → Computerized Tomography.
	* \*._FLAIR.nii → FLAIR MRI.

BIDS pairs:

	* <cogepistim_id> → COGEPISTIM unique identifier. CES<center>[1|2][0-9]{3}. e.g. CES1003, CES2097.
	* <clinical_course> → preimp (before implantation), postimp (after implantation), postop (after surgery).
	* <ieeg_task> → stimulation, baseline, seizure, locaVisu, locaLec1, locaLec2, locaMvis, locaMveb, locaAudi, locaCsc, locaMcse, locaRest1, locaRest2, locaRest3, locaMoto, locaArfa, locaJumpy, locaStab, locaMlah.
	* <anat_ce> → gadolinium.
	* <run> → Repetition number of an acquisition. e.g. 01, 02, 03…
	
Electrode description
---------------------

Clinical information
--------------------

Clinical information is limited to sex, handedness, age group and epilepsy location. 
*Sex* can be found in the *participants.tsv* file in BIDS *raw* directory.
Subjects underwent one or several implantations which correspond to BIDS *sessions*.
Handedness, age group and epilepsy location can be found in the *<subject>_sessions.tsv* file which reside in each subject's folder. 

Sex:

	* **F**: Female.
	* **M**: Male.
		
Handedness:

	* **R**: Right hand.
	* **L**: Left hand.
	* **A**: Ambidextrous.
	* **U**: Unspecified.
	
Age group:

	* **Infant**: Between 1 and 4 years old.
	* **Juvenile**: Between 5 and 16 years old.
	* **Young adult**: Between 17 and 25 years old.
	* **Adult**: 26 years old and more.
	
Epilepsy location (can be a combination, e.g. temporal left, frontal left):

	* **Temporal**: Temporal lobe.
	* **Frontal**: Frontal lobe.
	* **Parietal**: Parietal lobe.
	* **Occipital**: Occipital lobe.
	* **Central**: Paracentral lobule.
	* **Insular**: Insular lobe.
	* **Multifocal**: Multifocal epileptic activity.
	* **Indeterminate**: Indeterminate / Unspecified.
	* **Left**: Left hemisphere.
	* **Right**: Right hemisphere.
	* **Bilateral**: Left and right hemisphere.

License
=======

References
==========