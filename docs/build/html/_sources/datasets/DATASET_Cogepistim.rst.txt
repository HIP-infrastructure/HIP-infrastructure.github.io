.. include:: ../hip_header_msg.rst

.. warning::

    The COGEPISTIM database is not yet available on the HIP.

COGEPISTIM database
********************

.. TODO:
	Ask for localizers description.

Overview
=========

The COGEPISTIM database includes SEEG recordings and imaging data of 242 (28/07/2022) patients retrospectively collected from different research protocols:
	
	* F-TRACT: `The Functional Brain Tractography Project <https://f-tract.eu/>`_.
	* ISD SEEG: `Evaluation of the Risk of Cognitive Deficit After Surgery of Epilepsy by Dynamic Spectral Imaging (ISD) of the Cognitive Functions in Patients Explored in StereoElectroEncephaloGraphy <https://clinicaltrials.gov/ct2/show/NCT03094312>`_. 
	* EPISTIM: `Epileptogenic Zone's Cartography by Quantification of EEG's Signal and Intracerebral Stimulation <https://clinicaltrials.gov/ct2/show/NCT02844374>`_.
	* MAPCOG-SEEG: `Atlas of Human Cognition by SEEG <https://clinicaltrials.gov/ct2/show/NCT03644732>`_.

The COGEPISTIM database is BIDS compliant and contains imaging (T1, T2, CT, FLAIR) and SEEG (baselines, seizures, electrical stimulations, localizers) data with associated electrode coordinates.
Electrical stimulation, seizure and baseline SEEG come from the F-TRACT project, whereas localizers come from the ISD SEEG, EPISTIM and MAPCOG-SEEG research protocols.

SEEG data include:

	* 171 subjects with localizers.
	* 176 subjects with electrical stimulation data.
	* 105 subjects with both localizers and electrical stimulation data.
	* 75 subjects with seizure data.
	* 54 subjects with baseline data.
	* 34 subjects with localizers, electrical stimulation, seizure and baseline data.

All subjects have post-implantation imaging data (T1 or CT) and may have pre-implantation and postoperative imaging data.
Imaging data was defaced using SPM defacing feature (`www.fil.ion.ucl.ac.uk/spm/software/spm12 <https://www.fil.ion.ucl.ac.uk/spm/software/spm12/>`_).


Directories and files
----------------------

The COGEPISTIM database has been generated using :doc:`BIDS Manager </applications/APP_BIDS_Manager>` and follows BIDS guidelines
(`BIDS website <https://bids.neuroimaging.io/>`_) (BIDS-iEEG specifications available in [Holdgraf_2019]_).

File and directory structure:

::

	/root
	.. dataset_description.json
	.. participants.tsv
	.. /derivatives
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


Complementary information regarding file formats and file-internal data structures:

	* Tab-Separted Value format (.tsv): Labels in first row. Data of same type in columns.
	* JavaScript Object Notation (.json): 1D (non-nested) key-value pairs.
	* Neuroimaging Informatics Technology Initiative (.nii): Defaced imaging, native space.
	* BrainVision data format (.vhdr, .vmrk, .eeg): Unprocessed SEEG data (in BIDS *raw* directory).

Directory description:

	* /sub-<cogepistim_id> → Subject directory. BIDS subject entity. 
	* /ses-<session> →  Session directory. BIDS session entity.
	* /derivatives → Derivatives directory. BIDS derivatives. Processing pipeline and software outputs. Follows BIDS data structure.
	* /anat → Structural imaging data. BIDS data type. T1, T2, CT, FLAIR data.
	* /ieeg → intracranial electroencephalography data. BIDS data type. SEEG data with electrode coordinates.

File description:

	* dataset_description.json → short description of the dataset.
	* participants.tsv → Clinical information of the subjects.
	* \*_sessions.tsv → Session-specific clinical information of the subjects.
	* \*._scans.tsv → Session-wise file listing.
	* \*ieeg.vhdr → BrainVision text file. Header.
	* \*_ieeg.vmrk → BrainVision text file. Events.
	* \*_ieeg.eeg → BrainVision binary file. Voltage values.
	* \*_ieeg.json → BIDS acquisition infos. e.g. task, stimulation parameters, recording mode.
	* \*_events.tsv → BIDS event infos. e.g. onset, duration, type.
	* \*_channels.tsv → BIDS channel infos. e.g. name, type, sampling frequency.
	* \*_coordsystem.json → BIDS (i)EEG specific. Coordinate system info / spatial reference.
	* \*_electrodes.tsv → BIDS (i)EEG specific. (i)EEG electrode location.
	* \*_T1w.nii → T1 weighted MRI.
	* \*_T2w.nii → T2 weighted MRI.
	* \*_CT.nii → Computerized Tomography.
	* \*_FLAIR.nii → FLAIR MRI.

.. _cogepistim_bids_entities: 

BIDS entities:

	* <cogepistim_id> → COGEPISTIM unique identifier. CES<center> where <center> is a 4-digit number. e.g. CES1003, CES2097.
	* <session> → Subject implantation.  preimp<XX> (before implantation), postimp<XX> (after implantation), postop<XX> (postoperative) where <XX> is a 2-digit number indexing implantations. e.g. preimp01 and postimp01 are the pre- and post- implanation sessions for the first implantation, whereas postimp02 is the post-implantation session for the second implantation.
	* <ieeg_task> → SEEG task. stimulation, baseline, seizure, VISU, LEC1, LEC2, MVIS, MVEB, AUDI, CSC, MCSE, REST1, REST2, REST3, MOTO, ARFA, JUMPY, STAB, MLAH.
	* <ieeg_acq> → <><><> localizers results.
	* <ieeg_space> → Spatial reference to interpret electrode coordinates. e.g. MNI152Lin.
	* <anat_ce> → Contrast agent. e.g. gadolinium.
	* <run> → Repetition number of an acquisition. e.g. 01, 02, 03…
	

F-TRACT data description
========================

Electrical stimulation, seizure and baseline SEEG data where extracted from the F-TRACT project.
Data were initially collected for the F-TRACT study, following the ethical procedures for conducting international multicenter post-processing 
of clinical data defined by the International Review Board at `INSERM <https://www.inserm.fr/en/home/>`_.

Methods
--------

The F-TRACT project contains structural (imaging) and functional (neurophysiological) SEEG data from adult epileptic patients who were candidates
to resective surgery and undergone intracortical stimulations. The data were collected from a multicenter patient population.
Methods and materials for recording the data differed between epilepsy surgery units, and followed strict clinical procedures as defined
in every hospital. The recording procedures were not standardized in research perspective which sole objective was data-reuse.

For each patient, at least one anatomical MRI (T1 contrast if available, sometimes associated to a T2 and/or FLAIR contrast)
and an image with SEEG electrodes (T1 MRI or CT scan and accessory implantation scheme) were obtained in order to localise SEEG electrodes.
The average number of recording bipolar contacts per patient was about 150. 

Baselines, seizures and low-frequency stimulations were recorded as part of a pre-surgical evaluation of drug-resistant epilepsy.
In the database, we considered only stimulations performed at low frequency (<5 Hz) for a limited amount of time per stimulated area
(typically less than 40 pulses). Bipolar stimuli were delivered using a constant current rectangular pulse generator designed for a safe
diagnostic stimulation of the human brain, according to parameters proved to produce no structural damage.
All stimulations were performed between two contiguous contacts in the grey matter, and sometimes in the white matter, using monophasic 
or biphasic pulses. Pulse width and intensity of stimulation could vary (typically 1 ms duration pulses at 3 mA).
The clinical goals of the stimulations were the reproduction of the aura, the induction of an electroclinical seizure,
and/or the localisation of an eloquent cortical area that has to be spared during surgery.
Signals were acquired at a sampling frequency which varied between 512 Hz and 2048 Hz.
 
The main steps required to generate the database are as follows (see [Trebaul_2018]_ for full scientific details): 

.. _ftract_imaging_method: 

	* **Imaging** - The electrode contacts were localised and anatomically labelled using 
	  the :doc:`IntrAnat Electrodes software </applications/APP_IntrAnat>` ([Deman_2018]_) compatible with the `BrainVisa software <http://brainvisa.info>`_
	  ([Rivière_2009]_). Briefly, the volumetric images acquired before and after the electrode implantation were co-registered using a rigid-body
	  transformation computed either by ANTs ([Avants_2011]_) or SPM12 ([Ashburner_2009]_) software.
	  The grey and white matter volumes were segmented from the pre-implantation MRI using Morphologist as included in BrainVisa.
	  The electrode contact positions were computed in the native and MNI referentials using the spatial normalisation of SPM12 software.
	  For each patient, cortical parcels were obtained for different anatomical atlases defined either in the MRI native space
	  (MarsAtlas ([Auzias_2016]_), Freesurfer ([Destrieux_2010]_), Lausanne Atlas ([Hagmann_2008]_)) or in the MNI space
	  (Brodmann ([Brodmann_1909]_), Automated Anatomical Labeling AAL ([Tzourio-Mazoyer_2002]_), MaxProbMap ([Hammers_2003]_),
	  and Human Connectome Project ([Glasser_2016]_)).
	  Each electrode contact was assigned to the grey or white matter and to specific anatomical parcels by taking the most frequent voxel
	  label in a sphere of 3 mm radius around each contact centre ([Deman_2018]_).

	* **Neurophysiology**  - The SEEG signals were pre-processed automatically using a pipeline composed of the following steps,
	  supervised at the end for data quality check: i) detection and cropping of each stimulation run from stimulation artefacts
	  in raw iEEG files (i.e. a set a pulses consecutively applied between the same pair of contacts); ii) bad channels detection
	  with a machine learning approach ([Tuyisenge_2018]_). The detection of bad channels was based on a supervised machine-learning
	  model trained on a learning database with channels already classified by experts and using a set of features quantifying the signal
	  variance, spatio-temporal correlation and non-linear properties. 
	  
	  
Operationally, the data was extracted from the F-TRACT infrastructure of `Université Grenoble Alpes (UGA) <https://www.univ-grenoble-alpes.fr/>`_ , as an independent folder created 
by a F-TRACT to BIDS converter developed by `Aix-Marseille Université (AMU) <https://www.univ-amu.fr/>`_  for UGA’s use. 
F-TRACT to BIDS converter is a module of :doc:`BIDS Manager software</applications/APP_BIDS_Manager>` (BIDS Manager and Pipeline, version 0.2.4) developed by AMU to organise any database in BIDS format ([Roehri_2021a]_).


ISD data description
====================

**COGNITIVE DATA DESCRIPTION**

SEEG Electrode coordinates
===========================

SEEG electrode spatial reference and coordinates can be found for each subject in the following files (see :ref:` COGEPISTIM BIDS entities <cogepistim_bids_entities>`)):

	* sub-<cogepistim_id>_ses-<session>_space-<ieeg_space>_coordsystem.json (spatial reference).
	* sub-<cogepistim_id>_ses-<session>_space-<ieeg_space>_electrodes.tsv (electrode coordinates).

Electrode coordinates are specified in both native and MNI152 (ICBM Average Brain, 152 T1-weighted MRI scans,
using linear coregistration to the MNI305 space) spaces ([Evans_2001]_; [Mazziotta_2001]_).
 
For SEEG data coming from the F-TRACT project, each electrode contact was also assigned to specific anatomical parcels of a set of atlases (see :ref:`F-TRACT methods <ftract_imaging_method>`),
namely: MarsAtlas, Freesurfer, AAL, Broadman, Hammers, HCP_MMP1, AICHA, Lausanne2008.


Clinical information
====================

Clinical information is limited to sex, handedness, age group and epilepsy location. 
*Sex* can be found in the *participants.tsv* file in BIDS *raw* directory.
Subjects underwent one or several implantations which correspond to BIDS *sessions*.
*Handedness*, *age group* and *epilepsy location* can be found in the *<subject>_sessions.tsv* file which reside in each subject's folder. 

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

The COGEPISTIM database (iEEG and imaging data) is the property of `Aix-Marseille Université (AMU) <https://www.univ-amu.fr/>`_, France.
Its transfer and use outside the HIP, e.g. for research purposes, is prohibited without written consent.
For questions, please contact `Olivier David, PhD <mailto:Olivier.David@univ-amu.fr?subject=HIP%20COGEPISTIM%20dataset%20>`_.

Code availability
=================

The data have been prepared using a collection of processing toolboxes, namely:
	
	* Freesurfer (6.0.0, surfer.nmr.mgh.harvard.edu)
	* BrainVisa (4.5.0, brainvisa.info)
	* ANTs (1.9, svn release 1781, stnava.github.io/ANTs)
	* SPM12 (12b, fil.ion.ucl.ac.uk/spm/software/spm12)
	* ImaGIN and IntrAnat Electrodes (no versioning, f-tract.eu/software)

Acknowledgments
=================

The research leading to these results has received funding from the European Research Council under the European Union's Seventh Framework Programme (FP/2007-2013)/ERC Grant Agreement no. 616268 F-TRACT.

References
==========

.. [Ashburner_2009] Ashburner, J., 2009. Computational anatomy with the SPM software. Magn Reson Imaging 27, 1163–1174. doi:10.1016/j.mri.2009.01.006

.. [Auzias_2016] Auzias, G., Coulon, O., Brovelli, A., 2016. MarsAtlas: A cortical parcellation atlas for functional mapping. 37, 1573–1592. doi:10.1002/hbm.23121 

.. [Avants_2011] Avants, B.B., Tustison, N.J., Wu, J., Cook, P.A., Gee, J.C., 2011. An open source multivariate framework for n-tissue segmentation with evaluation on public data. Neuroinformatics 9, 381–400. doi:10.1007/s12021-011-9109-y.

.. [Brodmann_1909] Brodmann, K., 1909. Vergleichende Lokalisationslehre der Grosshirnrinde. Johann Ambrosius Barth, Leipzig. 

.. [Deman_2018] Deman, P., Bhattacharjee, M., Rivière, D., Tadel, F., Cointepas, Y., David, O., 2018. IntrAnat Electrodes: A free database software to visualize intracranial electroencephalographic data in patient’s referential and to initiate group studies. Front. Neuroinform. 12, 40. 

.. [Destrieux_2010] Destrieux C, Fischl B, Dale A, Halgren E. Automatic parcellation of human cortical gyri and sulci using standard anatomical nomenclature. Neuroimage. 2010 Oct 15;53(1):1-15. doi: 10.1016/j.neuroimage.2010.06.010. Epub 2010 Jun 12. PMID: 20547229; PMCID: PMC2937159.

.. [Evans_2001] Evans, A.C., Fox, P.T., Lancaster, J., Zilles, K., Woods, R., Paus, T., Simpson, G., Pike, B., Holmes, C., Collins, D.L., Thompson, P., MacDonald, D., Iacoboni, M., Schormann, T., Amunts, K., Palomero-Gallagher, N., Geyer, S., Parsons, L., Narr, K., Kabani, N., LeGoualher, G., Boomsma, D., Cannon, T., Kawashima, R., Mazoyer, B., 2001a. A probabilistic atlas and reference system for the human brain: International Consortium for Brain Mapping (ICBM). Philos. Trans. R. Soc. London B Biol. Sci. 356, 1293–1322.

.. [Glasser_2016] Glasser MF, Coalson TS, Robinson EC, Hacker CD, Harwell J, Yacoub E, Ugurbil K, Andersson J, Beckmann CF, Jenkinson M, Smith SM, Van Essen DC. A multi-modal parcellation of human cerebral cortex. Nature. 2016 Aug 11;536(7615):171-178. doi: 10.1038/nature18933. Epub 2016 Jul 20. PMID: 27437579; PMCID: PMC4990127.

.. [Hagmann_2008] Hagmann P, Cammoun L, Gigandet X, Meuli R, Honey CJ, Wedeen VJ, Sporns O. Mapping the structural core of human cerebral cortex. PLoS Biol. 2008 Jul 1;6(7):e159. doi: 10.1371/journal.pbio.0060159. PMID: 18597554; PMCID: PMC2443193.

.. [Hammers_2003] Hammers, A., Allom, R., Koepp, M.J., Free, S.L., Myers, R., Lemieux, L., Mitchell, T.N., Brooks, D.J., Duncan, J.S., 2003. Three-dimensional maximum probability atlas of the human brain, with particular reference to the temporal lobe 19, 224–247. doi:10.1002/hbm.10123.

.. [Holdgraf_2019] Holdgraf, C., Appelhoff, S., Bickel, S., Bouchard, K., D'Ambrosio, S., David, O., Devinsky, O., Dichter, B., Flinker, A., Foster, B., Gorgolewski, K., Groen, I., Groppe, D., Gunduz, A., Hamilton, L., Honey, C., Jas, M., Knight, K., Lachaux, J.P., Lau, J., N. Lundstrom, B., Lee-Messer, C., Miller, K., G. Ojemann, J., Oostenveld, R., Piantoni, G., Petridou, N., Pigorini, A., Pouratian, N., Ramsey, N., Stolk, A., C. Swann, N., Tadel, F., Voytek, B., Wandell, B., Winawer, J., Zehl, L., Hermes, D., 2019. BIDS-iEEG: an extension to the brain imaging data structure (BIDS) specification for human intracranial electrophysiology. Sci Data. 6(1):102.

.. [Mazziotta_2001] Mazziotta J, Toga A, Evans A, Fox P, Lancaster J, Zilles K, Woods R, Paus T, Simpson G, Pike B, Holmes C, Collins L, Thompson P, MacDonald D, Iacoboni M, Schormann T, Amunts K, Palomero-Gallagher N, Geyer S, Parsons L, Narr K, Kabani N, Le Goualher G, Boomsma D, Cannon T, Kawashima R, Mazoyer B. A probabilistic atlas and reference system for the human brain: International Consortium for Brain Mapping (ICBM). Philos Trans R Soc Lond B Biol Sci. 2001 Aug 29;356(1412):1293-322. doi: 10.1098/rstb.2001.0915. PMID: 11545704; PMCID: PMC1088516.

.. [Rivière_2009] Rivière, D., Geffroy, D., Denghien, I., Souedet, N., Cointepas, Y., 2009. BrainVISA: an extensible software environment for sharing multimodal neuroimaging data and processing tools. NeuroImage 47, S163. doi:10.1016/S1053-8119(09)71720-3.

.. [Roehri_2021a] Roehri N, Medina Villalon S, Jegou A, Colombet B, Giusiano B, Ponz A, Bartolomeo F, Bénar CG. Transfer, Collection and Organisation of Electrophysiological and Imaging Data for Multicentre Studies. Neuroinform., 2021.

.. [Trebaul_2018] Trebaul, L., Deman, P., Tuyisenge, V., Jedynak, M., Hugues, E., Rudrauf, D., Bhattacharjee, M., Tadel, F., Chanteloup-Forêt, B., Saubat, C., Reyes Mejia, G.C., Adam, C., Nica, A., Pail, M., Dubeau, F., Rheims, S., Trébuchon, A., Wang, H., Liu, S., Blauwblomme, T., Garces, M., De Palma, L., Valentín, A., Metsahonkala, E.-L., Petrescu, A.M., Landré, E., Szurhaj, W., Hirsch, E., Valton, L., Rocamora, R., Schulze-Bonhage, A., Mîndruţă, I., Francione, S., Maillard, L., Taussig, D., Kahane, P., David, O., 2018. Probabilistic functional tractography of the human cortex revisited. NeuroImage 181, 414–429. doi:10.1016/j.neuroimage.2018.07.039.

.. [Tuyisenge_2018] Tuyisenge, V., Trebaul, L., Bhattacharjee, M., Chanteloup-Forêt, B., Saubat-Guigui, C., Mîndruţă, I., Rheims, S., Maillard, L., Kahane, P., Taussig, D., David, O., 2018. Automatic bad channel detection in intracranial electroencephalographic recordings using ensemble machine learning. Clin Neurophysiol 129, 548–554. doi:10.1016/j.clinph.2017.12.013.

.. [Tzourio-Mazoyer_2002] Tzourio-Mazoyer, N., Landeau, B., Papathanassiou, D., Crivello, F., Etard, O., Delcroix, N., Mazoyer, B., Joliot, M., 2002. Automated anatomical labeling of activations in SPM using a macroscopic anatomical parcellation of the MNI MRI single-subject brain. NeuroImage 15, 273–289. doi:10.1006/nimg.2001.0978.
