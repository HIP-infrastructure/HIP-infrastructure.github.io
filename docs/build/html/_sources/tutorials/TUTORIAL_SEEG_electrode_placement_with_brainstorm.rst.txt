.. include:: ../hip_beta_warning.rst

SEEG electrode placement with Brainstorm
*****************************************

.. figure:: /tutorials/art/TUTORIAL_SEEG_electrode_placement_with_brainstorm/tutorial_seeg_placement_brainstorm_header.png
	:width: 600px
	:align: center

	**3D visualization of SEEG electrodes.** *SEEG electrodes have been generated and placed using* :doc:`Brainstorm</applications/APP_Brainstorm>` *.*

Disclaimer
==========

The methods and software used in this tutorial have not been certified for clinical practice and should be considered for 
research purposes only.  

About this tutorial
====================

The objective of this tutorial is to guide HIP users in placing SEEG electrodes on a post-implantation volume using Brainstorm.
It primarily consists of a video demonstration and should be viewed as an introductory tutorial because it does not go into all the intricacies of
the placement of SEEG electrodes.

For more in-depth information regarding the placement of SEEG electrodes using Brainstorm,
please refer to the following official tutorials:

	* `Brainstorm's "Editing implantation without recordings" tutorial <https://neuroimage.usc.edu/brainstorm/Tutorials/Epileptogenicity#Editing_implantation_without_recordings>`_   
	* `Brainstorm's "Edit the contacts positions" tutorial <https://neuroimage.usc.edu/brainstorm/Tutorials/Epileptogenicity#Edit_the_contacts_positions>`_

Requirements
------------

There are no technical requirements to follow this tutorial because the dataset and software are available on the HIP.

HIP software used in this tutorial:

	* :doc:`Brainstorm</applications/APP_Brainstorm>` (07-Jan-2022)

HIP dataset used in this tutorial:

	* :doc:`Epimap tutorial dataset</datasets/DATASET_Epimap>` (rev1.0)
	
.. _prepare_environment_SEEG_placement_brainstorm:

Prepare the working environment
==================================

This tutorial relies on data available in the :doc:`Epimap tutorial dataset </datasets/DATASET_Epimap>`, 
and the following file will be used:

	* anat/MRI/3DT1post_deface.nii

Copy this file into your private space so that it can be processed.
Please, refer to the :doc:`How to use the HIP spaces </guides/GUIDE_How_to_use_the_HIP_spaces_and_share_data_with_other_users>` guide if you need help with this step.
It is also advised to initiate a new Desktop.
Pleases refer to the :doc:`How to use Desktops and run applications from the App Catalog </guides/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog>` guide if you need help with this step.

.. _place_SEEG_brainstorm:

Place SEEG electrodes with Brainstorm
=======================================

.. important::
   Applications running in a Desktop environment have access to HIP user's Private Space data under the */home/<HIP_USER>/nextcloud* directory.
   Any data and/or configuration file outside of this directory will be lost when the application or desktop are closed.
   This is the only persistent directory as it is tied to the HIP user's Private Space at application startup.
   **Make sure you are always working within the /home/<HIP_USER>/nextcloud directory**.

The accurate placement of SEEG electrodes requires some knowledge and a good understanding of the implantation procedure
(an implantation scheme or equivalent) and of the type of material that has been implanted (SEEG electrode type/characteristics)
and some expertise in brain anatomy. 
It is also important to work on a high-resolution CT scan or T1 MRI scan acquired after the implantation of the depth electrodes so that
the recording contacts appear either in hypersignal or in hyposignal.

For confidentiality reasons, the implantation scheme will not be disclosed for this tutorial and the video demonstration focuses on the technical
procedure to place SEEG electrodes and generate a standardized implantation file using Brainstorm.


.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20SEEG%20electrode%20placement%20with%20Brainstorm/Videos/HIP%20Tutorial%20-%20Thumbnail%20-%20SEEG%20electrode%20placement%20with%20Brainstorm.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20SEEG%20electrode%20placement%20with%20Brainstorm/Videos/HIP%20Tutorial%20-%20SEEG%20electrode%20placement%20with%20Brainstorm.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>

|

	


