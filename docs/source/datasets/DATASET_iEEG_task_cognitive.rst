.. include:: ../hip_header_msg.rst

iEEG cognitive task
********************

.. TOADD:
   De-identification procedure ?
   Acquisition modalities ?
   Task description ?
   License ?
   References ?

Description
===========

This dataset includes 1 subject with pre- and post- implantation imaging data (T1, DTI) and SEEG data recorded while performing a cognitive task.

Data files
-----------

The dataset is accessible in a `publicly shared folder <https://thehip.app/apps/files/?dir=/tutorial_data/iEEG_task_cognitive&fileid=715791>`_.

File and directory structure:

::

	.. /iEEG_task_cognitive
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

Directory description:

	* /Anatomical_data → Anatomical imaging (T1, DTI).
	* /TRC → SEEG data.
	
File description:

	* \*T1\* →  T1 weighted MRI. 
	* \*Diffusion\* →  Diffusion Tensor Imaging.
	* \*(S)EEG\* →  SEEG recording.

Naming convention:

	* <hip_id> → Unique identifier of a SEEG file. Alphanumeric.
	
License
=======

This tutorial dataset (SEEG and imaging data) is the property of the Centre Hospitalier Universitaire de Lausanne, Swiss.
Its use and transfer outside this HIP tutorial, e.g. for research purposes, is prohibited without written consent.
For questions, please contact `Carolina Ciumas, MD, PhD <mailto:Carolina.Ciumas@chuv.ch?subject=HIP%20Cico%20dataset%20>`_.

