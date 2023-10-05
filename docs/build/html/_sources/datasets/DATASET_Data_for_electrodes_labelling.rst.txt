.. include:: ../hip_header_msg.rst

Data for electrodes labelling
******************************

.. TOADD:
   De-identification procedure ?
   Acquisition modalities ?
   Task description ?
   License ?
   References ?

Description
===========

This dataset includes imaging data and SEEG recordings for 3 subjects. Data include pre- and post- implantation
imaging data (T1, T2, CT, braincase, DTI) and SEEG recordings (ictal, interictal, sleep, electrical stimulation)
with corresponding implantation scheme.

The dataset is stored in a folder called “`Data_for_electrodes_labelling <https://thehip.app/apps/files/?dir=/tutorial_data/Data_for_electrodes_labelling&fileid=717735>`_” located inside the "*tutorial_data*" folder
accessible from the Private Space.


The arrangement of files and folders is depicted in :ref:`Fig.1 <labelling_structure>`, while the corresponding naming conventions are outlined in :ref:`Tab.1 <labelling_naming_convention>`. 
Files and folders are further described in :ref:`Tab.2 <labelling_file_desc>` and :ref:`Tab.3 <labelling_folder_desc>` respectively. For further insights into data formats, refer to :ref:`Tab.4 <labelling_file_format>`.


.. _labelling_structure:


.. code-block:: text

	/Data_for_electrodes_labelling
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
	.... /Stimulation_data	
	...... case<case_nb>EEG_<stim_run><task>.TRC	
	
.. raw:: html

   <center>	
	<b>Fig.1</b> <i>File and folder organization.</i>
   </center>
	
|

.. _labelling_naming_convention:

.. table::
	:align: center
	
	+----------------------------+-------------------------------------------------+
	| BIDS value                 | Description                                     |
	+============================+=================================================+
	| <case_nb>                  | Case number. Integer.                           |
	+----------------------------+-------------------------------------------------+
	| <scheme_idx> and <map_idx> | Implantation scheme index. Integer.             |
	+----------------------------+-------------------------------------------------+
	| <hip_id>                   | Unique identifier of a SEEG file. Alphanumeric. |
	+----------------------------+-------------------------------------------------+
	| <stim_run>                 | Stimulation run. Integer.                       |
	+----------------------------+-------------------------------------------------+
	| <task>                     | Task identifier of a SEEG files. Alphanumeric.  |
	+----------------------------+-------------------------------------------------+


.. raw:: html

   <center>	
	<b>Tab.1</b> <i>Naming convention.</i>
   </center>
	
|


.. _labelling_file_desc:

.. table::
	:align: center
	
	+-------------+---------------------------------+
	| File        | Description                     |
	+=============+=================================+
	| \*t1\*      | T1 weighted MRI.                |
	+-------------+---------------------------------+
	| \*t2\*      | T2 weighted MRI.                |
	+-------------+---------------------------------+
	| \*ct\*      | Computerized Tomography.        |
	+-------------+---------------------------------+
	| \*TRACEW\*  | Trace weight.                   |
	+-------------+---------------------------------+
	| \*FA\*      | Fractional Anisotropy.          |
	+-------------+---------------------------------+
	| \*ADC\*     | Apparent Diffusion Coefficient. |
	+-------------+---------------------------------+
	| \*DTI\*     | Diffusion Tensor Imaging.       |
	+-------------+---------------------------------+
	| \*(S)EEG\*  | SEEG recording.                 |
	+-------------+---------------------------------+


.. raw:: html

   <center>	
	<b>Tab.2</b> <i>File description.</i>
   </center>
	
|

.. _labelling_folder_desc:

.. table::
	:align: center
	
	+-----------------------------+--------------------------------------------------------------------+
	| Folder                      | Description                                                        |
	+=============================+====================================================================+
	| /Case<case_nb>              | Subject directory.                                                 |
	+-----------------------------+--------------------------------------------------------------------+
	| /Implatation schema         | Implantation schemes.                                              |
	+-----------------------------+--------------------------------------------------------------------+
	| /DTI_case<case_nb>          | Diffusion Tensor Imaging data.                                     |
	+-----------------------------+--------------------------------------------------------------------+
	| /Anatomical_data            | Anatomical imaging (T1, T2, CT) and Diffusion Tensor Imaging data. |
	+-----------------------------+--------------------------------------------------------------------+
	| /SEEG and /Stimulation_data | SEEG data.                                                         |
	+-----------------------------+--------------------------------------------------------------------+


.. raw:: html

   <center>	
	<b>Tab.3</b> <i>Folder description.</i>
   </center>
	
|

.. _labelling_file_format:

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
	| Portable Network Graphic                       | .png      | Implantation pictures.                     |
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

