.. include:: hip_beta_warning.rst

.. figure:: /art/hip_documentation_header_beta_onboarding.png
	:width: 800px
	:align: center

	**The HIP.** *An open-source platform designed for large scale and optimized
	collection, storage, curation, sharing and analysis of multiscale Human iEEG data at the international level.*

HIP Beta onboarding
********************

This quick start guide serves as an introduction to the HIP and briefly explains how to apply for a HIP account,
access the platform and operate its main features and services.
For more in depth information please refer to the :doc:`full documentation <index>`.

Get a HIP account
===================

An `EBRAINS <https://ebrains.eu/>`_ account is required to access the HIP and use all of its services. 
Apply for an EBRAINS account using the following `registration form <https://iam.ebrains.eu/auth/realms/hbp/protocol/openid-connect/registrations?response_type=code&client_id=xwiki&redirect_uri=https://wiki.ebrains.eu>`_.

Once your EBRAINS account has been activated, you can apply for a HIP account sending
an `e-mail to HIP support team <mailto:todo****@hip.eu?subject=HIP%20account%20request%20>`_ with the following 
information (items marked with an asterisk are mandatory):

	* **Full name**\*: First name and surname.
	* **HIP group(s)**\*: At least one :ref:`HIP group <list_identified_hip_groups>` you are affiliated with.
	* **EBRAINS username**\*: The username you use when logging into EBRAINS services.
	* **Institutional e-mail**\*: The e-mail that will be used by the HIP support team to contact you.
	* **Backup e-mail**\*: A backup e-mail.
	* **ORCID**: Open Researcher and Contributor ID.
	
.. admonition:: Affiliations and HIP groups

   All HIP users are also member of at least one group corresponding to pre-identified institutions
   listed in the table of :ref:`HIP groups <list_identified_hip_groups>`.
   Affiliations are cross-checked during the registration process.
	
Once your application has been validated, a confirmation e-mail will be sent to your institutional e-mail and you will be added to the HIP group
on EBRAINS so you can `log in the HIP <https://thehip.app/login>`_ using your EBRAINS credentials.
For more information regarding HIP accounts, please refer to the :doc:`How to create a HIP account </guides/GUIDE_How_to_create_a_HIP_account>` guide.
  
HIP services overview
======================

.. figure:: /guides/art/GUIDE_How_to_connect_to_the_HIP_portal_and_access_its_services/GUIDE_HIP_overview.png
	:width: 600px
	:align: center

	**HIP Dashboard.** *The HIP web interface provides services (5: Files, 6: Talk, 7: HIP) which can be selected and have their own
	interface (menu and view), that can be searched (1). The HIP account can be managed using the profile (4),
	contacts (3) and notifications (2) buttons.*
	
`Log in the HIP portal <https://thehip.app/login>`_ using your EBRAINS account. Once connected you will be redirected to
your Dashboard. The Dashboard gives an overview of the opened Desktops and BIDS databases available in all 3 HIP spaces.
Note that only the Private Space is available during the Beta phase. For more details regarding HIP Spaces, please refer
to the :doc:`How to use the HIP spaces and share data with other users </guides/GUIDE_How_to_use_the_HIP_spaces_and_share_data_with_other_users>` guide.

From the side navigation menu, it is also possible to access the App Catalog, which lists all the applications made available to the HIP users 
so they can process their data. Applications from the App Catalog are used from virtual :ref:`Desktops <onboarding_desktops_and_apps>`, which operate as remote computers.

The following video (2'15''), from the :doc:`How to connect to the HIP portal and access its services </guides/GUIDE_How_to_connect_to_the_HIP_portal_and_access_its_services>` guide,
shows the connection procedure and gives an overview of HIP services.

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Connect%20and%20overview/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Connect%20and%20overview.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Connect%20and%20overview/Videos/HIP%20Guide%20-%20Connect%20and%20overview.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|

Upload and download data
=========================

.. admonition:: Data Transfer Agreement (DTA)

   A Data Transfer Agreement has to be signed between the participating institution and the CHUV prior to any data transfer taking place.

The HIP user uploading data to the HIP qualify as Data Controller for the corresponding data.
It is the Data Controller responsibility to secure proper data pseudonymised/anonymised prior to the transfer, depending on the DTA.
Data can only be uploaded in the Private Space of the HIP user doing the transfer.
HIP users also have read and write access to the shared folder of each HIP group they belong to.
The shared folder is named according to the corresponding HIP group.

There are currently 2 solutions for uploading data to the HIP as explained in the :doc:`How to prepare and upload data to the HIP</guides/GUIDE_How_to_prepare_and_upload_data_to_the_HIP>` guide.
It is advised to set up a synchronized folder using the Nextcloud client as illustrated in the following video (2'27''):

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Upload%20data/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Upload%20data.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Upload%20data/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Upload%20data.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|

.. admonition:: Data type

   The HIP is an open-source European platform dedicated to Human intracerebral EEG data and only iEEG data
   and relevant health-related or research-related data should be uploaded to the platform.

.. _onboarding_desktops_and_apps:

Use desktops and run applications
=================================

Desktops operate as remote virtual computers where HIP users can run applications from the App Catalog to process data located in their Private Space. 
Once it has been initiated, a Desktop will persist until it is manually terminated. HIP users can safely log off and/or close their web browser.
Pending Desktops will remain unaltered and accessible for later use.
  
The procedure to open a Desktop and start applications from the App Catalog is illustrated in
the following video (2'30''), from the :doc:`How to use Desktops and run applications from the App Catalog</guides/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog>` guide:

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Use%20Desktops%20and%20run%20Apps/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Use%20Desktops%20and%20run%20Apps.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Use%20Desktops%20and%20run%20Apps/Videos/HIP%20Guide%20-%20Use%20Desktops%20and%20run%20Apps.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|

.. admonition:: Data persistence 

   Applications running in a Desktop have access to the HIP user's Private Space data under the */home/<HIP_USER>/Nextcloud* directory.
   Any data and/or configuration file outside of this directory will be lost when the application or desktop are closed.
   This is the only persistent directory as it is tied to the HIP user's Private Space at application startup.


Tutorials
---------

There are several tutorials available that can be used to get familiar with the platform:

	* :doc:`SEEG electrode placement with Brainstorm<tutorials/TUTORIAL_SEEG_electrode_placement_with_brainstorm>`
	* :doc:`SEEG electrode placement using Cico’s pipeline<tutorials/TUTORIAL_SEEG_electrode_placement_using_cicos_pipeline>`
	* :doc:`Epileptogenicity map computation with Brainstorm<tutorials/TUTORIAL_Epileptogenicity_map_computation_with_brainstorm>`
	
The Cico's pipeline, for example, can be used to place (non-rigid) SEEG electrodes on a post-implantation volume: 
	
.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20SEEG%20electrode%20placement%20using%20Cico%20pipeline/HIP%20Tutorial%20-%20Thumbnail%20-%20EEG%20electrode%20placement%20using%20Cico%20pipeline.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Tutorial%20-%20SEEG%20electrode%20placement%20using%20Cico%20pipeline/HIP%20Tutorial%20-%20EEG%20electrode%20placement%20using%20Cico%20pipeline.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>

|


	


