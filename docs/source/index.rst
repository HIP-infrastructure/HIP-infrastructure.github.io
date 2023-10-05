.. HIP user documentation documentation master file, created by
   sphinx-quickstart on Tue Feb 15 17:05:36 2022.

.. include:: hip_header_msg.rst

.. figure:: /art/hip_documentation_header.png
	:align: center	
	
|
	
The `HIP <https://www.humanbrainproject.eu/en/medicine/human-intracerebral-eeg-platform/>`_ is an open-source platform designed for large scale and optimized collection, storage, curation, sharing
and analysis of multiscale Human iEEG data at the international level. The HIP covers the entire field of iEEG-based research; i.e. multi-scale investigation of cognition, consciousness, connectomics and related disorders.

The HIP is also fully integrated in `EBRAINS <https://ebrains.eu/>`_ , a sustainable European Research Infrastructure providing tools and services in brain
research and brain-inspired technologies created by the EU-funded `Human Brain Project <https://www.humanbrainproject.eu>`_.
The HIP will offer links to other EBRAINS services, like the `Knowledge Graph <https://kg.ebrains.eu/>`_ and the `Human Brain Atlases <https://ebrains.eu/services#category1>`_. 

In line with the `FAIR principles <https://www.go-fair.org/fair-principles/>`_ , it will fully respect ethics and data privacy regulations, and optimise end-user access management. 

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Quick%20overview/Videos/HIP%20Guide%20-%20Thumbnail%20-%20quick%20overview.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Quick%20overview/Videos/HIP%20Guide%20-%20quick%20overview.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>

|
	
User documentation
**********************

All user documentation is accessible from the table of contents.
It contains the following sections:

	* **HIP guides**: Guides are standardized procedures designed to assist end users access the platform and operate all of its services.
	* **HIP tutorials**: Tutorials are fully documented use-cases about data processing and visualization on the platform.
	* **HIP datasets**: Datasets are available in the shared space and include tutorial datasets and BIDS-iEEG databases.
	* **HIP Apps**: A catalog of applications is available to explore and process data. Through the use of softwares,
	  HIP users agree to be bound by the terms and conditions of their respective licences. Softwares are provided “as is”
	  and without warranty of any kind, express, implied or otherwise.
	  

.. toctree::
   :hidden:   
   
   > > > > > > > Onboarding < < < < < < < <hip_onboarding>
   
.. toctree::
   :caption: HIP guides
   :hidden:
   
   How to create a HIP account<guides/GUIDE_How_to_create_a_HIP_account>
   How to connect to the HIP portal and access its services<guides/GUIDE_How_to_connect_to_the_HIP_portal_and_access_its_services>
   How to prepare and upload data to the HIP<guides/GUIDE_How_to_prepare_and_upload_data_to_the_HIP>
   How to convert data to BIDS format<guides/GUIDE_How_to_convert_data_to_BIDS_format>
   How to use Desktops and run applications from the App Catalog<guides/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog>
   How to transfer data from Micromed software to the HIP<guides/GUIDE_How_to_transfer_data_from_Micromed_software_to_the_HIP>
   How to use the HIP spaces and share data with other users<guides/GUIDE_How_to_use_the_HIP_spaces_and_share_data_with_other_users>
   How to use Collaborative Projects<guides/GUIDE_How_to_use_collaborative_projects>
   
.. toctree::
   :caption: HIP tutorials 
   :hidden:   
   
   SEEG electrode placement with Brainstorm<tutorials/TUTORIAL_SEEG_electrode_placement_with_brainstorm>
   SEEG electrode placement with 3D Slicer<tutorials/TUTORIAL_SEEG_electrode_placement_with_3D_slicer>
   Epileptogenicity map computation with Brainstorm<tutorials/TUTORIAL_Epileptogenicity_map_computation_with_brainstorm>
   CCEP computation with Brainstorm<tutorials/TUTORIAL_CCEP_computation_with_brainstorm>
   Simulation workflow with The Virtual Brain<tutorials/TUTORIAL_stimulation_workflow_tvb>

.. toctree:: 
   :caption: HIP datasets
   :hidden:
	
   Epimap tutorial dataset<datasets/DATASET_Epimap>
   COGEPISTIM dataset<datasets/DATASET_Cogepistim>
   Data for electrodes labelling<datasets/DATASET_Data_for_electrodes_labelling.rst>	
   iEEG cognitive task<datasets/DATASET_iEEG_task_cognitive.rst>	
   HIP iEEG seizure dataset<datasets/DATASET_HIP_iEEG_seizure_data.rst>	
   
.. toctree::
   :caption: HIP apps
   :hidden:   
   
   3D Slicer<applications/APP_3D_Slicer>
   AnyWave<applications/APP_AnyWave>
   BIDS Manager<applications/APP_BIDS_Manager>
   Brainstorm<applications/APP_Brainstorm>
   dcm2niix<applications/APP_dcm2niix>
   FileManager<applications/APP_FileManager>
   Freesurfer<applications/APP_Freesurfer>
   Frites<applications/APP_Frites>
   FSL<applications/APP_FSL>
   GARDEL<applications/APP_GARDEL>
   HiBoP<applications/APP_HiBoP>
   IntrAnat<applications/APP_IntrAnat>
   LibreOffice<applications/APP_LibreOffice>
   Localizer<applications/APP_Localizer>
   MATLAB<applications/APP_MATLAB>
   MNE-Python<applications/APP_MNE>
   MRI Deface<applications/APP_MRI_Deface>
   MRIcroGL<applications/APP_MRIcroGL>
   NiftyReg<applications/APP_NiftyReg>
   RStudio<applications/APP_RStudio>
   The Virtual Brain<applications/APP_The_Virtual_Brain>
   TRCAnonymizer<applications/APP_TRCAnonymizer>
   Visual Studio Code<applications/APP_VisualStudioCode>
   
.. comment:
   CCEP Manager<applications/APP_CCEP_Manager>
   
   
   
.. include:: hip_acknowledgement.rst
