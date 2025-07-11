.. # hard line break for HTML
.. |br| raw:: html

   <br />
   
.. comment:
   tables made with https://tableconvert.com/restructuredtext-generator

.. warning::

    The COGEPISTIM dataset is available in a `dedicated Collaborative Space <https://thehip.app/apps/hip/projects/HIP-COGEPISTIM>`_ with restricted access.

COGEPISTIM dataset
------------------

Overview
::::::::

The COGEPISTIM dataset reuses SEEG, imaging and clinical data from 241 (29/08/2023) subjects initially collected through 4 studies:

	* F-TRACT: `The Functional Brain Tractography Project <https://f-tract.eu/>`_.
	* ISD SEEG: `Evaluation of the Risk of Cognitive Deficit After Surgery of Epilepsy by Dynamic Spectral Imaging (ISD) of the Cognitive Functions in Patients Explored in StereoElectroEncephaloGraphy <https://clinicaltrials.gov/ct2/show/NCT03094312>`_. 
	* EPISTIM: `Epileptogenic Zone's Cartography by Quantification of EEG's Signal and Intracerebral Stimulation <https://clinicaltrials.gov/ct2/show/NCT02844374>`_.
	* MAPCOG-SEEG: `Atlas of Human Cognition by SEEG <https://clinicaltrials.gov/ct2/show/NCT03644732>`_.
	
The dataset ensures privacy through pseudonymization and adheres to the BIDS standard. It encompasses defaced imaging data (T1, T2, CT, FLAIR) and de-identified SEEG recordings
(baselines, seizures, electrical stimulations, localizers) accompanied by corresponding electrode coordinates. The SEEG data for baselines, seizures, and stimulations originate from the F-TRACT project,
while localizers are derived from the ISD SEEG, EPISTIM, and MAPCOG-SEEG clinical trials. Additionally, the dataset provides a limited set of clinical details like age categories and epileptogenic zones for each subject.

Data inventory
::::::::::::::

The complete and up-to-date data inventory can be found inside the dedicated *data_inventory.tsv* file, which is located in the */derivatives/inventory* folder of the COGEPISTIM dataset (see :ref:`Fig.1 <coge_structure>`).
This file lists all data available for each subject and is generated whenever the database is updated.

SEEG data summary (30/08/2023):

	* 167 subjects have localizer data.
	* 200 subjects have electrical stimulation data.
	* 75 subjects have seizure data.
	* 58 subjects have baseline data.
	* 34 subjects have localizer, electrical stimulation, seizure and baseline data.

Imaging data summary (30/08/2023):

	* 239 subjects have pre-implantation imaging data.
	* 237 subjects have post-implantation imaging data.
	* 84 subjects have post-operative imaging data.
	* 235 subjects have pre-implantation and post-implantation imaging data.
	* 81 subjects have pre-implantation, post-implantation, and post-operative imaging data.

Subjects typically possess at least one variety of SEEG data alongside the related electrode coordinates and the corresponding post-implantation volume,
either in the form of an MRI or a CT scan. Clinical data may be incomplete or missing for several subjects.

Data preparation
::::::::::::::::

The COGEPISTIM dataset has been prepared using `BIDS Manager software <https://github.com/Dynamap/BIDS_Manager>`_ (0.3.4) ([Roehri_2021a]_), a Python package to collect, organise and manage neuroscience data in BIDS format.
The dataset follows `BIDS specifications <https://bids.neuroimaging.io/>`_ (see [Holdgraf_2019]_ for BIDS-iEEG specifications) and has been validated using `BIDS-Validator tool <https://www.npmjs.com/package/bids-validator>`_
(1.12.0) ([Blair_2022]_).
Data have been pseudonymized. Subjects were assigned a unique identifier and personally identifiable information have been removed from the (meta)data of all files that have been imported into the dataset,
this includes events and notes typically found in SEEG data. Imaging data have been defaced using `SPM12's <https://www.fil.ion.ucl.ac.uk/spm/software/spm12/>`_ dedicated
`defacing feature  <https://github.com/neurodebian/spm12/blob/master/spm_deface.m>`_ which strips the face from the volumes.
Clinical information has been kept to a minimum and is limited to the sex, handedness, age category and epileptogenic zone(s) of each subject, when available.

Data structure
::::::::::::::

The COGEPISTIM dataset follows BIDS specifications. The arrangement of files and folders is depicted in :ref:`Fig.1 <coge_structure>`, while the corresponding naming conventions are outlined in :ref:`Tab.1 <coge_naming_convention>`. 
Files and folders are further described in :ref:`Tab.2 <coge_file_desc>` and :ref:`Tab.3 <coge_folder_desc>` respectively. For further insights into data formats, refer to :ref:`Tab.4 <coge_file_format>`.
The COGEPISTIM dataset encompasses longitudinal data, where subjects undergo data acquisitions both prior to and after the implantation of SEEG electrodes,
as well as after their subsequent surgical removal. Moreover, a single subject might have undergone several implantations. To effectively organize this data, the COGEPISTIM dataset employs BIDS session folders as follows:
The */ses-preimpXX*, */ses-postimpXX*, and */ses-postopXX* session folders correspond to data collected before implantation, after implantation, and after surgical electrode removal, respectively.
*XX* denotes a two-digit number that serves as an index for different implantation instances. 

.. _coge_structure:

.. code-block:: text

	/raw
	.. dataset_description.json
	.. participants.tsv
	.. /derivatives
	.... /data_inventory
	...... data_inventory.tsv
	.... /cognition
	...... /sub-<cogepistim_id>
	........ /ses-<session>
	.......... /ieeg
	............ sub-<cogepistim_id>_ses-<session>_task-<ieeg_task>_acq-<ieeg_acq>_run-<run>_ieeg.vhdr
	............ sub-<cogepistim_id>_ses-<session>_task-<ieeg_task>_acq-<ieeg_acq>_run-<run>_ieeg.vmrk
	............ sub-<cogepistim_id>_ses-<session>_task-<ieeg_task>_acq-<ieeg_acq>_run-<run>_ieeg.eeg
	.. /sub-<cogepistim_id>
	.... sub-<cogepistim_id>_sessions.tsv
	.... /ses-<session>
	...... sub-<cogepistim_id>_ses-<session>_scans.tsv
	...... /ieeg
	........ sub-<cogepistim_id>_ses-<session>_task-<ieeg_task>_run-<run>_ieeg.vhdr
	........ sub-<cogepistim_id>_ses-<session>_task-<ieeg_task>_run-<run>_ieeg.vmrk
	........ sub-<cogepistim_id>_ses-<session>_task-<ieeg_task>_run-<run>_ieeg.eeg
	........ sub-<cogepistim_id>_ses-<session>_task-<ieeg_task>_run-<run>_ieeg.json
	........ sub-<cogepistim_id>_ses-<session>_task-<ieeg_task>_run-<run>_events.tsv
	........ sub-<cogepistim_id>_ses-<session>_task-<ieeg_task>_run-<run>_channels.tsv
	........ sub-<cogepistim_id>_ses-<session>_space-<ieeg_space>_coordsystem.json
	........ sub-<cogepistim_id>_ses-<session>_space-<ieeg_space>_electrodes.tsv
	...... /anat
	........ sub-<cogepistim_id>_ses-<session>_run-<run>_T1w.nii
	........ sub-<cogepistim_id>_ses-<session>_ce-<anat_ce>_run-<run>_T1w.nii
	........ sub-<cogepistim_id>_ses-<session>_run-<run>_T2w.nii
	........ sub-<cogepistim_id>_ses-<session>_run-<run>_CT.nii
	........ sub-<cogepistim_id>_ses-<session>_run-<run>_FLAIR.nii

.. raw:: html

   <center>	
	<b>Fig.1</b> <i>File and folder organization.</i>
   </center>
	
|


.. _coge_naming_convention:

.. table::
	:align: center

	+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
	| BIDS value      | Description                                                                                                                                                                                                                                                  | Example                                            |
	+=================+==============================================================================================================================================================================================================================================================+====================================================+
	| <cogepistim_id> | COGEPISTIM unique identifier. CESXXXX where XXXX is a 4-digit number.                                                                                                                                                                                        | CES1003, CES2037                                   |
	+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
	| <session>       | Subject session. preimpXX (before implantation), postimpXX (after implantation), postopXX (postoperative) |br| where XX is a 2-digit number indexing implantations for a given subject.                                                                      | preimp01, postimp01, postop01, preim02, postimp02  |
	+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
	| <ieeg_task>     | SEEG task.                                                                                                                                                                                                                                                   | stimulation, baseline, seizure, VISU, MOTO         |
	+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
	| <ieeg_acq>      | Processing parameters used on localizers. The first two numbers are the low and high cut-off frequencies of the bandpass filter,  |br| the third number is the downsampling factor and the last number is the width of the smoothing window in milliseconds. | f8f24ds8sm500                                      |
	+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
	| <ieeg_space>    | Spatial reference to interpret electrode coordinates.                                                                                                                                                                                                        | MNI152Lin                                          |
	+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
	| <anat_ce>       | Contrast agent.                                                                                                                                                                                                                                              | gadolinium                                         |
	+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
	| <run>           | Repetition number of an identical acquisition                                                                                                                                                                                                                | 01, 02, 03                                         |
	+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+

.. raw:: html

   <center>	
	<b>Tab.1</b> <i>Naming convention.</i>
   </center>
	
|

.. _coge_file_desc:

.. table::
	:align: center

	+--------------------------+-----------------------------------------------------------------------+
	| File                     | Description                                                           |
	+==========================+=======================================================================+
	| dataset_description.json | Short description of the dataset.                                     |
	+--------------------------+-----------------------------------------------------------------------+
	| participants.tsv         | Clinical data for all subjects.                                       |
	+--------------------------+-----------------------------------------------------------------------+
	| data_inventory.tsv       | Table listing the data available for each subject.                    |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_sessions.tsv          | Session-specific clinical data for a given subject.                   |
	+--------------------------+-----------------------------------------------------------------------+
	| \*._scans.tsv            | Session-specific file listing.                                        |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_ieeg.vhdr             | BrainVision text file. Header.                                        |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_ieeg.vmrk             | BrainVision text file. Events.                                        |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_ieeg.eeg              | BrainVision binary file. Voltage values.                              |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_ieeg.json             | Acquisition info. e.g. task, stimulation parameters, recording mode.  |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_events.tsv            | Event info. e.g. onset, duration, type.                               |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_channels.tsv          | Channel info. e.g. name, type, sampling frequency.                    |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_coordsystem.json      | Coordinate system info / spatial reference.                           |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_electrodes.tsv        | (i)EEG electrode location.                                            |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_T1w.nii               | T1 weighted MRI.                                                      |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_T2w.nii               | T2 weighted MRI.                                                      |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_CT.nii                | Computerized Tomography.                                              |
	+--------------------------+-----------------------------------------------------------------------+
	| \*_FLAIR.nii             | FLAIR MRI.                                                            |
	+--------------------------+-----------------------------------------------------------------------+


.. raw:: html

   <center>	
	<b>Tab.2</b> <i>File description.</i>
   </center>
	
|

.. _coge_folder_desc:

.. table::
	:align: center

	+----------------------+--------------------------------------------------------------------------+
	| Folder               | Description                                                              |
	+======================+==========================================================================+
	| /sub-<cogepistim_id> | Subject directory.                                                       |
	+----------------------+--------------------------------------------------------------------------+
	| /ses-<session>       | Session directory.                                                       |
	+----------------------+--------------------------------------------------------------------------+
	| /derivatives         | Derivatives directory. Contains analysis outputs.                        |
	+----------------------+--------------------------------------------------------------------------+
	| /cognition           | Cognition data directory. Processed localizers.                          |
	+----------------------+--------------------------------------------------------------------------+
	| /inventory           | Data inventory directory.                                                |
	+----------------------+--------------------------------------------------------------------------+
	| /anat                | Structural imaging data. Contains T1, T2, CT, FLAIR volumes.             |
	+----------------------+--------------------------------------------------------------------------+
	| /ieeg                | iEEG data. Contains SEEG data with corresponding electrode coordinates.  |
	+----------------------+--------------------------------------------------------------------------+


.. raw:: html

   <center>	
	<b>Tab.3</b> <i>Folder description.</i>
   </center>
	
|

.. _coge_file_format:

.. table::
	:align: center

	+------------------------------------------------+--------------------+-----------------------------------------------------+
	| Format                                         | Extension          | Description                                         |
	+================================================+====================+=====================================================+
	| Tab-Separted Value format                      | .tsv               | Labels in first row. Data of same type in columns.  |
	+------------------------------------------------+--------------------+-----------------------------------------------------+
	| JavaScript Object Notation                     | .json              | 1D (non-nested) key-value pairs.                    |
	+------------------------------------------------+--------------------+-----------------------------------------------------+
	| Neuroimaging Informatics Technology Initiative | .nii               | Defaced imaging data. Native space.                 |
	+------------------------------------------------+--------------------+-----------------------------------------------------+
	| BrainVision data format                        | .vhdr, .vmrk, .eeg | SEEG data.                                          |
	+------------------------------------------------+--------------------+-----------------------------------------------------+


.. raw:: html

   <center>	
	<b>Tab.4</b> <i>Files formats.</i>
   </center>
	
|

Clinical data
:::::::::::::

Clinical data is limited to sex, handedness, age category and epileptogenic zone(s) for each subject. Sex can be found in the *participants.tsv* file, in the */raw* directory. Handedness, age group and epileptogenic zone(s)
are session-specific and can be found in *sub-<cogepistim_id>_sessions.tsv* files, in */sub-<cogepistim_id>* directories (see :ref:`Fig.1 <coge_structure>`). 
The clinical data found in the COGEPISTIM dataset is detailed in :ref:`Tab.5 <coge_clinical>`.

.. _coge_clinical:

.. table::
	:align: center

	+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Clinical data         | Description                                                                                                                          | Key        | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
	+=======================+======================================================================================================================================+============+=======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
	| Sex                   | Biological sex.                                                                                                                      | sex        | F (female), M (male), U (unspecified)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
	+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Handedness            | Dominant hand.                                                                                                                       | handedness | R (right), L (left), A (ambidextrous), U (unspecified)                                                                                                                                                                                                                                                                                                                                                                                                                                |
	+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Age category          | Age classified according to arbitrary categories.                                                                                    | age        | Infant (Between 1 and 4 years old), Juvenile (Between 5 and 16 years old), |br| Young adult (Between 17 and 25 years old), Adult (26 years old and more)                                                                                                                                                                                                                                                                                                                              |
	+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Epileptogenic zone(s) | Cortical area necessary for the generation |br| of clinical epileptic seizures. |br| Entry is a combination of anatomical landmarks. | epilepsy   | Temporal (temporal lobe), Frontal (frontal lobe), Parietal (parietal lobe), |br| Occipital (occipital lobe), Central (paracentral lobule), Paracentral (paracentral lobule), |br| Insular (insular lobe), Cingular (cingulate cortex), Multifocal (multifocal epileptic activity), |br| Polar (temporal pole), Hippocampus (hippocampus), Indeterminate (indeterminate or unspecified), |br| Left (left hemisphere), Right (right hemisphere), Bilateral (left and right hemispheres) |
	+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. raw:: html

   <center>	
	<b>Tab.5</b> <i>Clinical data.</i>
   </center>
	
|

Electrode coordinates
:::::::::::::::::::::

SEEG electrode coordinates and associated metadata can be found in dedicated *\*_electrodes.tsv* and *\*_coordsystem.json* files respectively. Those files are only found in the post-implantation session folder 
of a given subject (see :ref:`Fig.1 <coge_structure>`). Coordinates are specified in both native and MNI152 spaces (ICBM Average Brain, 152 T1-weighted MRI scans) ([Evans_2001]_, [Mazziotta_2001]_).

SEEG data gathered from the F-TRACT project also have anatomical parcels extracted from a set of atlases assigned to each contact (see [Trebaul_2018]_) (e.g. MarsAtlas, Freesurfer, AAL, Broadman, Hammers, HCP_MMP1, AICHA, Lausanne2008).

SEEG and imaging data
:::::::::::::::::::::

F-TRACT data
............

Baseline, seizure, stimulation SEEG data and associated imaging data come from the F-TRACT project and were initially collected following the ethical procedures for conducting international multicenter post-processing
of clinical data defined by the International Review Board at `INSERM <https://www.inserm.fr/en/home/>`_.

The F-TRACT project contains structural (imaging) and functional (neurophysiological) SEEG data from adult epileptic patients who were candidates to resective surgery and undergone intracortical stimulations.
The data were collected from a multicenter patient population. Methods and materials for recording the data differed between epilepsy surgery units, and followed strict clinical procedures as defined in every hospital.
The recording procedures were not standardized in research perspective which sole objective was data-reuse.
For each patient, at least one anatomical MRI (T1 contrast if available, sometimes associated to a T2 and/or FLAIR contrast) and an image with SEEG electrodes (T1 MRI or CT scan and accessory implantation scheme)
were obtained in order to localise SEEG electrodes. The average number of recording bipolar contacts per patient was about 150.
Baselines, seizures and low-frequency stimulations were recorded as part of a pre-surgical evaluation of drug-resistant epilepsy. Only stimulations performed at low frequency (<5 Hz) for a limited amount of time
per stimulated area (typically less than 40 pulses) were considered. Bipolar stimuli were delivered using a constant current rectangular pulse generator designed for a safe diagnostic stimulation of the human brain,
according to parameters proved to produce no structural damage. All stimulations were performed between two contiguous contacts in the grey matter, and sometimes in the white matter, using monophasic or biphasic pulses.
Pulse width and intensity of stimulation could vary (typically 1 ms duration pulses at 3 mA). The clinical goals of the stimulations were the reproduction of the aura, the induction of an electroclinical seizure,
and/or the localisation of an eloquent cortical area that has to be spared during surgery. Signals were acquired at a sampling frequency which varied between 512 Hz and 2048 Hz.

See [Trebaul_2018]_ for additional scientific details regarding the necessary procedures to generate the F-TRACT database.

ISD SEEG, EPISTIM and MAPCOG-SEEG data
......................................

Cognition SEEG data and associated imaging data come from 3 clinical trials:

	* ISD SEEG: `Evaluation of the Risk of Cognitive Deficit After Surgery of Epilepsy by Dynamic Spectral Imaging (ISD) of the Cognitive Functions in Patients Explored in StereoElectroEncephaloGraphy <https://clinicaltrials.gov/ct2/show/NCT03094312>`_. 
	* EPISTIM: `Epileptogenic Zone's Cartography by Quantification of EEG's Signal and Intracerebral Stimulation <https://clinicaltrials.gov/ct2/show/NCT02844374>`_.
	* MAPCOG-SEEG: `Atlas of Human Cognition by SEEG <https://clinicaltrials.gov/ct2/show/NCT03644732>`_.
	
These clinical trials encompass brain cognition recordings conducted as part of the standard clinical practice for patients experiencing focal drug-resistant epilepsy and who are explored using intracranial electrodes.
During their pre-surgical SEEG assessment, each patient went through a series of short cognitive tests, also known as localizers (:ref:`Tab.6 <coge_localizers>`), lasting about ten minutes each, and designed to generate task-specific,
and stimulus-specific high-frequency activity in several major functional systems, including language processing (LEC1 and LEC2), verbal and visuo-spatial working memory (MVEB and MVIS), visual attention (VISU),
motor behavior (MOTO), high-level visual (MCSE) and auditory perception (AUDI). Furthermore, patients were also recorded during resting state (REST) and during a series of tests designed to evaluate whether specific
types of actions can generate artefacts (ARFA).

Additional information regarding the aforementioned tasks and the corresponding SEEG data acquisitions can be found in [Vidal_2011]_, [Vidal_2012]_ and [Ossandón_2012]_.

.. _coge_localizers:

.. table::
	:align: center

	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Name | Type                                   | Description                                                                                                                                                | Instructions                                                                                                                                                                                                                                          |
	+======+========================================+============================================================================================================================================================+=======================================================================================================================================================================================================================================================+
	| ARFA | Resting State Paradigm                 | Subject does series of tests designed to evaluate whether specific types of actions can generate artefacts.                                                | Subjects had to make different types of movements known to occasionally elicit noise in SEEG signals.                                                                                                                                                 |
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| AUDI | Auditory Perception Task               | Subject listens to sounds of different types (voice, city noise, animals), |br| lasting 12 seconds, with a break of 3 seconds between each sound.          | At the end of the experiment, subjects will listen to sounds and tell if they heard them before.                                                                                                                                                      |
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| LEC1 | Word Recognition task                  | Subject reads strings of 5 characters. There are 3 types of strings: regular words, |br| pseudowords and unpronounceable words.                            | If the string is a word, the subject has to say if it is alive or not. If the string is a pseudoword, |br| they have to say if the word contains 1 or 2 syllables. If the string is unpronounceable, they have to say if it is uppercase or lowercase.|
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| LEC2 | Visual Selective Attention task        | Subject briefly reads words on the screen.                                                                                                                 | The subject must read the story written in grey and ignore the story written in white.                                                                                                                                                                |
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| MCSE | Visual Search Task                     | Subject sees an array filled with distractor symbols and a target. |br| Distractors and target follow different color schemes to increase difficulty.      | The subject has to press a button to indicate as fast as possible whether the target was in the upper or lower part of the array.                                                                                                                     |
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| MOTO | Instructed Moto-Coordination Task      | Subject sees squares on a screen. Either the square on the left or the right side is lit up, |br| indicating a body side.                                  | The participant is required to sequentially move various body parts while adhering to the body side indicated on the screen. |br| One of the movements involved pressing a button using either the left or right index finger.                        |
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| MVEB | Sternberg's Verbal Working Memory task | Subject sees a string of 6 characters, some are letters, some are #.                                                                                       | The subject must read and memorize these characters. Then another letter appears, and they must tell if this letter was part of those presented earlier.                                                                                              |
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| MVIS | Visuo-Spatial Working Memory Task      | Subject sees circles on a grid.                                                                                                                            | The subject must remember the position of these circles. After 3 seconds, a single circle is presented in the same grid. |br| The subject has to tell if this circle was already present in the first image.                                          |
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| REST | Resting State Paradigm                 | Subject were recorded at rest.                                                                                                                             | No other instruction than to keep their eyes closed for 5 minutes in a mind wandering state.                                                                                                                                                          |
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| VISU | Visual Oddball Task                    | Subject sees series of 5 images, followed by a short break to blink.                                                                                       | The subject has to push a button whenever they see a FRUIT (visual oddball).                                                                                                                                                                          |
	+------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. raw:: html

   <center>	
	<b>Tab.6</b> <i>Localizers.</i>
   </center>
	
|

The cognition SEEG data found in the */derivatives/cognition* folder of the COGEPISTIM dataset (see :ref:`Fig.1 <coge_structure>`) correspond to amplitude modulations extracted in two specific frequency bands:
8-24 Hz and 50-150 Hz. The method is fully detailed in [Ossandón_2012]_.

License
:::::::

The COGEPISTIM database is the property of `CHU Grenoble Alpes <https://www.chu-grenoble.fr/>`_, France.
Its transfer and use, e.g. for research or clinical purposes, is prohibited without signed data transfer agreement.
For questions, please contact `Philippe KAHANE, MD, PhD <mailto:PKahane@chu-grenoble.fr?subject=COGEPISTIM%20dataset>`_.
 
Code availability
:::::::::::::::::

The data have been prepared using a collection of software, namely:

	* `Freesurfer <https://surfer.nmr.mgh.harvard.edu/>`_ (6.0.0)
	* `BrainVisa <https://brainvisa.info/>`_ (4.5.0) 
	* `ANTs <https://stnava.github.io/ANTs/>`_ (1.9, svn release 1781) 
	* `SPM12 <https://www.fil.ion.ucl.ac.uk/spm/software/spm12/>`_ SPM12 (12b)
	* `ImaGIN and IntrAnat Electrodes <https://f-tract.eu/software/>`_ (no versioning)
	* `BIDS Manager <https://github.com/Dynamap/BIDS_Manager/>`_ (0.3.4)  
	* `BIDS-Validator <https://www.npmjs.com/package/bids-validator/>`_ (1.12.0)

Acknowledgments
:::::::::::::::

This research was supported by the EBRAINS research infrastructure, funded from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement
No. 945539 (`Human Brain Project SGA3 <https://cordis.europa.eu/project/id/945539/>`_).

The F-TRACT project, whose code has been used to preprocess the data, has received funding from the European Research Council under the European Union’s Seventh Framework Programme
(FP/2007-2013)/ERC Grant Agreement no. 616268 F-TRACT.

This reseach was made in collaboration with `Aix Marseille University <https://www.univ-amu.fr/>`_, `Université Grenoble Alpes <https://www.univ-grenoble-alpes.fr/>`_, `CHU Grenoble Alpes <https://www.chu-grenoble.fr/>`_,
`University Hospital of Lyon (Hospices Civils de Lyon) <https://www.chu-lyon.fr/>`_ and `Lausanne University Hospital (Centre Hospitalier Universitaire Vaudois) <https://www.chuv.ch/fr/chuv-home>`_.

Patches
:::::::

V1.1
....

	* Improved *\*_ieeg.vmrk* files associated with stimulation SEEG data so the events match those found in the associated *\*_events.tsv* file.

V1.2
....

	* Fixed commas in the notes of stimulation SEEG data to prevent breaking .vmrk files.
	* Updated the notes for '0Hz' stimulation in certain SEEG data to reflect the correct stimulation frequency.


References
::::::::::

.. [Blair_2022] Blair, Ross, Michael, Zack, Gorgolewski, Krzysztof J., Hardcastle, Nell, Hobson-Lowther, Teal, Nishikawa, David, Bhogawar, Suyash, Appelhoff, Stefan, Jas, Mainak, Grass, Brian, Markiewicz, Christopher J., Holdgraf, Chris, Jones, Alexander, Goyal, Rohan, Oostenveld, Robert, Noack, Gregory, Triplett, William, Naveau, Mikaël, Zito, Matthew, … Zulfikar, Wazeer. (2022). bids-validator (v1.9.3). Zenodo.
.. [Evans_2001] Evans, A.C., Fox, P.T., Lancaster, J., Zilles, K., Woods, R., Paus, T., Simpson, G., Pike, B., Holmes, C., Collins, D.L., Thompson, P., MacDonald, D., Iacoboni, M., Schormann, T., Amunts, K., Palomero-Gallagher, N., Geyer, S., Parsons, L., Narr, K., Kabani, N., LeGoualher, G., Boomsma, D., Cannon, T., Kawashima, R., Mazoyer, B., 2001a. A probabilistic atlas and reference system for the human brain: International Consortium for Brain Mapping (ICBM). Philos. Trans. R. Soc. London B Biol. Sci. 356, 1293–1322.
.. [Holdgraf_2019] Holdgraf, C., Appelhoff, S., Bickel, S., Bouchard, K., D'Ambrosio, S., David, O., Devinsky, O., Dichter, B., Flinker, A., Foster, B., Gorgolewski, K., Groen, I., Groppe, D., Gunduz, A., Hamilton, L., Honey, C., Jas, M., Knight, K., Lachaux, J.P., Lau, J., N. Lundstrom, B., Lee-Messer, C., Miller, K., G. Ojemann, J., Oostenveld, R., Piantoni, G., Petridou, N., Pigorini, A., Pouratian, N., Ramsey, N., Stolk, A., C. Swann, N., Tadel, F., Voytek, B., Wandell, B., Winawer, J., Zehl, L., Hermes, D., 2019. BIDS-iEEG: an extension to the brain imaging data structure (BIDS) specification for human intracranial electrophysiology. Sci Data. 6(1):102.
.. [Mazziotta_2001] Mazziotta J, Toga A, Evans A, Fox P, Lancaster J, Zilles K, Woods R, Paus T, Simpson G, Pike B, Holmes C, Collins L, Thompson P, MacDonald D, Iacoboni M, Schormann T, Amunts K, Palomero-Gallagher N, Geyer S, Parsons L, Narr K, Kabani N, Le Goualher G, Boomsma D, Cannon T, Kawashima R, Mazoyer B. A probabilistic atlas and reference system for the human brain: International Consortium for Brain Mapping (ICBM). Philos Trans R Soc Lond B Biol Sci. 2001 Aug 29;356(1412):1293-322. doi: 10.1098/rstb.2001.0915. PMID: 11545704; PMCID: PMC1088516.
.. [Roehri_2021a] Roehri N, Medina Villalon S, Jegou A, Colombet B, Giusiano B, Ponz A, Bartolomeo F, Bénar CG. Transfer, Collection and Organisation of Electrophysiological and Imaging Data for Multicentre Studies. Neuroinform., 2021.
.. [Trebaul_2018] Trebaul, L., Deman, P., Tuyisenge, V., Jedynak, M., Hugues, E., Rudrauf, D., Bhattacharjee, M., Tadel, F., Chanteloup-Forêt, B., Saubat, C., Reyes Mejia, G.C., Adam, C., Nica, A., Pail, M., Dubeau, F., Rheims, S., Trébuchon, A., Wang, H., Liu, S., Blauwblomme, T., Garces, M., De Palma, L., Valentín, A., Metsahonkala, E.-L., Petrescu, A.M., Landré, E., Szurhaj, W., Hirsch, E., Valton, L., Rocamora, R., Schulze-Bonhage, A., Mîndruţă, I., Francione, S., Maillard, L., Taussig, D., Kahane, P., David, O., 2018. Probabilistic functional tractography of the human cortex revisited. NeuroImage 181, 414–429. doi:10.1016/j.neuroimage.2018.07.039.
.. [Vidal_2011] Vidal, J.; Hamame, C.; Jerbi, K.; Dalal, S.; Ciumas, C.; Perrone-Bertolotti, M.; Ossandon, T.; Minotti, L.; Kahane, P.; Lachaux, J. Localizing cognitive functions in epilepsy with intracranial gammaband dynamic responses. In: Helmstaedter, C.; Lassonde, M.; Hermann, B.; Kahane, P.; Arzimanoglou, A., editors. Neuropsychology in the Care of People with Epilepsy. John Libbey Eurotext; Paris: 2011.
.. [Vidal_2012] Vidal, J. R., Freyermuth, S., Jerbi, K., Hamame, C. M., Ossandon, T., Bertrand, O., … Lachaux, J.-P. (2012). Long-Distance Amplitude Correlations in the High Gamma Band Reveal Segregation and Integration within the Reading Network. Journal of Neuroscience, 32(19), 6421–6434.
.. [Ossandón_2012] Ossandón T, Vidal JR, Ciumas C, Jerbi K, Hamamé CM, Dalal SS, Bertrand O, Minotti L, Kahane P, Lachaux JP. Efficient "pop-out" visual search elicits sustained broadband γ activity in the dorsal attention network. J Neurosci. 2012 Mar 7;32(10):3414-21. doi: 10.1523/JNEUROSCI.6048-11.2012. PMID: 22399764; PMCID: PMC6621042.



