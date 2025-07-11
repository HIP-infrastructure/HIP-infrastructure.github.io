Epileptogenicity map computation with Brainstorm
------------------------------------------------

.. figure:: /tutorials/art/TUTORIAL_Epileptogenicity_map_computation_with_brainstorm/tutorial_epileptogenicity_header.png
	:width: 600px
	:align: center

	**Epileptogenicity map.** *Epileptogenicity map computed and visualized using* :doc:`Brainstorm</applications/APP_Brainstorm>` *.*

Disclaimer
::::::::::

The methods and software used in this tutorial have not been certified for clinical practice and should be considered for 
research purposes only.  

About this tutorial
:::::::::::::::::::

The objective of this tutorial is to guide HIP users in computing maps of epileptogenicity from ictal iEEG recordings.
Epileptogenicity maps show the spatial distribution, and eventually the temporal evolution,
of the Epileptogenicity Index (EI) in the subject's brain.
The EI is based on both spectral and temporal properties of iEEG signals
and quantifies the presence of high-frequency oscillations also referred to *rapid discharges*.
*Rapid discharges* have long been recognized as a characteristic electrophysiological pattern of the epileptogenic zone
and can help identify brain regions generating seizures ([Bartolomei_2008]_).
This tutorial primarily consists of a video demonstration and should be viewed as an introductory tutorial because it does not go into all the intricacies
of the computation of epileptogenicity maps.

For more in-depth information regarding the computation of epileptogenicity maps using Brainstorm,
please refer to the official tutorial:

	* `Brainstorm's SEEG epileptogenicity maps tutorial <https://neuroimage.usc.edu/brainstorm/Tutorials/Epileptogenicity>`_

Requirements
::::::::::::

There are no technical requirements to follow this tutorial because the dataset and software are available on the HIP.

HIP software used in this tutorial:

	* :doc:`Brainstorm</applications/APP_Brainstorm>` (07-Jan-2022)

HIP dataset used in this tutorial:

	* :doc:`Epimap tutorial dataset</datasets/DATASET_Epimap>` (rev1.0)
	
.. _prepare_environment_epileptogenicity_brainstorm:

Prepare the working environment
:::::::::::::::::::::::::::::::

This tutorial relies on data available in the :doc:`Epimap tutorial dataset </datasets/DATASET_Epimap>`,
and the following files will be used:

	* anat/MRI/3DT1pre_deface.nii
	* anat/MRI/3DT1post_deface.nii
	* anat/implantation/elec_pos_patient.txt
	* seeg/SZ1.TRC
	* seeg/SZ2.TRC
	* seeg/SZ3.TRC


Copy those files into your private space so that they can be processed.
Please, refer to the :doc:`How to use the HIP spaces </guides/GUIDE_How_to_use_the_HIP_spaces_and_share_data_with_other_users>` guide if you need help with this step.
It is also advised to initiate a new Deskop.
Please, refer to the :doc:`How to use Desktops and run applications from the App Catalog </guides/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog>` guide if you need help with this step.

.. _compute_epileptogenicity_brainstorm:

Compute a map of epileptogenicity
:::::::::::::::::::::::::::::::::

.. include:: ../hip_data_persistence.rst

It is mandatory to have the 3D positions of the recording contacts of the SEEG electrodes to compute epileptogenicity maps. 
The contact names and coordinates of the SEEG electrodes are provided in the *elec_pos_patient.txt* implantation file that will
be used in this tutorial.
If you work on your own imaging data and wish to generate a dedicated implantation file, you may want to look at 
the :doc:`SEEG electrode placement with Brainstorm </tutorials/TUTORIAL_SEEG_electrode_placement_with_brainstorm>` tutorial.

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20Epileptogenicity%20map%20computation%20with%20Brainstorm/Videos/HIP%20Tutorial%20-%20Thumbnail%20-%20Epileptogenicity%20map%20computation%20with%20Brainstorm.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20Epileptogenicity%20map%20computation%20with%20Brainstorm/Videos/HIP%20Tutorial%20-%20Epileptogenicity%20map%20computation%20with%20Brainstorm.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|

References
::::::::::

.. [Bartolomei_2008] Bartolomei F, Chauvel P, Wendling F. Epileptogenicity of brain structures in human temporal lobe epilepsy: a quantified study from intracerebral EEG. Brain., 2008, 131(Pt 7):1818-30.

