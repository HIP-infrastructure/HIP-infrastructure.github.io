.. include:: ../hip_header_msg.rst

How to use the HIP spaces and share data with other users
**********************************************************

.. figure:: /guides/art/GUIDE_How_to_use_the_HIP_spaces_and_share_data_with_other_users/GUIDE_spaces_header.png
	:width: 800px
	:align: center

	**The HIP spaces.** *Privacy-aware environments to store, process and share iEEG data.*
	
The HIP adhere to FAIR data principles and provides a data privacy-aware environment divided into 3 spaces:
The Private Space, the Collaborative Space and the Public Space.

.. admonition:: Data policy

   The HIP endeavors to comply with national and international laws and regulations, comprising principles
   such as intellectual property rights and the protection of privacy, ethical considerations and security regulations
   when designing rules and conditions for access and the use of the platform in any of the aforementioned spaces.

The HIP Spaces
================

.. _the_private_space:

The Private Space
-----------------

The Private Space is where a HIP users from :ref:`an institution contributing to the iEEG data collection <list_identified_hip_groups>`
may upload, store and process their pseudonymised/anonymised data. 

The Private Space enables HIP users to curate, harmonize, process, or structure the data for specific pipelines, applications, or collaborations. 
Multiple technologies and methods can be used to :doc:`upload, store or extract data </guides/GUIDE_How_to_prepare_and_upload_data_to_the_HIP>`.  
Data types and formats in the Private Space are not monitored or controlled, primarily due to the security principles of the HIP.

Only :doc:`HIP users </guides/GUIDE_How_to_create_a_HIP_account>` have access to a Private Space.
The HIP user uploading data from patients onto the HIP will qualify as the Data Controller for the corresponding data,
which can only be shared with users from the same institution using the dedicated shared folders 
and can be processed with all available HIP functionalities.

Please refer to the :doc:`How to prepare and upload data to the HIP </guides/GUIDE_How_to_prepare_and_upload_data_to_the_HIP>` guide
for more information regarding the :ref:`Data Controller responsibilities <data_controller_responsabilities>` and the tools available :ref:`to transfer data to and from the HIP <uploading_data>`. 


.. _the_collaborative_space:

The Collaborative Space
------------------------

The Collaborative Space is a project-specific and access-restricted space where curated and pseudonymised data following the Collaborative Space guidelines may be shared with other accredited HIP users.
To share data within the Collaborative Space, users must utilize :doc:`Collaborative Projects </guides/GUIDE_How_to_use_collaborative_projects>`, which facilitate the controlled transfer of curated data from
the Private Space to the Collaborative Space.

By default, the creation of Collaborative Projects is a privilege reserved for :ref:`group leaders <list_identified_hip_groups>`, limited to their respective institutions. HIP users seeking permission to create
Collaborative Projects for their institution can make such requests through the `HIP support team <mailto:support@thehip.app?subject=HIP%20Collaborative%20project%20request%20>`_. 
These requests are subject to review and validation by the Group Leader.

The HIP user initiating a Collaborative Project assumes the role of Project Leader, concurrently becoming the :ref:`Data Controller <data_controller_responsabilities>` for that project.
The Project Leader holds the authority to add or remove HIP users from any projects under their responsibility and possesses the capability to delete projects entirely. 

Members of a project, referred to as Collaborators, are granted access to a set of services enabling them to transfer data and/or documents from their Private Space to the project's dedicated space.
This data transfer can only be performed using HIP's integrated tools, with no direct extraction options to prevent unauthorized data exfiltration. Once shared, the data can be managed and processed
using project-specific :doc:`BIDS tools </guides/GUIDE_How_to_convert_data_to_BIDS_format>` and Collaborative :doc:`Desktops </guides/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog>`.

The decision to move data from the Private Space to the project's space for collaborative purposes must always be approved by the Project Leader.
The Project Leader retains sole responsibility for the data, although each collaborator should exercise caution in sharing data and adhere to HIP data policies.


The Public Space (not yet available)
-------------------------------------

The Public Space is where public anonymised iEEG data is made available to the general public through EBRAINS.
Pursuant to the EBRAINS Access Policy, access to such data shall not require an EBRAINS accreditation.
Decision to move data from the Private or Collaborative Space to the Public Space can only be taken by the Data Controller of the
corresponding data, provided that the latter has been fully anonymised and patient’s informed consent to make his data public was provided. 

.. _tutorial_data:

Tutorial data
==============

The HIP provides several datasets which are listed in the *HIP DATASETS* section of this documentation and which come with different terms of use.
Their transfer and/or use outside their intended framework, e.g. for research purposes, is prohibited without written consent.
In practice, those datasets are available in a dedicated read-only shared folder called "tutorial_data" accessible from the Private Space.
 
.. figure:: /guides/art/GUIDE_How_to_use_the_HIP_spaces_and_share_data_with_other_users/GUIDE_spaces_tutorial.png
	:width: 600px
	:align: center

	**Tutorial data.** *A read-only shared folder called "tutorial_data" is available from the Private Space and contains tutorial datasets.*


Research studies and publications
==================================
	
The Data Controller defines the research studies and publications to which his data can contribute in the Collaborative Space,
and can decide to remove his data from this space at any time. All agreements regarding publications and authorship will be discussed
between relevant parties prior to making the data available. As a general publication policy principle, enforced by most scientific journals, all contributing co-authors, and thus,
all contributing Data Controllers, shall provide their explicit approval for submission of publications.  

HIP users in charge of the research projects and related publications, shall include all contributing Data Controllers,
or another representative from the same iEEG center than the Data Controller, in publications, unless agreed otherwise by both parties.
In the event that other publications than those originally agreed shall emerge from the research project,
HIP users in charge of the publication shall timely inform all participating Data Controllers of these new developments,
and obtain their approval to include their data.

Overall, Data Controllers will keep a full control of all scientific activities performed by the HIP community on their data transferred
in the HIP Collaborative Space, and no scientific publication integrating their data shall be submitted without their full consent.
Data Controllers who wish to make their data public, are required to fully anonymise the data and transfer them to the Public Space.
Thereafter, the Data Controllers will have no more control on how, and by whom, the public data might be used,
including in terms of scientific publications and authorship. However, the list of HIP users who would have contributed to the
public iEEG database will be made public for enabling acknowledgments of their contribution (DOI of the dataset).









