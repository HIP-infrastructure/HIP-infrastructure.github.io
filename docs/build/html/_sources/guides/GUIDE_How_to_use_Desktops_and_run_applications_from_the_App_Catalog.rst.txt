.. include:: ../hip_beta_warning.rst

How to use Desktops and run applications from the App Catalog 
**************************************************************

.. figure:: /guides/art/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog/GUIDE_desktops_header.png
	:width: 600px
	:align: center

	**Desktops on the HIP.** *Desktops are persistent environments used to run applications from the App Catalog.*

About this tutorial
====================

Objective
---------

The objective of this guide is to introduce HIP users to Desktops and how to use them 
in order to run applications available in the App Catalog. This guide briefly describes the basic principles of Desktops on the HIP,
which are also illustrated in a short video guide explaining how to: 

	* Create, display, pause/resume and switch between Desktop environments.
	* Start one or several applications simultaneously in a Desktop environment.

This guide also explains essential rules regarding data access and persistence inside a Desktop environment.  

Scope 
------

This guide focuses on how to create and operate Desktops. It does not cover the uses of the various applications available in the App Catalog.
In this perspective, the *HIP APPS* and *HIP TUTORIALS* sections accessible in the table of contents contain documentation, tutorials and
links to external resources.

Use Desktops and run applications from the App Catalog
=======================================================

Desktops are remote virtual computers running on a secure infrastructure where HIP users can run applications from the App Catalog
to work on their data. 
Desktops operate similarly to a personal computer and support most common features (drag and drop, full screen mode, clipboard, virtual keyboard).

Any application from the App Catalog, regardless if it is GUI- or CLI- based, can be run in a Desktop environment.
Desktops are available in all 3 HIP spaces: the Private, Collaborative and Public spaces, and work in a similar way.

Desktops and data persistence
-----------------------------

Once it has been initiated, a Desktop will persist until it is manually terminated. HIP users can safely log off and/or close their web browser. 
Pending Desktops will remain unaltered and accessible for later use.

.. important::
   Applications running in a Desktop environment have access to HIP user's Private Space data under the */home/<HIP_USER>/Nextcloud* directory.
   Any data and/or configuration file outside of this directory will be lost when the application or desktop are closed.
   This is the only persistent directory as it is tied to the HIP user's Private Space at application startup.

Video guide
------------

The following video guide (2'30'') serves as an introduction to Desktops and shows how to run applications from the App Catalog:  

.. raw:: html

   <center>	
   <video width="680"  poster="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Use%20Desktops%20and%20run%20Apps/Videos/HIP%20Guide%20-%20Thumbnail%20-%20Use%20Desktops%20and%20run%20Apps.png" controls>
   <source src="https://thehip.app/apps/sharingpath/anthonyboyer/Public/Guide%20-%20Use%20Desktops%20and%20run%20Apps/Videos/HIP%20Guide%20-%20Use%20Desktops%20and%20run%20Apps.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|






