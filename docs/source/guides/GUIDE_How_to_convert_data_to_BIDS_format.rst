.. include:: ../hip_beta_warning.rst

How to convert data to BIDS format
***********************************

.. figure:: /guides/art/GUIDE_How_to_convert_data_to_BIDS_format/GUIDE_BIDS_importer.png
	:width: 600px
	:align: center

	**The BIDS Importer.** *The BIDS Importer is a step-by-step tool that can be used to import raw data into a BIDS database.*

About this tutorial
====================

Objective
---------

The objective of this guide is to introduce HIP users to the BIDS Importer, a step-by-step tool designed specifically for the platform
and allowing its users to import raw data into a BIDS database.

This guide first gives a general introduction to the BIDS standard and its leading guidelines, so HIP users know its purpose and
become familiar with its basic principles.
It then focuses on the BIDS importer itself describing its main features and limitations, including a video guide explaining how to:

	* Create or select a BIDS database
	* Create or update a subject with associated clinical information
	* Select and describe data files to import using BIDS entities
	* Import the prepared data into a new or existing BIDS database	
	
Scope 
------

This guide explains how to use the BIDS importer and gives the basics regarding the BIDS standard. 
This guide along with the advice found in the BIDS importer itself should be sufficient to perform basic data importation without further a
priori knowledge regarding the standard.

The importation process is fully guided but has a limited scalability and is time consuming. Therefore, advanced users should rely on scripting
using the :doc:`BIDS Manager </applications/APP_BIDS_Manager>`, available on the platform, so they can programmatically prepare and import their data into a BIDS database.

This guide does not explain :doc:`how to prepare and upload data to the HIP </guides/GUIDE_How_to_prepare_and_upload_data_to_the_HIP>`,
nor goes into all the intricacies of the `BIDS standard <https://bids-specification.readthedocs.io/en/stable/>`_.

.. _BIDS_introduction:

The Brain Imaging Data Structure
=================================

The Brain Imaging Data Structure (BIDS) is a community driven standard for organizing, annotating, and describing neuroimaging, neurophysiological and 
behavioral data. It is a framework for organizing data that standardizes file organization and dataset description.

For more details regarding the standard, please refer to the following external resources:

	* `BIDS documentation (full specifications) <https://bids-specification.readthedocs.io/en/stable/>`_
	* `BIDS Git (BIDS validator, examples and starter kit) <https://github.com/bids-standard>`_
	* `BIDS website (BIDS extension proposals and converters) <https://bids.neuroimaging.io/>`_

BIDS is a community effort and specification can be extended to new data types using the guide for `BIDS extensions proposals <https://bids.neuroimaging.io/get_involved.html#extending-the-bids-specification>`_ . 
Several papers have been published covering the standard and its extensions:

	* [Gorgolewski_2016]_
	* [Gorgolewski_2017]_
	* [Pernet_2019]_
	* [Niso_2018]_ 
	* [Holdgraf_2018]_
	* [Moreau_2020]_
	
BIDS in practice
----------------

BIDS standardize the way to organize, name and describe files of a dataset.

In practice, a BIDS database is a directory containing all the data, called the **raw directory**, with a unique folder per subject.
Subject folders contain **data types subfolders** which group similar data together. Data files have to follow a specific naming convention relying
on **BIDS entities** and only a selection of open-source formats are allowed.
The dataset and its files are further described using **metadata files**. 

**BIDS directory tree** can be summarized as follow:

| **/project** - BIDS database raw directory.
| └── **/subject** - Subject folder. 1 per subject.
|     └── **/session(s)** - Optional  session folder to group data (e.g. subject's inclusions).
|        └── **/data type(s)** - Data type folder. Group data of the same type.

The database name should be as descriptive as possible and subject folder have to be unique. Session subfolders can be used to group data
in a logical manner, for example, a session folder for each subject's inclusion in a longitudinal study.
If used, session subfolders are required for all subjects to keep the directory tree consistent across subjects.
Data type folders group similar acquisition modalities together but not all types of data are supported by the standard which can
be extended through `BIDS extensions proposals <https://bids.neuroimaging.io/get_involved.html#extending-the-bids-specification>`_ . 

**BIDS data types** that are currently supported:

	* **func**:  functional MRI data
	* **dwi**:   diffusion weighted imaging data
	* **fmap**:  field inhomogeneity mapping data
	* **anat**:  structural imaging data
	* **meg**:   magnetoencephalography data
	* **eeg**:   electroencephalography data
	* **ieeg**:  intracranial electroencephalography data
	* **beh**:   behavioral data
	* **pet**:   positron emission tomography data
	* **perf**:  perfusion imaging data

The metadata used to describe the data files or the dataset itself is stored in companion **.json** or **.tsv** files, while the data files themselves
must conform to a selection of open-source formats given by the standard.

**BIDS file types** that can be found in a BIDS database:

	* **.json**: contain "key: value" metadata.
	* **.tsv**: contain tables of metadata.
	* **raw**: data files in BIDS compliant format (e.g. NIfTI, BrainVision, European data format).

An important aspect of the standard is that data file names have to use BIDS entities so they are unique and informative. 
BIDS entities are key-value pairs chained with underscores and are used to structure file names.

**BIDS file naming** convention is illustrated in the figure below:

.. figure:: /guides/art/GUIDE_How_to_convert_data_to_BIDS_format/GUIDE_BIDS_entities.png
	:width: 800px
	:align: center

	**BIDS file naming.** *File names are structured using BIDS entities (key-value pairs) connected with underscores and ending with a suffix and a file extension.*

BIDS entities are used at the subject level on raw data and associated metadata files, between- and within-subjects, 
but may not be used on some study-level metadata files (e.g. *dataset_description.json*, *participants.tsv*, *\*sessions.tsv*, *\*scans.tsv*)		
	
BIDS entities have a definite order. Keys are alphanumeric while values can be either alphanumeric or integers depending on the considered entity.
BIDS entities can be required or optional, depending on the modality and design choices of the BIDS database, and some have to be consistent across subjects/sessions when used.	

The following table is an example of BIDS entities which can be found in a BIDS database:

.. table::
	:align: center
	
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Entity                  | Key       |  Description                                                                                                                                                                         | Example             |
	+=========================+===========+======================================================================================================================================================================================+=====================+
	| Subject                 | sub       | A person or animal participating in the study.                                                                                                                                       | sub-johndoe         | 
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Session                 | ses       | An intermediate folder in BIDS folder hierarchy to group data that go "logically" together. If used, sessions must be pertinent and consistent across subjects.                      | ses-postsurgery     |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Task                    | task      | Identify the task performed by the subject during the acquisition. If used, must be consistent across subjects and sessions.                                                         | task-eyesclosed     |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Acquisition             | acq       | Identify the acquisition parameters used to perform the acquisition. If used, must be consistent across subjects and sessions.                                                       | acq-lowres          |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Contrast enhancing agent| ce        | Identify contrast agent. Does not have to be consistent.                                                                                                                             | ce-gadolinium       |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Reconstruction          | rec       | Identify reconstruction algorithms. Does not have to be consistent.                                                                                                                  | rec-lsqr            |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Phase-Encoding Direction| dir       | Identify phase-encoding directions. Does not have to be consistent.                                                                                                                  | dir-leftright       |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Run                     | run       | Identify repeated acquisitions. Does not have to be consistent. But becomes required if more than one acquisition. Value is an integer.                                              | run-01              |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Modality                | mod       | Identify modality label for defacing masks. Does not have to be consistent.                                                                                                          | mod-T1w_defacemask  |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Echo                    | echo      | Identify an echo file with its index. Does not have to be consistent. Value is an integer.                                                                                           | echo-01             |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Recording               | recording | Identify different continuous recording files. Does not have to be consistent.                                                                                                       | recording-saturation|
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Processed               | proc      | Identify processing applied during acquisition. Does not have to be consistent.                                                                                                      | proc-trans          |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Space                   | space     | Identify the space in which coordinates/positions should be interpreted. Does not have to be consistent. Value come from dedicated BIDS appendix VIII: Coordinate systems.           | space-MNI152Lin     | 
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Split                   | split     | Identify multiple parts of a file. Mostly used for .fif files. Does not have to be consistent. Value is an integer.                                                                  | split-01            |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
	| Tracer                  | trc       | Identify the radio tracer used during PET acquisition.                                                                                                                               | trc-fdg             |
	+-------------------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+


.. admonition:: Unsupported data files

   Data files that are not covered by the standard may still be imported in a BIDS database. They should follow BIDS guidelines as much as
   possible and have to be declared in a .bidsignore file in BIDS raw directory in order to pass BIDS validation. This is not supported by 
   the BIDS importer.
   
.. admonition:: Derivatives files

   Data files which have been processed and that cannot be considered as raw data anymore should go to BIDS *derivatives* folder. This is not supported by 
   the BIDS importer.	
	
.. _BIDS_importer:

The BIDS Importer
==================

The BIDS importer is a step-by-step tool designed specifically for the platform and allowing its users to import raw data into a BIDS database.
The BIDS importer emphasizes simplicity, readability and safeguarding. It purposefully restrains the importation procedure to a selection of modalities 
and is limited to mandatory BIDS entities with a few exceptions. 

.. _BIDS_importer_dtypes:

Data types and corresponding BIDS modalities available in the BIDS importer are as follows:

	* **anat**: T1w, T2w, T1rho, T1map, T2map, T2start, FLAIR, PD, Pdmap, PDT2, inplanteT1, inplanteT2, angio, defacemask, CT
	* **pet**: pet, petmr, petct
	* **func**: bold, sbref
	* **fmap**: phasediff, phase1, phase2, magnitude, magnitude1, magnitude2, fieldmap, epi
	* **dwi**: dwi
	* **ieeg**: ieeg
	* **eeg**: eeg
	* **meg**: meg
	* **ieegGlobalSidecars**: electrodes, coordsystem, photo
	* **eegGlobalSidecars**: electrodes, coordsystem, photo
	* **petGlobalSidecars**: blood

.. _BIDS_importer_formats:	

Data file formats compatible with the BIDS importer (with targeted file extension) are as follows:

	* **Micromed**: .trc (.trc)
	* **BrainVision**: .vhdr, .vmrk, .eeg (.vhdr)
	* **European data format**: .edf (.edf)
	* **BioSemi data format**: .bdf (.bdf)
	* **EEGLAB files**: .set (.set)
	* **DICOM**: .dcm (root directory of .dcm files)
	* **NifTi**: .nii (.nii)

Video guide
------------

The following video guide (X'XX'') serves as an introduction to the BIDS importer and how to import raw data into a BIDS database:  

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20BIDS%20importer/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Blank.png" controls>
   <source src="todo.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|


References
===========

.. [Gorgolewski_2016] Gorgolewski, K., Auer, T., Calhoun, V. et al. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. Sci Data 3, 160044 (2016).

.. [Gorgolewski_2017] Gorgolewski KJ, Alfaro-Almagro F, Auer T, Bellec P, Capotă M, Chakravarty MM, et al. BIDS apps: Improving ease of use, accessibility, and reproducibility of neuroimaging data analysis methods. PLoS Comput Biol 13(3) (2017).

.. [Pernet_2019] Pernet CR, Appelhoff S, Gorgolewski KJ, Flandin G, Phillips C, Delorme A, Oostenveld R. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Sci Data. 2019 Jun 25;6(1):103.

.. [Niso_2018] Niso, G., Gorgolewski, K., Bock, E. et al. MEG-BIDS, The brain imaging data structure extended to magnetoencephalography. Sci Data 5, 180110 (2018).

.. [Holdgraf_2018] Holdgraf, Chris et al. “BIDS-iEEG: an extension to the brain imaging data structure (BIDS) specification for human intracranial electrophysiology.” (2018).

.. [Moreau_2020] Clara A Moreau, Martineau Jean-Louis, Ross Blair, Christopher J Markiewicz, Jessica A Turner, Vince D Calhoun, Thomas E Nichols, Cyril R Pernet, The genetics-BIDS extension: Easing the search for genetic data associated with human brain imaging, GigaScience, Volume 9, Issue 10 (2020).