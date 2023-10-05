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

The dataset is stored in a folder called “`iEEG_task_cognitive <https://thehip.app/apps/files/?dir=/tutorial_data/iEEG_task_cognitive&fileid=715791>`_” located inside the "*tutorial_data*" folder
accessible from the Private Space.

It includes the following files:

	* /Anatomical_data: T1 weighted MRI and Diffusion Tensor Imaging.
	* /Data_HiBoP: Data used by HiBoP for display purposes.
	* /SEEG_<digit>HIP: Task SEEG recordings. 

For further insights into data formats, refer to :ref:`Tab.1 <cogtask_file_format>`.

	
.. _cogtask_file_format:

.. table::
	:align: center
	
	+------------------------------------------------+-----------+--------------------------------------------+
	| Format                                         | Extension | Description                                |
	+================================================+===========+============================================+
	| JavaScript Object Notation                     | .json     | 1D (non-nested) key-value pairs. Metadata. |
	+------------------------------------------------+-----------+--------------------------------------------+
	| Neuroimaging Informatics Technology Initiative | .nii      | Imaging data. Native space.                |
	+------------------------------------------------+-----------+--------------------------------------------+
	| Micromed raw SEEG data                         | .TRC      | Raw SEEG data.                             |
	+------------------------------------------------+-----------+--------------------------------------------+
	| b-vectors                                      | .bvec     | Diffusion gradient vectors. Text file.     |
	+------------------------------------------------+-----------+--------------------------------------------+
	| b-values                                       | .bval     | Diffusion gradient values. Text file.      |
	+------------------------------------------------+-----------+--------------------------------------------+

.. raw:: html

   <center>	
	<b>Tab.1</b> <i>Files formats.</i>
   </center>
	
|
	

	
License
=======

This tutorial dataset is the property of the `Lausanne University Hospital (Centre Hospitalier Universitaire Vaudois) <https://www.chuv.ch/fr/chuv-home>`_, Switzerland.
Its use and transfer outside this HIP tutorial, e.g. for research purposes, is prohibited without written consent.
For questions, please contact `Carolina Ciumas, MD, PhD <mailto:Carolina.Ciumas@chuv.ch?subject=HIP%20Cico%20dataset%20>`_.

