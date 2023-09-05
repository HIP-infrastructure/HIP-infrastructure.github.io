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


The dataset is stored in a folder called “`iEEG_task_cognitive <https://thehip.app/apps/files/?dir=/tutorial_data/iEEG_task_cognitive&fileid=715791>`_” located inside the "*tutorial_data*" folder
accessible from the Private Space.


The arrangement of files and folders is depicted in :ref:`Fig.1 <cogtask_structure>`, while the corresponding naming conventions are outlined in :ref:`Tab.1 <cogtask_naming_convention>`. 
Files and folders are further described in :ref:`Tab.2 <cogtask_file_desc>` and :ref:`Tab.3 <cogtask_folder_desc>` respectively. For further insights into data formats, refer to :ref:`Tab.4 <cogtask_file_format>`.


.. _cogtask_structure:

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
	
.. raw:: html

   <center>	
	<b>Fig.1</b> <i>File and folder organization.</i>
   </center>
	
|

.. _cogtask_naming_convention:

.. table::
	:align: center
	
	+----------------------------+-------------------------------------------------+
	| BIDS value                 | Description                                     |
	+============================+=================================================+
	| <hip_id>                   | Unique identifier of a SEEG file. Alphanumeric. |
	+----------------------------+-------------------------------------------------+



.. raw:: html

   <center>	
	<b>Tab.1</b> <i>Naming convention.</i>
   </center>
	
|


.. _cogtask_file_desc:

.. table::
	:align: center
	
	+----------------+---------------------------------+
	| File           | Description                     |
	+================+=================================+
	| \*T1\*         | T1 weighted MRI.                |
	+----------------+---------------------------------+
	| \*Diffusion\*  | Diffusion Tensor Imaging.       |
	+----------------+---------------------------------+
	| \*(S)EEG\*     | SEEG recording.                 |
	+----------------+---------------------------------+


.. raw:: html

   <center>	
	<b>Tab.2</b> <i>File description.</i>
   </center>
	
|

.. _cogtask_folder_desc:

.. table::
	:align: center
	
	+-----------------------------+--------------------------------------------------------------------+
	| Folder                      | Description                                                        |
	+=============================+====================================================================+
	| /Anatomical_data            | Anatomical imaging (T1, DTI).                                      |
	+-----------------------------+--------------------------------------------------------------------+
	| /TRC                        | SEEG data.                                                         |
	+-----------------------------+--------------------------------------------------------------------+


.. raw:: html

   <center>	
	<b>Tab.3</b> <i>Folder description.</i>
   </center>
	
|

	

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
	<b>Tab.4</b> <i>Files formats.</i>
   </center>
	
|
	

	
License
=======

This tutorial dataset is the property of the `Lausanne University Hospital (Centre Hospitalier Universitaire Vaudois) <https://www.chuv.ch/fr/chuv-home>`_, Switzerland.
Its use and transfer outside this HIP tutorial, e.g. for research purposes, is prohibited without written consent.
For questions, please contact `Carolina Ciumas, MD, PhD <mailto:Carolina.Ciumas@chuv.ch?subject=HIP%20Cico%20dataset%20>`_.

