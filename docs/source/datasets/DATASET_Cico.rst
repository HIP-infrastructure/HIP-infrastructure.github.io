.. include:: ../hip_beta_warning.rst

Cico tutorial dataset
***********************

.. TOADD:
   De-identification procedure ?
   Acquisition modalities ?
   Task description ?
   License ?
   References ?

Description
===========

This dataset includes imaging data and SEEG recordings for 4 subjects:
3 subjects have a similar set of files which includes pre- and post- implantation imaging data (T1, T2, CT, braincase, DTI) and SEEG recordings (ictal, interictal, sleep)
with corresponding implantation scheme.
The 4th subject has pre- and post- implantation imaging data (T1, DTI) and SEEG data recorded while performing a cognitive task.

Data files
-----------

The dataset is accessible in a `publicly shared folder <https://thehip.app/apps/files/?dir=/tutorial_data/Cico%20tutorial%20dataset&fileid=717735>`_.

File and directory structure:

::

	/Cico tutorial dataset
	.. /Case<case_nb>
	.... /Anatomical_data
	...... anon_t1_mprage_case<case_nb>.nii
	...... t1_mprage_case<case_nb>.json
	...... anon_CT_with_electrodes_case<case_nb>.nii
	...... CT_with_electrodes_case<case_nb>.json
	...... anon_t2_mprage_case<case_nb>.nii	
	...... t2_mprage_case<case_nb>.json
	...... anon_Bone_case<case_nb>.nii
	...... Bone_case<case_nb>.json
	.... /DTI_case<case_nb>
	...... DTI_case<case_nb>_TRACEW.nii
	...... DTI_case<case_nb>_TRACEW.json
	...... DTI_case<case_nb>_TRACEW.bvec
	...... DTI_case<case_nb>_TRACEW.bval
	...... DTI_case<case_nb>_FA.nii
	...... DTI_case<case_nb>_FA.json
	...... DTI_case<case_nb>_ADC.nii
	...... DTI_case<case_nb>_ADC.json	
	...... DTI_case<case_nb>.nii
	...... DTI_case<case_nb>.json
	...... DTI_case<case_nb>.bvec
	...... DTI_case<case_nb>.bval		
	.... /Implatation schema
	...... case<case_nb>_schema<scheme_idx>.png
	...... case<case_nb>-implantation-map<map_idx>.png
	.... /SEEG	
	...... case<case_nb>EEG_<hip_id>_<task>.TRC
	.. /SEEG-task-cognitif
	.... /Anatomical_data
	...... anon_T1_implated-cognitive-dataset.nii
	...... anon_T1_mprage-cognitive-dataset.nii
	...... Diffusion-cognitive-dataset.bval
	...... Diffusion-cognitive-dataset.bvec
	...... Diffusion-cognitive-dataset.json
	...... Diffusion-cognitive-dataset.nii
	...... T1_implanted-cognitive-dataset.json
	...... T1_mprage-cognitive-dataset.json
	.... /TRC	
	...... task-SEEG_<hip_id>.TRC
	...... task-SEEG_<hip_id>.TRC
	
Complementary information regarding file formats and file-internal data structures:

	* JavaScript Object Notation (.json): 1D (non-nested) key-value pairs. Metadata.
	* Neuroimaging Informatics Technology Initiative (.nii): Imaging, native space.
	* Micromed raw SEEG data (.TRC): Unprocessed SEEG data.
	* b-vectors (.bvec): Diffusion gradient vectors. Text file.
	* b-values (.bval): Diffusion gradient values. Text file.
	* Portable Network Graphic (.png): Implantation pictures.

Directory description:

	* /Case<case_nb> → Subject directory. 
	* /SEEG-task-cognitif → Subject directory.
	* /Implatation schema →  Implantation schemes.
	* /DTI_case<case_nb> → Diffusion Tensor Imaging data.
	* /Anatomical_data → Anatomical imaging (T1, T2, CT) and Diffusion Tensor Imaging data.
	* /SEEG and /TRC → intracranial electroencephalography data.
	
File description:

	* \*t1\* →  T1 weighted MRI. 
	* \*t2\* →  T2 weighted MRI.
	* \*ct\* →  Computerized Tomography.
	* \*TRACEW\* →  Trace weight.
	* \*FA\* →  Fractional Anisotropy.
	* \*ADC\* →  Apparent Diffusion Coefficient.
	* \*DTI\* →  Diffusion Tensor Imaging.
	* \*(S)EEG\* →  SEEG recording.

Naming convention:

	* <case_nb> → Case number. Integer.
	* <scheme_idx> and <map_idx> → Implantation scheme index. Integer.
	* <hip_id> → Unique identifier of a SEEG file. Alphanumeric.
	* <task> → Task identifier of a SEEG files. Alphanumeric.
	
License
=======

This tutorial dataset (SEEG and MRI data) is the property of the Centre Hospitalier Universitaire de Lausanne, Swiss.
Its use and transfer outside this HIP tutorial, e.g. for research purposes, is prohibited without written consent.
For questions, please contact `Carolina Ciumas, MD, PhD <mailto:Carolina.Ciumas@chuv.ch?subject=HIP%20Cico%20dataset%20>`_.

